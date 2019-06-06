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
from dialog_comment_analysis import Ui_CommentAnalysis
import sys
import resource.file.lstm_model.sentiment_lstm_self_making as predict_file
import resource.file.ltp_analyse.main_test as ltp_main  # ltp分词
import resource.file.score.key_score as key_score


# 输入评论测试的入口文件
class comment_analysis_window(QWidget, Ui_CommentAnalysis):
    def __init__(self, newDialog):
        super(comment_analysis_window, self).__init__()
        self.setupUi(newDialog)
        self.commentDialog = newDialog
        self.commentDialog.setWindowTitle("NCSAS-评价分析")
        self.setFixedSize(self.width(), self.height())
        self.buttonReturn.clicked.connect(self.returnMain)

        # 初始化
        self.buttonShowDiaGram.setVisible(False)
        self.attr_score_dict = {}

        # 点击开始分析的按钮开始分析
        self.buttonAnalyse.clicked.connect(self.one_sentence_analyse)

        # 点击图示按钮进行操作
        self.buttonShowDiaGram.clicked.connect(self.showDiaGram)

    # 返回主界面
    def returnMain(self):
        self.commentDialog.close()

    # 对一句话进行分析
    def one_sentence_analyse(self):
        sentence_str = self.lineEditComment.text()
        if len(sentence_str) < 10:
            self.textBrowserGeneral.setText("暂无数据！请确认输入内容是否符合要求")
            self.textBrowserRuleAndScore.setText("暂无数据！请确认输入内容是否符合要求")
            self.textBrowserPostagger.setText("暂无数据！请确认输入内容是否符合要求")
            self.textBrowserSegment.setText("暂无数据！请确认输入内容是否符合要求")
        else:
            sen_predict = self.one_sentence_predice()

            dic, sentence_after_process, word_list, arcs, tag_out, word_list_str = self.one_sentence_ltp()

            print("返回的字典是什么：", dic)
            print("返回的词列表是什么：", word_list)
            print("返回的词性标注列表是什么：", tag_out)
            print("返回处理之后的句子是什么", sentence_after_process)

            result_score = self.one_sentence_score(dic);

            self.textBrowserGeneral.setText("")
            self.textBrowserSegment.setText("")
            self.textBrowserRuleAndScore.setText("")
            self.textBrowserPostagger.setText("")

            # 总体极性部分
            if sen_predict == "positive":
                self.labelTip.setVisible(False)
                self.buttonTendency.setStyleSheet("QPushButton {\n"
                                                  "    font-size: 20px;\n"
                                                  "    font-style: bold;\n"
                                                  "    background: #EEEE00;\n"
                                                  "    border-style: outset;\n"
                                                  "    border-radius: 10px;\n"
                                                  "}")
                self.buttonTendency.setText('积极')
                self.textBrowserGeneral.setText(
                    "原评论：" + sentence_str + "\n" + "根据模型分析句子的情感倾向为：积极的情感倾向" + "（" + sen_predict + "）")
            else:
                self.buttonTendency.setStyleSheet("QPushButton {\n"
                                                  "    font-size: 20px;\n"
                                                  "    font-style: bold;\n"
                                                  "    background: #EE2C2C;\n"
                                                  "    border-style: outset;\n"
                                                  "    border-radius: 10px;\n"
                                                  "}")
                self.buttonTendency.setText('消极')
                self.textBrowserGeneral.setText(
                    sentence_str + "\n" + "根据模型分析句子的情感倾向为：消极的情感倾向" + "（" + sen_predict + "）")

            # 句子分词以及去停用词展示
            if word_list_str.strip() != "":
                self.textBrowserSegment.setText(word_list_str)

            # 句子词性标注结果展示
            if tag_out != "":
                self.textBrowserPostagger.setText(tag_out)

            # 规则抽取以及计算情感得分
            self.attr_score_dict = {}  # 初始化
            if dic != {} and result_score != "":
                self.buttonShowDiaGram.setVisible(True)
                rule_score_str = ""
                dic_key = list(dic.keys())
                for key in dic_key:
                    if len(dic[key]) > 0:
                        rule_score_str += key + " : "
                        for word_list in dic[key]:

                            for word in word_list:
                                rule_score_str += word + " "
                            rule_score_str += "   |   "
                        self.attr_score_dict[key] = result_score[key]  # 存进用于图示的字典
                        rule_score_str += "属性 <" + key + ">" + " 得分为：" + str(result_score[key]) + "\n"

                self.textBrowserRuleAndScore.setText(
                    "抽取词对如下：" + "\n" +
                    rule_score_str
                )
            else:
                self.buttonShowDiaGram.setVisible(False)
                self.textBrowserRuleAndScore.setText('暂无数据！')

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
        return "", "", "", "", ""

    # 对一句话进行细粒度的情感得分值计算 dic是上一步的处理结果
    def one_sentence_score(self, dic):
        sentence_str3 = self.lineEditComment.text()
        if dic is not None and sentence_str3 is not None:
            score_result = key_score.key_score(dic)
            return score_result
        return ""

    # 显示图片
    def showDiaGram(self):
        if self.attr_score_dict != {}:
            import matplotlib.pyplot as plt
            import numpy as np
            x, y = [], []
            for key in self.attr_score_dict.keys():
                x.append(key)
                y.append(self.attr_score_dict[key])
            fig = plt.figure(figsize=(6, 6))  # 设置尺寸
            ax = fig.add_subplot(111)
            index = np.arange(len(x))
            plt.xticks(index, x)  # x轴
            plt.bar(index, y, 0.5, color='#D64700', label='联想')  # y轴
            plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置显示中文
            plt.rcParams['axes.unicode_minus'] = False  # 显示负轴的负号
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = comment_analysis_window()
    ui.setupUi(Dialog)
    Dialog.show()
    # testWindow = view()
    sys.exit(app.exec_())
