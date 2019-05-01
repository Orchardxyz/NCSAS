#!/usr/bin/env python
# encoding: utf-8
'''
@author: jgy

@software: Pycharm
@file: RUN.py
@time: 2019/4/30 09:47
@desc:
'''

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import sys
import numpy as np
from login import Ui_Form

class mywindow(Ui_Form, QWidget):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('笔记本电脑评论情感分析系统登录')
        self.setFixedSize(610, 409)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mywindow()
    # w.pushButton.clicked.connect(w.gass)
    w.show()
    sys.exit(app.exec_())