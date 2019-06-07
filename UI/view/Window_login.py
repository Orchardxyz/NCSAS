# -*- coding: utf-8 -*-
# @Time    : 2019/6/7 01:52
# @Author  : JackeyChen
# @FileName: Window_login.py
# @Software: PyCharm

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import sys
from login import Ui_Form
from Window_main import test as mainWindow


class loginWindow(Ui_Form, QWidget):
    def __init__(self):
        super(loginWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('NCSAS LOGIN')
        self.setFixedSize(610, 409)
        self.buttonLogin.clicked.connect(self.login)

    # 登录
    def login(self):
        if self.inputUsername.text() == 'admin' and self.inputPassword.text() == '123456':
            self.hide()
            main.show()
            # mainWindow.show()
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


