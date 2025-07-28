from flask import request, jsonify, flash, url_for, Response
from app.db.models import User,  Expense
from app import database, app, routes
from app.objects import ControllerResult
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

def if_user_exists_controller(user: User) -> bool:
    checked_user = User.query.where(User.username == user.username).first()
    if checked_user:
        return True
    
    return False

def add_user_controller(username: str, password: str) -> ControllerResult:
    
    new_user = User(
        username = username,
        hashed_password = bcrypt.generate_password_hash(password),
    )

    if if_user_exists_controller(new_user) == False:
        database.session.add(new_user)
        database.session.commit()
        
        
        is_success = True
        message = 'Your registration was complete. Please login.'
        response = Response(status=200, response=message)
        data = new_user
        
        controller_result = ControllerResult(is_success, message, response, data)
        
        return controller_result
    
    is_success = False
    message = 'Your registration was not complete. That username already exists.'
    data = None
    response = Response(status=409, response=message)
    
    controller_result = ControllerResult(is_success, message, response, data)
    return controller_result
    
    
def get_and_authenticate_user_controller(username: str, password: str):
    user = User.query.where(username==User.username).first()
    if bcrypt.check_password_hash(user.hashed_password, password):
        return True, user
    else:
        return False, None
    
    
def add_expense_controller(user: User, expense: Expense) -> ControllerResult:
    return

    

