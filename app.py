#This is a project for build one bookstore using microservices architecture

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
import sqlite3
from forms import RegisterForm, PurchaseBookForm
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY']='9d10dc09c925e33b6021ccf3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booksCatalog.db'
db = SQLAlchemy(app)

app.app_context().push()
    
class Books(db.Model):
    isbn = db.Column(db.String(10), primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    amount = db.Column(db.Integer)
    price = db.Column(db.Float)



@app.route('/')
def index():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/catalog', methods=['GET', 'POST'])
def catalog():
    
    purchaseForm = PurchaseBookForm() #create a PurchaseBookForm object
    print("Entrando a ruta")
    if request.method == 'POST': #if the request method is POST, the form was submitted and the user wants to purchase a book
        print("Entrando a post")
        purchaseBook = request.form.get('purchaseBook') #get the value of the purchaseBook field from the form data
        print(purchaseBook)
        a_book = Books.query.filter_by(title=purchaseBook).first() #query the Books table for the book with the specified title
        if a_book:
            a_book.amount -= 1 #decrement the amount of the book by 1
            db.session.commit() #commit the changes to the database
            flash(f'Book {a_book.title} purchased successfully!', category='success') #display a success message
        elif a_book.amount == 0:
            flash(f'Book {a_book.title} is out of stock!', category='error') #display an error message if the book is out of stock
        return redirect(url_for('catalog')) #redirect the user to the catalog page after the purchase is complete
    
    
    if request.method == 'GET': #if the request method is GET, the form was not submitted and the user wants to view the catalog
        
        #conn = sqlite3.connect('db/catalog.db') #connect to database
        #cursor = conn.cursor() #create a cursor object to interact with the database
        #cursor.execute('SELECT * FROM books') #execute a SQL query to retrieve all books from the database
        #books = cursor.fetchall()  #fetch all rows from the cursor and store them in the books variable. Book is a list of tuples. Each tuple represents a book.
        books = Books.query.all() #query the Books table and retrieve all books
        
        return render_template('catalog.html', purchaseForm=purchaseForm, books=books) #render the catalog template and pass the books variable to it



@app.route('/register')
def login():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('User created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/cart')
def cart():
    return render_template('cart.html')
    
@app.route('/order')
def order():
    return render_template('order.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)