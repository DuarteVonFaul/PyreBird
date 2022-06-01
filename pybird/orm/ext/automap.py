from pybird.models.basicmodel import BasicModel
import copy


class auto_map():

    def __init__(self,con):
        self.cur = con.cursor()
        self.classes = {}
        pass

    def all(self):
        tablelist = []
        self.cur.execute('SELECT RDB$RELATION_NAME FROM RDB$RELATIONS WHERE RDB$SYSTEM_FLAG = 0 OR RDB$SYSTEM_FLAG IS NULL')
        for c in  self.cur.fetchall():
            tablelist.append(str(c[0]).strip())
        for table in tablelist:
            self.cur.execute(f" SELECT r.RDB$FIELD_NAME AS nome, f.RDB$FIELD_TYPE AS tipo FROM RDB$RELATION_FIELDS r LEFT JOIN RDB$FIELDS f ON r.RDB$FIELD_SOURCE = f.RDB$FIELD_NAME WHERE r.RDB$RELATION_NAME='{table}' ORDER BY r.RDB$FIELD_POSITION")
            self.classes[str(table).strip()] = BasicModel(self.cur.fetchall(),table)
        
        return self

    
    def get(self,table:str):
        self.cur.execute(f" SELECT r.RDB$FIELD_NAME AS nome, f.RDB$FIELD_TYPE AS tipo FROM RDB$RELATION_FIELDS r LEFT JOIN RDB$FIELDS f ON r.RDB$FIELD_SOURCE = f.RDB$FIELD_NAME WHERE r.RDB$RELATION_NAME='{table}' ORDER BY r.RDB$FIELD_POSITION")
        self.classes[table] = BasicModel(self.cur.fetchall(),table)

        return self
        
    
    def filter_by(self,tablelist:list):
        self.listclass = {}
        for table in tablelist:
            self.cur.execute(f" SELECT r.RDB$FIELD_NAME AS nome, f.RDB$FIELD_TYPE AS tipo FROM RDB$RELATION_FIELDS r LEFT JOIN RDB$FIELDS f ON r.RDB$FIELD_SOURCE = f.RDB$FIELD_NAME WHERE r.RDB$RELATION_NAME='{table}' ORDER BY r.RDB$FIELD_POSITION")
            self.classes[str(table).strip()] = BasicModel(self.cur.fetchall(),table)

        return self

    
    def get_class(self,classe:str):
        return copy.copy(self.classes[classe])

    def classes_keys(self):
        string = ""
        for clss in self.classes:
            string = str(string) + " " + str(clss)
        return string