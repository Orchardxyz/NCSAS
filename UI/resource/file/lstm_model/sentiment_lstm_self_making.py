# -*- coding: utf-8 -*-

import yaml
import sys
import os

from sklearn.cross_validation import train_test_split  # 处理向量
import multiprocessing  # 多线程处理
import numpy as np
from gensim.models.word2vec import Word2Vec
from gensim.corpora.dictionary import Dictionary

from keras.preprocessing import sequence  # 导入sequence模块，将用于截长补短让所有数字列表长度为100，tokenizer是用于建立字典的（英文）
from keras.models import Sequential  # 蛋糕架子
from keras.layers.embeddings import Embedding  # 词向量嵌入模块
from keras.layers.recurrent import LSTM  # 模块的LSTM层
from keras.layers.core import Dense, Dropout, Activation  # 用于添加层，dropout数据， 激活函数
from keras.models import model_from_yaml  # 用于存储模型数据

import jieba
import pandas as pd
import pymysql

np.random.seed(1337)  #
sys.setrecursionlimit(1000000)  # 设置允许最大的迭代次数是 1千万次

# 设置参数
vocab_dim = 250  # 指特征向量的维度，默认为100。大的size需要更多的训练数据,但是效果会更好. 推荐值为几十到几百。
maxlen = 100  # 字数的最大长度（原本100）
n_iterations = 15  # 迭代次数，默认为5
n_exposures = 5  # 对字典做截断. 词频少于min_count次数的单词会被丢弃掉, 默认值为5
window_size = 5  # 表示当前词与预测词在一个句子中的最大距离是多少，默认为5
batch_size = 32  # 每批次运行的数据量大小，默认32
epochs = 10  # 默认10
input_length = 100  # 输入长度（原本100）
cpu_count = multiprocessing.cpu_count()  # cpu多线程个数


# 调整词典，可调节单个词语的词频，使其能（或不能）被分出来，调整分词效果
def adjust_jieba_dict(adjust_word_file):
    f = open(adjust_word_file, encoding='gbk')
    adjust_list = f.readlines()
    for i in adjust_list:
        jieba.suggest_freq(i.strip(), True)
    f.close()

# 先对句子进行分词， 并去掉换行符, 数据处理的不完整，后期再完善
def tokenizer(text):
    text = [jieba.lcut(document.replace("\n", '')) for document in text]
    return text

# 创建词语字典，并返回每个词语的索引，词向量，以及每个句子所对应的词语索引
def create_dictionaries(model=None, combined=None):
    """
    :param model: 传进去的模型（词向量模型）
    :param combined: 数据集语料的对应向量
    :return: 1-创建的每个词对应的索引字典  2-创建一个词向量的字典  3-转换训练与测试数据集的字典
    """
    if (combined is not None) and (model is not None):
        gensim_dict = Dictionary()  # 创建gensim字典
        gensim_dict.doc2bow(model.wv.vocab.keys(), allow_update=True)

        w2_index = {v : k + 1 for k, v in gensim_dict.items()}  # 所有频数超过10的词语的索引
        w2_vec = {word : model[word] for word in w2_index.keys()}  # 所有频数超过10的词语的词向量

        def parse_dataset(combined):
            """词语变成了整数数字"""

            data = []
            for sentence in combined:
                new_txt = []
                for word in sentence:
                    try:
                        new_txt.append(w2_index[word])
                    except:
                        new_txt.append(0)
                data.append(new_txt)
            return data

        combined = parse_dataset(combined)
        # 每个句子所含词语对应的索引，所以句子中含有频数小于10的词语索引为0
        combined = sequence.pad_sequences(combined, maxlen=maxlen)  # 设置每个句子的最大长度为maxlen，低于的补0，多出的截断
        return w2_index, w2_vec, combined
    else:
        print('NO data provided....没有数据提供了，会发生错误')

# 往下都是预测的函数
def input_tranform(string):
    words = jieba.lcut(string)
    words = np.array(words).reshape(1, -1)

    filepath = os.path.dirname(os.path.abspath (__file__)) + os.path.sep + "Word2vec/Word2vec_model_change1.pkl"
    model = Word2Vec.load(filepath)

    test_str = ""

    print(words)

    _, _, combined = create_dictionaries(model, words)
    return combined


# 进行lstm预测
def lstm_sentence_predict(string):
    print("loading model加载模型...")

    filepath1 = os.path.dirname (os.path.abspath (__file__)) + os.path.sep + "Word2vec/lstm.yml"
    with open (filepath1,'r') as f:
        yaml_string = yaml.load (f)

    model = model_from_yaml(yaml_string)

    print("loading weights... 加载权重")

    filepath2 = os.path.dirname (os.path.abspath (__file__)) + os.path.sep + "Word2vec/lstm.h5"
    model.load_weights(filepath2)

    model.compile(loss="binary_crossentropy",
                  optimizer='adam',
                  metrics=['accuracy'])
    data = input_tranform(string)
    data.reshape(1, -1)
    # predict_classes：用于对测试数据的分类预测，和evaluate函数中的参数一样。返回：对于测试数据的预测分类结果数组。
    result = model.predict_classes(data)

    if result[0][0] == 1:
        return "positive"
    else:
        return "negative"


if __name__ == '__main__':
    string = "对电脑本身还是很满意的，室友都说颜值不错，很好看，1.99mm，一开始以为很厚，可是拿到手的时候感觉还不错，问了客服很多问题，他也一一解答了。唯一不足的就是，物流，无缘无故的在长沙停留了那么久，毕竟五千多的东西，免不了担起心来，而且之所以这么急，也在于距离计算机考试就这么几天了。。。。。。。总体来说还不错，好评"
    print(lstm_sentence_predict(string))

