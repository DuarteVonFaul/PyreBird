from pybird.insert import Insert
from test_createTabel import User
from database           import MySession


user = User('Duarte001', '1234')


Insert(MySession, user).values( USER_NAME = 'Duarte001', 
                                USER_PASSWORD = '1234').execute()