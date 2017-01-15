from PyQt5.QtWidgets import QDesktopWidget, QFileDialog, QMainWindow, QMessageBox, QStackedWidget
from PyQt5.QtWidgets import QSizePolicy

from Filmlibrary import config
from Filmlibrary.models.Film import Film
from Filmlibrary.ui.templates import Ui_MainWindow
from Filmlibrary.ui.widgets import OpenWidget, TableWidget, FormWidget
from Filmlibrary.ui.widgets import SearchWidget


class Main(QMainWindow, Ui_MainWindow):
    width = 800
    height = 550
    title = "Film library 4.1"
    centralWidget = None
    openWidget = None
    tableWidget = None
    formWidget = None
    searchWidget = None

    def __init__(self, parent=None, app=None):
        super(Main, self).__init__(parent)
        self.app = app
        self.setupUi(self)

        self.actionNew.triggered.connect(self.create_file_dialog)
        self.actionOpen.triggered.connect(self.open_file_dialog)
        self.actionClose.triggered.connect(self.close_file)
        self.actionExit.triggered.connect(self.close)
        self.actionCreate.triggered.connect(self.create_film)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.resize(self.width, self.height)
        self.center()
        self.setWindowTitle(self.title)

        self.openWidget = OpenWidget(app=self.app)
        self.tableWidget = TableWidget(app=self.app)
        self.formWidget = FormWidget(app=self.app)
        self.searchWidget = SearchWidget(app=self.app)

        self.setup_central_widgets()

        self.show()

    def center(self):
        frame_geometry = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center)
        self.move(frame_geometry.topLeft())

    def setup_central_widgets(self):
        self.centralWidget = QStackedWidget()
        self.setCentralWidget(self.centralWidget)

        self.centralWidget.addWidget(self.openWidget)
        self.openWidget.buttonCreate.clicked.connect(self.create_file_dialog)
        self.openWidget.buttonOpen.clicked.connect(self.open_file_dialog)

        self.centralWidget.addWidget(self.tableWidget)
        self.tableWidget.buttonAdd.clicked.connect(self.create_film)
        self.tableWidget.buttonEdit.clicked.connect(self.edit_film)
        self.tableWidget.buttonDelete.clicked.connect(self.delete_film)
        self.tableWidget.buttonFind.clicked.connect(self.search)

        self.centralWidget.addWidget(self.formWidget)

        self.centralWidget.addWidget(self.searchWidget)
        self.searchWidget.result.cellDoubleClicked.connect(self.edit_film_search)

        self.choose_central_widget()

    def choose_central_widget(self):
        if self.app.isOpen:
            self.tableWidget.display()
        else:
            self.openWidget.display()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.app.close()
            event.accept()
        else:
            event.ignore()

    def open_file_dialog(self):
        db_file = QFileDialog.getOpenFileName(self, 'Open file', '', "DB files (*.db)")

        if len(db_file[0]) > 0:
            self.app.dbFile = db_file[0]
            self.app.connect()

        self.choose_central_widget()

    def create_file_dialog(self):
        db_file = QFileDialog.getSaveFileName(self, 'Create file', config.defaultDbFileName, 'DB files (*.db)')

        if len(db_file[0]) > 0:
            self.app.dbFile = db_file[0]
            self.app.connect()

        self.choose_central_widget()

    def create_film(self):
        self.formWidget.display()

    def edit_film(self):
        self.formWidget.load(self.tableWidget.selectedFilmId)
        self.formWidget.display()

    def edit_film_search(self):
        self.formWidget.load(self.searchWidget.selectedFilmId)
        self.formWidget.display()

    def delete_film(self):
        confirm = QMessageBox.question(
            self,
            "Delete film",
            "Are you sure to delete?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if confirm == QMessageBox.Yes and self.tableWidget.selectedFilmId is not None:
            film = Film.get(Film.id == self.tableWidget.selectedFilmId)
            film.delete_instance()
            self.tableWidget.load_values()

    def close_file(self):
        self.app.close()
        self.app.settings.remove("LastOpenedDatabaseFile")
        self.choose_central_widget()

    def search(self):
        self.searchWidget.display()
