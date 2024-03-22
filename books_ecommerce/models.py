from books_ecommerce import db, login_manager
from flask_login import UserMixin

class Books(db.Model):
    isbn = db.Column(db.String(10), primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    amount = db.Column(db.Integer)
    price = db.Column(db.Float)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))   

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    budget = db.Column(db.Float, default=100)
    
    def __repr__(self):
        return f'User {self.username}'
        
    
    def check_password_correction(self, attempted_password):
        return self.password_hash == attempted_password