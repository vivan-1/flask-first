from apps import db, app

from apps import login_manager
from werkzeug import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(128))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def checkpassword(self, password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))