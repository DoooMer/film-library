from PyQt5.QtWidgets import QWidget

from Filmlibrary.ui.templates import Ui_OpenView


class OpenWidget(QWidget, Ui_OpenView):
    def __init__(self, app=None):
        super().__init__()
        self.setupUi(self)
        self.app = app

    def display(self):
        self.parent().setCurrentWidget(self)
