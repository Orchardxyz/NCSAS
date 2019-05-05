# -*- coding: utf-8 -*-
# @Time    : 2019/5/4 22:34
# @Author  : JackeyChen
# @FileName: Window_help_manual.py
# @Software: PyCharm

from dialog_help import Ui_Form
from PyQt5.QtWidgets import *
import sys

# 输入评论测试的入口文件
class help_manual_window(QWidget, Ui_Form):
    def __init__(self):
        super(help_manual_window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("帮助手册")
        self.pushButton.clicked.connect(self.returnMain)

    # 返回主界面
    def returnMain(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = help_manual_window()
    ui.setupUi(Form)
    Form.show()
    # testWindow = test()
    sys.exit(app.exec_())

