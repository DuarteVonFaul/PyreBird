def para_dict(obj):
    # Se for um objeto, transforma num dict
    if hasattr(obj, '__dict__'):
        obj = obj.__dict__

    # Se for um dict, lê chaves e valores; converte valores
    if isinstance(obj, dict):
        return { k:para_dict(v) for k,v in obj.items() }
    # Se for uma lista ou tupla, lê elementos; também converte
    elif isinstance(obj, list) or isinstance(obj, tuple):
        return [para_dict(e) for e in obj]
    # Se for qualquer outra coisa, usa sem conversão
    else: 
        return obj


def Type_column(argument,campo):
    match argument:
       case 261     : return confirmString(campo)#'BLOB',
       case 14      : return confirmString(campo)#'CHAR'
       case 40      : return confirmString(campo)#'CSTRING'
       case 11      : return confirmFloat(campo)#'D_FLOAT'
       case 27      : return confirmFloat(campo)#'DOUBLE'
       case 10      : return confirmFloat(campo)#'FLOAT'
       case 16      : return confirmFloat(campo)#'Numeric' - Decimal
       case 8       : return confirmInt(campo)#'INTEGER'
       case 9       : return confirmString(campo)#'QUAD'
       case 7       : return confirmInt(campo)#'SMALLINT'
       case 12      : return confirmString(campo)#'DATE'
       case 13      : return confirmString(campo)#'TIME'
       case 35      : return confirmString(campo)#'TIMESTAMP'
       case 37      : return confirmString(campo)#'VARCHAR'
       case default : return confirmString("Algo de errado não está certo")


def confirmInt(campo):
    try:
        return int(campo)
    except:
        return None
    
def confirmFloat(campo):
    try:
        return float(campo)
    except:
        return None

def confirmString(campo):
    try:
        return str(campo)
    except:
        return None