from test_createTabel import *

from pybird.insert            import Insert
from pybird.select            import Select
from pybird.utils.utils       import to_dict
from pybird.orm.ext.migrate   import Migration
from database import MySession, Base


Migration.migrations(User,Product, TabelTest)
Migration.makeMigrations(MySession)

user = User(4,'Sousa')

#Insert(MySession, user).values(ID = user.id, NAME = str(user.name)).execute()

query = Select(MySession, user).execute()
query2 = Select(MySession, Base.get_class('TB_USER')).execute()
print(to_dict(query))
print(to_dict(query2))