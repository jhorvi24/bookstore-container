from books_ecommerce import db

class Books(db.Model):
    isbn = db.Column(db.String(10), primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    amount = db.Column(db.Integer)
    price = db.Column(db.Float)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    budget = db.Column(db.Float, default=100)