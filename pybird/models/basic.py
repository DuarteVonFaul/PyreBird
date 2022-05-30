class BasicModel():
    def __init__(self,list, root):
        setattr(self,'root',root)
        for  attr in list:
            setattr(self,str(attr[0]).strip(),None)
        pass

class Model():
    def __init__(self) -> None:
        pass