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
    # def __init__(self):
    #     # 自己给自己初始化,可运行
    #     super(archievement_window, self).__init__()
    #     self.setupUi(self)
    #     self.setWindowTitle("NCSAS-研究成果")
    #
    #     self.buttonReturn.clicked.connect(self.returnMain)
    #
    #
    #
    #
    #
    #     #惠普差评的跳转
    #     self.buttonBad_2.clicked.connect(self.switchToHpBad)
    #
    #     #联想好评的跳转
    #     self.buttonPraise_2.clicked.connect(self.switchToHpPraise)
    #
    #     # 联想差评的跳转
    #     self.buttonBad.clicked.connect (self.switchToLenovoBad)
    #
    #     # 联想好评的跳转
    #     self.buttonPraise.clicked.connect (self.switchToLenovoPraise)


    # 下面这个init是第二次试验版本的
    def __init__(self, newDialog):
        # 自己给自己初始化
        super(archievement_window, self).__init__()

        self.setupUi(newDialog)
        self.setWindowTitle("NCSAS-研究成果")

        self.buttonReturn.clicked.connect(self.returnMain)





        #惠普差评的跳转
        self.buttonBad_2.clicked.connect(self.switchToHpBad)

        #联想好评的跳转
        self.buttonPraise_2.clicked.connect(self.switchToHpPraise)

        # 联想差评的跳转
        self.buttonBad.clicked.connect (self.switchToLenovoBad)

        # 联想好评的跳转
        self.buttonPraise.clicked.connect (self.switchToLenovoPraise)


    # def returnMain2(self):
    #     super.returnMain

    def switchToLenovoBad(self):
        #联想差评
        self.stackedWidgetContent.setCurrentWidget(self.pageBad)

    def switchToLenovoPraise(self):
        #联想好评
        self.stackedWidgetContent.setCurrentWidget(self.pagePraise)

    def switchToHpBad(self):
        #惠普差评
        self.stackedWidgetContent_2.setCurrentWidget(self.pageBad_2)

    def switchToHpPraise(self):
        #惠普好评
        self.stackedWidgetContent_2.setCurrentWidget(self.pagePraise_2)



# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = archievement_window()
#     window.show()
#     sys.exit(app.exec_())