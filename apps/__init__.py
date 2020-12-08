from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
print('hello main')
app = Flask(__name__)


app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Vivekshukla@123@localhost/calc'

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "logger.login"

from apps.login.routes import logger
app.register_blueprint(logger)

from apps.calc.routes import calculate
app.register_blueprint(calculate)
