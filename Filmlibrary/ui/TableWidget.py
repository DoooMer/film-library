from PyQt5.QtWidgets import QWidget

from Filmlibrary.ui.MainView import Ui_MainView


class TableWidget(QWidget, Ui_MainView):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
