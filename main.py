from database   import MySession
from pybird     import Select,auto_map,create_object,Insert
from product    import productTabel
from util       import Permission

# Execute the SELECT statement:

userAcess = Permission.SUPORTE.value

model = auto_map(MySession,'TB_OPERAD')

print(Insert(MySession,'TB_OPERAD').tableModel(model).valuesTable(" 438," + 
                                                            "'Duarte'," + 
                                                            "'1234',"+
                                                            f"'{userAcess.get('OP_PDES')}',"+
                                                            f"'{userAcess.get('OP_ACRE')}',"+
                                                            f"'{userAcess.get('OP_CANC')}',"+
                                                            f"'{userAcess.get('OP_INID')}',"+
                                                            f"'{userAcess.get('OP_GAVT')}',"+
                                                            f"'{userAcess.get('OP_LEIX')}',"+
                                                            f"'{userAcess.get('OP_FIMD')}',"+
                                                            f"'{userAcess.get('OP_SANG')}',"+
                                                            f"'{userAcess.get('OP_RECB')}',"+
                                                            f"'{userAcess.get('OP_TOTA')}',"+
                                                            f"'{userAcess.get('OP_CANCCP')}',"+
                                                            f"'{userAcess.get('OP_ALTPREC')}',"+
                                                            f"'{userAcess.get('OP_CDUS')}',"+
                                                            f"{int(userAcess.get('OP_IDCNT'))},"+
                                                            f"NULL,"+
                                                            f"'{userAcess.get('OP_CONFIG')}',"+
                                                            f"'{userAcess.get('OP_LIBCLI')}',"+
                                                            f"{float(userAcess.get('OP_DESCONTO'))}").return_query())
'''query = Select(MySession, 'TB_OPERAD','*').filter("OP_SENHA = '987654'").execute()

create_object(model,query,productTabel)

for obj in productTabel.List:
    print('OP_CODI' + ':' + obj[str('OP_CODI')] + '  OP_DESC' + ':' + obj[str('OP_DESC')])'''
