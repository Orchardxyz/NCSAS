# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 11:10
# @Author  : JackeyChen
# @FileName: Window_dialog_archievement.py
# @Software: PyCharm

from PyQt5.QtWidgets import *
from dialog_archievement import Ui_Dialog
import sys


# 研究成果展示页面运行入口2
class archievement_window(QWidget, Ui_Dialog):
    def __init__(self):
        # 自己给自己初始化
        super(archievement_window, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("NCSAS-研究成果")

        self.buttonReturn.clicked.connect(self.returnMain)


    def returnMain2(self):
        print("研究成果啦啦")
        super.returnMain


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = archievement_window()
    window.show()
    sys.exit(app.exec_())