from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from sqlalchemy import inspect

load_dotenv()

# access environment variables
SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASE_NAME = os.environ.get('DATABASE_NAME') 

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_NAME}'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

# import views and models to register routes and models
from app import views, models

def check_and_create_tables():
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    if 'user' not in tables:
        db.create_all()

# ensure the tables are created
with app.app_context():
    check_and_create_tables()
