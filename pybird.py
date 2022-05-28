import fdb
from utils               import Type_column,para_dict

#Funcionalidades ORM
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
    def __init__(self,list, root):
        setattr(self,'root',root)
        for  attr in list:
            setattr(self,str(attr[0]).strip(),None)
        pass

class Model():
    def __init__(self) -> None:
        pass



#CRUD
class Select():
    SQL : str

    def __init__(self,con, obj, filter_column='*'):
        self.table = obj
        self.SQL = f'SELECT {filter_column}  FROM  {self.table.root}'
        self.con = con
    
    def filter_by(self, **kwargs):
        query = f"{self.SQL} WHERE"
        for key, value in kwargs.items():
            if(type(value) == str):
                query = query +  f" {key} = '{value}'"
            else:
                query = query +  f" {key} = {value}"
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

    def __init__(self,con, table):
        self.table = table
        self.SQL = f'INSERT INTO  {self.table.root}'
        self.con = con
    
    def values(self, **kwargs):
        i = 0
        SQLVALUE = ''
        SQLINTO = ''
        for key, value in kwargs.items():
            if i > 0:
                SQLINTO = SQLINTO  + f", {key}"
                if(type(value) == str):
                    SQLVALUE = SQLVALUE  + f", '{value}'"
                else:
                    SQLVALUE = SQLVALUE  + f", {value}"
            else:
                SQLINTO = SQLINTO  + f" ( {key}"
                if(type(value) == str):
                    SQLVALUE = SQLVALUE  + f"( '{value}'"
                else:
                    SQLVALUE = SQLVALUE  + f"( {value}"    
            i = i + 1
        SQLVALUE = SQLVALUE + ' )'
        SQLINTO = SQLINTO + ' )'
        self.SQL = f'{self.SQL} {SQLINTO} VALUES {SQLVALUE}'


        return self
        
    
    def return_query(self):
        return self.SQL
    
    def execute(self):
        self.cur = self.con.cursor()
        self.cur.execute(self.SQL)
        self.con.commit()


class Delete():
    SQL:str

    def __init__(self,con, table, filter_column='*'):
        self.table = table
        self.SQL = f'DELETE {filter_column} INTO  {self.table.root}'
        self.con = con
    
    def filter_by(self, **kwargs):
        query = f"{self.SQL} WHERE"
        for key, value in kwargs.items():
            if(type(value) == str):
                query = query +  f" {key} = '{value}'"
            else:
                query = query +  f" {key} = {value}"
        self.SQL = query
        return self
    
    def return_query(self):
        return self.SQL
    
    def execute(self):
        self.cur = self.con.cursor()
        self.cur.execute(self.SQL)
        self.con.commit()

    
class Update():
    SQL:str

    def __init__(self,con, table, filter_column='*'):
        self.table = table
        self.SQL = f'UPDATE {self.table.root}'
        self.con = con
    
    def setUpdate(self, **kwargs):
        query = f"{self.SQL} SET"
        for key, value in kwargs.items():
            if(type(value) == str):
                query = query +  f" {key} = '{value}'"
            else:
                query = query +  f" {key} = {value}"
        self.SQL = query
        return self

    def filter_by(self, **kwargs):
        query = f"{self.SQL} WHERE"
        for key, value in kwargs.items():
            if(type(value) == str):
                query = query +  f" {key} = '{value}'"
            else:
                query = query +  f" {key} = {value}"
        self.SQL = query
        return self
    
    def return_query(self):
        return self.SQL
    
    def execute(self):
        self.cur = self.con.cursor()
        self.cur.execute(self.SQL)
        self.con.commit()











