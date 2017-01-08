from PyQt5.QtWidgets import QWidget

from Filmlibrary.ui.OpenView import Ui_OpenView


class OpenWidget(QWidget, Ui_OpenView):
    def __init__(self):
        super().__init__()
        self.setupUi(self)