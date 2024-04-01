#This is a project for build a bookstore

from books_ecommerce import app


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)