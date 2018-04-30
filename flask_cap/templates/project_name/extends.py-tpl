from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

api = Api()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = "home.login"