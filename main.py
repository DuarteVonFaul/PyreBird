from database   import MySession, Base
from pybird     import Select,Insert, Delete, Update
from product    import productTable


"""query = Select(MySession,productTable).filter_by(PRD_CODR = '00001').return_query()

print(query)
"""
print(Base)

