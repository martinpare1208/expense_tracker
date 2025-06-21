from flask import Flask
import os
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.db.models import User, database
from flask_login import LoginManager


app = Flask(__name__)


load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database.init_app(app)
migrate = Migrate(app, database)


login_manager = LoginManager()
login_manager.init_app(app)


