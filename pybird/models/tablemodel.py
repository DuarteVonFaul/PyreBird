from ..utils.utils import to_dict


class TableModel:

    __TableName__ = None

    def __init__(self) -> None:
        setattr(self,'map', self.__return_attrs())
        setattr(self,'root', self.return_name())

        

    @classmethod
    @staticmethod
    def to_type(type):

        if type == "INTEGER":
            return int
        elif type[:7] == "VARCHAR":
            return str
        elif type == "FLOAT":
            return float
        else:
            return 'None Type' 


    @classmethod
    def return_name(cls) -> str:
        if cls.__TableName__ != None:
            return cls.__TableName__
        else:
            return cls.__name__

    @classmethod
    def __return_attrs(cls):
        listAttrs = cls.__dict__

        attrs = {}
        for key in listAttrs:
            if(key[0:2] != '__'):
                attrs[key] = cls.to_type(listAttrs[key]['Type'])
        return attrs 
    ...

    
        