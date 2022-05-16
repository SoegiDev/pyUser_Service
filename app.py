"""System module."""
import os
from flask import Flask,json,jsonify,request
from database import db
from service import typeService,service
from database import create_first
app = Flask(__name__)
init_db = db(app)
init_service = service(app)

HOST = "0.0.0.0"
PORT = 5002
if os.environ.get('FLASK_ENV') == 'dev':
    # app.logger.info(os.environ.get('FLASK_ENV'))
    app.config.from_object('config.Development')
elif os.environ.get('FLASK_ENV') == 'testing':
    # app.logger.info(os.environ.get('FLASK_ENV'))
    app.config.from_object('config.Testing')
else:
    # app.logger.info(os.environ.get('FLASK_ENV'))
    app.config.from_object('config.Production')
@app.route("/login",methods=["POST"])
def user_login():
    """A dummy docstring."""
    payload = json.loads(request.data)
    column = None
    param = payload
    init_service.set(typeService.data_user.value,typeService.data_userlogin.value)
    val = init_service.getService(column,param)
    if val['status'] is True and val['error'] is False :
        return jsonify({
                "error":val['error'],
                "data":val['data']
            }), 200
    if val['status'] is False and val['error'] is False :
        return jsonify({
                "error":val['error'],
                "message":val['message']
            }), 400
    return jsonify({
        "error":val['error'],
        "message":val['message']
        }), 500
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
        return jsonify({
                "error":val['error'],
                "data":val['data']
            }), 200
    if val['status'] is False and val['error'] is False :
        return jsonify({"error":val['error'],"message":val['message']}),400
    return jsonify({"error":val['error'],"message":val['message']}),500
@app.route("/single",methods=["GET"])
def user_single():
    """A dummy docstring."""
    username = request.args.get('username')
    column = None
    param = {"username":username}
    init_service.set(typeService.data_user.value,typeService.data_usersingle.value)
    val = init_service.getService(column,param)
    if val['status'] is True and val['error'] is False :
        return jsonify({
                "error":val['error'],
                "data":val['data']
            }), 200
    if val['status'] is False and val['error'] is False :
        return jsonify({
                "error":val['error'],
                "message":val['message']
            }), 400
    return jsonify({
        "error":val['error'],
        "message":val['message']
        }), 500
@app.route("/register",methods=["POST"])
def user_register():
    """A dummy docstring."""
    payload = json.loads(request.data)
    column = None
    param = payload
    init_service.set(typeService.data_user.value,typeService.data_userregister.value)
    val = init_service.getService(column,param)
    if val['status'] is True and val['error'] is False :
        return jsonify({
                "error":val['error'],
                "data":val['data']
            }), 200
    if val['status'] is False and val['error'] is False :
        return jsonify({
                "error":val['error'],
                "message":val['message']
            }), 400
    return jsonify({
        "error":val['error'],
        "message":val['message']
        }), 500
@app.route("/create",methods=["GET"])
def create_user():
    """A dummy docstring."""
    init=  app.config.get('INIT_FIRST')
    status = False
    message = "Table user sudah ada"
    if init :
        run = create_first.CreateDatabase(app)
        run.createUser()
        run.createMigrations()
        run.createConfiguration()
        run.getDataConfig()
        run.cursorClose()
        run.connClose
        status = True
        message= "Berhasil Create"
        app.config['INIT_FIRST'] = False
    return jsonify({
        "status" : status,
        "message":f"{message}"
    }),200
if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
    