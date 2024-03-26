from books_ecommerce import app, db
from flask import render_template, request, redirect, url_for, flash
from books_ecommerce.forms import PurchaseBookForm, RegisterForm, LoginForm
from books_ecommerce.models import Books, Users
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/catalog', methods=['GET', 'POST'])
def catalog():
    
    purchaseForm = PurchaseBookForm() #create a PurchaseBookForm object
    print("Entrando a ruta")
    if request.method == 'POST': #if the request method is POST, the form was submitted and the user wants to purchase a book
        print("Entrando a post")
        if current_user.is_authenticated: #check if the user is authenticated            
            purchaseBook = request.form.get('purchaseBook') #get the value of the purchaseBook field from the form data            
            a_book = Books.query.filter_by(title=purchaseBook).first() #query the Books table for the book with the specified title
            
            if a_book and a_book.amount>0:
                a_book.amount -= 1 #decrement the amount of the book by 1
                db.session.commit() #commit the changes to the database
                flash(f'Book {a_book.title} purchased successfully!', category='success') #display a success message
            elif a_book.amount == 0:
                flash(f'Book {a_book.title} is out of stock!', category='error') #display an error message if the book is out of stock
            return redirect(url_for('catalog')) #redirect the user to the catalog page after the purchase is complete
        else:
            flash('You must be logged in to purchase a book!', category='error') #display an error message if the user is not authenticated
            return redirect(url_for('login')) #redirect the user to the login page after displaying the error message
    
    if request.method == 'GET': #if the request method is GET, the form was not submitted and the user wants to view the catalog
                
        books = Books.query.all() #query the Books table and retrieve all books
        
        return render_template('catalog.html', purchaseForm=purchaseForm, books=books) #render the catalog template and pass the books variable to it



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        created_user = Users(username=form.username.data, 
                             password_hash=form.password1.data, 
                             email=form.email.data)
        db.session.add(created_user)
        db.session.commit()
        login_user(created_user)
        
        flash('User created successfully! You are now logged in as {create_user.username}', category='success')
        return redirect(url_for('catalog'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = Users.query.filter_by(username=form.username.data).first()
        print(attempted_user)
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('catalog'))
        else:
            flash('Username and password are not match! Please try again', category='danger')
            return redirect(url_for('login'))

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out!', category='info')
    return redirect(url_for('home'))
    

