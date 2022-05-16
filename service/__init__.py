import importlib
from subprocess import call
import sys
import enum
class typeService(enum.Enum):
    data_user = "service.data_"
    data_userlist = "list"
    data_usersingle = "single"
    data_userlogin = "login"
    data_userregister = "register"
class service():
    modulecall = None
    callback = None
    def __init__(self,app):
        self.app = app    
    def set(self,modulecall : str = None,callback : str = None) -> None:
        self.callback = callback
        self.modulecall = modulecall
    def getService(self,column, field):
            mod = importlib.import_module(self.modulecall)
            str = self.callback
            #class_, func_ = str.rsplit(".", 1)
            #class_= getattr(mod,class_)
            func_ = getattr(mod,str)
            running = None
            if column is None:
                running = func_(**field)
            else:
                running = func_(*column,**field)
            return running
    
    
    
    
    
    
    