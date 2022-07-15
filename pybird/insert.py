class Insert():
    SQL:str

    def __init__(self,con, table):
        self.table = table
        self.SQL = f'INSERT INTO  "{self.table.root}" '
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