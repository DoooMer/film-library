# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Filmlibrary/ui/openview.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OpenView(object):
    def setupUi(self, OpenView):
        OpenView.setObjectName("OpenView")
        OpenView.resize(640, 480)
        self.staticText = QtWidgets.QLabel(OpenView)
        self.staticText.setGeometry(QtCore.QRect(30, 30, 381, 17))
        self.staticText.setObjectName("staticText")
        self.buttonCreate = QtWidgets.QPushButton(OpenView)
        self.buttonCreate.setGeometry(QtCore.QRect(30, 70, 99, 27))
        self.buttonCreate.setObjectName("buttonCreate")
        self.buttonOpen = QtWidgets.QPushButton(OpenView)
        self.buttonOpen.setGeometry(QtCore.QRect(160, 70, 99, 27))
        self.buttonOpen.setObjectName("buttonOpen")

        self.retranslateUi(OpenView)
        QtCore.QMetaObject.connectSlotsByName(OpenView)

    def retranslateUi(self, OpenView):
        _translate = QtCore.QCoreApplication.translate
        OpenView.setWindowTitle(_translate("OpenView", "Form"))
        self.staticText.setText(_translate("OpenView", "Создайте новый или выберите существующий файл"))
        self.buttonCreate.setText(_translate("OpenView", "Создать..."))
        self.buttonCreate.setShortcut(_translate("OpenView", "Ctrl+N"))
        self.buttonOpen.setText(_translate("OpenView", "Открыть..."))
        self.buttonOpen.setShortcut(_translate("OpenView", "Ctrl+O"))

