import fdb

def Create_Session( dsn:str,user:str,password:str,charset:str):
    con = fdb.connect(dsn=dsn, user=user, password=password, charset=charset)
    return con