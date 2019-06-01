#!/usr/bin/env python
# encoding: utf-8
'''
@author: jgy

@software: Pycharm
@file: Window_comment_analysis.py
@time: 2019/5/4 15:58
@desc:
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dialog_comment_analysis import Ui_CommentAnalysis
import sys
import resource.file.lstm_model.sentiment_lstm_self_making as predict_file
# import resource.file.ltp_analyse.main as ltp_main
import resource.file.ltp_analyse.main_test as ltp_main  #陈jia棋后面加上去的分词，采用ltp分词工具替代结巴
import resource.file.score.key_score as key_score


# 输入评论测试的入口文件
class comment_analysis_window(QWidget, Ui_CommentAnalysis):
    def __init__(self, newDialog):
        super(comment_analysis_window, self).__init__()
        self.setupUi(newDialog)
        self.commentDialog = newDialog
        self.commentDialog.setWindowTitle("NCSAS-评价分析")
        self.buttonReturn.clicked.connect(self.returnMain)

        # 点击开始分析的按钮开始尽心分析
        self.buttonAnalyse.clicked.connect(self.one_sentence_analyse)



    # 返回主界面
    def returnMain(self):
        # self.hide()
        # self.testWindow = test()
        # self.testWindow.show()
        self.commentDialog.close()

    # 对一句话进行分析
    def one_sentence_analyse(self):
        sentence_str = self.lineEditComment.text()
        print(sentence_str, "啦啦啦")
        sen_predict = self.one_sentence_predice()

        dic, sentence_after_process, word_list, arcs = self.one_sentence_ltp()

        print("返回的字典是什么：", dic)
        print("依存句法分析Wie：", arcs)

        result_score = self.one_sentence_score(dic);



        print(result_score,"结束啦做完啦")


        print("哈哈哈哈结束预测很简单的啦", sen_predict)


    # 先对一句话进行总体预测
    def one_sentence_predice(self):
        sentence_str = self.lineEditComment.text()
        if sentence_str is not None:
            predict_result = predict_file.lstm_sentence_predict(self.lineEditComment.text())
            return predict_result
        return ""

    # 对一句话进行细粒度的抽取
    def one_sentence_ltp(self):
        sentence_str2 = self.lineEditComment.text()
        if sentence_str2 is not None:
             return ltp_main.sentence_analyse(sentence_str2)
        return "","","","",""

    # 对一句话进行细粒度的情感得分值计算 dic是上一步的处理结果
    def one_sentence_score(self, dic):
        sentence_str3 = self.lineEditComment.text ()
        if dic is not None and sentence_str3 is not None:
            score_result =  key_score.key_score(dic)
            return score_result
        return ""




if __name__ == '__main__':
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = comment_analysis_window()
    ui.setupUi(Dialog)
    Dialog.show()
    # testWindow = test()
    sys.exit(app.exec_())