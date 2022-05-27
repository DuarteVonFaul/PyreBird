'''import firebirdsql

conn = firebirdsql.connect(  user='SYSDBA', 
                            password='masterkey', 
                            database='C:/Users/Estagiario-03/Desktop/GitHub/SGEHeroku/SGENFCE.FDB',
                            host='localhost',
                            charset='ANSI')

cur = conn.cursor()

cur.execute('select * from TB_Prod')

for c in cur.fetchall():
    print("Produto:")
    print(c)
conn.close()'''





from database   import MySession
from pybird     import Select,auto_map
from product    import productTabel

# Execute the SELECT statement:



model = auto_map(MySession,'TB_PROD')
query = Select(MySession, 'TB_PROD','*').filter("PRD_CODR = '00007'").execute()

for item in query:
    i = 0
    for  campo in item:
        aux = model[i]
        productTabel.productModel[str(aux[0]).strip()] = str(campo)
        i = i + 1

for item in productTabel.productModel:
    print(item + ": "+ productTabel.productModel[item])


