



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