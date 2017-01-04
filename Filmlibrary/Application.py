from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget


class Application:
    title = "Film library 4.1"

    def __init__(self, argv, width=600, height=400):
        self.width = width
        self.height = height
        self.qApp = QApplication(argv)

        widget = QWidget()
        widget.resize(self.width, self.height)
        widget.setWindowTitle(self.title)
        widget.show()

        super().__init__()

    def exec(self):
        return self.qApp.exec_()
