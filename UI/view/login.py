# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
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
"    background-image: url(:/loginbg/computerlogin.png);\n"
"}\n"
"QLineEdit {\n"
"    color: #000000;\n"
"    font-size: 23px;\n"
"    font-style: Italic bold;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"    border: 2px solid rgba(255,255,255, 0.2); \n"
"}\n"
"QPushButton {\n"
"    font-size: 35px;\n"
"    font-style: bold;\n"
"    background: #F7F7F7;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    border-style: inset;\n"
"}\n"
"QCheckBox {\n"
"    \n"
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
        self.buttonLogin = QtWidgets.QPushButton(self.frame)
        self.buttonLogin.setGeometry(QtCore.QRect(210, 270, 151, 51))
        self.buttonLogin.setObjectName("buttonLogin")
        self.inputUsername = QtWidgets.QLineEdit(self.frame)
        self.inputUsername.setGeometry(QtCore.QRect(160, 100, 271, 51))
        self.inputUsername.setObjectName("inputUsername")
        self.inputPassword = QtWidgets.QLineEdit(self.frame)
        self.inputPassword.setGeometry(QtCore.QRect(160, 190, 271, 51))
        self.inputPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPassword.setObjectName("inputPassword")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.buttonLogin.setText(_translate("Form", "Login"))
        self.inputUsername.setPlaceholderText(_translate("Form", "Enter Your Username"))
        self.inputPassword.setPlaceholderText(_translate("Form", "Enter Your Password"))



import qrc.loginbg
