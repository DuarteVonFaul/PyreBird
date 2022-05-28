from database   import MySession, Base
from pybird     import Select,Insert, Delete, Update
from product    import productTable


'''query = Select(MySession,productTable).filter_by(PRD_CODR = '28600').return_query()

print('\n'+query)


query = Insert(MySession,productTable).values(PRD_CODR = '2356', PRD_NOME = 'test', PRD_PREC = 34.5 ).return_query()

print('\n'+query)

query = Delete(MySession,productTable).filter_by(PRD_CODR = '28600').return_query()

print('\n'+query)

query = Update(MySession,productTable).setUpdate(PRD_NOME ='test2', PRD_PREC = 13.50).filter_by(PRD_CODR = '28600').return_query()

print('\n'+query+'\n')'''

for b in Base:
    print(b)

