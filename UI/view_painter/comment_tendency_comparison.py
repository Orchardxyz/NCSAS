#!/usr/bin/env python
# encoding: utf-8
'''
@author: jgy

@software: Pycharm
@file: comment_tendency_comparison.py
@time: 2019/6/2 15:00
@desc:
'''
'''两个品牌的好评率与差评率图形绘制'''

import matplotlib.pyplot as plt

if __name__ == '__main__':
    '''数据处理'''
    hp = {}
    lenovo = {}
    with open('../resource/file/comment_tendency/hp.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            temp = line.split(':')
            hp[temp[0]] = float(temp[1].strip('\n'))
        print('惠普：', hp)
    with open('../resource/file/comment_tendency/lenovo.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            temp = line.split(':')
            lenovo[temp[0]] = float(temp[1].strip('\n'))
        print('联想：', lenovo)

    '''绘图前'''
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False    # 解决‘-’表现为方块的问题
    labels = u'好评', u'差评'
    colors = 'cornflowerblue', 'lightcoral'

    '''惠普'''
    figHp = plt.figure(figsize=(5, 5))

    fracsHp = [hp['好评率'], hp['差评率']]
    plt.axes(aspect=1)

    # 设置饼图的凸出显示
    explode = [0.1, 0]
    # 画饼状图， 并且指定标签和对应的颜色
    # 指定阴影效果
    plt.pie(x=fracsHp, labels=labels, colors=colors, explode=explode, autopct='%3.1f %%',
            shadow=False, labeldistance=1.1, startangle=90, pctdistance=0.6)
    plt.legend(loc='upper right')

    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.title('惠普')
    plt.savefig('../resource/file/picture/hp_tendency.png')

    '''联想'''
    figLenovo = plt.figure(figsize=(5, 5))

    fracsLenovo = [lenovo['好评率'], lenovo['差评率']]
    plt.axes(aspect=1)

    # 设置饼图的凸出显示
    explode = [0.1, 0]
    # 画饼状图， 并且指定标签和对应的颜色
    # 指定阴影效果
    plt.pie(x=fracsLenovo, labels=labels, colors=colors, explode=explode, autopct='%3.1f %%',
            shadow=False, labeldistance=1.1, startangle=90, pctdistance=0.6)
    plt.legend(loc='upper right')

    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.title('联想')
    plt.savefig('../resource/file/picture/lenovo_tendency.png')

    plt.show()