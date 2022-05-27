from database   import MySession
from pybird     import Select,auto_map,create_object,Insert
from product    import ProductTabel
from util       import Permission, Type_column

# Execute the SELECT statement:

userAcess = Permission.SUPORTE.value


'''print(Insert(MySession,'TB_OPERAD').tableModel(model).valuesTable(" 438," + 
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
                                                            f"{float(userAcess.get('OP_DESCONTO'))}").return_query())'''


'''Insert(MySession,'TB_OPERAD').tableModel(model).valuesTable(" 438," + 
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
                                                            f"{float(userAcess.get('OP_DESCONTO'))}").execute()'''




model = auto_map(MySession)

print(model['TB_PROD'].PRD_CODR)

'''for m in model:
    print(str(m[0]) + ':' + str(Type_column(int(m[1]))))'''

'''query = Select(MySession, 'TB_PROD','*').filter("PRD_CODI = '0000000028890'").execute()

create_object(model,query,productTabel)

for obj in productTabel.List:
    for item in obj:
        print(f"{item} : {obj[f'{item}']}")'''
