from src.user import bp
from src.models import User
from flask import request
import uuid

@bp.route('/user/signup', methods=['POST'])
def signup_route():
    _id = uuid.uuid4().hex
    name =  request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    user_data = {
        "_id": _id,
        "name": name,
        "email": email,
        "password": password
    }
    return User().signup(user_data)

@bp.route('/user/signout')
def signout_route():
    return User().signout()

@bp.route('/user/login', methods=['POST'])
def login_route():
    email = request.form.get('email')
    password = request.form.get('password')
    user_data = {
        "email": email,
        "password": password
    }
    return User().login(user_data)
