from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QWidget

from Filmlibrary.models.Film import Film
from Filmlibrary.ui.templates import Ui_FilmForm
from Filmlibrary.ui.widgets import TableWidget
from Filmlibrary.validators.FilmValidator import FilmValidator


class FormWidget(QWidget, Ui_FilmForm):
    film = None
    backWidget = None

    def __init__(self, app=None):
        super().__init__()
        self.setupUi(self)
        self.app = app

        reg_ex = QRegExp("[\w\d\-]{1,}")
        title_validator = QRegExpValidator(reg_ex, self.titleInput)
        self.titleInput.setValidator(title_validator)

        self.buttonSave.clicked.connect(self.save)
        self.buttonCancel.clicked.connect(self.cancel)

    def display(self):
        assert isinstance(self.parent(), QStackedWidget)
        self.parent().setCurrentWidget(self)

    def cancel(self):
        self.clear_inputs()
        self.go_back()

    def clear_inputs(self):
        self.diskInput.setValue(1)
        self.titleInput.clear()
        self.yearInput.clear()
        self.genreInput.clear()
        self.directorInput.clear()
        self.roleInput.clear()

    def go_back(self):
        self.parent().setCurrentWidget(self.backWidget)

    def set_back_widget(self, widget):
        self.backWidget = widget

    def save(self):
        if self.film is not None:
            self.film.disk_number = self.diskInput.value()
            self.film.title = self.titleInput.text()
            self.film.year = self.yearInput.text()
            self.film.genre = self.genreInput.text()
            self.film.director = self.directorInput.text()
            self.film.role = self.roleInput.text()
        else:
            self.film = Film(
                disk_number=self.diskInput.value(),
                title=self.titleInput.text(),
                year=self.yearInput.text(),
                genre=self.genreInput.text(),
                director=self.directorInput.text(),
                role=self.roleInput.text()
            )

        # валидация
        validator = FilmValidator(self.film)
        validator.validate()

        if len(validator.errors) > 0:
            # вывод ошибок
            message = "Ошибка\n"

            for field, error in validator.errors.items():
                message += "\n" + error

            self.show_error(message + "\n")
        else:
            # попытка сохранить в базе
            try:
                self.film.save()

                # вызывает событие обновления таблицы
                if isinstance(self.backWidget, TableWidget):
                    self.backWidget.refreshList.emit()

            except ValueError:
                self.show_error()
            else:
                self.film = None
                self.clear_inputs()
                self.go_back()

    def load(self, film_id):
        self.film = Film.get(Film.id == film_id)

        self.diskInput.setValue(self.film.disk_number)
        self.titleInput.setText(self.film.title)
        self.yearInput.setText(str(self.film.year))
        self.genreInput.setText(self.film.genre)
        self.directorInput.setText(self.film.director)
        self.roleInput.setText(self.film.role)

    @staticmethod
    def show_error(text=None):
        message = QMessageBox()
        message.setIcon(QMessageBox.Warning)
        message.setText("Ошибка сохранения" if text is None else text)
        message.setWindowTitle("Ошибка")
        message.setStandardButtons(QMessageBox.Ok)
        message.exec_()
