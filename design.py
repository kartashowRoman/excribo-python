# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 237)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Text = QtWidgets.QTextBrowser(self.centralwidget)
        self.Text.setObjectName("Text")
        self.verticalLayout.addWidget(self.Text)
        self.Copy = QtWidgets.QPushButton(self.centralwidget)
        self.Copy.setObjectName("Copy")
        self.verticalLayout.addWidget(self.Copy)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Copy.setToolTip(_translate("MainWindow", "<html><head/><body><p>Press the button and highlight the area on your screen to convert img text to txt format</p></body></html>"))
        self.Copy.setText(_translate("MainWindow", "Copy"))
