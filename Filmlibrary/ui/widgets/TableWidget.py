import os

from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtCore import QModelIndex
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QWidget

from Filmlibrary.models.Film import Film
from Filmlibrary.ui.templates import Ui_MainView


class TableWidget(QWidget, Ui_MainView):
    tableHeaders = ["ID", "Диск", "Название", "Год", "Жанр", "Режиссер", "В ролях"]
    selectedRow = None

    def __init__(self, app=None):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.buttonEdit.hide()
        self.buttonDelete.hide()
        self.list.hideColumn(0)
        self.list.setHorizontalHeaderLabels(self.tableHeaders)
        self.list.cellClicked.connect(self.toggleEditButtons)

    def display(self):
        self.buttonEdit.hide()
        self.buttonDelete.hide()
        self.selectedRow = None
        self.list.clearSelection()
        self.loadValues()
        assert isinstance(self.parent(), QStackedWidget)
        self.parent().setCurrentWidget(self)

    def loadValues(self):
        iterator = 0
        films = Film.select()
        self.list.setRowCount(len(films))

        for film in films:
            self.list.setItem(iterator, 0, QTableWidgetItem(str(film.id)))
            self.list.setItem(iterator, 1, QTableWidgetItem(str(film.disk_number)))
            self.list.setItem(iterator, 2, QTableWidgetItem(film.title))
            self.list.setItem(iterator, 3, QTableWidgetItem(str(film.year)))
            self.list.setItem(iterator, 4, QTableWidgetItem(film.genre))
            self.list.setItem(iterator, 5, QTableWidgetItem(film.director))
            self.list.setItem(iterator, 6, QTableWidgetItem(film.role))
            iterator += 1

    def toggleEditButtons(self, row):
        self.selectedRow = row
        self.buttonEdit.show()
        self.buttonDelete.show()
        # print(self.selectedRow)
