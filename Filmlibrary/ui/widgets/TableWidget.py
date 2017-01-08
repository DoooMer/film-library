from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QWidget

from Filmlibrary.models.Film import Film
from Filmlibrary.ui.templates import Ui_MainView


class TableWidget(QWidget, Ui_MainView):
    tableHeaders = ["ID", "Диск", "Название", "Год", "Жанр", "Режиссер", "В ролях"]

    def __init__(self, app=None):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.list.hideColumn(0)
        self.list.setHorizontalHeaderLabels(self.tableHeaders)

    def display(self):
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
