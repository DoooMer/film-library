from Filmlibrary import config
from Filmlibrary.models.Version import Version


def check_version():
    return Version.table_exists() and Version.select().order_by(Version.value.desc()).get() == config.dbVersion
