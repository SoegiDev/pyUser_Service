
import uuid
import datetime
import bcrypt
import os
import re
        
def CreateUserUniqueID(last_Uniqueid)->str:
        prefix = datetime.datetime.today().strftime('%y%m%d')
        result = ''
        if last_Uniqueid is None :
            result = "USR00001"
        else:
            uniqueid =  last_Uniqueid
            result = str(int(uniqueid[3:]) + 1)
            result = uniqueid[0:-(len(result))] + result
        return result

def CreatePassword(password: str):
        password = bytes(password, encoding='utf-8')
        return bcrypt.hashpw(password, bcrypt.gensalt())