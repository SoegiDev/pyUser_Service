from ast import arg
import re
from database import db
import sys
sys.path.append('./')
from validation import *
from model.User import User
from helper import *
from app import connection
# def connect_db():
#     d = dict()
#     init_db = db(app)
#     status = None
#     closed = None
#     messages = None
#     cursor = None
#     conn = None
#     status , closed , messages = init_db.ConnectionToDB()
#     if(status == 1) and (closed == 0):
#         conn,cursor,closed,status,messages = init_db.connect()
#         return conn,cursor,closed,status,messages,d
#     else:
#         return conn,cursor,closed,status,messages,d
    
    
def list(*args,**kwargs):
    try:
        users = User()
        defcolumn = defcolumn = (users.nm_id,users.nm_firstname,users.nm_lastname,users.nm_email,users.nm_email_confirmed,users.nm_job,users.nm_bio,users.nm_avatar,users.nm_added,users.nm_unique_id,users.nm_public,users.nm_identity) 
        conn,cursor,closed,status,message,d = connection()
        query = None
        datacolumn = None
        if kwargs.__len__() > 0:
            param = " and ".join(f"{key}='{value}'" for key, value in kwargs.items())
            if args.__len__() > 0:
                column = " , ".join(f"{value}" for value in args)
                datacolumn = args
                query = f"SELECT {column} FROM users where {param};"
            else:    
                column = " , ".join(f"{value}" for key, value in enumerate(defcolumn))  
                datacolumn = defcolumn
                query = f"SELECT {column} FROM users where {param};"
        else:
            if args.__len__() > 0:
                column = " , ".join(f"{value}" for key, value in enumerate(args))
                query = f"SELECT {column} FROM users;"
                datacolumn = args
            else:                 
                column = " , ".join(f"{value}" for key, value in enumerate(defcolumn))
                datacolumn = defcolumn
                query = f"SELECT {column} FROM users;"
        cursor.execute(query)
        rows = cursor.fetchall()
        data = []
        
        for row in rows:
            dicsss = dict(zip(datacolumn,row))
            data.append(
               dicsss
            )
        cursor.close()
        conn.close()
        d['status']  = True
        d['error']  = False
        d['message'] = "Successfully"
        d['data'] = data
        return d
    except Exception as err:
        print(f"ERROR: {err}")
        d['status']  = False
        d['error'] = True
        d['message'] = f"{err} {message}"
        return d
    
def single(*args,**kwargs):
    try:
        users = User()             
        defcolumn = (users.nm_id,users.nm_firstname,users.nm_lastname,users.nm_email,users.nm_email_confirmed,users.nm_job,users.nm_bio,users.nm_avatar,users.nm_added,users.nm_unique_id,users.nm_public,users.nm_identity)
        conn,cursor,closed,status,message,d = connection()
        query = None
        datacolumn = None
        if kwargs.__len__() > 0:
            param = " and ".join(f"{key}='{value}'" for key, value in kwargs.items())
            if args.__len__() > 0:
                column = " , ".join(f"{value}" for value in args)
                query = f"SELECT {column} FROM users where {param};"
            else:      
                column = " , ".join(f"{value}" for key, value in enumerate(defcolumn))  
                datacolumn  = defcolumn
                query = f"SELECT {column} FROM users where {param};"
        else:
            if args.__len__() > 0:
                column = " , ".join(f"{value}" for key, value in enumerate(args))
                query = f"SELECT {column} FROM users;"
                datacolumn = args
            else:                 
                column = " , ".join(f"{value}" for key, value in enumerate(defcolumn))
                datacolumn = args
                query = f"SELECT {column} FROM users;"
        cursor.execute(query)
        row = cursor.fetchone()
        data = dict(zip(datacolumn,row))
        cursor.close()
        conn.close()
        d['status']  = True
        d['error'] = False
        d['message'] = "Successfully"
        d['data'] = data
        return d
    except Exception as err:
        d['status']  = False
        d['error'] = True
        d['message'] = f"{err} {message}"
        return d
    
def login(*args,**kwargs):
    try:
        users = User()             
        defcolumn = (users.nm_id,users.nm_public,users.nm_unique_id,users.nm_email,users.nm_username,users.nm_password)
        conn,cursor,closed,status,message,d = connection()
        query = None
        datacolumn = None
        username = kwargs['username']
        password = kwargs['password']
        column = " , ".join(f"{value}" for key, value in enumerate(defcolumn))
        query = f"SELECT {column} FROM public.users WHERE username='{username}';"
        cursor.execute(query)
        if(cursor.rowcount == 0 ):
            d['status']  = False
            d['error']  = False
            d['message'] = "Username Not Exist"
            d['data'] = None
            return d
        row = cursor.fetchone()
        users = User()
        users.set_id(row[0])
        users.set_public_id(row[1])
        users.set_unique_id(row[2])
        users.set_email(row[3])
        users.set_username(row[4])
        users.set_password(bytes(row[5]))
        if not users.checkPassword(password):
                d['status']  = False
                d['error']  = False
                d['message'] = "Password Not Valid"
                d['data'] = None
                return d
        result = users.format_login()
        cursor.close()
        conn.close()
        data = {"username":result['username'].lower(),
                "public_id":result['public_id'],
                "email":result['email'].lower()}
        d['status']  = True
        d['error']  = False
        d['message'] = "Successfully"
        d['data'] = result
        return d
    except Exception as err:
        print(f"ERROR: {err}")
        d['status']  = False
        d['error']  = True
        d['message'] = f"{err} {message}"
        return d
    
def register(*args, **kwargs):
    try:
        conn,cursor,closed,status,message,d = connection()
        required_fields = ["first_name", "last_name",
                "email", "username", "password"]
        for field in required_fields:
            if field not in kwargs:
                d['status']  = False
                d['error']  = False
                d['message'] = '%s is required' % field
                d['data'] = None
                return d   
        username = kwargs["username"]
        password = kwargs["password"]
        first_name = kwargs['first_name']
        last_name = kwargs['last_name']
        email = kwargs["email"]
        val = validation(type.email.value).validate_man(email)
        if val['status'] == False :
            d['status']  = False
            d['error']  = False
            d['message'] = 'Email Not Valid'
            d['data'] = None
            return d 
        query = f"SELECT * FROM users WHERE username='{username}'"
        cursor.execute(query)
        print("Hasil",str(cursor.rowcount))
        if(cursor.rowcount == 1):
                cursor.close()
                conn.close()
                d['status']  = False
                d['error']  = False
                d['message'] = 'Account already Exist'
                d['data'] = None
                return d   
                # Get Number ID USER
        qr = f"SELECT unique_id FROM users order by unique_id desc ;"
        cursor.execute(qr)
        row = cursor.fetchone()[0]
        unique_id = CreateUserUniqueID(row)
        hashed = CreatePassword(password).decode('utf-8')
        public_id = str(uuid.uuid4())
        #Insert To Database
        query = f"\
            INSERT INTO users(id, email, password) VALUES('{uuid.uuid4()}','{email}','{password}')\
            # "
        qr = f"WITH users as ( \
            INSERT INTO users(first_name,last_name,email,username,password,unique_id,public_id) \
            VALUES ('{first_name}','{last_name}','{email}','{username}','{hashed}','{unique_id}','{public_id}') RETURNING *)\
            INSERT INTO users_roles(user_id, role_id) \
            VALUES ((select users.id from users), 1);"
        cursor.execute(qr)
        conn.commit()
        cursor.close()
        conn.close()
        data = {'email':email,'username':username}
        d['status']  = True
        d['error']  = False
        d['message'] = 'Registered'
        d['data'] = data
        return d
    except Exception as err:
        print(f"ERROR: {err}")
        d['status']  = False
        d['error']  = True
        d['message'] = f"{err} {message}"
        return d
            