#!/usr/bin/env python
# encoding: utf-8
'''
@author: jgy

@software: Pycharm
@file: Window_archievement.py
@time: 2019/5/4 17:32
@desc:
'''
from PyQt5.QtWidgets import *
from main_archievement import Ui_Form
import sys


# 研究成果展示页面运行入口
class archievement_window(QWidget, Ui_Form):
    def __init__(self):
        super(archievement_window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("NCSAS-研究成果")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = archievement_window()
    window.show()
    sys.exit(app.exec_())