from peewee import Model
from Filmlibrary import config


class BaseModel(Model):
    class Meta:
        database = config.db
