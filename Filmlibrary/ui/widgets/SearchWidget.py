from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QWidget
from peewee import Expression

from Filmlibrary.models.Film import Film
from Filmlibrary.ui.templates import Ui_SearchForm


class SearchWidget(QWidget, Ui_SearchForm):
    tableHeaders = ["ID", "Диск", "Название", "Год", "Жанр", "Режиссер", "В ролях"]
    selectedFilmId = None

    def __init__(self, app=None):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.result.hideColumn(0)
        self.result.setHorizontalHeaderLabels(self.tableHeaders)
        self.result.cellClicked.connect(self.select_film)

        self.buttonSearch.clicked.connect(self.search)
        self.buttonCancel.clicked.connect(self.cancel)

    def display(self):
        self.parent().setCurrentWidget(self)

    def search(self):
        self.reset_selection()
        iterator = 0
        query = self.queryInput.text()
        condition = None

        if self.checkboxDisk.isChecked():
            if condition is None:
                condition = (Film.disk_number == int(query))
            else:
                condition |= (Film.disk_number == query)

        if self.checkboxTitle.isChecked():
            if condition is None:
                condition = Film.title.contains(query)
            else:
                condition = condition | Film.title.contains(query)

        if self.checkboxYear.isChecked():
            if condition is None:
                condition = (Film.year == int(query))
            else:
                condition |= (Film.year == int(query))

        if self.checkboxGenre.isChecked():
            if condition is None:
                condition = Film.genre.contains(query)
            else:
                condition = condition | Film.genre.contains(query)

        if self.checkboxDirector.isChecked():
            if condition is None:
                condition = Film.director.contains(query)
            else:
                condition = condition | Film.director.contains(query)

        if self.checkboxRole.isChecked():
            if condition is None:
                condition = Film.role.contains(query)
            else:
                condition = condition | Film.role.contains(query)

        films = Film.select().where(condition)
        self.result.setRowCount(len(films))

        for film in films:
            self.result.setItem(iterator, 0, QTableWidgetItem(str(film.id)))
            self.result.setItem(iterator, 1, QTableWidgetItem(str(film.disk_number)))
            self.result.setItem(iterator, 2, QTableWidgetItem(film.title))
            self.result.setItem(iterator, 3, QTableWidgetItem(str(film.year)))
            self.result.setItem(iterator, 4, QTableWidgetItem(film.genre))
            self.result.setItem(iterator, 5, QTableWidgetItem(film.director))
            self.result.setItem(iterator, 6, QTableWidgetItem(film.role))
            iterator += 1

    def cancel(self):
        self.reset_selection()
        self.queryInput.clear()
        self.result.setRowCount(0)
        self.go_back()

    def go_back(self):
        self.parent().parent().tableWidget.display()

    def select_film(self, row):
        indexes = self.result.selectionModel().selectedIndexes()
        model = self.result.selectionModel().model()
        # grab ID from hidden first column
        self.selectedFilmId = model.data(indexes[0])

    def reset_selection(self):
        self.selectedFilmId = None
        self.result.clearSelection()
