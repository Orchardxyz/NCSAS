# -*- coding: utf-8 -*-
# @Time    : 2019/6/7 13:41
# @Author  : JackeyChen
# @FileName: Window_dict_help.py
# @Software: PyCharm


from dialog_dic_explain import Ui_Dialog
from PyQt5.QtWidgets import *
import sys

class help_dict_window(QWidget, Ui_Dialog):
    def __init__(self,newDialog):
        super(help_dict_window, self).__init__()
        self.setupUi(newDialog)
        self.setWindowTitle("词典说明")
        self.setFixedSize(self.width(), self.height())
        # self.pushButtonDict.clicked.connect(self.returnMain)
        self.pushButtonDict.clicked.connect(lambda: self.returnMain(newDialog))

    def returnMain(self, newDialog):
        # self.close()
        newDialog.close()
        # Dialog.close()

        print("之后打印的退出")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = help_dict_window(Dialog)
    # ui.setupUi(Dialog)
    Dialog.show()
    # testWindow = view()
    sys.exit(app.exec_())
