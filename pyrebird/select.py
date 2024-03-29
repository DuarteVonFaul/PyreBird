from pyrebird.utils.utils         import convert_type,refacture_args
from typing                     import Optional
from pyrebird.models.model        import Model

class Base():
    def __init__(self) -> None:
        pass    

        #Metodo Where column = value and
    def filter_by(self, **kwargs):
        query = f"{self.SQL} WHERE"
        conditions = []
        first_condition = True
        for key, value in kwargs.items():
            if first_condition:
                placeholder = "'{}'" if isinstance(value, str) else "{}"
                conditions.append(f"{key} = {placeholder.format(value)}")
                first_condition = False
            else:
                placeholder = "'{}'" if isinstance(value, str) else "{}"
                conditions.append(f" AND {key} = {placeholder.format(value)}") 

        self.SQL = f"{query} ".join(conditions)
        return self

    def return_query(self):
        return self.SQL
    
    def execute(self):
        self.cur = self.con.cursor()
        self.cur.execute(self.SQL)
        return self.cur.fetchone()[0]

class Select(Base):
    SQL : str

    #Metodo Construtor
    def __init__(self,con, obj, *args:Optional[list], first=0):
        self.con = con
        self.table = obj
        self.SQL = f'SELECT FIRST {first}' if first > 0 else 'SELECT'
        self.SQL += f' *' if len(args) <= 0 else f' ' + refacture_args(args)
        self.SQL += f' FROM {self.table.root}'
        self.filter_column = args

    #Metodo para adicionar query manualmente
    def manualQuery(self, filter:str):
        query = f"{self.SQL} {filter}"
        self.SQL = query
        return self

        #Metodo Orden By
    def orden_by(self,*args, Keyword = "Desc"):
        query = f"{self.SQL} ORDER BY"
        self.SQL = query +f" {refacture_args(args)} "+ Keyword
        return self

    #Retorna um unico resultado da query
    def execute(self):
        self.cur = self.con.cursor()
        self.cur.execute(self.SQL)
        self.listObj = self.cur.fetchone()
        i = 0
        Obj = Model()
        if(len(self.filter_column) <= 0):
            for attr in self.table.map:
                setattr(Obj,attr,convert_type(self.table.map[attr],(self.listObj)[i]))
                i += 1
            return Obj
        else:
            for attr in self.filter_column:
                setattr(Obj,attr,convert_type(self.table.map[attr],(self.listObj)[i]))
                i += 1
            return Obj
    
    #Retorna todos os resultado da query
    def all(self):
        self.cur = self.con.cursor()
        self.cur.execute(self.SQL)
        self.listObj = self.cur.fetchall()

        list = []
        if(len(self.filter_column) <= 0):
            for x in self.listObj:
                Obj = Model()
                i = 0
                for attr in self.table.map:
                    setattr(Obj,attr,convert_type(self.table.map[attr],x[i]))
                    i += 1 
                list.append(Obj)
                
            return list
        else:
            for x in self.listObj:
                Obj = Model()
                i = 0
                for attr in self.filter_column:
                    setattr(Obj,attr,convert_type(self.table.map[attr],x[i]))
                    i += 1
                list.append(Obj)
            
            return list
    
class Like():
    pass

class Max(Base):
    def __init__(self,con, obj,column):
        self.con = con
        self.table = obj
        self.SQL = f'SELECT MAX '
        self.SQL = f'{self.SQL} ({column}) FROM {self.table.root}'

class Min(Base):
    def __init__(self,con, obj,column):
        self.con = con
        self.table = obj
        self.SQL = f'SELECT MIN '
        self.SQL = f'{self.SQL} ({column}) FROM {self.table.root}'

class Count(Base):
    def __init__(self,con, obj,column):
        self.con = con
        self.table = obj
        self.SQL = f'SELECT COUNT '
        self.SQL = f'{self.SQL} ({column}) FROM {self.table.root}'

class AVG(Base):
    def __init__(self,con, obj,column):
        self.con = con
        self.table = obj
        self.SQL = f'SELECT AVG '
        self.SQL = f'{self.SQL} ({column}) FROM {self.table.root}'

class Sum(Base):
    def __init__(self,con, obj,column):
        self.con = con
        self.table = obj
        self.SQL = f'SELECT SUM '
        self.SQL = f'{self.SQL} ({column}) FROM {self.table.root}'