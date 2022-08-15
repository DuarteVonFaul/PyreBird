from pybird.models.tablemodel import TableModel
from pybird.orm.table         import Colunm, TableTypes
from pybird.orm.ext.migrate   import Migration
from database import MySession


class User(TableModel):

    __TableName__ = "TB_USER"

    id = Colunm(TableTypes.INTEGER(), PrimaryKey= True, NotNUll= True)
    name = Colunm(TableTypes.VARCHAR(10))


class Product(TableModel):

    __TableName__ = 'TB_PRODUCT'

    id = Colunm(TableTypes.INTEGER(), PrimaryKey= True, NotNUll= True)
    name = Colunm(TableTypes.VARCHAR(10))
    price = Colunm(TableTypes.FLOAT())


class TabelTest(TableModel):

    id = Colunm(TableTypes.INTEGER(), PrimaryKey= True, NotNUll= True)
    name = Colunm(TableTypes.VARCHAR(10))


Migration().migrations(User,Product,TabelTest)
Migration().makeMigrations(MySession)




