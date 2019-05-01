#!/usr/bin/env python
# encoding: utf-8
'''
@author: jgy

@software: Pycharm
@file: RUN_MAIN.py
@time: 2019/4/30 13:35
@desc:
'''
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QHeaderView, QPushButton, QLabel, QHBoxLayout
import sys
import numpy as np
from main import Ui_Form

class mywindow(Ui_Form, QWidget):
    def __init__(self, parent=None):
        super(mywindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('笔记本电脑评论情感分析系统')
        self.table()

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.addStretch()
        self.btn_left = QPushButton('<<')
        self.btn_left.setStyleSheet("QPushButton{border:0;font-size:16px}QPushButton::hover{background-color:green}")
        self.layout.addWidget(self.btn_left)
        self.label_page = QLabel('1')
        self.label_page.setStyleSheet("font-size:14px;")
        self.layout.addWidget(self.label_page)
        self.btn_right = QPushButton('>>')
        self.btn_right.setStyleSheet("QPushButton{border:0;font-size:16px}QPushButton::hover{background-color:green}")
        self.layout.addWidget(self.btn_right)
        self.layout.addStretch()
        self.label_all = QLabel('共1页')
        self.label_all.setStyleSheet("font-size:14px;")
        self.layout.addWidget(self.label_all)

        self.current_page = 1
        self.all_page = 1
        self.lenth = 1
        self.num = 1

    def table(self):
        # 列宽根据内容自适应
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)

    def set_page_num(self, lenth, num):
        self.lenth = lenth
        self.num = num
        if lenth % num == 0:
            self.all_page = lenth // num
        else:
            self.all_page = lenth // num + 1
        self.refresh_page_info()

    def refresh_page_info(self):
        self.label_all.setText('共' + str(self.all_page) + '页')
        self.label_page.setText(str(self.current_page))

    def get_index(self, index):
        if index < self.all_page:
            return self.num * (index - 1), self.num * index - 1
        elif index == self.all_page:
            return self.num * (index - 1), self.lenth - 1
        else:
            return 0, 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mywindow()
    w.show()
    sys.exit(app.exec_())