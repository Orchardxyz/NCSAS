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
        Form.resize(1043, 662)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1041, 661))
        self.frame.setStyleSheet("* {\n"
"    background-color: #FAFAFA;\n"
"}\n"
"QTabWidget::tab-bar { \n"
"    alignment: center; \n"
"} ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.mainModule = QtWidgets.QTabWidget(self.frame)
        self.mainModule.setGeometry(QtCore.QRect(30, 30, 981, 611))
        self.mainModule.setStyleSheet("QTabWidget {\n"
"    border-radius: 5px;\n"
"}")
        self.mainModule.setTabPosition(QtWidgets.QTabWidget.North)
        self.mainModule.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.mainModule.setObjectName("mainModule")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(740, 30, 93, 28))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    font-size: 18px;\n"
"    font-style: bold;\n"
"    background: #6495ED;\n"
"    border-style: outset;\n"
"    border-radius: 10px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 30, 571, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    border: 1px solid;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.frameAnalysisResult = QtWidgets.QFrame(self.tab_3)
        self.frameAnalysisResult.setGeometry(QtCore.QRect(100, 80, 801, 461))
        self.frameAnalysisResult.setStyleSheet("QFrame {\n"
"    background-color: white;\n"
"    border-radius: 5px;\n"
"}")
        self.frameAnalysisResult.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameAnalysisResult.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAnalysisResult.setObjectName("frameAnalysisResult")
        self.mainModule.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabOptions = QtWidgets.QTabWidget(self.tab_4)
        self.tabOptions.setGeometry(QtCore.QRect(40, 20, 911, 561))
        self.tabOptions.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabOptions.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabOptions.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabOptions.setObjectName("tabOptions")
        self.tabOverall = QtWidgets.QWidget()
        self.tabOverall.setObjectName("tabOverall")
        self.tabOptions.addTab(self.tabOverall, "")
        self.tabFilter = QtWidgets.QWidget()
        self.tabFilter.setObjectName("tabFilter")
        self.tabOptions.addTab(self.tabFilter, "")
        self.tabWords = QtWidgets.QWidget()
        self.tabWords.setObjectName("tabWords")
        self.tabOptions.addTab(self.tabWords, "")
        self.tabAttrScore = QtWidgets.QWidget()
        self.tabAttrScore.setObjectName("tabAttrScore")
        self.tabOptions.addTab(self.tabAttrScore, "")
        self.tabComments = QtWidgets.QWidget()
        self.tabComments.setObjectName("tabComments")
        self.tableView = QtWidgets.QTableView(self.tabComments)
        self.tableView.setGeometry(QtCore.QRect(20, 50, 871, 461))
        self.tableView.setObjectName("tableView")
        self.comboBox = QtWidgets.QComboBox(self.tabComments)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 87, 22))
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tabOptions.addTab(self.tabComments, "")
        self.mainModule.addTab(self.tab_4, "")

        self.retranslateUi(Form)
        self.mainModule.setCurrentIndex(0)
        self.tabOptions.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "开始分析"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "请在此输入一条或一段有关笔记本电脑的评论"))
        self.mainModule.setTabText(self.mainModule.indexOf(self.tab_3), _translate("Form", "评价分析"))
        self.tabOptions.setTabText(self.tabOptions.indexOf(self.tabOverall), _translate("Form", "整体极性"))
        self.tabOptions.setTabText(self.tabOptions.indexOf(self.tabFilter), _translate("Form", "去重"))
        self.tabOptions.setTabText(self.tabOptions.indexOf(self.tabWords), _translate("Form", "分词标注"))
        self.tabOptions.setTabText(self.tabOptions.indexOf(self.tabAttrScore), _translate("Form", "属性词得分"))
        self.comboBox.setItemText(0, _translate("Form", "惠普好评"))
        self.comboBox.setItemText(1, _translate("Form", "惠普差评"))
        self.comboBox.setItemText(2, _translate("Form", "联想好评"))
        self.comboBox.setItemText(3, _translate("Form", "联想差评"))
        self.tabOptions.setTabText(self.tabOptions.indexOf(self.tabComments), _translate("Form", "品牌评论数据"))
        self.mainModule.setTabText(self.mainModule.indexOf(self.tab_4), _translate("Form", "品牌对比"))

