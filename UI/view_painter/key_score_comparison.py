#!/usr/bin/env python
# encoding: utf-8
'''
@author: jgy

@software: Pycharm
@file: matplotlibTest.py
@time: 2019/5/30 00:04
@desc:
'''
'''两个品牌的主要属性评分对比'''
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 从文件中读取标签及对应分值，存进字典
    hpAttr = {}
    with open('../resource/file/keys_score/hp_keys_score.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            temp = line.split(':')
            hpAttr[temp[0]] = float(temp[1].strip('\n'))
        print('惠普：', hpAttr)
    lenovoAttr = {}
    with open('../resource/file/keys_score/lenovo_keys_score.txt', 'r', encoding='gbk') as f:
        for line in f.readlines():
            temp = line.split(':')
            lenovoAttr[temp[0]] = float(temp[1].strip('\n'))
        print('联想：', lenovoAttr)

    # 显示部分标签（25个）
    x = ['内存', '屏幕', '颜值', '声音', '性能', '硬盘', '品牌',
         '鼠标', '机身', '风扇', '接口', '质量', '分辨率', '性价比',
         '电池', '包装', '物流', '颜色', '外观', '价格', '配置',
         '快递', '售后', '散热', '服务']
    # 惠普的分值
    hpValue = []
    for key in hpAttr.keys():
        if key in x:
            hpValue.append(hpAttr[key])
    # 联想的分值
    lenovoValue = []
    for key in lenovoAttr.keys():
        if key in x:
            lenovoValue.append(lenovoAttr[key])

    # 绘制图形
    import numpy as np

    fig = plt.figure(figsize=(9.5, 6))  # 设置尺寸
    ax = fig.add_subplot(111)
    index = np.arange(len(x))
    bar_width = 0.5
    # y轴显示
    plt.bar(index, lenovoValue, bar_width - 0.05, color='#B3B3B3', label='联想')
    plt.bar(index + bar_width, hpValue, bar_width - 0.05, color='#4C4C4C', label='惠普')
    plt.xticks(index + bar_width, x)  # x轴
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置显示中文
    ax.set_xticklabels(x, rotation=40)  # 横轴坐标斜着显示
    plt.rcParams['axes.unicode_minus'] = False  # 显示负轴的负号
    plt.ylim(ymax=0.8)
    plt.title(u'两大品牌属性词评分对比')
    plt.legend(loc=1, fancybox=True, ncol=5)  # 图例显示
    # 隐藏部分边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.savefig('../resource/file/picture/attr_score_comparison.png')

    plt.show()
