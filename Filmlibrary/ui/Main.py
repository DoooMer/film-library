from PyQt5.QtWidgets import QDesktopWidget, QFileDialog, QMainWindow, QMessageBox, QStackedWidget

from Filmlibrary.ui.templates import Ui_MainWindow
from Filmlibrary.ui.widgets import OpenWidget, TableWidget


class Main(QMainWindow, Ui_MainWindow):
    width = 800
    height = 550
    title = "Film library 4.1"

    def __init__(self, parent=None, app=None):
        super(Main, self).__init__(parent)
        self.app = app
        self.setupUi(self)
        self.actionNew.triggered.connect(self.createFileDialog)
        self.actionOpen.triggered.connect(self.openFileDialog)
        self.actionExit.triggered.connect(self.close)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.resize(self.width, self.height)
        self.center()
        self.setWindowTitle(self.title)
        self.setupCentralWidget()
        self.show()

    def center(self):
        frame_geometry = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center)
        self.move(frame_geometry.topLeft())

    def setupCentralWidget(self):
        self.centralWidget = QStackedWidget()
        self.setCentralWidget(self.centralWidget)

        openWidget = OpenWidget(app=self.app)
        self.centralWidget.addWidget(openWidget)
        openWidget.buttonCreate.clicked.connect(self.createFileDialog)
        openWidget.buttonOpen.clicked.connect(self.openFileDialog)

        tableWidget = TableWidget(app=self.app)
        self.centralWidget.addWidget(tableWidget)
        # self.centralWidget.setCurrentWidget(tableWidget)

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
        print(self.app)

    def createFileDialog(self):
        dbfile = QFileDialog.getSaveFileName(self, 'Create file', 'default.db', 'DB files (*.db)')
        self.app.dbFile = dbfile[0]
        self.app.connect()
