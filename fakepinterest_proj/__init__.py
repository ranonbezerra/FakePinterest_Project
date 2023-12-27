from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///fakepinterest_database.db'
app.config["SECRET_KEY"] = 'ad58f44870ef1d388849da006553fac3f7221d11e6defec4b2206e6df92a9d1c'
app.config['UPLOAD_FOLDER'] = 'static/post_images'


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'


from fakepinterest_proj import routes