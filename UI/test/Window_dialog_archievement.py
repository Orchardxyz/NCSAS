# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 11:10
# @Author  : JackeyChen
# @FileName: Window_dialog_archievement.py
# @Software: PyCharm

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dialog_archievement import Ui_Dialog
import sys

from dbConnect import dbConnect


# 研究成果展示页面运行入口2，现在正在使用
class archievement_window(QWidget, Ui_Dialog):

    # 原评论数据表名
    # tableNameList = ['lenovoscoreneg', 'lenovoscorepos','hpscoreneg','hpscorepos']
    tableNameList = ['lenovoscorepos', 'lenovoscoreneg', 'hpscorepos', 'hpscoreneg']

    # def __init__(self):
    #     # 自己给自己初始化,可运行
    #     super(archievement_window, self).__init__()
    #     self.setupUi(self)
    #     self.setWindowTitle("NCSAS-研究成果")
    #
    #     self.buttonReturn.clicked.connect(self.returnMain)
    #
    #
    #
    #
    #
    #     #惠普差评的跳转
    #     self.buttonBad_2.clicked.connect(self.switchToHpBad)
    #
    #     #联想好评的跳转
    #     self.buttonPraise_2.clicked.connect(self.switchToHpPraise)
    #
    #     # 联想差评的跳转
    #     self.buttonBad.clicked.connect (self.switchToLenovoBad)
    #
    #     # 联想好评的跳转
    #     self.buttonPraise.clicked.connect (self.switchToLenovoPraise)

    # 下面这个init是第二次试验版本的
    def __init__(self, newDialog):
        # 自己给自己初始化
        super(archievement_window, self).__init__()

        self.setupUi(newDialog)
        self.setWindowTitle("NCSAS-研究成果")

        self.archieveDialog = newDialog

        self.buttonReturn.clicked.connect (self.returnMain)

        # 原评论数据表：[联想好评/差评，惠普好评/差评]
        self.originTable = [self.tableViewComments, self.tableViewComments_2, self.tableViewComments_3, self.tableViewComments_4]

        #惠普差评的跳转
        self.buttonBad_2.clicked.connect(self.switchToHpBad)

        #联想好评的跳转
        self.buttonPraise_2.clicked.connect(self.switchToHpPraise)

        # 联想差评的跳转
        self.buttonBad.clicked.connect (self.switchToLenovoBad)

        # 联想好评的跳转
        self.buttonPraise.clicked.connect (self.switchToLenovoPraise)


    def returnMain(self):
        self.archieveDialog.close()

    '''联想/惠普 的 好评/差评 切换事件'''

    def switchToLenovoPraise(self):
        #联想好评
        self.stackedWidgetContent.setCurrentWidget(self.pagePraise)
        self.loadingOriginData('lenovo', 0)

    def switchToLenovoBad(self):
        #联想差评
        self.stackedWidgetContent.setCurrentWidget(self.pageBad)
        self.loadingOriginData('lenovo', 1)

    def switchToHpPraise(self):
        #惠普好评
        self.stackedWidgetContent_2.setCurrentWidget(self.pagePraise_2)
        self.loadingOriginData('hp', 2)

    def switchToHpBad(self):
        #惠普差评
        self.stackedWidgetContent_2.setCurrentWidget(self.pageBad_2)
        self.loadingOriginData('hp', 3)

    '''数据加载'''
    # 原评论
    def loadingOriginData(self, brand, index):
        comm_type = 'PRAISE:' if (index % 2 == 0) else 'BAD:'
        print(comm_type, brand, 'origin data loading...')
        data = dbConnect(self.tableNameList[index])
        row = len(data)  # 表格行数
        vol = 1  # 表格列数
        # 设置数据层次结构，10行2列
        self.model = QStandardItemModel(10, 1)
        # 设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(['评论'])
        for i in range(row):
            for j in range(vol):
                # 只展示“评论”列的数据
                temp_data = data[i][j + 1]  # 临时记录，不能直接插入表格
                item = QStandardItem(str(temp_data))
                self.model.setItem(i, j, item)
        self.originTable[index].setModel(self.model)
        # 设置行样式
        self.originTable[index].setAlternatingRowColors(True)
        # 隐藏横向滚动条
        self.originTable[index].setHorizontalScrollBarPolicy(False)
        # 所有列自动拉伸，充满界面，适用于列数较多且内容合适的表格model
        self.originTable[index].horizontalHeader().setStretchLastSection(True)
        self.originTable[index].horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = archievement_window()
#     window.show()
#     sys.exit(app.exec_())