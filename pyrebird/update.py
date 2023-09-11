  
class Update():
    SQL:str

    def __init__(self,con, table):
        self.table = table
        self.SQL = f'UPDATE {self.table.root}'
        self.sql_filter = ""
        self.sql_set = ""
        self.con = con
    
    def set(self, **kwargs):
        conditions = []
        first_condition = True

        for key, value in kwargs.items():
            # Evite a repetição de código usando placeholders
            if first_condition:
                placeholder = "'{}'" if isinstance(value, str) else "{}"
                conditions.append(f"{key} = {placeholder.format(value)}")
                first_condition = False
            else:
                placeholder = "'{}'" if isinstance(value, str) else "{}"
                conditions.append(f" AND {key} = {placeholder.format(value)}")

        query = " SET ".join(conditions)  
        self.sql_set = query
        return self

    def filter_by(self, **kwargs):
        conditions = []
        first_condition = True

        for key, value in kwargs.items():
            # Evite a repetição de código usando placeholders
            if first_condition:
                placeholder = "'{}'" if isinstance(value, str) else "{}"
                conditions.append(f"{key} = {placeholder.format(value)}")
                first_condition = False
            else:
                placeholder = "'{}'" if isinstance(value, str) else "{}"
                conditions.append(f" AND {key} = {placeholder.format(value)}")

        self.sql_filter = " WHERE ".join(conditions)
        return self
    
    def is_null(self, field):

        query = f"{self.SQL} WHERE {field} is null"

        self.sql_set = query
        return self
    
    def return_query(self):
        return self.SQL
    
    def execute(self):
        self.cur = self.con.cursor()
        self.cur.execute(self.SQL)
        self.con.commit()