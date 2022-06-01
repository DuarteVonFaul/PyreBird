from pybird.utils.convertType import column
from pybird.models.model import Model



class Select():
    SQL : str

    #Metodo Construtor
    def __init__(self,con, obj, filter_column='*'):
        self.table = obj
        if filter_column != '*':
            self.column = filter_column.split(',')
        else:
            self.column = filter_column
        self.SQL = f'SELECT {filter_column}  FROM  {self.table.root}'
        self.con = con
    
    #Metodo para adicionar query manualmente
    def manualQuery(self, filter:str):
        query = f"{self.SQL} {filter}"
        self.SQL = query
        return self

    #Metodo Orden By
    def orden_by(self,*args, Keyword = "Desc"):
        query = f"{self.SQL} ORDER BY"
        i = 0
        for qry in args:
            if i == 0:
                query = f"{query} {str(qry)}"
                i += 1
            else:
                query = f"{query}, {str(qry)}"
        self.SQL = query + Keyword
        return self

    #Metodo Where column = value and
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
    
    #Retorna a Query no formado de String
    def return_query(self):
        return self.SQL
    
    #Retorna um unico resultado da query
    def only(self):
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
    
    #Retorna todos os resultado da query
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