from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QWidget

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
        print(self.queryInput.text())
        iterator = 0
        films = Film.select().where(Film.title == self.queryInput.text())
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
        self.queryInput.clear()
        self.go_back()

    def go_back(self):
        self.parent().parent().tableWidget.display()

    def select_film(self, row):
        indexes = self.result.selectionModel().selectedIndexes()
        model = self.result.selectionModel().model()
        # grab ID from hidden first column
        self.selectedFilmId = model.data(indexes[0])
