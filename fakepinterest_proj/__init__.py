from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///fakepinterest_database.db'

database = SQLAlchemy(app)

from fakepinterest_proj import routes