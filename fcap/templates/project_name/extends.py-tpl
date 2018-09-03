from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_redis import FlaskRedis
from fet.tools.cryptor import Cryptor

api = Api()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
mail = Mail()
redis_store = FlaskRedis()
cryptor = Cryptor()