import fdb
from typing              import List


#Gerenciamento do Banco
def Create_Session( dsn:str,user:str,password:str,charset:str):
    con = fdb.connect(dsn=dsn, user=user, password=password, charset=charset)
    return con

def auto_map(con,table):
        cur = con.cursor()
        cur.execute(f" SELECT r.RDB$FIELD_NAME AS nome, f.RDB$FIELD_TYPE AS tipo FROM RDB$RELATION_FIELDS r LEFT JOIN RDB$FIELDS f ON r.RDB$FIELD_SOURCE = f.RDB$FIELD_NAME WHERE r.RDB$RELATION_NAME='{table}' ORDER BY r.RDB$FIELD_POSITION")
        return cur.fetchall()

def create_object(model,query,obj):
    for item in query:
        i = 0
        obj.Model = {'test':23}
        for  campo in item:
            aux = model[i]
            obj.Model[str(str(aux[0]).strip())] = str(campo)
            i = i + 1
        obj.List.append(obj.Model)

#Modelos
class BasicModel():
    def __init__(self):
        self.Model = {'test':23}
        self.List = []
        pass



#CRUD
class Select():
    SQL : str

    def __init__(self,con, table:str, filter_column:str):
        self.table = table
        self.SQL = f'SELECT {filter_column}  FROM  {self.table}'
        self.con = con

    '''def filter_by(self, listrequest = List[ModelRequest]):
        
        query = self.SQL + " WHERE"
        for request in listrequest:
            query = query + " " + request.column + " = " + "'" + request.value + "'"
        self.SQL = query
        return self'''
    
    def filter(self, conditions:str):
        
        query = f"{self.SQL} WHERE  {conditions}"
        self.SQL = query
        return self

    def return_query(self):
        return self.SQL
    
    def execute(self):
        listrequest = []
        self.cur = self.con.cursor()
        self.cur.execute(self.SQL)
        return self.cur.fetchall()


class Insert():
    SQL:str

    def __init__(self,con, table:str):
        self.table = table
        self.SQL = f'INSERT INTO  {self.table} ('
        self.con = con
    
    def tableModel(self,modeltable):
        
        for model in modeltable:
            self.SQL = self.SQL + f" {str(model[0]).strip()},"
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











