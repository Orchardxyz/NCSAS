#!/usr/bin/env python
# encoding: utf-8
'''
@author: jgy

@software: Pycharm
@file: Window_main.py
@time: 2019/5/4 15:04
@desc:
'''
from PyQt5.QtWidgets import *
from qtpy import QtCore

from main import Ui_Form as UI_MAIN

from Window_comment_analysis import comment_analysis_window
from Window_dialog_archievement import archievement_window

from dialog_help import Ui_Form as help_window

from Window_help_manual import help_manual_window

import sys


# 主界面的入口
class test(UI_MAIN, QWidget):
    def __init__(self):
        super(test, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Notebook Computer Sentiment Analysis System")
        self.setFixedSize(self.width()-3, self.height()-3)
        self.comment_analysis_window = comment_analysis_window
        self.archievement_window = archievement_window

        # 一句话分析按钮效果触发
        self.buttonCommentAnalysis.clicked.connect(self.switchToCommentAnalysis)

        # 帮助窗口
        self.help_window = help_window

        # 帮助手册按钮触发的事件
        self.buttonHelp.clicked.connect(self.switchToHelpManual)

        # 退出系统
        self.buttonExit.clicked.connect(self.exitMainWindow)

        # 研究成果按钮触发
        self.buttonArchievement.clicked.connect(self.switchToArchievement)

    def switchToCommentAnalysis(self):
        self.hide()
        newCommDiag = QDialog()
        newUi = comment_analysis_window(newCommDiag)
        newCommDiag.show()
        newCommDiag.exec_()
        self.show()

    def switchToHelpManual(self):
        # 退出帮助
        HelpWindow.show()

    def exitMainWindow(self):
        # 退出系统触发
        self.close()

    def switchToArchievement(self):
        self.hide()
        newArchDiag = QDialog()
        newArchUi = archievement_window(newArchDiag)
        newArchDiag.show()
        newArchDiag.exec_()
        self.show()


if __name__ == '__main__':
    # 电脑外观很漂亮大气，开机迅速，运行流畅，系统也很好，性价比太高了！
    app = QApplication(sys.argv)
    TestWindow = test()
    HelpWindow = help_manual_window()
    TestWindow.show()
    sys.exit(app.exec_())