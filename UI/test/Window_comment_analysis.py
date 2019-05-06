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
from PyQt5.QtGui import *
from dialog_comment_analysis import Ui_CommentAnalysis
import sys


# 输入评论测试的入口文件
class comment_analysis_window(QWidget, Ui_CommentAnalysis):
    def __init__(self, newDialog):
        super(comment_analysis_window, self).__init__()
        self.setupUi(newDialog)
        self.commentDialog = newDialog
        self.commentDialog.setWindowTitle("NCSAS-评价分析")
        self.buttonReturn.clicked.connect(self.returnMain)

    # 返回主界面
    def returnMain(self):
        # self.hide()
        # self.testWindow = test()
        # self.testWindow.show()
        self.commentDialog.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = comment_analysis_window()
    ui.setupUi(Dialog)
    Dialog.show()
    # testWindow = test()
    sys.exit(app.exec_())