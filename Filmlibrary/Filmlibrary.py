from PyQt5.QtWidgets import QApplication
from peewee import SqliteDatabase

from Filmlibrary.ui.Main import Main


class Filmlibrary:
    def __init__(self, argv):
        self.qApp = QApplication(argv)
        super().__init__()

    def run(self):
        main = Main(app=self)
        self.dbFile = "default.db"
        return self.qApp.exec_()

    def connect(self, file=None):
        if file is not None:
            self.dbFile = file

        self.close()
        self.db = SqliteDatabase(self.dbFile)
        self.db.connect()

    def close(self):
        if hasattr(self, 'db') and isinstance(self.db, SqliteDatabase):
            self.db.close()
