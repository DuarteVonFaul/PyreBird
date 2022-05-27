
def Type_column(argument):
    match argument:
       case 261 : return 'BLOB',
       case 14  : return 'CHAR',
       case 40  : return 'CSTRING',
       case 11  : return 'D_FLOAT',
       case 27  : return 'DOUBLE',
       case 10  : return 'FLOAT',
       case 16  : return 'INT64',
       case 8   : return 'INTEGER',
       case 9   : return 'QUAD',
       case 7   : return 'SMALLINT',
       case 12  : return 'DATE',
       case 13  : return 'TIME',
       case 35  : return 'TIMESTAMP',
       case 37  : return 'VARCHAR',


from enum import Enum

class Permission(Enum):
    OPCAIXA =  {
                'OP_PDES'        : 'N',
                'OP_ACRE'        : 'N',
                'OP_CANC'        : 'N',
                'OP_INID'        : 'S',
                'OP_GAVT'        : 'N',
                'OP_LEIX'        : 'N',
                'OP_FIMD'        : 'S',
                'OP_SANG'        : 'N',
                'OP_RECB'        : 'N',
                'OP_TOTA'        : 'N',
                'OP_CANCCP'      : 'N',
                'OP_ALTPREC'     : 'N',
                'OP_CDUS'        : '001',
                'OP_IDCNT'       :  0,
                'OP_CONFIG'      : 'N',
                'OP_LIBCLI'      : 'N',
                'OP_DESCONTO'    : 0.00,
                }
    GERENTE =  {
                'OP_PDES'        : 'S',
                'OP_ACRE'        : 'S',
                'OP_CANC'        : 'S',
                'OP_INID'        : 'S',
                'OP_GAVT'        : 'S',
                'OP_LEIX'        : 'S',
                'OP_FIMD'        : 'S',
                'OP_SANG'        : 'S',
                'OP_RECB'        : 'S',
                'OP_TOTA'        : 'N',
                'OP_CANCCP'      : 'S',
                'OP_ALTPREC'     : 'S',
                'OP_CDUS'        : '001',
                'OP_IDCNT'       :  0,
                'OP_CONFIG'      : 'N',
                'OP_LIBCLI'      : 'S',
                'OP_DESCONTO'    : 0.00,
                }
    SUPORTE =  {
                'OP_PDES'        : 'S',
                'OP_ACRE'        : 'S',
                'OP_CANC'        : 'S',
                'OP_INID'        : 'S',
                'OP_GAVT'        : 'S',
                'OP_LEIX'        : 'S',
                'OP_FIMD'        : 'S',
                'OP_SANG'        : 'S',
                'OP_RECB'        : 'S',
                'OP_TOTA'        : 'S',
                'OP_CANCCP'      : 'S',
                'OP_ALTPREC'     : 'S',
                'OP_CDUS'        : '001',
                'OP_IDCNT'       :  0,
                'OP_CONFIG'      : 'S',
                'OP_LIBCLI'      : 'S',
                'OP_DESCONTO'    : 0.00,
                }
    
    Permission = Enum('Permission', ['OPCAIXA', 'GERENTE', 'SUPORTE'])
    