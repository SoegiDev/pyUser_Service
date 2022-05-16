import sys
sys.path.append('./')
from validation import validate
import enum
class type(enum.Enum):
    email = "email"
    username = "username"
    password = "password"
class validation():
    callback = None
    def __init__(self,callback : str) -> None:
        self.callback = callback
    def validate_man(self,s):
        method = getattr(validate,self.callback)
        callback = method(s)
        return callback
    
    
    
    
    