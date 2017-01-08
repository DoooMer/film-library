from PyQt5.QtWidgets import QWidget

from Filmlibrary.ui.templates import Ui_CreateForm


class CreateWidget(QWidget, Ui_CreateForm):
    def __init__(self, app=None):
        super().__init__()
        self.setupUi(self)
        self.app = app
