#!/usr/bin/env python
# encoding: utf-8
'''
@author: jgy

@software: Pycharm
@file: Test.py
@time: 2019/5/4 15:04
@desc:
'''
from PyQt5.QtWidgets import *
from mainlala import Ui_Form as UI_MAIN
# from Window_comment_analysis import comment_analysis_window
# from Window_archievement import archievement_window
from dialog_comment_analysis import Ui_Dialog as comment_analysis_window
# from dialog_archievement import Ui_Dialog as archievement_window

from Window_dialog_archievement import archievement_window

from dialog_help import Ui_Form as help_window

from Window_help_manual import help_manual_window as HMW

import sys


# 主界面的入口
class test(UI_MAIN, QWidget):
    def __init__(self):
        super(test, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Notebook Computer Sentiment Analysis System")
        self.comment_analysis_window = comment_analysis_window
        self.archievement_window = archievement_window

        self.buttonCommentAnalysis.clicked.connect(self.switchToCommentAnalysis)

        # 帮助窗口
        self.help_window = help_window

        # 帮助手册按钮触发事件
        self.buttonHelp.clicked.connect(self.switchToHelpManual)

        # 退出系统
        self.buttonExit.clicked.connect(self.exitMainWindow)

        # 研究成果按钮触发
        self.buttonArchievement.clicked.connect(self.switchToArchievement)

    def switchToCommentAnalysis(self):
        self.hide()
        newForm = QDialog()
        newUi = comment_analysis_window()
        newUi.setupUi(newForm)
        newForm.show()
        newForm.exec_()
        self.show()

    def switchToHelpManual(self):
        # 退出帮助
        window.show()

    def exitMainWindow(self):
        # 退出系统触发
        self.close()

    def switchToArchievement(self):
        # 可运行的第一次
        # self.hide()
        # newArchDiag = QDialog()
        # newArchUi = archievement_window()
        # newArchUi.setupUi(newArchDiag)
        # newArchDiag.show()
        # newArchDiag.exec_()
        # self.show()

        # 第二次试验，测试成功，就用这个
        self.hide()
        newArchDiag = QDialog()
        newArchUi = archievement_window(newArchDiag)
        newArchDiag.show()
        newArchDiag.exec_()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    TestWindow = test()
    # CommentWindow = comment_analysis_window()
    # ArchievementWindow = archievement_window()
    window = HMW ()
    TestWindow.show()
    sys.exit(app.exec_())