  
class Update():
    SQL:str

    def __init__(self,con, table):
        self.table = table
        self.SQL = f'UPDATE {self.table.root}'
        self.con = con
    
    def set(self, **kwargs):
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
    
    def is_null(self, field):

        query += f"{self.SQL} WHERE {field} is null"

        self.SQL = query
        return self
    
    def return_query(self):
        return self.SQL
    
    def execute(self):
        self.cur = self.con.cursor()
        self.cur.execute(self.SQL)
        self.con.commit()