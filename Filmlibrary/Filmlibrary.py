from PyQt5.QtWidgets import QApplication

from Filmlibrary.ui.Main import Main


class Filmlibrary:
    def __init__(self, argv):
        self.qApp = QApplication(argv)
        super().__init__()

    def run(self):
        main = Main()
        return self.qApp.exec_()
