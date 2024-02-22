#This is a project for build one bookstore using microservices architecture

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/catalog')
def catalog():
    
    conn = sqlite3.connect('db/catalog.db') #connect to database
    cursor = conn.cursor() #create a cursor object to interact with the database
    cursor.execute('SELECT * FROM books') #execute a SQL query to retrieve all books from the database
    books = cursor.fetchall()  #fetch all rows from the cursor and store them in the books variable. Book is a list of tuples. Each tuple represents a book.
      
    return render_template('catalog.html', books=books)

@app.route('/cart')
def cart():
    return render_template('cart.html')
    
@app.route('/order')
def order():
    return render_template('order.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)