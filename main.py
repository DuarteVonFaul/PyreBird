from database   import MySession
from pybird     import Select,Insert

from product    import productTable


Select(MySession,productTable,'*').filter("PRD_CODR = '00001'").execute().scalar()

print(type(productTable.PRD_PREC))
