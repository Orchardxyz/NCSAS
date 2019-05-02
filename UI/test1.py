# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 20:14
# @Author  : JackeyChen
# @FileName: test1.py
# @Software: PyCharm


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QDialog,
                             QDialogButtonBox, QGridLayout, QHBoxLayout, QLabel, QLayout, QLineEdit,
                             QPushButton, QVBoxLayout, QWidget)


class FindDialog (QDialog):
    def __init__(self, parent=None):
        super (FindDialog, self).__init__ (parent)

        label = QLabel ("Find &what:")
        lineEdit = QLineEdit ()
        label.setBuddy (lineEdit)

        caseCheckBox = QCheckBox ("Match &case")
        fromStartCheckBox = QCheckBox ("Search from &start")
        fromStartCheckBox.setChecked (True)

        findButton = QPushButton ("&Find")
        findButton.setDefault (True)

        moreButton = QPushButton ("&More")
        moreButton.setCheckable (True)
        moreButton.setAutoDefault (False)

        extension = QWidget ()

        wholeWordsCheckBox = QCheckBox ("&Whole words")
        backwardCheckBox = QCheckBox ("Search &backward")
        searchSelectionCheckBox = QCheckBox ("Search se&lection")

        buttonBox = QDialogButtonBox (Qt.Vertical)
        buttonBox.addButton (findButton, QDialogButtonBox.ActionRole)
        buttonBox.addButton (moreButton, QDialogButtonBox.ActionRole)

        moreButton.toggled.connect (extension.setVisible)

        extensionLayout = QVBoxLayout ()
        extensionLayout.setContentsMargins (0, 0, 0, 0)
        extensionLayout.addWidget (wholeWordsCheckBox)
        extensionLayout.addWidget (backwardCheckBox)
        extensionLayout.addWidget (searchSelectionCheckBox)
        extension.setLayout (extensionLayout)

        topLeftLayout = QHBoxLayout ()
        topLeftLayout.addWidget (label)
        topLeftLayout.addWidget (lineEdit)

        leftLayout = QVBoxLayout ()
        leftLayout.addLayout (topLeftLayout)
        leftLayout.addWidget (caseCheckBox)
        leftLayout.addWidget (fromStartCheckBox)

        mainLayout = QGridLayout ()
        # 关键性的参数设置
        mainLayout.setSizeConstraint (QLayout.SetFixedSize)

        mainLayout.addLayout (leftLayout, 0, 0)
        mainLayout.addWidget (buttonBox, 0, 1)
        mainLayout.addWidget (extension, 1, 0, 1, 2)
        mainLayout.setRowStretch (2, 1)
        self.setLayout (mainLayout)

        self.setWindowTitle ("Extension")
        extension.hide ()


if __name__ == '__main__':
    import sys

    app = QApplication (sys.argv)
    dialog = FindDialog ()
    dialog.show ()
    sys.exit (app.exec_ ())
