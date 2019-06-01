# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_comment_analysis.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CommentAnalysis(object):
    def setupUi(self, CommentAnalysis):
        CommentAnalysis.setObjectName("CommentAnalysis")
        CommentAnalysis.resize(1118, 766)
        self.frameCommentAnalysis = QtWidgets.QFrame(CommentAnalysis)
        self.frameCommentAnalysis.setGeometry(QtCore.QRect(0, 0, 1121, 771))
        self.frameCommentAnalysis.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCommentAnalysis.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCommentAnalysis.setObjectName("frameCommentAnalysis")
        self.lineEditComment = QtWidgets.QLineEdit(self.frameCommentAnalysis)
        self.lineEditComment.setGeometry(QtCore.QRect(180, 60, 591, 41))
        self.lineEditComment.setStyleSheet("QLineEdit {\n"
"    border: 1px solid;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"}")
        self.lineEditComment.setObjectName("lineEditComment")
        self.frameAnalysisResult = QtWidgets.QFrame(self.frameCommentAnalysis)
        self.frameAnalysisResult.setGeometry(QtCore.QRect(70, 140, 981, 541))
        self.frameAnalysisResult.setStyleSheet("QFrame {\n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"}")
        self.frameAnalysisResult.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameAnalysisResult.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAnalysisResult.setObjectName("frameAnalysisResult")
        self.buttonAnalyse = QtWidgets.QPushButton(self.frameCommentAnalysis)
        self.buttonAnalyse.setGeometry(QtCore.QRect(790, 60, 131, 41))
        self.buttonAnalyse.setStyleSheet("QPushButton {\n"
"    font-size: 18px;\n"
"    font-style: bold;\n"
"    background: #6495ED;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: #BEBEBE;\n"
"}")
        self.buttonAnalyse.setObjectName("buttonAnalyse")
        self.buttonReturn = QtWidgets.QPushButton(self.frameCommentAnalysis)
        self.buttonReturn.setGeometry(QtCore.QRect(1010, 720, 93, 28))
        self.buttonReturn.setStyleSheet("QPushButton {\n"
"    border: 1px solid;\n"
"    border-radius: 5px;\n"
"}")
        self.buttonReturn.setObjectName("buttonReturn")
        self.labelExample = QtWidgets.QLabel(self.frameCommentAnalysis)
        self.labelExample.setGeometry(QtCore.QRect(180, 110, 561, 16))
        self.labelExample.setStyleSheet("QLabel {\n"
"    font-style: bold;\n"
"}")
        self.labelExample.setObjectName("labelExample")

        self.retranslateUi(CommentAnalysis)
        QtCore.QMetaObject.connectSlotsByName(CommentAnalysis)

    def retranslateUi(self, CommentAnalysis):
        _translate = QtCore.QCoreApplication.translate
        CommentAnalysis.setWindowTitle(_translate("CommentAnalysis", "Dialog"))
        self.lineEditComment.setPlaceholderText(_translate("CommentAnalysis", "请在此输入一条或一段有关笔记本电脑的评论（不少于10个字）"))
        self.buttonAnalyse.setText(_translate("CommentAnalysis", "开始分析"))
        self.buttonReturn.setText(_translate("CommentAnalysis", "返回"))
        self.labelExample.setText(_translate("CommentAnalysis", "示例：外观很漂亮，开机非常迅速，运行流畅，电池耐用，总体来说，性价比很不错！"))


