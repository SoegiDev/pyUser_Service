"""System module."""
import os
from flask import Flask,json,jsonify,request
from database import db,create_first
from service import typeService,service
from helper import response
app = Flask(__name__)
if os.environ.get('FLASK_ENV') == 'development':
    # app.logger.info(os.environ.get('FLASK_ENV'))
    app.config.from_object('config.Development')
    init_db = db(app)
elif os.environ.get('FLASK_ENV') == 'testing':
    # app.logger.info(os.environ.get('FLASK_ENV'))
    app.config.from_object('config.Testing')
    init_db = db(app)
else:
    # app.logger.info(os.environ.get('FLASK_ENV'))
    app.config.from_object('config.Production')
    init_db = db(app)
init_service = service(app)
HOST = "0.0.0.0"
PORT = 5002

@app.route("/login",methods=["POST"])
def user_login():
    """A dummy docstring."""
    payload = json.loads(request.data)
    column = None
    param = payload
    init_service.set(typeService.data_user.value,typeService.data_userlogin.value)
    val = init_service.getService(column,param)
    if val['status'] is True and val['error'] is False :
        return response.itsOk(val)
    if val['status'] is False and val['error'] is False :
        return response.badRequest(val)
    return response.unProcess(val)
@app.route("/hello",methods=['GET'])
def hello():
    """A dummy docstring."""
    return jsonify({
        "data":"Hello World"
    })
@app.route("/list",methods=["GET"])
def user_list():
    """A dummy docstring."""
    column = None
    param = {}
    init_service.set(typeService.data_user.value,typeService.data_userlist.value)
    val = init_service.getService(column,param)
    if val['status'] is True and val['error'] is False :
        return response.itsOk(val)
    if val['status'] is False and val['error'] is False :
        return response.badRequest(val)
    return response.unProcess(val)
@app.route("/single",methods=["GET"])
def user_single():
    """A dummy docstring."""
    username = request.args.get('username')
    column = None
    param = {"username":username}
    init_service.set(typeService.data_user.value,typeService.data_usersingle.value)
    val = init_service.getService(column,param)
    if val['status'] is True and val['error'] is False :
        return response.itsOk(val)
    if val['status'] is False and val['error'] is False :
        return response.badRequest(val)
    return response.unProcess(val)
@app.route("/register",methods=["POST"])
def user_register():
    """A dummy docstring."""
    payload = json.loads(request.data)
    column = None
    param = payload
    init_service.set(typeService.data_user.value,typeService.data_userregister.value)
    val = init_service.getService(column,param)
    if val['status'] is True and val['error'] is False :
        return response.itsOk(val)
    if val['status'] is False and val['error'] is False :
        return response.badRequest(val)
    return response.unProcess(val)
@app.route("/create",methods=["GET"])
def create_user():
    """A dummy docstring."""
    init=  app.config.get('INIT_FIRST')
    if init :
        initial = create_first.CreateDatabase()
        initial.createUser()
        initial.createMigrations()
        initial.createConfiguration()
        initial.getDataConfig()
        initial.cursorClose()
        initial.connClose()
        app.config['INIT_FIRST'] = False
    result ={}
    result['error'] = False
    result['message'] = "Successfully Create Table"
    return response.itsOk(result)
if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
    