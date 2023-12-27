from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from fakepinterest_proj.secret import secret_key

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///fakepinterest_database.db'
app.config["SECRET_KEY"] = secret_key
app.config['UPLOAD_FOLDER'] = 'static/post_images'


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'


from fakepinterest_proj import routes