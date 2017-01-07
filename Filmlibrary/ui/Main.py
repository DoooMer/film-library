from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox

from Filmlibrary import config
from Filmlibrary.models.Film import Film
from Filmlibrary.ui.MainWindow import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    width = 600
    height = 400
    title = "Film library 4.1"

    def __init__(self, parent=None, app=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.app = app
        self.actionNew.triggered.connect(self.createFileDialog)
        self.actionOpen.triggered.connect(self.openFileDialog)
        self.actionExit.triggered.connect(self.close)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.resize(self.width, self.height)
        self.center()
        self.setWindowTitle(self.title)
        self.show()

    def center(self):
        frame_geometry = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center)
        self.move(frame_geometry.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.app.close()
            event.accept()
        else:
            event.ignore()

    def openFileDialog(self):
        dbfile = QFileDialog.getOpenFileName(self, 'Open file', '', "DB files (*.db)")
        self.app.dbFile = dbfile[0]
        self.app.connect()

    def createFileDialog(self):
        dbfile = QFileDialog.getSaveFileName(self, 'Create file', 'default.db', '*.db')
        self.app.dbFile = dbfile[0]
        self.app.connect()
        config.db.create_tables([Film], True)
