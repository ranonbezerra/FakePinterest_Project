#THIS IS USED ONLY TO THE INITIAL CREATION OF THE DATABASE, DELETE LATER!

from fakepinterest_proj import database, app
from fakepinterest_proj.models import User, Post

with app.app_context():
    database.create_all()