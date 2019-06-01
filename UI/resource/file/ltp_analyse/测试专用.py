# -*- coding: utf-8 -*-
# @Time    : 2019/6/1 16:51
# @Author  : JackeyChen
# @FileName: 测试专用.py
# @Software: PyCharm


import os
from pyltp import Postagger
from pyltp import Segmentor
from pyltp import Parser

LTP_DATA_DIR = "/Users/chenjiaqi/Downloads/addition-jar/ltp_data_v3.4.0"
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')
seg_model_path = os.path.join(LTP_DATA_DIR,'cws.model') #分词模型

segmentor = Segmentor()  # 初始化实例
segmentor.load(seg_model_path)  # 加载模型
words = segmentor.segment('电脑还行，屏幕太棒了')  # 分词
print(words,"啦啦啦啦")
print(' '.join(words))
for i in words:
    print(i,type(i))
segmentor.release()  # 释放模型