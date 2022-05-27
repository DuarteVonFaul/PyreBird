from pybird import Create_Session




class DataBase():

    def __init__(self) -> None:
        pass

    def create_session(self):
        return Create_Session(  dsn='F:/GITHUB/sge-totem/SGENFCE.FDB',
                                user='sysdba',password='masterkey',
                                charset='ANSI')


myBase = DataBase()
MySession = myBase.create_session()