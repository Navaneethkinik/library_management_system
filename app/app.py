# app/app.py
from flask import render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Author, db

from app import app

# Connect to the SQLite database
engine = create_engine('sqlite:///library.db', echo=True)
db.init_app(app)
with app.app_context():
    db.create_all()

Session = sessionmaker(bind=engine)
session = Session()

# Route to display authors and allow updates
@app.route('/')
def index():
    authors = session.query(Author).all()
    return render_template('index.html', authors=authors)

# Route to update author information
@app.route('/update_author/<int:author_id>', methods=['GET', 'POST'])
def update_author(author_id):
    author = session.query(Author).get(author_id)
    
    if request.method == 'POST':
        author.name = request.form['name']
        author.bio = request.form['bio']
        author.nationality = request.form['nationality']
        session.commit()
        return redirect(url_for('index'))

    return render_template('update_author.html', author=author)

# Route to add a new author
@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        new_author = Author(
            name=request.form['name'],
            bio=request.form['bio'],
            nationality=request.form['nationality']
        )
        session.add(new_author)
        session.commit()
        return redirect(url_for('index'))

    return render_template('add_author.html')
