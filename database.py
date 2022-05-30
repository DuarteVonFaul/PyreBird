from pybird.orm.session     import Create_Session
from pybird.orm.ext.automap import auto_map


class DataBase():


    def __init__(self) -> None:
        pass


    def create_session():
        return Create_Session(  dsn='C:/Users/Estagiario-03/Desktop/GitHub/SGEHeroku/SGENFCE.FDB',
                                user='sysdba',password='masterkey',
                                charset='ANSI')


MyBase = DataBase
MySession = MyBase.create_session()
Base = auto_map(MySession).all()