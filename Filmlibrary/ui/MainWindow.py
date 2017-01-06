# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Filmlibrary/ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStatusTip("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setStatusTip("")
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionExit.setObjectName("actionExit")
        self.actionCreate = QtWidgets.QAction(MainWindow)
        self.actionCreate.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionCreate.setObjectName("actionCreate")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setEnabled(False)
        self.actionEdit.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionEdit.setObjectName("actionEdit")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setEnabled(False)
        self.actionDelete.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSearch = QtWidgets.QAction(MainWindow)
        self.actionSearch.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionSearch.setObjectName("actionSearch")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionUpdate.setObjectName("actionUpdate")
        self.menu.addAction(self.actionExit)
        self.menu_2.addAction(self.actionUpdate)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionCreate)
        self.menu_2.addAction(self.actionEdit)
        self.menu_2.addAction(self.actionDelete)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionSearch)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Film library"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Фильм"))
        self.actionExit.setText(_translate("MainWindow", "Выход"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Закрыть приложение"))
        self.actionCreate.setText(_translate("MainWindow", "Добавить"))
        self.actionCreate.setStatusTip(_translate("MainWindow", "Добавить фильм"))
        self.actionEdit.setText(_translate("MainWindow", "Редактировать"))
        self.actionEdit.setStatusTip(_translate("MainWindow", "Редактировать выбранный фильм"))
        self.actionDelete.setText(_translate("MainWindow", "Удалить"))
        self.actionDelete.setStatusTip(_translate("MainWindow", "Удалить выбранный фильм"))
        self.actionSearch.setText(_translate("MainWindow", "Поиск"))
        self.actionSearch.setStatusTip(_translate("MainWindow", "Найти фильм"))
        self.actionUpdate.setText(_translate("MainWindow", "Обновить список"))
        self.actionUpdate.setStatusTip(_translate("MainWindow", "Обновить список фильмов"))
