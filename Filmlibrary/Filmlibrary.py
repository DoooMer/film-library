import sys
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QApplication
from peewee import SqliteDatabase

from Filmlibrary import config
from Filmlibrary import models
from Filmlibrary.models.Film import Film
from Filmlibrary.ui.Main import Main


class Filmlibrary:
    dbFile = config.defaultDbFileName
    db = config.db
    isOpen = False

    def __init__(self, argv):
        self.qApp = QApplication(argv)
        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, 'Filmlibrary', 'Filmlibrary')
        self.restore()
        super().__init__()

    def run(self):
        main = Main(app=self)
        return self.qApp.exec_()

    def connect(self):
        self.close()
        config.db.init(self.dbFile)

        if models.check_version():
            # require do import
            pass

        config.db.create_tables([Film], True)
        self.settings.setValue('LastOpenedDatabaseFile', self.dbFile)
        self.isOpen = True

    def close(self):
        if isinstance(self.db, SqliteDatabase) and not self.db.is_closed():
            self.db.close()
            self.isOpen = False

    def restore(self):
        self.dbFile = self.settings.value('LastOpenedDatabaseFile')
        if self.dbFile is not None:
            self.connect()
