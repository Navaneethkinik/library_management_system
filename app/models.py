# app/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    nationality = db.Column(db.String(50))
    books = db.relationship('Book', back_populates='author')

class Book(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    genre = db.Column(db.String(100))
    quantity_available = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.author_id'))
    transactions = db.relationship('Transaction', back_populates='book')
    author = db.relationship('Author', back_populates='books')

class Transaction(db.Model):
    __tablename__ = 'transactions'
    transaction_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    transaction_type = db.Column(db.String(10))
    transaction_date = db.Column(db.Date)
    due_date = db.Column(db.Date)
    return_date = db.Column(db.Date)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'))
    book = db.relationship('Book', back_populates='transactions')
