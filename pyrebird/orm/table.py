
class TableTypes():
    @staticmethod
    def INTEGER():
        return 'INTEGER'
        ...
    @staticmethod
    def VARCHAR(amount):
        return f'VARCHAR({amount})'
        ...
    @staticmethod
    def FLOAT():
        return 'FLOAT'
        ...



def Colunm(Type, PrimaryKey = False, NotNUll = False):
    return { 'Type':Type, 'PrimaryKey':PrimaryKey, 'NotNUll':NotNUll}
    ...