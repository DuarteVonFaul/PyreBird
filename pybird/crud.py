from pybird.utils.convertType import column
from pybird.models.model import Model

class Select():
    SQL : str

    def __init__(self,con, obj, filter_column='*'):
        self.table = obj
        if filter_column != '*':
            self.column = filter_column.split(',')
        else:
            self.column = filter_column
        self.SQL = f'SELECT {filter_column}  FROM  {self.table.root}'
        self.con = con
    
    def manual(self, filter:str):
        query = f"{self.SQL} {filter}"
        self.SQL = query
        return self

    def filter_by(self, **kwargs):
        query = f"{self.SQL} WHERE"
        
        i = 0
        for key, value in kwargs.items():
            if(i == 0):
                if(type(value) == str):
                    query = query +  f" {key} = '{value}'"
                    i += 1 
                else:
                    query = query +  f" {key} = {value}"
                    i += 1 
            else:
                if(type(value) == str):
                    query = query +  f" AND {key} = '{value}'"
                else:
                    query = query +  f" AND  {key} = {value}"
        self.SQL = query
        return self

    def return_query(self):
        return self.SQL
        
    def scalar(self):
        self.cur = self.con.cursor()
        self.cur.execute(self.SQL)
        self.listObj = self.cur.fetchone()
        i = 0
        Obj = Model()
        if(self.column == '*'):
            for attr in self.table.map:
                setattr(Obj,attr,column(self.table.map[attr],(self.listObj)[i]))
                i = 1 + i
            return Obj
        else:
            for attr in self.column:
                setattr(Obj,str(attr).strip(),column(self.table.map[str(attr).strip()],(self.listObj)[i]))
                i = 1 + i
            return Obj

        
    def all(self):
        self.cur = self.con.cursor()
        self.cur.execute(self.SQL)
        self.listObj = self.cur.fetchall()

        list = []
        j = 0
        if(self.column == '*'):
            for x in self.listObj:
                Obj = Model()
                j = j + 1
                i = 0
                for attr in self.table.map:
                    setattr(Obj,attr,column(self.table.map[attr],x[i]))
                    i = 1 + i
                list.append(Obj)
                
            return list
        else:
            for x in self.listObj:
                Obj = Model()
                j = j + 1
                i = 0
                for attr in self.column:
                    setattr(Obj,str(attr).strip(),column(self.table.map[str(attr).strip()],x[i]))
                    i = 1 + i
                list.append(Obj)
            
            return list


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
        print(self.SQL)
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