from pybird.models.tablemodel import TableModel
from database import Base, MySession



class User(TableModel):

    ID_USER:int
    USER_NAME:str
    USER_PASSWORD:str
    USER_CASH:float

    def __init__(self, userName, userPassword) -> None:
        self.ID_USER:int
        self.USER_NAME = userName
        self.USER_PASSWORD = userPassword
        self.USER_CASH:float

        super().__init__()

    def __str__(self) -> str:
        return "User(username= 'Duarte001', userPassword = '1234')"
        




