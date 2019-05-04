#!/usr/bin/env python
# encoding: utf-8
'''
@author: jgy

@software: Pycharm
@file: Window_comment_analysis.py
@time: 2019/5/4 15:58
@desc:
'''
from PyQt5.QtWidgets import *
# from main_comment_analysis import Ui_Form
from dialog_comment_analysis import Ui_Dialog
from Test import test
import sys


class comment_analysis_window(QWidget, Ui_Dialog):
    def __init__(self):
        super(comment_analysis_window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("NCSAS-评价分析")
        self.buttonReturn.clicked.connect(self.returnMain)

    # 返回主界面
    def returnMain(self):
        # self.hide()
        # self.testWindow = test()
        # self.testWindow.show()
        print('111111111111')
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = comment_analysis_window()
    ui.setupUi(Dialog)
    Dialog.show()
    # testWindow = test()
    sys.exit(app.exec_())