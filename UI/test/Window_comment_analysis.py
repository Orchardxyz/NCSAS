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

        dic, sentence_after_process, word_list, arcs, tag_out, word_list_str = self.one_sentence_ltp()


        print("返回的字典是什么：", dic)
        print("返回的词列表是什么：", word_list)
        print("返回的词性标注列表是什么：", tag_out)
        print("返回处理之后的句子是什么", sentence_after_process)

        result_score = self.one_sentence_score(dic);



        print(result_score,"结束啦做完啦")


        print("哈哈哈哈结束预测很简单的啦", sen_predict)

        self.textBrowserGeneral.setText("")
        self.textBrowserSegment.setText("")
        self.textBrowserRuleAndScore.setText("")
        self.textBrowserPostagger.setText("")


        # 总体极性部分
        if sen_predict == "positive":
            self.textBrowserGeneral.setText(sentence_str + "\n" + "根据模型分析句子的情感倾向为：积极的情感倾向"+"（"+ sen_predict+"）")
        else:
            self.textBrowserGeneral.setText(sentence_str + "\n" + "根据模型分析句子的情感倾向为：消极的情感倾向"+"（"+ sen_predict+"）")



        # 句子分词以及去停用词展示
        if word_list_str.strip () != "":
            self.textBrowserSegment.setText(word_list_str)

        # 句子词性标注结果展示
        if tag_out != "":
            self.textBrowserPostagger.setText(tag_out)

        # 规则抽取以及计算情感得分
        if dic!={} and result_score!="":
            rule_score_str = ""
            dic_key = list(dic.keys())
            for key in dic_key:
                if len(dic[key])>0:
                    rule_score_str += key + " : "
                    for word_list in dic[key]:

                        for word in word_list:
                            rule_score_str += word + " "
                        rule_score_str += "   |   "
                    rule_score_str += "属性 <"+key +">"+" 得分为：" + str(result_score[key]) +"\n"

            self.textBrowserRuleAndScore.setText(
                "抽取词对如下：" + "\n" +
                rule_score_str
            )




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