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

        self.load_settings()

        self.result.hideColumn(0)
        self.result.setHorizontalHeaderLabels(self.tableHeaders)
        self.result.cellClicked.connect(self.select_film)

        self.buttonSearch.clicked.connect(self.search)
        self.buttonCancel.clicked.connect(self.cancel)

        self.checkboxDisk.clicked.connect(self.remember_selection)
        self.checkboxTitle.clicked.connect(self.remember_selection)
        self.checkboxYear.clicked.connect(self.remember_selection)
        self.checkboxGenre.clicked.connect(self.remember_selection)
        self.checkboxDirector.clicked.connect(self.remember_selection)
        self.checkboxRole.clicked.connect(self.remember_selection)

    def load_settings(self):
        disk_enabled = self.app.settings.value('Search/disk', False, type=bool)
        self.checkboxDisk.setChecked(bool(disk_enabled))

        title_enabled = self.app.settings.value('Search/title', False)
        self.checkboxTitle.setChecked(bool(title_enabled))

        year_enabled = self.app.settings.value('Search/year', False)
        self.checkboxYear.setChecked(bool(year_enabled))

        genre_enabled = self.app.settings.value('Search/genre', False)
        self.checkboxGenre.setChecked(bool(genre_enabled))

        director_enabled = self.app.settings.value('Search/director', False)
        self.checkboxDirector.setChecked(bool(director_enabled))

        role_enabled = self.app.settings.value('Search/role', False)
        self.checkboxRole.setChecked(bool(role_enabled))

    def display(self):
        self.parent().setCurrentWidget(self)

    def search(self):
        self.reset_selection()
        iterator = 0
        query = self.queryInput.text()
        condition = None

        if self.checkboxDisk.isChecked() and len(query) > 0:
            if condition is None:
                condition = (Film.disk_number == int(query))
            else:
                condition |= (Film.disk_number == query)

        if self.checkboxTitle.isChecked():
            if condition is None:
                condition = Film.title.contains(query)
            else:
                condition = condition | Film.title.contains(query)

        if self.checkboxYear.isChecked() and len(query) > 0:
            try:
                if condition is None:
                    condition = (Film.year == int(query))
                else:
                    condition |= (Film.year == int(query))
            except ValueError:
                pass

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

    def remember_selection(self):
        self.app.settings.setValue('Search/disk', self.checkboxDisk.isChecked())
        self.app.settings.setValue('Search/title', self.checkboxTitle.isChecked())
        self.app.settings.setValue('Search/year', self.checkboxYear.isChecked())
        self.app.settings.setValue('Search/genre', self.checkboxGenre.isChecked())
        self.app.settings.setValue('Search/director', self.checkboxDirector.isChecked())
        self.app.settings.setValue('Search/role', self.checkboxRole.isChecked())
