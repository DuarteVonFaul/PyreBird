
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
    