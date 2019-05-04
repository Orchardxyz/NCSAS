#!/usr/bin/env python
# encoding: utf-8
'''
@author: jgy

@software: Pycharm
@file: RUN_MAIN.py
@time: 2019/4/30 13:35
@desc:
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from main import Ui_Form
import sys
import pymysql

_brand = ['hpscorepos', 'hpscoreneg','lenovoscorepos', 'lenovoscoreneg']

class mainWindow(Ui_Form, QWidget):

    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('笔记本电脑评论情感分析系统')
        self.tableComments(_brand[0])    # 默认初始化为惠普好评数据
        self.comboBox.currentIndexChanged.connect(self.comboBoxSelected)

    def tableComments(self, tableName):
        data = self.dbConnect(tableName)
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

        self.tableView.setModel(self.model)
        # 设置行样式
        self.tableView.setAlternatingRowColors(True)
        # 设置不同列宽
        self.tableView.setColumnWidth(0, 45)
        self.tableView.setColumnWidth(1, 800)
        # 隐藏横向滚动条
        self.tableView.setHorizontalScrollBarPolicy(True)
        layout = QVBoxLayout()
        # 将下拉框与表格放进同一个layout
        layout.addWidget(self.comboBox)
        layout.addWidget(self.tableView)
        layout.setSpacing(10)
        # layout.setStretchFactor(self.comboBox, 1)
        # layout.setStretchFactor(self.tableView, 10)
        self.tabComments.setLayout(layout)
        # 所有列自动拉伸，充满界面，适用于列数较多且内容合适的表格model
        # self.tableView.horizontalHeader().setStretchLastSection(True)
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def comboBoxSelected(self, index):
        print('当前所在位置：', self.comboBox.itemText(index))
        self.tableComments(_brand[index])

    # 连接数据库
    def dbConnect(self, tableName):
        try:
            db = pymysql.connect("localhost", "root", "Xg123456", "preprocessing", charset='utf8')
            # db = pymysql.connect("localhost", "root", "123456", "preprocessing", charset='utf8')
            cur = db.cursor()
            cur.execute("SELECT * FROM "+tableName+" WHERE id BETWEEN 1 AND 100")
            data = cur.fetchall()
            print('SUCCESS: 数据库连接成功！')
            cur.close()
            db.close()
            return data
        except:
            print('ERROR: 数据库连接失败！')
            return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mainWindow()
    w.show()
    sys.exit(app.exec_())