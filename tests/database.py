from pybird.orm.session import Create_Session
from pybird.orm.ext.automap import auto_map


class DataBase():

    def __init__(self, path) -> None:
        self.path = path
        pass

    def get_engine(self):

        return Create_Session(dsn=f'{self.path}',
                                user='sysdba',password='masterkey',
                                charset='ANSI')


database = DataBase("./tests/FireBird.FDB")

MySession = database.get_engine()
Base      = auto_map(MySession).all()

