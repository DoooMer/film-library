from PyQt5.QtWidgets import QApplication
from peewee import SqliteDatabase
from Filmlibrary import config
from Filmlibrary.ui.Main import Main


class Filmlibrary:
    dbFile = "default.db"
    db = config.db

    def __init__(self, argv):
        self.qApp = QApplication(argv)
        super().__init__()

    def run(self):
        main = Main(app=self)
        return self.qApp.exec_()

    def connect(self):
        self.close()
        config.db.init(self.dbFile)

    def close(self):
        if isinstance(self.db, SqliteDatabase) and not self.db.is_closed():
            self.db.close()
