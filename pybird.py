import fdb
from typing              import List

#Utils

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
       case 9       : return confirmString(campo)#'QUAD',
       case 7       : return confirmInt(campo)#'SMALLINT'
       case 12      : return confirmString(campo)#'DATE',
       case 13      : return confirmString(campo)#'TIME',
       case 35      : return confirmString(campo)#'TIMESTAMP',
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

#Gerenciamento do Banco
def Create_Session( dsn:str,user:str,password:str,charset:str):
    con = fdb.connect(dsn=dsn, user=user, password=password, charset=charset)
    return con

def auto_map(con):
        listclass = {}
        tablelist = []
        cur = con.cursor()
        cur.execute('SELECT RDB$RELATION_NAME FROM RDB$RELATIONS WHERE RDB$SYSTEM_FLAG = 0 OR RDB$SYSTEM_FLAG IS NULL')
        for c in  cur.fetchall():
            tablelist.append(str(c[0]).strip())
        for table in tablelist:
            cur.execute(f" SELECT r.RDB$FIELD_NAME AS nome, f.RDB$FIELD_TYPE AS tipo FROM RDB$RELATION_FIELDS r LEFT JOIN RDB$FIELDS f ON r.RDB$FIELD_SOURCE = f.RDB$FIELD_NAME WHERE r.RDB$RELATION_NAME='{table}' ORDER BY r.RDB$FIELD_POSITION")
            listclass[str(table).strip()] = BasicModel(cur.fetchall(),table)

        return listclass

#Modelos
class BasicModel():
    def __init__(self,list, raiz):
        setattr(self,'root',raiz)
        for  attr in list:
            setattr(self,str(attr[0]).strip(),None)
        pass

class Model():
    def __init__(self) -> None:
        pass



#CRUD
class Select():
    SQL : str

    def __init__(self,con, obj, filter_column:str):
        self.table = obj
        self.SQL = f'SELECT {filter_column}  FROM  {self.table.root}'
        self.con = con
    
    def filter(self, conditions:str):
        query = f"{self.SQL} WHERE  {conditions}"
        self.SQL = query
        return self

    def return_query(self):
        return self.SQL
        
    def scalar(self):
        self.cur = self.con.cursor()
        self.cur.execute(f" SELECT r.RDB$FIELD_NAME AS nome, f.RDB$FIELD_TYPE AS tipo FROM RDB$RELATION_FIELDS r LEFT JOIN RDB$FIELDS f ON r.RDB$FIELD_SOURCE = f.RDB$FIELD_NAME WHERE r.RDB$RELATION_NAME='{self.table.root}' ORDER BY r.RDB$FIELD_POSITION")
        self.listattr = self.cur.fetchall()
        self.cur.execute(self.SQL)
        self.listObj = self.cur.fetchone()
        i = 0
        for attr in self.listattr:
            setattr(self.table,(str(attr[0]).split())[0],Type_column(attr[1],(self.listObj)[i]))
            i = 1 + i
        return para_dict(self.table)
        
    def all(self):
        self.cur = self.con.cursor()
        self.cur.execute(f" SELECT r.RDB$FIELD_NAME AS nome, f.RDB$FIELD_TYPE AS tipo FROM RDB$RELATION_FIELDS r LEFT JOIN RDB$FIELDS f ON r.RDB$FIELD_SOURCE = f.RDB$FIELD_NAME WHERE r.RDB$RELATION_NAME='{self.table.root}' ORDER BY r.RDB$FIELD_POSITION")
        self.listattr = self.cur.fetchall()
        self.cur.execute(self.SQL)
        self.listObj = self.cur.fetchall()

        list = []
        j = 0
        for obj in self.listObj:
            Obj = Model()
            j = j + 1
            i = 0
            for attr in self.listattr:
                setattr(Obj,str((str(attr[0]).split())[0]),Type_column(attr[1],obj[i]))
                i = 1 + i
            list.append(Obj)
            
        return para_dict(list)


class Insert():
    SQL:str

    def __init__(self,con, table:str):
        self.table = table
        self.SQL = f'INSERT INTO  {self.table} ('
        self.con = con
    
    def tableModel(self,modeltable):
        i = 0
        for model in modeltable:
            if i > 0:
                self.SQL = self.SQL + f" ,{str(model[0]).strip()}"
            else:
                self.SQL = self.SQL + f" {str(model[0]).strip()}"
            i = i + 1
        self.SQL = self.SQL + ')'


        return self
        
    
    def valuesTable(self,values:str):
        self.SQL = self.SQL +f" VALUES ({values});"
        return self
    
    def return_query(self):
        return self.SQL
    
    def execute(self):
        self.cur = self.con.cursor()
        self.cur.execute(self.SQL)
        self.con.commit()











