# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_comment_analysis.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1122, 766)
        self.frameCommentAnalysis = QtWidgets.QFrame(Form)
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEditComment.setPlaceholderText(_translate("Form", "请在此输入一条或一段有关笔记本电脑的评论（不少于10个字）"))
        self.buttonAnalyse.setText(_translate("Form", "开始分析"))
        self.buttonReturn.setText(_translate("Form", "返回"))
        self.labelExample.setText(_translate("Form", "示例：电脑外观很漂亮大气，开机迅速，运行流畅，系统也很好，性价比太高了！"))

