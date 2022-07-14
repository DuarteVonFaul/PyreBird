class TableModel:
    
    @classmethod
    def __create_query(cls):

        list = cls.__annotations__
        query = f'CREATE TABLE {str(cls.__name__)} \n'
        for key in list:
            if key[0:2].upper() == 'ID':
                query += f' {str(key)} {cls.to_type(list[key])} not null primary key\n'
            elif cls.to_type(list[key]) != 'None Type':
                query += f' {str(key)} {cls.to_type(list[key])}\n'
            else:
                ...
        
        return query
            
    @classmethod
    def create_table(cls):
        
        print(cls.__create_query())
    
    @classmethod
    @staticmethod
    def to_type(type):

        if type == int:
            return 'Integer'
        elif type == str:
            return 'String'
        elif type == float:
            return 'Number(5,7)'
        else:
            return 'None Type' 

        