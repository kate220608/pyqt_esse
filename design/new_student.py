# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_student.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewStudentWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(371, 266)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ok_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ok_btn.setGeometry(QtCore.QRect(110, 160, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ok_btn.setFont(font)
        self.ok_btn.setObjectName("ok_btn")
        self.name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_edit.setGeometry(QtCore.QRect(30, 30, 311, 21))
        self.name_edit.setObjectName("name_edit")
        self.add_esse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_esse_btn.setGeometry(QtCore.QRect(110, 70, 131, 23))
        self.add_esse_btn.setObjectName("add_esse_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 371, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ok_btn.setText(_translate("MainWindow", "Готово"))
        self.name_edit.setText(_translate("MainWindow", "Фамилия и имя ученика"))
        self.add_esse_btn.setText(_translate("MainWindow", "Загрузить сочинение"))
