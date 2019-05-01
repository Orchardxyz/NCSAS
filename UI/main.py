# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1036, 720)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1021, 701))
        self.frame.setStyleSheet("* {\n"
"    background-color: #FAFAFA;\n"
"}\n"
"QTabWidget::tab-bar { \n"
"    alignment: center; \n"
"} \n"
"QTabBar::tab {\n"
"    height: 28px;\n"
"    min-width: 85px;\n"
"    margin-right: 5px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabOptions = QtWidgets.QTabWidget(self.frame)
        self.tabOptions.setGeometry(QtCore.QRect(40, 150, 941, 541))
        self.tabOptions.setObjectName("tabOptions")
        self.tabSentiment = QtWidgets.QWidget()
        self.tabSentiment.setObjectName("tabSentiment")
        self.tabOptions.addTab(self.tabSentiment, "")
        self.tabWords = QtWidgets.QWidget()
        self.tabWords.setObjectName("tabWords")
        self.tabOptions.addTab(self.tabWords, "")
        self.tabAttrScore = QtWidgets.QWidget()
        self.tabAttrScore.setObjectName("tabAttrScore")
        self.tabOptions.addTab(self.tabAttrScore, "")
        self.tabComparison = QtWidgets.QWidget()
        self.tabComparison.setObjectName("tabComparison")
        self.tabOptions.addTab(self.tabComparison, "")
        self.tabComments = QtWidgets.QWidget()
        self.tabComments.setObjectName("tabComments")
        self.tableView = QtWidgets.QTableView(self.tabComments)
        self.tableView.setGeometry(QtCore.QRect(30, 80, 871, 401))
        self.tableView.setObjectName("tableView")
        self.comboBox = QtWidgets.QComboBox(self.tabComments)
        self.comboBox.setGeometry(QtCore.QRect(30, 10, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tabOptions.addTab(self.tabComments, "")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(71, 100, 151, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(230, 100, 551, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(810, 100, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.tabOptions.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabOptions.setTabText(self.tabOptions.indexOf(self.tabSentiment), _translate("Form", "语句情感"))
        self.tabOptions.setTabText(self.tabOptions.indexOf(self.tabWords), _translate("Form", "分词标注"))
        self.tabOptions.setTabText(self.tabOptions.indexOf(self.tabAttrScore), _translate("Form", "属性词得分"))
        self.tabOptions.setTabText(self.tabOptions.indexOf(self.tabComparison), _translate("Form", "品牌对比"))
        self.comboBox.setItemText(0, _translate("Form", "惠普好评"))
        self.comboBox.setItemText(1, _translate("Form", "惠普差评"))
        self.comboBox.setItemText(2, _translate("Form", "联想好评"))
        self.comboBox.setItemText(3, _translate("Form", "联想差评"))
        self.tabOptions.setTabText(self.tabOptions.indexOf(self.tabComments), _translate("Form", "品牌评论数据"))
        self.label.setText(_translate("Form", "请在此输入一条评论："))
        self.pushButton.setText(_translate("Form", "开始分析"))

