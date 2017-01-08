# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Filmlibrary/ui/mainview.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainView(object):
    def setupUi(self, MainView):
        MainView.setObjectName("MainView")
        MainView.resize(800, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainView.sizePolicy().hasHeightForWidth())
        MainView.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtWidgets.QWidget(MainView)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 40, 801, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(20, 10, 20, 20)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.list = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list.sizePolicy().hasHeightForWidth())
        self.list.setSizePolicy(sizePolicy)
        self.list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.list.setColumnCount(7)
        self.list.setObjectName("list")
        self.list.setRowCount(0)
        self.verticalLayout.addWidget(self.list)
        self.buttonAdd = QtWidgets.QPushButton(MainView)
        self.buttonAdd.setGeometry(QtCore.QRect(20, 10, 131, 27))
        self.buttonAdd.setObjectName("buttonAdd")
        self.buttonFind = QtWidgets.QPushButton(MainView)
        self.buttonFind.setGeometry(QtCore.QRect(170, 10, 131, 27))
        self.buttonFind.setObjectName("buttonFind")

        self.retranslateUi(MainView)
        QtCore.QMetaObject.connectSlotsByName(MainView)

    def retranslateUi(self, MainView):
        _translate = QtCore.QCoreApplication.translate
        MainView.setWindowTitle(_translate("MainView", "Form"))
        self.buttonAdd.setText(_translate("MainView", "Добавить"))
        self.buttonFind.setText(_translate("MainView", "Найти"))

