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
from dialog_archievement import Ui_Dialog as archievement_window

import sys


class test(UI_MAIN, QWidget):
    def __init__(self):
        super(test, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Notebook Computer Sentiment Analysis System")
        self.comment_analysis_window = comment_analysis_window
        self.archievement_window = archievement_window

        self.buttonCommentAnalysis.clicked.connect(self.switchToCommentAnalysis)
        # self.buttonArchievement.clicked.connect(self.switchToArchievement)

    def switchToCommentAnalysis(self):
        self.hide()
        newForm = QDialog()
        newUi = comment_analysis_window()
        newUi.setupUi(newForm)
        newForm.show()
        newForm.exec_()
        self.show()

    # def switchToArchievement(self):
    #     self.hide()
    #     ArchievementWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    TestWindow = test()
    # CommentWindow = comment_analysis_window()
    # ArchievementWindow = archievement_window()
    TestWindow.show()
    sys.exit(app.exec_())