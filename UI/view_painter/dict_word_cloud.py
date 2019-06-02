#!/usr/bin/env python
# encoding: utf-8
'''
@author: jgy

@software: Pycharm
@file: dict_word_cloud.py
@time: 2019/6/2 16:04
@desc:
'''
from wordcloud import WordCloud
from matplotlib import pyplot as plt
font_path = './file/simfang.ttf'     # 设置显示中文字体

'''属性词词云'''
figAttr = plt.figure(figsize=(8, 6))
axAttr = figAttr.add_subplot(111)
with open(r'./file/属性词词典.txt', encoding='utf-8') as f:
    text = f.read()
attr_cloudword=WordCloud(width=800,
                      height=600,
                      font_path=font_path,
                      scale=1,
                      margin=2,
                      background_color='white',
                      max_words=200,
                      min_font_size=20,
                      max_font_size=130,
                      random_state=50).generate(text)
axAttr.imshow(attr_cloudword)
axAttr.axis("off")
plt.savefig(('../resource/file/picture/attr_dict.png'))

'''否定词词云'''
figNeg = plt.figure(figsize=(8, 6))
axNeg = figNeg.add_subplot(111)
with open(r'./file/否定词词典.txt', encoding='utf-8') as f:
    text = f.read()
neg_cloudword=WordCloud(width=800,
                      height=600,
                      font_path=font_path,
                      scale=1,
                      margin=2,
                      background_color='white',
                      max_words=200,
                      min_font_size=20,
                      max_font_size=130,
                      random_state=50).generate(text)
axNeg.imshow(neg_cloudword)
axNeg.axis("off")
plt.savefig(('../resource/file/picture/neg_dict.png'))

'''副词词云'''
figAdv = plt.figure(figsize=(8, 6))
axAdv = figAdv.add_subplot(111)
with open(r'./file/副词词典.txt', encoding='utf-8') as f:
    text = f.read()
adv_cloudword=WordCloud(width=800,
                      height=600,
                      font_path=font_path,
                      scale=1,
                      margin=2,
                      background_color='white',
                      max_words=200,
                      min_font_size=20,
                      max_font_size=130,
                      random_state=50).generate(text)
axAdv.imshow(adv_cloudword)
axAdv.axis("off")
plt.savefig(('../resource/file/picture/adv_dict.png'))

'''连接词词云'''
figConj = plt.figure(figsize=(8, 6))
axConj = figConj.add_subplot(111)
with open(r'./file/连接词词典.txt', encoding='utf-8') as f:
    text = f.read()
conj_cloudword=WordCloud(width=800,
                      height=600,
                      font_path=font_path,
                      scale=1,
                      margin=2,
                      background_color='white',
                      max_words=200,
                      min_font_size=20,
                      max_font_size=130,
                      random_state=50).generate(text)
axConj.imshow(conj_cloudword)
axConj.axis("off")
plt.savefig(('../resource/file/picture/conj_dict.png'))

'''停用词词云'''
figStop = plt.figure(figsize=(8, 6))
axStop = figStop.add_subplot(111)
with open(r'./file/停用词词典.txt', encoding='utf-8') as f:
    text = f.read()
stop_cloudword=WordCloud(width=800,
                      height=600,
                      font_path=font_path,
                      scale=1,
                      margin=2,
                      background_color='white',
                      max_words=200,
                      min_font_size=15,
                      max_font_size=115,
                      random_state=50).generate(text)
axStop.imshow(stop_cloudword)
axStop.axis("off")
plt.savefig(('../resource/file/picture/stop_dict.png'))

plt.show()