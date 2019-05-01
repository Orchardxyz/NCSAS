#!/usr/bin/env python
# encoding: utf-8
'''
@author: jgy

@software: Pycharm
@file: RUN.py
@time: 2019/4/30 09:47
@desc:
'''

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import sys
from login import Ui_Form
from RUN_MAIN import mainWindow

class loginWindow(Ui_Form, QWidget):
    def __init__(self):
        super(loginWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('笔记本电脑评论情感分析系统登录界面')
        self.setFixedSize(610, 409)
        self.buttonLogin.clicked.connect(self.login)

    # 登录
    def login(self):
        if (self.inputUsername.text()=='admin' and self.inputPassword.text()=='123456'):
            self.hide()
            main.show()
        else:
            self.loginErr()

    # 登录错误
    def loginErr(self):
        reply = QMessageBox.information(self,  # 使用infomation信息框
                                        "登录错误",
                                        "用户名或密码错误！",
                                        QMessageBox.Ok | QMessageBox.No)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = loginWindow()
    main = mainWindow()
    login.show()
    sys.exit(app.exec_())