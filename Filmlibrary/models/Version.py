from peewee import TextField

from Filmlibrary.models.BaseModel import BaseModel


class Version(BaseModel):
    value = TextField(unique=True, index=True)

    class Meta:
        db_table = "version"
