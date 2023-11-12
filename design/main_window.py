# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 120, 681, 401))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_student_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.add_student_btn.setFont(font)
        self.add_student_btn.setObjectName("add_student_btn")
        self.verticalLayout.addWidget(self.add_student_btn)
        self.managment_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.managment_btn.setFont(font)
        self.managment_btn.setObjectName("managment_btn")
        self.verticalLayout.addWidget(self.managment_btn)
        self.format_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.format_btn.setFont(font)
        self.format_btn.setObjectName("format_btn")
        self.verticalLayout.addWidget(self.format_btn)
        self.plagiat_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plagiat_btn.setFont(font)
        self.plagiat_btn.setObjectName("plagiat_btn")
        self.verticalLayout.addWidget(self.plagiat_btn)
        self.marks_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.marks_btn.setFont(font)
        self.marks_btn.setObjectName("marks_btn")
        self.verticalLayout.addWidget(self.marks_btn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.inform_btn = QtWidgets.QPushButton(self.centralwidget)
        self.inform_btn.setGeometry(QtCore.QRect(10, 10, 21, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inform_btn.setFont(font)
        self.inform_btn.setObjectName("inform_btn")
        self.inform_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.inform_edit.setGeometry(QtCore.QRect(20, 40, 131, 121))
        self.inform_edit.setObjectName("inform_edit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Проверка ОГЭ сочинений 2023-2024</span></p></body></html>"))
        self.add_student_btn.setText(_translate("MainWindow", "Добавить ученика"))
        self.managment_btn.setText(_translate("MainWindow", "Критерии оценки сочинения"))
        self.format_btn.setText(_translate("MainWindow", "Проверка сочинения"))
        self.plagiat_btn.setText(_translate("MainWindow", "Плагиат"))
        self.marks_btn.setText(_translate("MainWindow", "Просмотр оценок"))
        self.inform_btn.setText(_translate("MainWindow", "i"))
        self.inform_edit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Данное приложение помогает частично автоматизировать проверку сочинение для ОГЭ. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Также у вас есть возможность занести в базу данных оценки.</p></body></html>"))