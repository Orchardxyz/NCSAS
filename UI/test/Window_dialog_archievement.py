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

    tableNameList = ['lenovoscoreneg', 'lenovoscorepos','hpscoreneg','hpscorepos']

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

    def switchToLenovoBad(self):
        #联想差评
        self.stackedWidgetContent.setCurrentWidget(self.pageBad)
        self.loadingLenovoBadOrigin()

    def switchToLenovoPraise(self):
        #联想好评
        self.stackedWidgetContent.setCurrentWidget(self.pagePraise)

    def switchToHpBad(self):
        #惠普差评
        self.stackedWidgetContent_2.setCurrentWidget(self.pageBad_2)

    def switchToHpPraise(self):
        #惠普好评
        self.stackedWidgetContent_2.setCurrentWidget(self.pagePraise_2)

    def loadingLenovoBadOrigin(self):
        # 加载 联想 差评 原评论数据
        # self.tableViewComments
        print("lenovo data loading...")

        data = dbConnect(self.tableNameList[0])

        row = len(data)

        vol = len(data[1])

        # 设置数据层次结构，10行2列
        self.model = QStandardItemModel(10, 2)
        # 设置水平方向四个头标签文本内容
        self.model.setHorizontalHeaderLabels(['序号', '评论'])
        for i in range(row):
            for j in range(vol):
                temp_data = data[i][j]  # 临时记录，不能直接插入表格
                # print(temp_data)
                item = QStandardItem(str(temp_data))
                self.model.setItem(i, j, item)

        self.tableViewComments_2.setModel (self.model)
        # 设置行样式
        self.tableViewComments_2.setAlternatingRowColors (True)
        # 设置不同列宽
        self.tableViewComments_2.setColumnWidth (0, 45)
        self.tableViewComments_2.setColumnWidth (1, 800)
        # 隐藏横向滚动条
        self.tableViewComments_2.setHorizontalScrollBarPolicy (True)
        # layout = QVBoxLayout ()
        # 将下拉框与表格放进同一个layout
        # layout.addWidget (self.comboBox)
        # layout.addWidget (self.tableViewComments_2)
        # layout.setSpacing (10)
        # layout.setStretchFactor(self.comboBox, 1)
        # layout.setStretchFactor(self.tableView, 10)
        # self.tabComments.setLayout (layout)
        # 所有列自动拉伸，充满界面，适用于列数较多且内容合适的表格model
        self.tableViewComments_2.horizontalHeader().setStretchLastSection(True)
        self.tableViewComments_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)



# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = archievement_window()
#     window.show()
#     sys.exit(app.exec_())