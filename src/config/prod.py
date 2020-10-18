from config.dev import ConfigDB

class ConfigDB():
    """
    Configuration database production
    """

    def __init__(self):
        configDB = ConfigDB()
        self.HOST = configDB.HOST
        self.DATABASE = configDB.DATABASE
        self.USER = configDB.USER
        self.PASSWORD = configDB.PASSWORD
