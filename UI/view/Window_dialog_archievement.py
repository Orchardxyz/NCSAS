# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 11:10
# @Author  : JackeyChen
# @FileName: Window_dialog_archievement.py
# @Software: PyCharm

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dialog_archievement import Ui_Archievements
import sys

from dbConnect import dbConnect

from Window_dict_help import help_dict_window


# 研究成果展示页面运行入口2，现在正在使用
class archievement_window(QWidget, Ui_Archievements):

    # 原评论数据表名
    originalTableNameList = ['lenovo_pos_original', 'lenovo_neg_original', 'hp_pos_original', 'hp_neg_original']
    # 过滤的数据表名
    filterTableNameList = ['lenovo_pos_filter', 'lenovo_neg_filter', 'hp_pos_filter', 'hp_neg_filter']
    # 分词标注的数据表名
    segPosTableNameList = ['lenovo_pos_segandpos', 'lenovo_neg_segandpos', 'hp_pos_segandpos', 'hp_neg_segandpos' ]

    # 下面这个init是第二次试验版本的
    def __init__(self, newDialog):
        # 自己给自己初始化
        super(archievement_window, self).__init__()

        self.setupUi(newDialog)

        self.archieveDialog = newDialog
        self.archieveDialog.setWindowTitle("NCSAS-研究成果")

        self.buttonReturn.clicked.connect(self.returnMain)

        # 按钮点击时的样式切换
        self.clickStyle = "QPushButton{" "background: rgb(40,40,40);" "color: #FFF;" "}"
        self.unclickStyle = "QPushButton{"  "}"

        '''-******** [预处理]tab界面设置 ********-'''

        # 原评论数据表：[联想好评/差评，惠普好评/差评]
        self.originTable = [self.tableViewComments, self.tableViewComments_2, self.tableViewComments_3, self.tableViewComments_4]
        # 过滤后的评论数据表：[联想好评/差评，惠普好评/差评]
        self.filterTable = [self.tableViewGetRid, self.tableViewGetRid_2, self.tableViewGetRid_3, self.tableViewGetRid_4]
        # 分词&标注&去停用词后的评论数据表：[联想好评/差评，惠普好评/差评]
        self.segPosTable = [self.tableViewTagWords, self.tableViewTagWords_2, self.tableViewTagWords_3, self.tableViewTagWords_4]

        '''页面加载完毕时初始化页面组件'''
        # 设置默认tab
        self.tabArchievements.setCurrentIndex(0)
        self.tabBrand.setCurrentIndex(0)
        # 隐藏数据表
        self.stackedWidgetContentLenovo.setVisible(False)
        self.stackedWidgetContentHp.setVisible(False)
        # 设置默认toolBox
        self.toolBoxPraise.setCurrentIndex(0)
        self.toolBoxBad.setCurrentIndex(0)
        self.toolBoxPraise_2.setCurrentIndex(0)
        self.toolBoxBad_2.setCurrentIndex(0)

        '''按钮事件'''
        #惠普差评的跳转
        self.buttonBad_2.clicked.connect(self.switchToHpBad)

        #联想好评的跳转
        self.buttonPraise_2.clicked.connect(self.switchToHpPraise)

        # 联想差评的跳转
        self.buttonBad.clicked.connect(self.switchToLenovoBad)

        # 联想好评的跳转
        self.buttonPraise.clicked.connect(self.switchToLenovoPraise)

        '''-******** [品牌对比]tab界面设置 ********-'''
        self.scrollAreaComparison.setStyleSheet("QScrollArea {background-color:#FFF;}")
        self.scrollAreaComparison.viewport().setStyleSheet("background-color:transparent;")

        '''-******** [词典]tab界面设置 ********-'''
        # 初始化
        self.dictAttributes.setStyleSheet(self.clickStyle)
        self.stackedWidgetDict.setCurrentIndex(0)
        self.path = '../view_painter/file'
        # 建立词典按钮列表
        self.dictionaryButtons = [self.dictAttributes, self.dictNegWords, self.dictAdverbs,
                                  self.dictConjunctions, self.dictStopWords]
        # lambda表达式传参
        self.dictAttributes.clicked.connect(lambda: self.dictClicked(0))
        self.dictNegWords.clicked.connect(lambda: self.dictClicked(1))
        self.dictAdverbs.clicked.connect(lambda: self.dictClicked(2))
        self.dictConjunctions.clicked.connect(lambda: self.dictClicked(3))
        self.dictStopWords.clicked.connect(lambda: self.dictClicked(4))

        self.pushButton.clicked.connect(self.openDictFile)

        #词典帮助说明
        self.pushButtonExplain.clicked.connect(self.dictHelpWindow)


    # 返回主界面
    def returnMain(self):
        self.archieveDialog.close()

    '''-////////// [预处理]tab界面的事件处理及方法 //////////-'''
    '''联想/惠普 的 好评/差评 切换事件'''
    # 联想好评
    def switchToLenovoPraise(self):
        self.buttonPraise.setStyleSheet(self.clickStyle)
        self.buttonBad.setStyleSheet(self.unclickStyle)
        self.stackedWidgetContentLenovo.setCurrentWidget(self.pagePraise)
        # 数据连接
        self.loadingOriginData('lenovo', 0)
        self.loadingFilterData('lenovo', 0)
        self.loadingSegPosData('lenovo', 0)

    # 联想差评
    def switchToLenovoBad(self):
        self.buttonBad.setStyleSheet(self.clickStyle)
        self.buttonPraise.setStyleSheet(self.unclickStyle)
        self.stackedWidgetContentLenovo.setCurrentWidget(self.pageBad)
        # 数据连接
        self.loadingOriginData('lenovo', 1)
        self.loadingFilterData('lenovo', 1)
        self.loadingSegPosData('lenovo', 1)

    # 惠普好评
    def switchToHpPraise(self):
        self.buttonPraise_2.setStyleSheet(self.clickStyle)
        self.buttonBad_2.setStyleSheet(self.unclickStyle)
        self.stackedWidgetContentHp.setCurrentWidget(self.pagePraise_2)
        # 数据连接
        self.loadingOriginData('hp', 2)
        self.loadingFilterData('hp', 2)
        self.loadingSegPosData('hp', 2)

    # 惠普差评
    def switchToHpBad(self):
        self.buttonBad_2.setStyleSheet(self.clickStyle)
        self.buttonPraise_2.setStyleSheet(self.unclickStyle)
        self.stackedWidgetContentHp.setCurrentWidget(self.pageBad_2)
        # 数据连接
        self.loadingOriginData('hp', 3)
        self.loadingFilterData('hp', 3)
        self.loadingSegPosData('hp', 3)

    '''数据加载'''
    # 原评论
    def loadingOriginData(self, brand, index):
        comm_type = 'PRAISE:' if (index % 2 == 0) else 'BAD:'
        print(comm_type, brand, 'origin data loading...')
        data = dbConnect(self.originalTableNameList[index])
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
        if brand == 'lenovo': self.stackedWidgetContentLenovo.setVisible(True)
        else: self.stackedWidgetContentHp.setVisible(True)
        '''表格样式'''
        # 设置行样式
        self.originTable[index].setAlternatingRowColors(True)
        # 隐藏横向滚动条
        self.originTable[index].setHorizontalScrollBarPolicy(False)
        # 所有列自动拉伸，充满界面，适用于列数较多且内容合适的表格model
        self.originTable[index].horizontalHeader().setStretchLastSection(True)
        self.originTable[index].horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    # 过滤后的数据
    def loadingFilterData(self, brand, index):
        comm_type = 'PRAISE:' if (index % 2 == 0) else 'BAD:'
        print(comm_type, brand, 'filter data loading...')
        data = dbConnect(self.filterTableNameList[index])
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
        self.filterTable[index].setModel(self.model)
        if brand == 'lenovo':
            self.stackedWidgetContentLenovo.setVisible(True)
        else:
            self.stackedWidgetContentHp.setVisible(True)
        '''表格样式'''
        # 设置行样式
        self.filterTable[index].setAlternatingRowColors(True)
        # 隐藏横向滚动条
        self.filterTable[index].setHorizontalScrollBarPolicy(False)
        # 所有列自动拉伸，充满界面，适用于列数较多且内容合适的表格model
        self.filterTable[index].horizontalHeader().setStretchLastSection(True)
        self.filterTable[index].horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    # 分词标注
    def loadingSegPosData(self, brand, index):
        comm_type = 'PRAISE:' if (index % 2 == 0) else 'BAD:'
        print(comm_type, brand, 'seg and pos data loading...')
        data = dbConnect(self.segPosTableNameList[index])
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
        self.segPosTable[index].setModel(self.model)
        if brand == 'lenovo':
            self.stackedWidgetContentLenovo.setVisible(True)
        else:
            self.stackedWidgetContentHp.setVisible(True)
        '''表格样式'''
        # 设置行样式
        self.segPosTable[index].setAlternatingRowColors(True)
        # 隐藏横向滚动条
        self.segPosTable[index].setHorizontalScrollBarPolicy(False)
        # 所有列自动拉伸，充满界面，适用于列数较多且内容合适的表格model
        self.segPosTable[index].horizontalHeader().setStretchLastSection(True)
        self.segPosTable[index].horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    '''-////////// [品牌对比]tab界面的事件处理及方法 //////////-'''

    '''-////////// [词典]tab界面的事件处理及方法 //////////-'''
    # 词典按钮点击事件
    def dictClicked(self, index):
        # 按钮变色
        self.dictionaryButtons[index].setStyleSheet(self.clickStyle)
        for i in range(0, len(self.dictionaryButtons)):
            if i != index:
                self.dictionaryButtons[i].setStyleSheet(self.unclickStyle)
        # 词云展示
        self.stackedWidgetDict.setCurrentIndex(index)

    # 查看词典的源文件
    def openDictFile(self):
        fileName_choose, filetype = \
            QFileDialog.getOpenFileName(self,"选取文件", self.path,  # 起始路径
                                         "Text Files (*.txt)")  # 设置文件扩展名过滤,用双分号间隔
        if fileName_choose == "":
            print("\n取消选择")
            return
        # 使用系统默认方式打开文件
        import os
        os.system(fileName_choose)

    # 查看词典的帮助说明
    def dictHelpWindow(self):
        newDictHelpDialog = QDialog()
        newUi = help_dict_window(newDictHelpDialog)
        newDictHelpDialog.show()
        newDictHelpDialog.exec_ ()

