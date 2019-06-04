# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_help.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(942, 592)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(1, 0, 941, 591))
        self.frame.setStyleSheet("QLabel{\n"
"    \n"
"    font: 30pt \"Helvetica Neue\";\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(400, 10, 201, 61))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(20, 60, 901, 461))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(810, 540, 113, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "帮助手册"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">一、系统介绍</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">       本系统为笔记本在线评论情感分析系统，功能模块有两个：“评论分析”模块和“研究成果”模块。“评论分析”模块用于笔记本评论文本的总体极性情感倾向性分析以及细粒度情感分析；“研究成果”模块用于展示我们的研究成果。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">二、操作步骤</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">1. 主界面</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">       进入主界面，界面中部有两个按钮，分别对应两个功能模块。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">       位于主界面中部上方位置的按钮对应“评论分析”功能模块。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">       位于主界面中部下方位置的按钮对应“研究成果”功能模块。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">       点击主界面右下角的“帮助手册”按钮弹出本系统的操作说明。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">       点击主界面右下角的“退出”按钮退出系统。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">2. “评论分析”模块：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">       在主界面中鼠标点击“评论分析”按钮，进入评论分析界面。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">       在界面上方的文本框中输入笔记本的评论文本，输入的评论文本的字数不少于5个字，如做测试可以输入文本框下方的示例文本，输入完毕后，点击“开始分析”按钮，分析过程需要一定时间，请耐心等待。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">       分析完毕后，界面下方部分会分别显示“总体情感倾向”、“分词及去停用词”、“词性标注”、“词对抽取&amp;属性得分”结果。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">       “总体情感倾向”：系统根据模型判断输入评论文本的情感倾向，若为积极的情感倾向，则显示积极的情感倾向（positive），反之，显示消极的情感倾向（negative）。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">       本系统使用哈工大的LTP工具进行分词、词性标注、句法分析工具，词性标注的符号解析如下所示。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/postaggerPic/postagger.png\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">       点击“词对抽取&amp;属性得分”按钮旁的“图示”按钮，可以查看属性得分结果示意图。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">       点击右下角“返回”按钮返回主界面。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">3. “研究成果”模块</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">       在主界面中鼠标点击“研究成果”按钮，进入研究成果界面。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">       点击“预处理”标签，分别查看联想笔记本、惠普笔记本的好评和差评处理结果，两个品牌笔记本的好评和差评部分均由“原评论”、“过滤无效评论”、“分词标注”三部分组成，分别点击，查看数据预处理的结果。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">       “原评论”数据是通过爬虫程序爬下的未处理的文本数据，且只显示100条数据；“过滤无效评论”数据是对“原评论”数据进行去重、去短文本（5个字以内）并去无效评论如“系统默认好评”；“分词标注”数据对“过滤无效评论”数据进行分词、去停用词、词性标注的数据。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">        点击“品牌对比”标签，在下方区域鼠标上下滚动查看联想笔记本和惠普笔记本的对比结果。饼状图显示的结果是使用LSTM模型预测评论文本总体情感倾向后的评论文本好评和差评的所占比重；柱状图显示的结果是通过细粒度的“属性词-情感词”对抽取并计算属性得分计算后，两个品牌笔记本相同属性词的评分对比；最后对结果进行分析。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">        点击“词典”标签，再分别点击“属性词词典”、“否定词词典”、“副词词典”、“连接词词典”、“停用词词典”按钮查看词典生成的词云图；点击“打开源文件”按钮，直接查看源文件词典文本；点击返回按钮，返回主界面。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; background-color:#ffffff;\">        点击“退出”按钮，退出系统。</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "关闭"))


import resource.file.picture.postaggerExam
