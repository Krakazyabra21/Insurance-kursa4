# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_w.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(617, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.createStr = QtWidgets.QPushButton(self.centralwidget)
        self.createStr.setGeometry(QtCore.QRect(60, 120, 211, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.createStr.setFont(font)
        self.createStr.setObjectName("createStr")
        self.extendStr = QtWidgets.QPushButton(self.centralwidget)
        self.extendStr.setGeometry(QtCore.QRect(360, 120, 211, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setItalic(False)
        self.extendStr.setFont(font)
        self.extendStr.setObjectName("extendStr")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 531, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.exitApp = QtWidgets.QPushButton(self.centralwidget)
        self.exitApp.setGeometry(QtCore.QRect(470, 270, 121, 51))
        self.exitApp.setObjectName("exitApp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.createStr.setText(_translate("MainWindow", "Создать страховку"))
        self.extendStr.setText(_translate("MainWindow", "Продлить страховку"))
        self.label.setText(_translate("MainWindow", "Программа для создания страховок"))
        self.exitApp.setText(_translate("MainWindow", "Закрыть"))