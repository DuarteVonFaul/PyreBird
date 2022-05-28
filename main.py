from database   import MySession, Base
from pybird     import Select,Insert
import json
from product    import productTable


query = Select(MySession,productTable,'*').filter("PRD_CODR = '28600'").all()






print(query)

