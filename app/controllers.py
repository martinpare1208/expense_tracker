from flask import request, jsonify, flash, url_for
import uuid
from app.db.models import User
from app import database, app, routes, objects
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

def if_user_exists_controller(user: User) -> bool:
    checked_user = User.query.where(User.username == user.username).first()
    if checked_user:
        return True
    
    return False

def add_user_controller(username: str, password: str) -> objects.ControllerResult:
    
    new_user = User(
        username = username,
        hashed_password = bcrypt.generate_password_hash(password),
    )

    if if_user_exists_controller(new_user) == False:
        database.session.add(new_user)
        database.session.commit()
        
        
        is_success = True
        message = 'Your registration was complete. Please login.'
        data = new_user
        
        controller_result = objects.ControllerResult(is_success, message, data)
        
        return controller_result
    
    is_success = False
    message = 'Your registration was not complete. That username already exists.'
    data = None
    controller_result = objects.ControllerResult(is_success, message, data)
    return controller_result
    
    
def get_and_authenticate_user_controller(username, password):
    user = User.query.where(username==User.username).first()
    if bcrypt.check_password_hash(user.hashed_password, password):
        return True, user
    else:
        return False, None

    

