from flask import request, jsonify
import uuid
from app.db.models import User
from app import database, app

def add_user_controller():
    new_user = User(
        id = 1,
        username = 'martin',
        hashed_password = 'test',
    )

    database.session.add(new_user)
    database.session.commit()
