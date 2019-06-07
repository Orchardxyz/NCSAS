# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_dic_explain.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(903, 598)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 1, 903, 598))
        self.frame.setStyleSheet("QLabel{\n"
"    \n"
"    font: 30pt \"Helvetica Neue\";\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelDict = QtWidgets.QLabel(self.frame)
        self.labelDict.setGeometry(QtCore.QRect(350, 0, 221, 51))
        self.labelDict.setObjectName("labelDict")
        self.textBrowserDict = QtWidgets.QTextBrowser(self.frame)
        self.textBrowserDict.setGeometry(QtCore.QRect(32, 60, 841, 481))
        self.textBrowserDict.setObjectName("textBrowserDict")
        self.pushButtonDict = QtWidgets.QPushButton(self.frame)
        self.pushButtonDict.setGeometry(QtCore.QRect(760, 550, 113, 41))
        self.pushButtonDict.setStyleSheet("QPushButton {\n"
"    background: #FFF;\n"
"    border: 1px solid;\n"
"    border-radius: 5px;\n"
"    font-size: 26px;\n"
"    font-weight: bold;\n"
"    font-family: \"KaiTi\";\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgb(209, 209, 209);\n"
"}\n"
"QPushButton:pressed {\n"
"    background: rgb(200, 200, 200);\n"
"}")
        self.pushButtonDict.setObjectName("pushButtonDict")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelDict.setText(_translate("Dialog", "词典说明"))
        self.textBrowserDict.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt; font-weight:600;\">一、属性词词典</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">    1. 属性词词典中的词语，均与笔记本电脑相关的属性词，对应源文件中的“属性词词典.txt”文件。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">    2. 属性词是使用大量的笔记本评论数据通过频繁挖掘算法筛选出所有的名词和所有的动词中出现频率较高的词语，并对一次过滤的结果进行二次过滤得到的。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">    3. 该属性词词典描述了笔记本电脑的细粒度的属性，如“颜值”、“分辨率”、“硬盘”等。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">    </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt; font-weight:600;\">二、否定词词典</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">    1. 否定词词典总结了中文中常用的否定词，如“不”、“不是”、“非”、“未”等，对应源文件中的“属性词词典.txt”文件。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">    2. 中文的否定词会对中文句子表达的语义进行反转，如句子“这台电脑的屏幕真的很不好”中“不”字反转了“好”字的情感表达，表示电脑屏幕不好。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\'; font-size:13pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt; font-weight:600;\">三、副词词典</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">    1. 副词词典中总结了一些常用的副词，如“太”、“更加”、“很”等，对应源文件中的“副词词典.txt”文件。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">    2. 副词的作用在于不改变句子意义的情况下，加深句子中情感表达的程度，如句子“电脑的运行速度真的太快了”中“太”加深了电脑运行速度的情感表达。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\'; font-size:13pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt; font-weight:600;\">四、连接词词典</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">    1. 连接词词典中整理笔记本电脑的评论数据中常用的连接词、常用颜文字等，对应源文件中的“连接词词典.txt”文件。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">    2. 连接词的目的是去掉评论文本中无意义的词语，而为了能够在去停用词时过滤掉颜文字，在连接词中还加入了常用的38个颜文字，为了使这些颜文字在中文分词的过程中被正确分开，</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\'; font-size:13pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:14pt; font-weight:600;\">五、停用词词典</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">    1. 停用词词典中整理了生活中常用的语气词、介词、HTML中一些无用符号等，对应源文件中的“停用词词典.txt”文件。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.SF NS Text\'; font-size:13pt;\">    2. 停用词的目的是为了去掉评论文本中的无用词语，减少噪音，提高结果的准确率。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\'; font-size:13pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\'; font-size:13pt;\"><br /></p></body></html>"))
        self.pushButtonDict.setText(_translate("Dialog", "关闭"))

