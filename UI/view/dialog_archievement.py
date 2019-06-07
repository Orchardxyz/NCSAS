# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_archievement.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Archievements(object):
    def setupUi(self, Archievements):
        Archievements.setObjectName("Archievements")
        Archievements.resize(1129, 775)
        self.frameArchievement = QtWidgets.QFrame(Archievements)
        self.frameArchievement.setGeometry(QtCore.QRect(0, 0, 1121, 771))
        self.frameArchievement.setStyleSheet("")
        self.frameArchievement.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameArchievement.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameArchievement.setObjectName("frameArchievement")
        self.tabArchievements = QtWidgets.QTabWidget(self.frameArchievement)
        self.tabArchievements.setGeometry(QtCore.QRect(20, 10, 1081, 721))
        self.tabArchievements.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabArchievements.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabArchievements.setStyleSheet("/* tab样式 */\n"
"QTabWidget::pane{\n"
"    border: 1px solid rgb(241, 241, 241);\n"
"    border-radius: 10px;\n"
"}\n"
"QTabBar::tab{\n"
"    min-width:95px;\n"
"    min-height:35px;\n"
"}\n"
" \n"
"QTabBar::tab:selected{\n"
"    border: 1px solid;\n"
"    border-bottom: 0;\n"
"    /*border-top-left-radius: 10%;\n"
"    border-top-right-radius: 10%;*/\n"
"    color: #FFF;\n"
"    /*background: rgb(0, 170, 255);*/\n"
"    background: rgb(47, 47, 47);\n"
"    font: bold;\n"
"    font-size: 23px;\n"
"}\n"
" \n"
"QTabBar::tab:!selected{\n"
"    margin-top: 6px;\n"
"    margin-bottom: -7px;\n"
"    color: black;\n"
"    border: 1px solid;\n"
"    /*border-top-left-radius: 10%;\n"
"    border-top-right-radius: 10%;*/\n"
"    border-bottom-color: rgb(241, 241, 241);\n"
"}\n"
"QTabBar::tab:pressed{\n"
"    background: rgb(47, 47, 47);\n"
"}")
        self.tabArchievements.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabArchievements.setTabBarAutoHide(False)
        self.tabArchievements.setObjectName("tabArchievements")
        self.tabPreProcessed = QtWidgets.QWidget()
        self.tabPreProcessed.setObjectName("tabPreProcessed")
        self.tabBrand = QtWidgets.QTabWidget(self.tabPreProcessed)
        self.tabBrand.setGeometry(QtCore.QRect(20, 20, 1041, 661))
        self.tabBrand.setStyleSheet("/* button样式 */\n"
"QPushButton {\n"
"    border: 1px solid;\n"
"    border-radius: 5px;\n"
"    font-size: 40px;\n"
"    font-family: \"KaiTi\";\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgb(209, 209, 209);\n"
"}\n"
"QPushButton:pressed {\n"
"    background: rgb(200, 200, 200);\n"
"}\n"
"/*QPushButton:checked {\n"
"    background: gray;\n"
"}*/\n"
"/* tab样式 */\n"
"QTabWidget::pane\n"
"{\n"
"    border: 1px solid rgb(241, 241, 241);\n"
"    border-radius: 10px;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
" \n"
"QTabBar::tab{\n"
"    min-width:75px;\n"
"    min-height:25px;\n"
"}\n"
" \n"
"QTabBar::tab:selected{\n"
"    border: 1px solid;\n"
"    border-bottom: 0;\n"
"    border-top-left-radius: 10%;\n"
"    border-top-right-radius: 10%;\n"
"    color: black;\n"
"    background: rgb(0, 170, 255);\n"
"    font-size: 20px;\n"
"}\n"
" \n"
"QTabBar::tab:!selected{\n"
"    color: black;\n"
"    border: 1px solid;\n"
"    border-top-left-radius: 10%;\n"
"    border-top-right-radius: 10%;\n"
"    border-bottom-color: rgb(241, 241, 241);\n"
"}\n"
"QTabBar::tab:pressed{\n"
"    background:rgb(102, 184, 255);\n"
"}\n"
"")
        self.tabBrand.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabBrand.setObjectName("tabBrand")
        self.tabLenovo = QtWidgets.QWidget()
        self.tabLenovo.setObjectName("tabLenovo")
        self.frameLenovo = QtWidgets.QFrame(self.tabLenovo)
        self.frameLenovo.setGeometry(QtCore.QRect(10, 10, 1011, 621))
        self.frameLenovo.setStyleSheet("QFrame {\n"
"    background: #FFFFFF;\n"
"}")
        self.frameLenovo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLenovo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLenovo.setObjectName("frameLenovo")
        self.buttonBad = QtWidgets.QPushButton(self.frameLenovo)
        self.buttonBad.setGeometry(QtCore.QRect(40, 320, 61, 151))
        self.buttonBad.setCheckable(False)
        self.buttonBad.setChecked(False)
        self.buttonBad.setObjectName("buttonBad")
        self.stackedWidgetContentLenovo = QtWidgets.QStackedWidget(self.frameLenovo)
        self.stackedWidgetContentLenovo.setGeometry(QtCore.QRect(140, 40, 841, 571))
        self.stackedWidgetContentLenovo.setStyleSheet("QStackedWidget {\n"
"    background: #FFF;\n"
"    border: 1px solid;\n"
"    border-radius: 5px;\n"
"}\n"
"QToolBox::tab {\n"
"    /* 向左渐变 */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                            stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                            stop: 0.5 #D8D8D8, stop: 1 #D3D3D3);\n"
"    /*background: rgb(173, 173, 173);*/\n"
"    border-radius: 3px;\n"
"    /*color: darkgray;*/\n"
"}\n"
"QToolBox::tab:selected {\n"
"    font: bold;\n"
"    color: black;\n"
"    font-size: 19px;\n"
"}\n"
"QToolBoxButton { \n"
"    min-height:30px; \n"
"}")
        self.stackedWidgetContentLenovo.setObjectName("stackedWidgetContentLenovo")
        self.pagePraise = QtWidgets.QWidget()
        self.pagePraise.setObjectName("pagePraise")
        self.toolBoxPraise = QtWidgets.QToolBox(self.pagePraise)
        self.toolBoxPraise.setGeometry(QtCore.QRect(10, 30, 801, 521))
        self.toolBoxPraise.setObjectName("toolBoxPraise")
        self.pageItemComments = QtWidgets.QWidget()
        self.pageItemComments.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemComments.setObjectName("pageItemComments")
        self.tableViewComments = QtWidgets.QTableView(self.pageItemComments)
        self.tableViewComments.setGeometry(QtCore.QRect(0, 0, 801, 411))
        self.tableViewComments.setObjectName("tableViewComments")
        self.toolBoxPraise.addItem(self.pageItemComments, "")
        self.pageItemGetRid = QtWidgets.QWidget()
        self.pageItemGetRid.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemGetRid.setObjectName("pageItemGetRid")
        self.tableViewGetRid = QtWidgets.QTableView(self.pageItemGetRid)
        self.tableViewGetRid.setGeometry(QtCore.QRect(0, 0, 801, 411))
        self.tableViewGetRid.setObjectName("tableViewGetRid")
        self.toolBoxPraise.addItem(self.pageItemGetRid, "")
        self.pageItemTagWords = QtWidgets.QWidget()
        self.pageItemTagWords.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemTagWords.setObjectName("pageItemTagWords")
        self.tableViewTagWords = QtWidgets.QTableView(self.pageItemTagWords)
        self.tableViewTagWords.setGeometry(QtCore.QRect(0, 0, 801, 411))
        self.tableViewTagWords.setObjectName("tableViewTagWords")
        self.toolBoxPraise.addItem(self.pageItemTagWords, "")
        self.stackedWidgetContentLenovo.addWidget(self.pagePraise)
        self.pageBad = QtWidgets.QWidget()
        self.pageBad.setObjectName("pageBad")
        self.toolBoxBad = QtWidgets.QToolBox(self.pageBad)
        self.toolBoxBad.setGeometry(QtCore.QRect(10, 30, 801, 521))
        self.toolBoxBad.setObjectName("toolBoxBad")
        self.pageItemComments_2 = QtWidgets.QWidget()
        self.pageItemComments_2.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemComments_2.setObjectName("pageItemComments_2")
        self.tableViewComments_2 = QtWidgets.QTableView(self.pageItemComments_2)
        self.tableViewComments_2.setGeometry(QtCore.QRect(0, 0, 801, 411))
        self.tableViewComments_2.setObjectName("tableViewComments_2")
        self.toolBoxBad.addItem(self.pageItemComments_2, "")
        self.pageItemGetRid_2 = QtWidgets.QWidget()
        self.pageItemGetRid_2.setGeometry(QtCore.QRect(0, 0, 801, 410))
        self.pageItemGetRid_2.setObjectName("pageItemGetRid_2")
        self.tableViewGetRid_2 = QtWidgets.QTableView(self.pageItemGetRid_2)
        self.tableViewGetRid_2.setGeometry(QtCore.QRect(0, 0, 801, 411))
        self.tableViewGetRid_2.setObjectName("tableViewGetRid_2")
        self.toolBoxBad.addItem(self.pageItemGetRid_2, "")
        self.pageItemTagWords_2 = QtWidgets.QWidget()
        self.pageItemTagWords_2.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemTagWords_2.setObjectName("pageItemTagWords_2")
        self.tableViewTagWords_2 = QtWidgets.QTableView(self.pageItemTagWords_2)
        self.tableViewTagWords_2.setGeometry(QtCore.QRect(0, 0, 801, 421))
        self.tableViewTagWords_2.setObjectName("tableViewTagWords_2")
        self.toolBoxBad.addItem(self.pageItemTagWords_2, "")
        self.stackedWidgetContentLenovo.addWidget(self.pageBad)
        self.buttonPraise = QtWidgets.QPushButton(self.frameLenovo)
        self.buttonPraise.setGeometry(QtCore.QRect(40, 140, 61, 151))
        self.buttonPraise.setCheckable(False)
        self.buttonPraise.setChecked(False)
        self.buttonPraise.setObjectName("buttonPraise")
        self.labelTips = QtWidgets.QLabel(self.frameLenovo)
        self.labelTips.setGeometry(QtCore.QRect(0, 10, 451, 16))
        self.labelTips.setStyleSheet("QLabel {\n"
"    font-size: 17px;\n"
"    font-family: \"KaiTi\"\n"
"}")
        self.labelTips.setObjectName("labelTips")
        self.tabBrand.addTab(self.tabLenovo, "")
        self.tabHp = QtWidgets.QWidget()
        self.tabHp.setObjectName("tabHp")
        self.frameHp = QtWidgets.QFrame(self.tabHp)
        self.frameHp.setGeometry(QtCore.QRect(10, 10, 1011, 621))
        self.frameHp.setStyleSheet("QFrame {\n"
"    background: #FFFFFF;\n"
"}")
        self.frameHp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameHp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameHp.setObjectName("frameHp")
        self.buttonBad_2 = QtWidgets.QPushButton(self.frameHp)
        self.buttonBad_2.setGeometry(QtCore.QRect(40, 320, 61, 151))
        self.buttonBad_2.setObjectName("buttonBad_2")
        self.stackedWidgetContentHp = QtWidgets.QStackedWidget(self.frameHp)
        self.stackedWidgetContentHp.setGeometry(QtCore.QRect(140, 40, 841, 571))
        self.stackedWidgetContentHp.setStyleSheet("QStackedWidget {\n"
"    background: #FFF;\n"
"    border: 1px solid;\n"
"    border-radius: 5px;\n"
"}\n"
"QToolBox::tab {\n"
"    /* 向左渐变 */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                            stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                            stop: 0.5 #D8D8D8, stop: 1 #D3D3D3);\n"
"    /*background: rgb(173, 173, 173);*/\n"
"    border-radius: 3px;\n"
"    /*color: darkgray;*/\n"
"}\n"
"QToolBox::tab:selected {\n"
"    font: bold;\n"
"    color: black;\n"
"    font-size: 19px;\n"
"}\n"
"QToolBoxButton { \n"
"    min-height:30px; \n"
"}")
        self.stackedWidgetContentHp.setObjectName("stackedWidgetContentHp")
        self.pagePraise_2 = QtWidgets.QWidget()
        self.pagePraise_2.setObjectName("pagePraise_2")
        self.toolBoxPraise_2 = QtWidgets.QToolBox(self.pagePraise_2)
        self.toolBoxPraise_2.setGeometry(QtCore.QRect(10, 30, 801, 521))
        self.toolBoxPraise_2.setObjectName("toolBoxPraise_2")
        self.pageItemComments_3 = QtWidgets.QWidget()
        self.pageItemComments_3.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemComments_3.setObjectName("pageItemComments_3")
        self.tableViewComments_3 = QtWidgets.QTableView(self.pageItemComments_3)
        self.tableViewComments_3.setGeometry(QtCore.QRect(0, 0, 801, 411))
        self.tableViewComments_3.setObjectName("tableViewComments_3")
        self.toolBoxPraise_2.addItem(self.pageItemComments_3, "")
        self.pageItemGetRid_3 = QtWidgets.QWidget()
        self.pageItemGetRid_3.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemGetRid_3.setObjectName("pageItemGetRid_3")
        self.tableViewGetRid_3 = QtWidgets.QTableView(self.pageItemGetRid_3)
        self.tableViewGetRid_3.setGeometry(QtCore.QRect(0, 0, 801, 411))
        self.tableViewGetRid_3.setObjectName("tableViewGetRid_3")
        self.toolBoxPraise_2.addItem(self.pageItemGetRid_3, "")
        self.pageItemTagWords_3 = QtWidgets.QWidget()
        self.pageItemTagWords_3.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemTagWords_3.setObjectName("pageItemTagWords_3")
        self.tableViewTagWords_3 = QtWidgets.QTableView(self.pageItemTagWords_3)
        self.tableViewTagWords_3.setGeometry(QtCore.QRect(0, 0, 801, 411))
        self.tableViewTagWords_3.setObjectName("tableViewTagWords_3")
        self.toolBoxPraise_2.addItem(self.pageItemTagWords_3, "")
        self.stackedWidgetContentHp.addWidget(self.pagePraise_2)
        self.pageBad_2 = QtWidgets.QWidget()
        self.pageBad_2.setObjectName("pageBad_2")
        self.toolBoxBad_2 = QtWidgets.QToolBox(self.pageBad_2)
        self.toolBoxBad_2.setGeometry(QtCore.QRect(10, 30, 801, 521))
        self.toolBoxBad_2.setObjectName("toolBoxBad_2")
        self.pageItemComments_4 = QtWidgets.QWidget()
        self.pageItemComments_4.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemComments_4.setObjectName("pageItemComments_4")
        self.tableViewComments_4 = QtWidgets.QTableView(self.pageItemComments_4)
        self.tableViewComments_4.setGeometry(QtCore.QRect(0, 0, 801, 411))
        self.tableViewComments_4.setObjectName("tableViewComments_4")
        self.toolBoxBad_2.addItem(self.pageItemComments_4, "")
        self.pageItemGetRid_4 = QtWidgets.QWidget()
        self.pageItemGetRid_4.setGeometry(QtCore.QRect(0, 0, 801, 410))
        self.pageItemGetRid_4.setObjectName("pageItemGetRid_4")
        self.tableViewGetRid_4 = QtWidgets.QTableView(self.pageItemGetRid_4)
        self.tableViewGetRid_4.setGeometry(QtCore.QRect(0, 0, 801, 411))
        self.tableViewGetRid_4.setObjectName("tableViewGetRid_4")
        self.toolBoxBad_2.addItem(self.pageItemGetRid_4, "")
        self.pageItemTagWords_4 = QtWidgets.QWidget()
        self.pageItemTagWords_4.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemTagWords_4.setObjectName("pageItemTagWords_4")
        self.tableViewTagWords_4 = QtWidgets.QTableView(self.pageItemTagWords_4)
        self.tableViewTagWords_4.setGeometry(QtCore.QRect(0, 0, 801, 421))
        self.tableViewTagWords_4.setObjectName("tableViewTagWords_4")
        self.toolBoxBad_2.addItem(self.pageItemTagWords_4, "")
        self.stackedWidgetContentHp.addWidget(self.pageBad_2)
        self.buttonPraise_2 = QtWidgets.QPushButton(self.frameHp)
        self.buttonPraise_2.setGeometry(QtCore.QRect(40, 140, 61, 151))
        self.buttonPraise_2.setObjectName("buttonPraise_2")
        self.labelTips_2 = QtWidgets.QLabel(self.frameHp)
        self.labelTips_2.setGeometry(QtCore.QRect(0, 10, 451, 16))
        self.labelTips_2.setStyleSheet("QLabel {\n"
"    font-size: 17px;\n"
"    font-family: \"KaiTi\"\n"
"}")
        self.labelTips_2.setObjectName("labelTips_2")
        self.tabBrand.addTab(self.tabHp, "")
        self.tabArchievements.addTab(self.tabPreProcessed, "")
        self.tabBrandComparison = QtWidgets.QWidget()
        self.tabBrandComparison.setObjectName("tabBrandComparison")
        self.brandFrame = QtWidgets.QFrame(self.tabBrandComparison)
        self.brandFrame.setGeometry(QtCore.QRect(-10, -10, 1091, 711))
        self.brandFrame.setStyleSheet("QLabel{\n"
"    \n"
"    font: 60px \"American Typewriter\";\n"
"    font-weight:500;\n"
"}")
        self.brandFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.brandFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.brandFrame.setObjectName("brandFrame")
        self.frameVLenovo = QtWidgets.QFrame(self.brandFrame)
        self.frameVLenovo.setGeometry(QtCore.QRect(10, 10, 561, 80))
        self.frameVLenovo.setStyleSheet("#frameVLenovo {\n"
"    background-color:rgb(179, 179, 179);\n"
"    border: 1px solid;\n"
"    border-right: 0;\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}")
        self.frameVLenovo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameVLenovo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameVLenovo.setObjectName("frameVLenovo")
        self.labelVLenovo = QtWidgets.QLabel(self.frameVLenovo)
        self.labelVLenovo.setGeometry(QtCore.QRect(20, 0, 491, 81))
        self.labelVLenovo.setStyleSheet("")
        self.labelVLenovo.setObjectName("labelVLenovo")
        self.labelV = QtWidgets.QLabel(self.frameVLenovo)
        self.labelV.setGeometry(QtCore.QRect(510, 0, 71, 81))
        self.labelV.setStyleSheet("QLabel{\n"
" background-color:transparent;\n"
"font-size:500%;\n"
"\n"
"    font: 85 60pt \"American Typewriter\";\n"
"font-weight:500;\n"
"}")
        self.labelV.setObjectName("labelV")
        self.frameSHp = QtWidgets.QFrame(self.brandFrame)
        self.frameSHp.setGeometry(QtCore.QRect(570, 10, 511, 80))
        self.frameSHp.setStyleSheet("#frameSHp {\n"
"    background-color:rgb(76, 76, 76);\n"
"    border: 1px solid;\n"
"    border-left: 0;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"}")
        self.frameSHp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSHp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSHp.setObjectName("frameSHp")
        self.labelSHp = QtWidgets.QLabel(self.frameSHp)
        self.labelSHp.setGeometry(QtCore.QRect(60, 0, 371, 81))
        self.labelSHp.setStyleSheet("QLabel{\n"
"color:rgb(230, 230, 230)\n"
"}")
        self.labelSHp.setObjectName("labelSHp")
        self.labelS = QtWidgets.QLabel(self.frameSHp)
        self.labelS.setGeometry(QtCore.QRect(0, -10, 51, 101))
        self.labelS.setStyleSheet("QLabel{\n"
" background-color:transparent;\n"
"    font: 85 60pt \"American Typewriter\";\n"
"font-weight:500;\n"
"color:rgb(179, 179, 179)\n"
"}")
        self.labelS.setObjectName("labelS")
        self.scrollAreaComparison = QtWidgets.QScrollArea(self.brandFrame)
        self.scrollAreaComparison.setGeometry(QtCore.QRect(10, 90, 1071, 601))
        self.scrollAreaComparison.setStyleSheet("QScrollArea {\n"
"    background: #FFF;\n"
"}\n"
"#scrollAreaWidgetContents {\n"
"    background: #FFF;\n"
"}")
        self.scrollAreaComparison.setWidgetResizable(True)
        self.scrollAreaComparison.setObjectName("scrollAreaComparison")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1048, 1300))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 1300))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frameASC = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frameASC.setGeometry(QtCore.QRect(40, 450, 971, 581))
        self.frameASC.setStyleSheet("#frameASC {\n"
"    background: url(\':picture/attr_score_comparison\')\n"
"}")
        self.frameASC.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameASC.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameASC.setObjectName("frameASC")
        self.textEditResultAnalysis = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEditResultAnalysis.setGeometry(QtCore.QRect(40, 1070, 971, 211))
        self.textEditResultAnalysis.setStyleSheet("QTextEdit {\n"
"    border: 0;\n"
"}")
        self.textEditResultAnalysis.setObjectName("textEditResultAnalysis")
        self.ButtonResultAnalysis = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ButtonResultAnalysis.setGeometry(QtCore.QRect(40, 1040, 141, 31))
        self.ButtonResultAnalysis.setStyleSheet("QPushButton {\n"
"    color: #FFF;\n"
"    background: rgb(0, 85, 127);\n"
"    border: 1px solid;\n"
"    border-left: 0;\n"
"    font-size: 25px;\n"
"    border-bottom-right-radius: 15%;\n"
"    border-top-right-radius: 15%;\n"
"    font-family: \"KaiTi\";\n"
"}")
        self.ButtonResultAnalysis.setObjectName("ButtonResultAnalysis")
        self.frameHpLenovoTendency = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frameHpLenovoTendency.setGeometry(QtCore.QRect(40, 0, 971, 461))
        self.frameHpLenovoTendency.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameHpLenovoTendency.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameHpLenovoTendency.setObjectName("frameHpLenovoTendency")
        self.frameLenovoTendency = QtWidgets.QFrame(self.frameHpLenovoTendency)
        self.frameLenovoTendency.setGeometry(QtCore.QRect(0, 0, 521, 451))
        self.frameLenovoTendency.setStyleSheet("#frameLenovoTendency{\n"
"    background: url(\':picture/lenovo_tendency.png\');\n"
"}")
        self.frameLenovoTendency.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLenovoTendency.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLenovoTendency.setObjectName("frameLenovoTendency")
        self.frameHpTendency = QtWidgets.QFrame(self.frameHpLenovoTendency)
        self.frameHpTendency.setGeometry(QtCore.QRect(519, -1, 451, 451))
        self.frameHpTendency.setStyleSheet("#frameHpTendency{\n"
"    background: url(\':picture/hp_tendency.png\');\n"
"}")
        self.frameHpTendency.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameHpTendency.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameHpTendency.setObjectName("frameHpTendency")
        self.scrollAreaComparison.setWidget(self.scrollAreaWidgetContents)
        self.tabArchievements.addTab(self.tabBrandComparison, "")
        self.tabDictionary = QtWidgets.QWidget()
        self.tabDictionary.setObjectName("tabDictionary")
        self.frameDictionary = QtWidgets.QFrame(self.tabDictionary)
        self.frameDictionary.setGeometry(QtCore.QRect(0, 10, 1081, 681))
        self.frameDictionary.setStyleSheet("QFrame{\n"
" background-color: #FFF;\n"
"}\n"
"QPushButton {\n"
"    font-size: 35px;\n"
"    font-family: \"KaiTi\";\n"
"    border-bottom: 1px solid;\n"
"    border-radius: 0;\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgb(209, 209, 209);\n"
"}")
        self.frameDictionary.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDictionary.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDictionary.setObjectName("frameDictionary")
        self.dictNegWords = QtWidgets.QPushButton(self.frameDictionary)
        self.dictNegWords.setGeometry(QtCore.QRect(20, 180, 221, 81))
        self.dictNegWords.setObjectName("dictNegWords")
        self.dictAttributes = QtWidgets.QPushButton(self.frameDictionary)
        self.dictAttributes.setGeometry(QtCore.QRect(20, 100, 221, 81))
        self.dictAttributes.setObjectName("dictAttributes")
        self.dictStopWords = QtWidgets.QPushButton(self.frameDictionary)
        self.dictStopWords.setGeometry(QtCore.QRect(20, 420, 221, 81))
        self.dictStopWords.setObjectName("dictStopWords")
        self.dictConjunctions = QtWidgets.QPushButton(self.frameDictionary)
        self.dictConjunctions.setGeometry(QtCore.QRect(20, 340, 221, 81))
        self.dictConjunctions.setObjectName("dictConjunctions")
        self.dictAdverbs = QtWidgets.QPushButton(self.frameDictionary)
        self.dictAdverbs.setGeometry(QtCore.QRect(20, 260, 221, 81))
        self.dictAdverbs.setObjectName("dictAdverbs")
        self.stackedWidgetDict = QtWidgets.QStackedWidget(self.frameDictionary)
        self.stackedWidgetDict.setGeometry(QtCore.QRect(240, 30, 821, 551))
        self.stackedWidgetDict.setObjectName("stackedWidgetDict")
        self.pageAttr = QtWidgets.QWidget()
        self.pageAttr.setObjectName("pageAttr")
        self.frameAttrDict = QtWidgets.QFrame(self.pageAttr)
        self.frameAttrDict.setGeometry(QtCore.QRect(0, 0, 791, 541))
        self.frameAttrDict.setStyleSheet("QFrame {\n"
"    background: url(\':dictionary/attr_dict.png\');\n"
"}")
        self.frameAttrDict.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameAttrDict.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAttrDict.setObjectName("frameAttrDict")
        self.stackedWidgetDict.addWidget(self.pageAttr)
        self.pageNeg = QtWidgets.QWidget()
        self.pageNeg.setObjectName("pageNeg")
        self.frameNegDict = QtWidgets.QFrame(self.pageNeg)
        self.frameNegDict.setGeometry(QtCore.QRect(0, 0, 791, 541))
        self.frameNegDict.setStyleSheet("QFrame {\n"
"    background: url(\':dictionary/neg_dict.png\');\n"
"}")
        self.frameNegDict.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameNegDict.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameNegDict.setObjectName("frameNegDict")
        self.stackedWidgetDict.addWidget(self.pageNeg)
        self.pageAdv = QtWidgets.QWidget()
        self.pageAdv.setObjectName("pageAdv")
        self.frameAdvDict = QtWidgets.QFrame(self.pageAdv)
        self.frameAdvDict.setGeometry(QtCore.QRect(0, 0, 791, 541))
        self.frameAdvDict.setStyleSheet("QFrame {\n"
"    background: url(\':dictionary/adv_dict.png\');\n"
"}")
        self.frameAdvDict.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameAdvDict.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAdvDict.setObjectName("frameAdvDict")
        self.stackedWidgetDict.addWidget(self.pageAdv)
        self.pageConj = QtWidgets.QWidget()
        self.pageConj.setObjectName("pageConj")
        self.frameConjDict = QtWidgets.QFrame(self.pageConj)
        self.frameConjDict.setGeometry(QtCore.QRect(0, 0, 791, 541))
        self.frameConjDict.setStyleSheet("QFrame {\n"
"    background: url(\':dictionary/conj_dict.png\');\n"
"}")
        self.frameConjDict.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameConjDict.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameConjDict.setObjectName("frameConjDict")
        self.stackedWidgetDict.addWidget(self.pageConj)
        self.pageStop = QtWidgets.QWidget()
        self.pageStop.setObjectName("pageStop")
        self.frameStopDict = QtWidgets.QFrame(self.pageStop)
        self.frameStopDict.setGeometry(QtCore.QRect(0, 0, 791, 541))
        self.frameStopDict.setStyleSheet("QFrame {\n"
"    background: url(\':dictionary/stop_dict.png\');\n"
"}")
        self.frameStopDict.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameStopDict.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameStopDict.setObjectName("frameStopDict")
        self.stackedWidgetDict.addWidget(self.pageStop)
        self.pushButton = QtWidgets.QPushButton(self.frameDictionary)
        self.pushButton.setGeometry(QtCore.QRect(940, 580, 111, 28))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    font-size: 20px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButtonExplain = QtWidgets.QPushButton(self.frameDictionary)
        self.pushButtonExplain.setGeometry(QtCore.QRect(820, 580, 111, 28))
        self.pushButtonExplain.setStyleSheet("QPushButton {\n"
"    font-size: 20px;\n"
"}")
        self.pushButtonExplain.setObjectName("pushButtonExplain")
        self.tabArchievements.addTab(self.tabDictionary, "")
        self.buttonReturn = QtWidgets.QPushButton(self.frameArchievement)
        self.buttonReturn.setGeometry(QtCore.QRect(1020, 740, 93, 28))
        self.buttonReturn.setStyleSheet("QPushButton {\n"
"    border: 1px solid;\n"
"    border-radius: 5px;\n"
"}")
        self.buttonReturn.setObjectName("buttonReturn")

        self.retranslateUi(Archievements)
        self.tabArchievements.setCurrentIndex(1)
        self.tabBrand.setCurrentIndex(1)
        self.stackedWidgetContentLenovo.setCurrentIndex(1)
        self.toolBoxPraise.setCurrentIndex(1)
        self.toolBoxBad.setCurrentIndex(1)
        self.stackedWidgetContentHp.setCurrentIndex(1)
        self.toolBoxPraise_2.setCurrentIndex(1)
        self.toolBoxBad_2.setCurrentIndex(1)
        self.stackedWidgetDict.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Archievements)
        Archievements.setTabOrder(self.tabArchievements, self.buttonReturn)
        Archievements.setTabOrder(self.buttonReturn, self.tabBrand)
        Archievements.setTabOrder(self.tabBrand, self.buttonBad)
        Archievements.setTabOrder(self.buttonBad, self.tableViewComments)
        Archievements.setTabOrder(self.tableViewComments, self.tableViewGetRid)
        Archievements.setTabOrder(self.tableViewGetRid, self.tableViewTagWords)
        Archievements.setTabOrder(self.tableViewTagWords, self.tableViewComments_2)
        Archievements.setTabOrder(self.tableViewComments_2, self.tableViewGetRid_2)
        Archievements.setTabOrder(self.tableViewGetRid_2, self.tableViewTagWords_2)
        Archievements.setTabOrder(self.tableViewTagWords_2, self.buttonPraise)
        Archievements.setTabOrder(self.buttonPraise, self.buttonBad_2)
        Archievements.setTabOrder(self.buttonBad_2, self.tableViewComments_3)
        Archievements.setTabOrder(self.tableViewComments_3, self.tableViewGetRid_3)
        Archievements.setTabOrder(self.tableViewGetRid_3, self.tableViewTagWords_3)
        Archievements.setTabOrder(self.tableViewTagWords_3, self.tableViewComments_4)
        Archievements.setTabOrder(self.tableViewComments_4, self.tableViewGetRid_4)
        Archievements.setTabOrder(self.tableViewGetRid_4, self.tableViewTagWords_4)
        Archievements.setTabOrder(self.tableViewTagWords_4, self.buttonPraise_2)
        Archievements.setTabOrder(self.buttonPraise_2, self.dictNegWords)
        Archievements.setTabOrder(self.dictNegWords, self.dictAttributes)
        Archievements.setTabOrder(self.dictAttributes, self.dictStopWords)
        Archievements.setTabOrder(self.dictStopWords, self.dictConjunctions)
        Archievements.setTabOrder(self.dictConjunctions, self.dictAdverbs)

    def retranslateUi(self, Archievements):
        _translate = QtCore.QCoreApplication.translate
        Archievements.setWindowTitle(_translate("Archievements", "Dialog"))
        self.buttonBad.setText(_translate("Archievements", "差\n"
"评"))
        self.toolBoxPraise.setItemText(self.toolBoxPraise.indexOf(self.pageItemComments), _translate("Archievements", "原评论"))
        self.toolBoxPraise.setItemText(self.toolBoxPraise.indexOf(self.pageItemGetRid), _translate("Archievements", "过滤无效评论"))
        self.toolBoxPraise.setItemText(self.toolBoxPraise.indexOf(self.pageItemTagWords), _translate("Archievements", "分词标注"))
        self.toolBoxBad.setItemText(self.toolBoxBad.indexOf(self.pageItemComments_2), _translate("Archievements", "原评论"))
        self.toolBoxBad.setItemText(self.toolBoxBad.indexOf(self.pageItemGetRid_2), _translate("Archievements", "过滤无效评论"))
        self.toolBoxBad.setItemText(self.toolBoxBad.indexOf(self.pageItemTagWords_2), _translate("Archievements", "分词标注"))
        self.buttonPraise.setText(_translate("Archievements", "好\n"
"评"))
        self.labelTips.setText(_translate("Archievements", "tip:点击不同按钮即可选择查看不同评价的预处理数据"))
        self.tabBrand.setTabText(self.tabBrand.indexOf(self.tabLenovo), _translate("Archievements", "联想"))
        self.buttonBad_2.setText(_translate("Archievements", "差\n"
"评"))
        self.toolBoxPraise_2.setItemText(self.toolBoxPraise_2.indexOf(self.pageItemComments_3), _translate("Archievements", "原评论"))
        self.toolBoxPraise_2.setItemText(self.toolBoxPraise_2.indexOf(self.pageItemGetRid_3), _translate("Archievements", "过滤无效评论"))
        self.toolBoxPraise_2.setItemText(self.toolBoxPraise_2.indexOf(self.pageItemTagWords_3), _translate("Archievements", "分词标注"))
        self.toolBoxBad_2.setItemText(self.toolBoxBad_2.indexOf(self.pageItemComments_4), _translate("Archievements", "原评论"))
        self.toolBoxBad_2.setItemText(self.toolBoxBad_2.indexOf(self.pageItemGetRid_4), _translate("Archievements", "过滤无效评论"))
        self.toolBoxBad_2.setItemText(self.toolBoxBad_2.indexOf(self.pageItemTagWords_4), _translate("Archievements", "分词标注"))
        self.buttonPraise_2.setText(_translate("Archievements", "好\n"
"评"))
        self.labelTips_2.setText(_translate("Archievements", "tip:点击不同按钮即可选择查看不同评价的预处理数据"))
        self.tabBrand.setTabText(self.tabBrand.indexOf(self.tabHp), _translate("Archievements", "惠普"))
        self.tabArchievements.setTabText(self.tabArchievements.indexOf(self.tabPreProcessed), _translate("Archievements", "预处理"))
        self.labelVLenovo.setText(_translate("Archievements", "联想Lenovo笔记本"))
        self.labelV.setText(_translate("Archievements", "V"))
        self.labelSHp.setText(_translate("Archievements", "惠普HP笔记本"))
        self.labelS.setText(_translate("Archievements", "S"))
        self.textEditResultAnalysis.setHtml(_translate("Archievements", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:14pt;\">    通过粗粒度分析可以看出二者在相同数据量的前提下其好评率与差评率都相差无几，而通过细粒度的属性评分方法，可以得到联想和惠普各自的属性评分。这里只选择其中主要的25个属性词进行对比，得到结果如图所示。从结果可以看出，品牌属性的评分均在[-1,1]区间内浮动，惠普笔记本的内存、屏幕、硬盘、运行等评价属性的正向情感倾向均比联想的笔记本的高，但从鼠标、做工、散热等评价属性得分可以看出，联想笔记本更胜一筹。从总体上来说，惠普笔记本的硬件设备受到更多的好评。</span></p></body></html>"))
        self.ButtonResultAnalysis.setText(_translate("Archievements", "结果与分析"))
        self.tabArchievements.setTabText(self.tabArchievements.indexOf(self.tabBrandComparison), _translate("Archievements", "品牌对比"))
        self.dictNegWords.setText(_translate("Archievements", "否定词词典"))
        self.dictAttributes.setText(_translate("Archievements", "属性词词典"))
        self.dictStopWords.setText(_translate("Archievements", "停用词词典"))
        self.dictConjunctions.setText(_translate("Archievements", "连接词词典"))
        self.dictAdverbs.setText(_translate("Archievements", "副词词典"))
        self.pushButton.setText(_translate("Archievements", "打开源文件"))
        self.pushButtonExplain.setText(_translate("Archievements", "词典说明"))
        self.tabArchievements.setTabText(self.tabArchievements.indexOf(self.tabDictionary), _translate("Archievements", "词典"))
        self.buttonReturn.setText(_translate("Archievements", "返回"))

import resource.file.picture.attr_score_comparison
import resource.file.picture.dictionary
