from peewee import *

from Filmlibrary.models.BaseModel import BaseModel


class Film(BaseModel):
    id = PrimaryKeyField()
    disk_number = IntegerField()
    title = TextField()
    year = IntegerField()
    genre = TextField()
    director = TextField()
    role = TextField()
