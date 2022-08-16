from pybird.models.tablemodel import TableModel
from pybird.orm.table         import Colunm, TableTypes
from pybird.orm.ext.migrate   import Migration
from database import MySession, Base


print(f' \n \n Minhas Tabelas {Base.classes_keys()} \n \n')

class User(TableModel):

    __TableName__ = "TB_USER"

    id = Colunm(Type=TableTypes.INTEGER(), PrimaryKey= True, NotNUll= True)
    name = Colunm(Type=TableTypes.VARCHAR(10))


class Product(TableModel):

    __TableName__ = 'TB_PRODUCT'

    id = Colunm(Type=TableTypes.INTEGER(), PrimaryKey= True, NotNUll= True)
    name = Colunm(Type=TableTypes.VARCHAR(10))
    price = Colunm(Type=TableTypes.FLOAT())


class TabelTest(TableModel):

    id = Colunm(Type=TableTypes.INTEGER(), PrimaryKey= True, NotNUll= True)
    name = Colunm(Type=TableTypes.VARCHAR(10), NotNUll=True)
    








