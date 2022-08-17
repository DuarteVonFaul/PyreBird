from pybird.models.tablemodel import TableModel
from pybird.orm.table         import Colunm, TableTypes



class User(TableModel):

    __TableName__ = "TB_USER"

    id = Colunm(Type=TableTypes.INTEGER(), PrimaryKey= True, NotNUll= True)
    name = Colunm(Type=TableTypes.VARCHAR(10))

    def __init__(self, id, name) -> None:
        super().__init__()

        self.id     = id
        self.name   = name



class Product(TableModel):

    __TableName__ = 'TB_PRODUCT'

    id = Colunm(Type=TableTypes.INTEGER(), PrimaryKey= True, NotNUll= True)
    name = Colunm(Type=TableTypes.VARCHAR(10))
    price = Colunm(Type=TableTypes.FLOAT())

    def __init__(self, id, name) -> None:
        super().__init__()

        self.id     = id
        self.name   = name


class TabelTest(TableModel):

    id = Colunm(Type=TableTypes.INTEGER(), PrimaryKey= True, NotNUll= True)
    name = Colunm(Type=TableTypes.VARCHAR(10), NotNUll=True)

    def __init__(self, id, name) -> None:
        super().__init__()

        self.id     = id
        self.name   = name


    








