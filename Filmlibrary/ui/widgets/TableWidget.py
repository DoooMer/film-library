from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QWidget

from Filmlibrary.ui.templates import Ui_MainView


class TableWidget(QWidget, Ui_MainView):
    def __init__(self, app=None):
        super().__init__()
        self.setupUi(self)
        self.app = app

    def display(self):
        assert isinstance(self.parent(), QStackedWidget)
        self.parent().setCurrentWidget(self)
