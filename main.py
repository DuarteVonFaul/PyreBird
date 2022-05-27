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
from pybird     import Select,auto_map,create_object
from product    import productTabel

# Execute the SELECT statement:



model = auto_map(MySession,'TB_PROD')
query = Select(MySession, 'TB_PROD','*').filter("PRD_NOME = 'BIFE DO VAZIO CONG BOVINO PACU'").execute()

create_object(model,query,productTabel)

for obj in productTabel.List:
    print('PRD_NOME' + ':' + obj[str('PRD_NOME')] + '  PRD_CODI' + ':' + obj[str('PRD_CODI')])
