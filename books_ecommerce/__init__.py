from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY']='9d10dc09c925e33b6021ccf3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booksCatalog.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from books_ecommerce import routes
app.app_context().push()