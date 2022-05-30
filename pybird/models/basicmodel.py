class BasicModel():
    def __init__(self,list, root):
        setattr(self,'root',root)
        self.map = {}
        for  attr in list:
            self.map[str(attr[0]).strip()] = int(str(attr[1]).strip())
            #setattr(self,str(attr[0]).strip(),{str(attr[0]).strip():int(str(attr[1]).strip())})
        pass