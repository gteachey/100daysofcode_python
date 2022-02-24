import sqlite3
# from sqlite3 import dbapi2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books_collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"{self.title}, {self.author}, {self.rating}"


book1 = Book(title='Harry Potter', author='J.K. Rowling', rating='9.3')
book2 = Book(title='Discworld', author='Terry Pratchett', rating='10')

try:
    db.create_all()
except:
    print("Database already created. Continuing")

if not Book.query.filter_by(title="Harry Potter").first():
    db.session.add(book1)
    added_something = True
    db.session.commit()

db.session.delete(Book.query.filter_by(title="Harry Potter").first())
print(Book.query.all())

book = Book.query.filter_by(title="Harry Potter").first()
print(book)
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

# # cursor.execute("CREATE TABLE books ( \
# #     id INTEGER PRIMARY KEY AUTOINCREMENT, \
# #     title varchar(250) NOT NULL UNIQUE, \
# #     author varchar(250) NOT NULL, \
# #     rating FLOAT NOT NULL)"
# #     )

# cursor.execute("INSERT INTO books (title, author, rating) VALUES('Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
