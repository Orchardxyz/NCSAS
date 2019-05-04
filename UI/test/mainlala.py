# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainlala.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1124, 712)
        self.frameMain = QtWidgets.QFrame(Form)
        self.frameMain.setGeometry(QtCore.QRect(0, 0, 1121, 711))
        self.frameMain.setStyleSheet("* {\n"
"    background: rgb(255,255,255);\n"
"    font-size: 15px;\n"
"    font-family: sans-serif;\n"
"}\n"
"QFrame {\n"
"    border: solid 1px rgba(0,0,0);\n"
"    /*background-image: url(:/main/newmainla.png);\n"
"    background: #FFFFF0;*/\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-size: 35px;\n"
"    font-style: bold;\n"
"    background: #F7F7F7;\n"
"    background: rgb(204, 204, 204);\n"
"\n"
"    border-style: outset;\n"
"\n"
"    border-radius: 10px;\n"
"opacity:0.7;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    border-style: inset;\n"
"}")
        self.frameMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMain.setObjectName("frameMain")
        self.buttonArchievement = QtWidgets.QPushButton(self.frameMain)
        self.buttonArchievement.setGeometry(QtCore.QRect(430, 350, 221, 101))
        self.buttonArchievement.setObjectName("buttonArchievement")
        self.buttonCommentAnalysis = QtWidgets.QPushButton(self.frameMain)
        self.buttonCommentAnalysis.setGeometry(QtCore.QRect(430, 200, 221, 101))
        self.buttonCommentAnalysis.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.buttonCommentAnalysis.setFlat(False)
        self.buttonCommentAnalysis.setObjectName("buttonCommentAnalysis")
        self.buttonHelp = QtWidgets.QPushButton(self.frameMain)
        self.buttonHelp.setGeometry(QtCore.QRect(910, 670, 93, 28))
        self.buttonHelp.setStyleSheet("QPushButton{\n"
"font-size: 16px;\n"
"    font-family: sans-serif;\n"
"font-weight: bold;\n"
"    \n"
"}")
        self.buttonHelp.setFlat(True)
        self.buttonHelp.setObjectName("buttonHelp")
        self.buttonExit = QtWidgets.QPushButton(self.frameMain)
        self.buttonExit.setGeometry(QtCore.QRect(1020, 670, 93, 28))
        self.buttonExit.setStyleSheet("QPushButton{\n"
"font-size: 16px;\n"
"    font-family: sans-serif;\n"
"font-weight: bold;\n"
"    \n"
"}")
        self.buttonExit.setFlat(True)
        self.buttonExit.setObjectName("buttonExit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.buttonArchievement.setText(_translate("Form", "研究成果"))
        self.buttonCommentAnalysis.setText(_translate("Form", "评价分析"))
        self.buttonHelp.setText(_translate("Form", "帮助手册"))
        self.buttonExit.setText(_translate("Form", "退出"))

