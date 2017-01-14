from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QWidget

from Filmlibrary.models.Film import Film
from Filmlibrary.ui.templates import Ui_FilmForm


class CreateWidget(QWidget, Ui_FilmForm):
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
        self.clearInputs()
        self.goBack()

    def clearInputs(self):
        self.diskInput.setValue(1)
        self.titleInput.clear()
        self.yearInput.clear()
        self.genreInput.clear()
        self.directorInput.clear()
        self.roleInput.clear()

    def goBack(self):
        self.parent().parent().tableWidget.display()

    def save(self):
        film = Film(
            disk_number=self.diskInput.value(),
            title=self.titleInput.text(),
            year=self.yearInput.text(),
            genre=self.genreInput.text(),
            director=self.directorInput.text(),
            role=self.roleInput.text()
        )

        try:
            film.save()
        except ValueError:
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setText("Ошибка сохранения")
            message.setWindowTitle("Ошибка")
            message.setStandardButtons(QMessageBox.Ok)
            message.exec_()
        else:
            self.clearInputs()
            self.goBack()
