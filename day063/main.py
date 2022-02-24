from flask import Flask, render_template, request, redirect, url_for
import sqlite3
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
        return f"{self.title}, {self.author}, {self.rating}\n"
        # return {
        #     'title': self.title,
        #     'author': self.author, 
        #     'rating': self.rating
        # } 


try:
    db.create_all()
except:
    print("Database already created. Continuing")

# all_books = [
#      {
#         "title": "Harry Potter",
#         "author": "J. K. Rowling",
#         "rating": 9,
#     }
# ]
all_books = []


@app.route('/delete/<int:id>')
def delete(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id):
    if request.method == 'POST':
        book = Book.query.get(id)
        book.rating = request.form['rating']
        print(request.form['rating'])
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html")


@app.route('/')
def home():
    books = Book.query.all()
    # for book in books:
    # print(book.__dict__)
    return render_template("index.html", books=books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # print(request.form['title'])
        book_title = request.form['title']

        if not Book.query.filter_by(title=book_title).first():
            book = Book(title=book_title, author=request.form['author'], rating=request.form['rating'])

            db.session.add(book)
            db.session.commit()
        # # book_dict = {}
        # for (k,v) in request.form.items():
        #     book_dict[k] = v
        # all_books.append(book_dict)
        # # print(all_books)
        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
