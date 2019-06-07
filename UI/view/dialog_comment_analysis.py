# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_comment_analysis.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CommentAnalysis(object):
    def setupUi(self, CommentAnalysis):
        CommentAnalysis.setObjectName("CommentAnalysis")
        CommentAnalysis.resize(1118, 766)
        self.frameCommentAnalysis = QtWidgets.QFrame(CommentAnalysis)
        self.frameCommentAnalysis.setGeometry(QtCore.QRect(0, 0, 1121, 771))
        self.frameCommentAnalysis.setStyleSheet("#labelWarn {\n"
"    font-size: 22px;\n"
"    color: red\n"
"}")
        self.frameCommentAnalysis.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCommentAnalysis.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCommentAnalysis.setObjectName("frameCommentAnalysis")
        self.lineEditComment = QtWidgets.QLineEdit(self.frameCommentAnalysis)
        self.lineEditComment.setGeometry(QtCore.QRect(180, 60, 591, 41))
        self.lineEditComment.setStyleSheet("QLineEdit {\n"
"    border: 1px solid;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"}")
        self.lineEditComment.setObjectName("lineEditComment")
        self.frameAnalysisResult = QtWidgets.QFrame(self.frameCommentAnalysis)
        self.frameAnalysisResult.setGeometry(QtCore.QRect(70, 140, 981, 571))
        self.frameAnalysisResult.setStyleSheet("QFrame {\n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"QLabel {\n"
"    background: #6495ED;\n"
"    font-size: 25px;\n"
"    font-family: \"KaiTi\";\n"
"    border-top-right-radius: 16%;\n"
"    border-bottom-right-radius: 16%\n"
"}")
        self.frameAnalysisResult.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameAnalysisResult.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAnalysisResult.setObjectName("frameAnalysisResult")
        self.textBrowserGeneral = QtWidgets.QTextBrowser(self.frameAnalysisResult)
        self.textBrowserGeneral.setGeometry(QtCore.QRect(0, 43, 981, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowserGeneral.setFont(font)
        self.textBrowserGeneral.setStyleSheet("QTextBrowser{\n"
"background:#F2F2F2\n"
"}")
        self.textBrowserGeneral.setObjectName("textBrowserGeneral")
        self.labelGeneralEmotion = QtWidgets.QLabel(self.frameAnalysisResult)
        self.labelGeneralEmotion.setGeometry(QtCore.QRect(0, 0, 221, 43))
        self.labelGeneralEmotion.setStyleSheet("")
        self.labelGeneralEmotion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelGeneralEmotion.setObjectName("labelGeneralEmotion")
        self.labelSegment = QtWidgets.QLabel(self.frameAnalysisResult)
        self.labelSegment.setGeometry(QtCore.QRect(0, 120, 221, 43))
        self.labelSegment.setStyleSheet("")
        self.labelSegment.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSegment.setObjectName("labelSegment")
        self.textBrowserSegment = QtWidgets.QTextBrowser(self.frameAnalysisResult)
        self.textBrowserSegment.setGeometry(QtCore.QRect(0, 163, 981, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowserSegment.setFont(font)
        self.textBrowserSegment.setStyleSheet("QTextBrowser{\n"
"background:#F2F2F2\n"
"}")
        self.textBrowserSegment.setObjectName("textBrowserSegment")
        self.labelPostagger = QtWidgets.QLabel(self.frameAnalysisResult)
        self.labelPostagger.setGeometry(QtCore.QRect(0, 242, 221, 43))
        self.labelPostagger.setStyleSheet("")
        self.labelPostagger.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPostagger.setObjectName("labelPostagger")
        self.textBrowserPostagger = QtWidgets.QTextBrowser(self.frameAnalysisResult)
        self.textBrowserPostagger.setGeometry(QtCore.QRect(0, 284, 981, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowserPostagger.setFont(font)
        self.textBrowserPostagger.setStyleSheet("QTextBrowser{\n"
"background:#F2F2F2\n"
"}")
        self.textBrowserPostagger.setObjectName("textBrowserPostagger")
        self.labelRuleAndScore = QtWidgets.QLabel(self.frameAnalysisResult)
        self.labelRuleAndScore.setGeometry(QtCore.QRect(0, 366, 221, 41))
        self.labelRuleAndScore.setStyleSheet("")
        self.labelRuleAndScore.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRuleAndScore.setObjectName("labelRuleAndScore")
        self.textBrowserRuleAndScore = QtWidgets.QTextBrowser(self.frameAnalysisResult)
        self.textBrowserRuleAndScore.setGeometry(QtCore.QRect(0, 407, 981, 165))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowserRuleAndScore.setFont(font)
        self.textBrowserRuleAndScore.setStyleSheet("QTextBrowser{\n"
"background:#F2F2F2\n"
"}")
        self.textBrowserRuleAndScore.setObjectName("textBrowserRuleAndScore")
        self.buttonShowDiaGram = QtWidgets.QPushButton(self.frameAnalysisResult)
        self.buttonShowDiaGram.setGeometry(QtCore.QRect(250, 366, 71, 41))
        self.buttonShowDiaGram.setStyleSheet("QPushButton {\n"
"    font-size: 20px;\n"
"    font-style: bold;\n"
"    background: rgb(214, 71, 0);\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: #BEBEBE;\n"
"}")
        self.buttonShowDiaGram.setObjectName("buttonShowDiaGram")
        self.buttonTendency = QtWidgets.QPushButton(self.frameAnalysisResult)
        self.buttonTendency.setGeometry(QtCore.QRect(250, 1, 71, 41))
        self.buttonTendency.setStyleSheet("#buttonTendency {\n"
"    font-size: 20px;\n"
"    font-style: bold;\n"
"    background: #FFF;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"}")
        self.buttonTendency.setText("")
        self.buttonTendency.setObjectName("buttonTendency")
        self.buttonAnalyse = QtWidgets.QPushButton(self.frameCommentAnalysis)
        self.buttonAnalyse.setGeometry(QtCore.QRect(790, 60, 131, 41))
        self.buttonAnalyse.setStyleSheet("QPushButton {\n"
"    font-size: 18px;\n"
"    font-style: bold;\n"
"    background: #6495ED;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: #BEBEBE;\n"
"}")
        self.buttonAnalyse.setObjectName("buttonAnalyse")
        self.buttonReturn = QtWidgets.QPushButton(self.frameCommentAnalysis)
        self.buttonReturn.setGeometry(QtCore.QRect(1010, 720, 93, 28))
        self.buttonReturn.setStyleSheet("QPushButton {\n"
"    border: 1px solid;\n"
"    border-radius: 5px;\n"
"}")
        self.buttonReturn.setObjectName("buttonReturn")
        self.labelExample = QtWidgets.QLabel(self.frameCommentAnalysis)
        self.labelExample.setGeometry(QtCore.QRect(180, 110, 561, 16))
        self.labelExample.setStyleSheet("QLabel {\n"
"    font-style: bold;\n"
"}")
        self.labelExample.setObjectName("labelExample")
        self.labelTip = QtWidgets.QLabel(self.frameCommentAnalysis)
        self.labelTip.setGeometry(QtCore.QRect(10, 10, 231, 16))
        self.labelTip.setStyleSheet("QLabel {\n"
"    font-size: 17px;\n"
"    font-family: \"KaiTi\"\n"
"}")
        self.labelTip.setObjectName("labelTip")

        self.retranslateUi(CommentAnalysis)
        QtCore.QMetaObject.connectSlotsByName(CommentAnalysis)

    def retranslateUi(self, CommentAnalysis):
        _translate = QtCore.QCoreApplication.translate
        CommentAnalysis.setWindowTitle(_translate("CommentAnalysis", "Dialog"))
        self.lineEditComment.setPlaceholderText(_translate("CommentAnalysis", "请在此输入一条或一段有关笔记本电脑的评论（不少于5个字）"))
        self.labelGeneralEmotion.setText(_translate("CommentAnalysis", "总体情感倾向"))
        self.labelSegment.setText(_translate("CommentAnalysis", "分词及去停用词"))
        self.labelPostagger.setText(_translate("CommentAnalysis", "词性标注"))
        self.labelRuleAndScore.setText(_translate("CommentAnalysis", "词对抽取&属性得分"))
        self.buttonShowDiaGram.setText(_translate("CommentAnalysis", "图示"))
        self.buttonAnalyse.setText(_translate("CommentAnalysis", "开始分析"))
        self.buttonReturn.setText(_translate("CommentAnalysis", "返回"))
        self.labelExample.setText(_translate("CommentAnalysis", "示例：外观很漂亮，开机非常快，运行流畅，电池耐用，总体来说，性价比很高！"))
        self.labelTip.setText(_translate("CommentAnalysis", "tip: 分析过程请耐心等候哦"))

