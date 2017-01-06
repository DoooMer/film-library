from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QWidget

from Filmlibrary.ui.Main import Main


class Filmlibrary:
    title = "Film library 4.1"

    def __init__(self, argv, width=600, height=400):
        self.width = width
        self.height = height
        self.qApp = QApplication(argv)
        super().__init__()

    def run(self):
        main = Main()
        return self.qApp.exec_()
