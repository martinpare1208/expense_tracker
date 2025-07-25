from flask import request, jsonify, flash
import uuid
from app.db.models import User
from app import database, app, routes
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

def add_user_controller(username, password):
    new_user = User(
        username = username,
        hashed_password = bcrypt.generate_password_hash(password),
    )
    
    database.session.add(new_user)
    database.session.commit()
    
    
def get_and_authenticate_user_controller(username, password):
    user = User.query.where(username==User.username).first()
    if bcrypt.check_password_hash(user.hashed_password, password):
        return True, user
    else:
        return False, None

    

