from flask import Flask
import os
from app.db import models
from dotenv import load_dotenv

app = Flask(__name__)


# Init .env
load_dotenv()

what = os.getenv("TEST")
print(what)


# Save the database in /app/db/
db_dir = os.path.abspath(os.path.dirname(__file__)) + '/db/'

# Init models
models.database.init_app(app)




