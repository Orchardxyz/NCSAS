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
        Archievements.resize(1120, 775)
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
        self.tableViewComments.setGeometry(QtCore.QRect(0, 0, 801, 391))
        self.tableViewComments.setObjectName("tableViewComments")
        self.toolBoxPraise.addItem(self.pageItemComments, "")
        self.pageItemGetRid = QtWidgets.QWidget()
        self.pageItemGetRid.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemGetRid.setObjectName("pageItemGetRid")
        self.tableViewGetRid = QtWidgets.QTableView(self.pageItemGetRid)
        self.tableViewGetRid.setGeometry(QtCore.QRect(0, 0, 801, 391))
        self.tableViewGetRid.setObjectName("tableViewGetRid")
        self.toolBoxPraise.addItem(self.pageItemGetRid, "")
        self.pageItemTagWords = QtWidgets.QWidget()
        self.pageItemTagWords.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemTagWords.setObjectName("pageItemTagWords")
        self.tableViewTagWords = QtWidgets.QTableView(self.pageItemTagWords)
        self.tableViewTagWords.setGeometry(QtCore.QRect(0, 0, 801, 391))
        self.tableViewTagWords.setObjectName("tableViewTagWords")
        self.toolBoxPraise.addItem(self.pageItemTagWords, "")
        self.pageItemAttrScore = QtWidgets.QWidget()
        self.pageItemAttrScore.setGeometry(QtCore.QRect(0, 0, 801, 373))
        self.pageItemAttrScore.setObjectName("pageItemAttrScore")
        self.toolBoxPraise.addItem(self.pageItemAttrScore, "")
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
        self.tableViewComments_2.setGeometry(QtCore.QRect(0, 0, 801, 371))
        self.tableViewComments_2.setObjectName("tableViewComments_2")
        self.toolBoxBad.addItem(self.pageItemComments_2, "")
        self.pageItemGetRid_2 = QtWidgets.QWidget()
        self.pageItemGetRid_2.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemGetRid_2.setObjectName("pageItemGetRid_2")
        self.tableViewGetRid_2 = QtWidgets.QTableView(self.pageItemGetRid_2)
        self.tableViewGetRid_2.setGeometry(QtCore.QRect(0, 0, 801, 371))
        self.tableViewGetRid_2.setObjectName("tableViewGetRid_2")
        self.toolBoxBad.addItem(self.pageItemGetRid_2, "")
        self.pageItemTagWords_2 = QtWidgets.QWidget()
        self.pageItemTagWords_2.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemTagWords_2.setObjectName("pageItemTagWords_2")
        self.tableViewTagWords_2 = QtWidgets.QTableView(self.pageItemTagWords_2)
        self.tableViewTagWords_2.setGeometry(QtCore.QRect(0, 0, 801, 371))
        self.tableViewTagWords_2.setObjectName("tableViewTagWords_2")
        self.toolBoxBad.addItem(self.pageItemTagWords_2, "")
        self.pageItemAttrScore_2 = QtWidgets.QWidget()
        self.pageItemAttrScore_2.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemAttrScore_2.setObjectName("pageItemAttrScore_2")
        self.toolBoxBad.addItem(self.pageItemAttrScore_2, "")
        self.stackedWidgetContentLenovo.addWidget(self.pageBad)
        self.buttonPraise = QtWidgets.QPushButton(self.frameLenovo)
        self.buttonPraise.setGeometry(QtCore.QRect(40, 140, 61, 151))
        self.buttonPraise.setCheckable(False)
        self.buttonPraise.setChecked(False)
        self.buttonPraise.setObjectName("buttonPraise")
        self.labelTips = QtWidgets.QLabel(self.frameLenovo)
        self.labelTips.setGeometry(QtCore.QRect(0, 10, 381, 16))
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
        self.tableViewComments_3.setGeometry(QtCore.QRect(0, 0, 801, 371))
        self.tableViewComments_3.setObjectName("tableViewComments_3")
        self.toolBoxPraise_2.addItem(self.pageItemComments_3, "")
        self.pageItemGetRid_3 = QtWidgets.QWidget()
        self.pageItemGetRid_3.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemGetRid_3.setObjectName("pageItemGetRid_3")
        self.tableViewGetRid_3 = QtWidgets.QTableView(self.pageItemGetRid_3)
        self.tableViewGetRid_3.setGeometry(QtCore.QRect(0, 0, 801, 371))
        self.tableViewGetRid_3.setObjectName("tableViewGetRid_3")
        self.toolBoxPraise_2.addItem(self.pageItemGetRid_3, "")
        self.pageItemTagWords_3 = QtWidgets.QWidget()
        self.pageItemTagWords_3.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemTagWords_3.setObjectName("pageItemTagWords_3")
        self.tableViewTagWords_3 = QtWidgets.QTableView(self.pageItemTagWords_3)
        self.tableViewTagWords_3.setGeometry(QtCore.QRect(0, 0, 801, 371))
        self.tableViewTagWords_3.setObjectName("tableViewTagWords_3")
        self.toolBoxPraise_2.addItem(self.pageItemTagWords_3, "")
        self.pageItemAttrScore_3 = QtWidgets.QWidget()
        self.pageItemAttrScore_3.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemAttrScore_3.setObjectName("pageItemAttrScore_3")
        self.toolBoxPraise_2.addItem(self.pageItemAttrScore_3, "")
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
        self.tableViewComments_4.setGeometry(QtCore.QRect(0, 0, 801, 371))
        self.tableViewComments_4.setObjectName("tableViewComments_4")
        self.toolBoxBad_2.addItem(self.pageItemComments_4, "")
        self.pageItemGetRid_4 = QtWidgets.QWidget()
        self.pageItemGetRid_4.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemGetRid_4.setObjectName("pageItemGetRid_4")
        self.tableViewGetRid_4 = QtWidgets.QTableView(self.pageItemGetRid_4)
        self.tableViewGetRid_4.setGeometry(QtCore.QRect(0, 0, 801, 371))
        self.tableViewGetRid_4.setObjectName("tableViewGetRid_4")
        self.toolBoxBad_2.addItem(self.pageItemGetRid_4, "")
        self.pageItemTagWords_4 = QtWidgets.QWidget()
        self.pageItemTagWords_4.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemTagWords_4.setObjectName("pageItemTagWords_4")
        self.tableViewTagWords_4 = QtWidgets.QTableView(self.pageItemTagWords_4)
        self.tableViewTagWords_4.setGeometry(QtCore.QRect(0, 0, 801, 371))
        self.tableViewTagWords_4.setObjectName("tableViewTagWords_4")
        self.toolBoxBad_2.addItem(self.pageItemTagWords_4, "")
        self.pageItemAttrScore_4 = QtWidgets.QWidget()
        self.pageItemAttrScore_4.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.pageItemAttrScore_4.setObjectName("pageItemAttrScore_4")
        self.toolBoxBad_2.addItem(self.pageItemAttrScore_4, "")
        self.stackedWidgetContentHp.addWidget(self.pageBad_2)
        self.buttonPraise_2 = QtWidgets.QPushButton(self.frameHp)
        self.buttonPraise_2.setGeometry(QtCore.QRect(40, 140, 61, 151))
        self.buttonPraise_2.setObjectName("buttonPraise_2")
        self.labelTips_2 = QtWidgets.QLabel(self.frameHp)
        self.labelTips_2.setGeometry(QtCore.QRect(0, 10, 381, 16))
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
        self.frame = QtWidgets.QFrame(self.brandFrame)
        self.frame.setGeometry(QtCore.QRect(10, 90, 1071, 611))
        self.frame.setStyleSheet("QFrame{\n"
" background-color:rgb(255, 255, 255)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
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
        self.labelV.setGeometry(QtCore.QRect(510, 0, 51, 81))
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
        self.tabArchievements.addTab(self.tabBrandComparison, "")
        self.tabDictionary = QtWidgets.QWidget()
        self.tabDictionary.setObjectName("tabDictionary")
        self.frameDictionary = QtWidgets.QFrame(self.tabDictionary)
        self.frameDictionary.setGeometry(QtCore.QRect(0, 10, 1081, 681))
        self.frameDictionary.setStyleSheet("/*QPushButton{\n"
"    background:rgb(204, 204, 204);\n"
"\n"
"    \n"
"    font: 75 20pt \"Helvetica Neue\";\n"
"\n"
"font-weight:500;\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: rgb(230, 230, 230)\n"
"}\n"
"\n"
"QFrame{\n"
" background-color:rgb(255, 255, 255)\n"
"}*/\n"
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
        self.dictSentiment = QtWidgets.QPushButton(self.frameDictionary)
        self.dictSentiment.setGeometry(QtCore.QRect(0, 170, 221, 81))
        self.dictSentiment.setObjectName("dictSentiment")
        self.dictAttributes = QtWidgets.QPushButton(self.frameDictionary)
        self.dictAttributes.setGeometry(QtCore.QRect(0, 90, 221, 81))
        self.dictAttributes.setObjectName("dictAttributes")
        self.dictStopWords = QtWidgets.QPushButton(self.frameDictionary)
        self.dictStopWords.setGeometry(QtCore.QRect(0, 410, 221, 81))
        self.dictStopWords.setObjectName("dictStopWords")
        self.dictConjunctions = QtWidgets.QPushButton(self.frameDictionary)
        self.dictConjunctions.setGeometry(QtCore.QRect(0, 330, 221, 81))
        self.dictConjunctions.setObjectName("dictConjunctions")
        self.dictAdverbs = QtWidgets.QPushButton(self.frameDictionary)
        self.dictAdverbs.setGeometry(QtCore.QRect(0, 250, 221, 81))
        self.dictAdverbs.setObjectName("dictAdverbs")
        self.textBrowser = QtWidgets.QTextBrowser(self.frameDictionary)
        self.textBrowser.setGeometry(QtCore.QRect(230, 50, 791, 591))
        self.textBrowser.setObjectName("textBrowser")
        self.tabArchievements.addTab(self.tabDictionary, "")
        self.buttonReturn = QtWidgets.QPushButton(self.frameArchievement)
        self.buttonReturn.setGeometry(QtCore.QRect(1020, 740, 93, 28))
        self.buttonReturn.setStyleSheet("QPushButton {\n"
"    border: 1px solid;\n"
"    border-radius: 5px;\n"
"}")
        self.buttonReturn.setObjectName("buttonReturn")

        self.retranslateUi(Archievements)
        self.tabArchievements.setCurrentIndex(2)
        self.tabBrand.setCurrentIndex(0)
        self.stackedWidgetContentLenovo.setCurrentIndex(0)
        self.toolBoxPraise.setCurrentIndex(3)
        self.toolBoxBad.setCurrentIndex(3)
        self.stackedWidgetContentHp.setCurrentIndex(1)
        self.toolBoxPraise_2.setCurrentIndex(2)
        self.toolBoxBad_2.setCurrentIndex(3)
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
        Archievements.setTabOrder(self.buttonPraise_2, self.dictSentiment)
        Archievements.setTabOrder(self.dictSentiment, self.dictAttributes)
        Archievements.setTabOrder(self.dictAttributes, self.dictStopWords)
        Archievements.setTabOrder(self.dictStopWords, self.dictConjunctions)
        Archievements.setTabOrder(self.dictConjunctions, self.dictAdverbs)
        Archievements.setTabOrder(self.dictAdverbs, self.textBrowser)

    def retranslateUi(self, Archievements):
        _translate = QtCore.QCoreApplication.translate
        Archievements.setWindowTitle(_translate("Archievements", "Dialog"))
        self.buttonBad.setText(_translate("Archievements", "差\n"
"评"))
        self.toolBoxPraise.setItemText(self.toolBoxPraise.indexOf(self.pageItemComments), _translate("Archievements", "原评论"))
        self.toolBoxPraise.setItemText(self.toolBoxPraise.indexOf(self.pageItemGetRid), _translate("Archievements", "去重"))
        self.toolBoxPraise.setItemText(self.toolBoxPraise.indexOf(self.pageItemTagWords), _translate("Archievements", "分词标注"))
        self.toolBoxPraise.setItemText(self.toolBoxPraise.indexOf(self.pageItemAttrScore), _translate("Archievements", "属性词得分"))
        self.toolBoxBad.setItemText(self.toolBoxBad.indexOf(self.pageItemComments_2), _translate("Archievements", "原评论"))
        self.toolBoxBad.setItemText(self.toolBoxBad.indexOf(self.pageItemGetRid_2), _translate("Archievements", "去重"))
        self.toolBoxBad.setItemText(self.toolBoxBad.indexOf(self.pageItemTagWords_2), _translate("Archievements", "分词标注"))
        self.toolBoxBad.setItemText(self.toolBoxBad.indexOf(self.pageItemAttrScore_2), _translate("Archievements", "属性词得分"))
        self.buttonPraise.setText(_translate("Archievements", "好\n"
"评"))
        self.labelTips.setText(_translate("Archievements", "(•ᴗ•)点击不同按钮即可选择查看不同评价的预处理数据"))
        self.tabBrand.setTabText(self.tabBrand.indexOf(self.tabLenovo), _translate("Archievements", "联想"))
        self.buttonBad_2.setText(_translate("Archievements", "差\n"
"评"))
        self.toolBoxPraise_2.setItemText(self.toolBoxPraise_2.indexOf(self.pageItemComments_3), _translate("Archievements", "原评论"))
        self.toolBoxPraise_2.setItemText(self.toolBoxPraise_2.indexOf(self.pageItemGetRid_3), _translate("Archievements", "去重"))
        self.toolBoxPraise_2.setItemText(self.toolBoxPraise_2.indexOf(self.pageItemTagWords_3), _translate("Archievements", "分词标注"))
        self.toolBoxPraise_2.setItemText(self.toolBoxPraise_2.indexOf(self.pageItemAttrScore_3), _translate("Archievements", "属性词得分"))
        self.toolBoxBad_2.setItemText(self.toolBoxBad_2.indexOf(self.pageItemComments_4), _translate("Archievements", "原评论"))
        self.toolBoxBad_2.setItemText(self.toolBoxBad_2.indexOf(self.pageItemGetRid_4), _translate("Archievements", "去重"))
        self.toolBoxBad_2.setItemText(self.toolBoxBad_2.indexOf(self.pageItemTagWords_4), _translate("Archievements", "分词标注"))
        self.toolBoxBad_2.setItemText(self.toolBoxBad_2.indexOf(self.pageItemAttrScore_4), _translate("Archievements", "属性词得分"))
        self.buttonPraise_2.setText(_translate("Archievements", "好\n"
"评"))
        self.labelTips_2.setText(_translate("Archievements", "(•ᴗ•)点击不同按钮即可选择查看不同评价的预处理数据"))
        self.tabBrand.setTabText(self.tabBrand.indexOf(self.tabHp), _translate("Archievements", "惠普"))
        self.tabArchievements.setTabText(self.tabArchievements.indexOf(self.tabPreProcessed), _translate("Archievements", "预处理"))
        self.labelVLenovo.setText(_translate("Archievements", "联想Lenovo笔记本"))
        self.labelV.setText(_translate("Archievements", "V"))
        self.labelSHp.setText(_translate("Archievements", "惠普HP笔记本"))
        self.labelS.setText(_translate("Archievements", "S"))
        self.tabArchievements.setTabText(self.tabArchievements.indexOf(self.tabBrandComparison), _translate("Archievements", "品牌对比"))
        self.dictSentiment.setText(_translate("Archievements", "情感词典"))
        self.dictAttributes.setText(_translate("Archievements", "属性词词典"))
        self.dictStopWords.setText(_translate("Archievements", "停用词词典"))
        self.dictConjunctions.setText(_translate("Archievements", "连接词词典"))
        self.dictAdverbs.setText(_translate("Archievements", "副词词典"))
        self.tabArchievements.setTabText(self.tabArchievements.indexOf(self.tabDictionary), _translate("Archievements", "词典"))
        self.buttonReturn.setText(_translate("Archievements", "返回"))

