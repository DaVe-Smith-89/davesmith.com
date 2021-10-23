from flask import Flask
from flask_login import  LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
admin = Admin(app, url='/3xf8z81HUddaTkyqZBXJm9PG')

app.config['SECRET_KEY'] = '49d373ffd06031f5bb8b3d54823ab22b1d630e89d6dab19fd320c3640408ed43'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://uk7ffmkxooxbon3o:N9JWxqwP8rZiddZRkNC6@bodlbp3olvcjoewvmkih-mysql.services.clever-cloud.com:3306/bodlbp3olvcjoewvmkih'

login_manager.login_view = 'login'

from dave.routes import app
