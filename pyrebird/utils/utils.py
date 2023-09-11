from ast import arguments
from email.policy import default


def refacture_args(args):
    aux = str(args[0])
    i = 1
    while i < len(args):
        aux += f', {args[i]}'
        i += 1
    return aux


def to_dict(obj):
    # Se for um objeto, transforma num dict
    if hasattr(obj, '__dict__'):
        obj = obj.__dict__

    # Se for um dict, lê chaves e valores; converte valores
    if isinstance(obj, dict):
        return { k:to_dict(v) for k,v in obj.items() }
    # Se for uma lista ou tupla, lê elementos; também converte
    elif isinstance(obj, list) or isinstance(obj, tuple):
        return [to_dict(e) for e in obj]
    # Se for qualquer outra coisa, usa sem conversão
    else: 
        return obj


def convert_type(argument,campo):
    match argument:
       case 261     : return confirm_string(campo)  #'BLOB',
       case 14      : return confirm_string(campo)  #'CHAR'
       case 40      : return confirm_string(campo)  #'CSTRING'
       case 11      : return confirm_float(campo)   #'D_FLOAT'
       case 27      : return confirm_float(campo)   #'DOUBLE'
       case 10      : return confirm_float(campo)   #'FLOAT'
       case 16      : return confirm_float(campo)   #'Numeric' - Decimal
       case 8       : return confirm_int(campo)     #'INTEGER'
       case 9       : return confirm_string(campo)  #'QUAD'
       case 7       : return confirm_int(campo)     #'SMALLINT'
       case 12      : return confirm_string(campo)  #'DATE'
       case 13      : return confirm_string(campo)  #'TIME'
       case 35      : return confirm_string(campo)  #'TIMESTAMP'
       case 37      : return confirm_string(campo)  #'VARCHAR'
       case default : return argument(campo)

def confirm_int(campo):
    try:
        return int(campo)
    except:
        return None
    
def confirm_float(campo):
    try:
        return float(campo)
    except:
        return None

def confirm_string(campo):
    try:
        return str(campo)
    except:
        return None
    
