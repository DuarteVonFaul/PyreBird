from calendar import c
import fdb
from typing              import List




class ModelRequest():

    column : str
    value  : str

    def __init__(self) -> None:
        pass


def Create_Session( dsn:str,user:str,password:str,charset:str):
    con = fdb.connect(dsn=dsn, user=user, password=password, charset=charset)
    return con

def auto_map(con,table):
        cur = con.cursor()
        cur.execute(f" SELECT r.RDB$FIELD_NAME AS nome, f.RDB$FIELD_TYPE AS tipo FROM RDB$RELATION_FIELDS r LEFT JOIN RDB$FIELDS f ON r.RDB$FIELD_SOURCE = f.RDB$FIELD_NAME WHERE r.RDB$RELATION_NAME='{table}' ORDER BY r.RDB$FIELD_POSITION")
        return cur.fetchall()


class Select():

    SQL : str

    def __init__(self,con, table:str, filter_column:str):
        self.table = table
        self.SQL = 'SELECT ' + filter_column + ' FROM ' + self.table
        self.con = con
    
    

    def filter_by(self, listrequest = List[ModelRequest]):
        
        query = self.SQL + " WHERE"
        for request in listrequest:
            query = query + " " + request.column + " = " + "'" + request.value + "'"
        self.SQL = query
        return self
    
    def filter(self, conditions:str):
        
        query = self.SQL + " WHERE " + conditions
        self.SQL = query
        return self

    def return_query(self):
        return self.SQL
    
    def execute(self):
        listrequest = []
        self.cur = self.con.cursor()
        self.cur.execute(self.SQL)
        return self.cur.fetchall()










