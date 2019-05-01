# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(610, 419)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 611, 421))
        self.frame.setStyleSheet("* {\n"
"    background: rgb(255,255,255);\n"
"    font-size: 15px;\n"
"    font-family: sans-serif;\n"
"}\n"
"QFrame {\n"
"    border: solid 1px rgba(0,0,0);\n"
"    background-image: url(\':/image/computer3.jpg\')\n"
"}\n"
"QLineEdit {\n"
"    /*color: #8d98a1;*/\n"
"    color: #FFFFFF;\n"
"    font-size: 20px;\n"
"    font-style: Italic bold;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    /*background-color: #405361;*/\n"
"    background-color: #0066CC;\n"
"}\n"
"QPushButton {\n"
"    font-size: 25px;\n"
"    background: #ced1d8;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224,0,0);\n"
"    border-style: inset;\n"
"}\n"
"QCheckBox {\n"
"    background: rgba(85,170,255,0);\n"
"    color: white;\n"
"}\n"
"QLabel {\n"
"    background: rgba(85,170,255,0);\n"
"    color: white;\n"
"    font-style: Italic bold;\n"
"    font-size: 15px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(230, 280, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(180, 110, 271, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 200, 271, 51))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Login in"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter Your Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Enter Your Password"))

import qrc.bg

