from pybird import Create_Session,auto_map




class DataBase():

    def __init__(self) -> None:
        pass

    def create_session(self):
        return Create_Session(  dsn='C:/Users/Estagiario-03/Desktop/GitHub/SGEHeroku/SGENFCE.FDB',
                                user='sysdba',password='masterkey',
                                charset='ANSI')


myBase = DataBase()
MySession = myBase.create_session()
Base = auto_map(MySession)