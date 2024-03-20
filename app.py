#This is a project for build one bookstore using microservices architecture

from books_ecommerce import app


if __name__ == '__main__':
    app.run(debug=True, port=5001)