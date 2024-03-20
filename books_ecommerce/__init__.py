from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY']='9d10dc09c925e33b6021ccf3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booksCatalog.db'
db = SQLAlchemy(app)
from books_ecommerce import routes
app.app_context().push()