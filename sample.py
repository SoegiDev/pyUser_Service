from flask import *
from database import db
import sys
sys.path.append('./')
from service import *
from validation import *
app = Flask(__name__)
HOST = "0.0.0.0"
PORT = 5001
def connection():
    initdb = db()
    status = None
    closed = None
    messages = None
    cursor = None
    conn = None
    status , closed , messages = initdb.ConnectionToDB()
    connection = False
    if(status == 1) and (closed == 0):
        conn,cursor,closed,status,messages = initdb.connect()
        return conn,cursor,closed,status,messages
    else:
        return conn,cursor,closed,status,messages
    
def validationEmail():
    x = input("Enter Your Email: ")
    val = validation(type.email.value).validate_man(x)
    if val :
        print("Email Valid")
    else:
        print("Email tidak valid")
        
def validateusername():
    x = input("Enter Your Username: ")
    val = validation(type.username.value).validate_man(x)
    if val['status'] :
        print(val['message'])
    else:
        print(val['message'])

def validatepassword():
    x = input("Enter Your password: ")
    val = validation(type.password.value).validate_man(x)
    if val['status'] :
        print(val['message'])
    else:
        print(val['message'])


@app.route("/connect",methods=["GET"])
def connect():
    conn,cursor,closed,status,message = connection()
    print("message", message)
    return jsonify({
        "status" : status,
        "message":f"{message}"
    }),200
    

if __name__ == "__main__":
    connection()
    validationEmail()
    validatepassword()
