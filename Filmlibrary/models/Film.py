from peewee import *


db = SqliteDatabase('../../Library.db')


class Film(Model):
    id = PrimaryKeyField()
    disk_number = IntegerField()
    title = TextField()
    year = IntegerField()
    genre = TextField()
    director = TextField()
    role = TextField()

    class Meta:
        database = db
