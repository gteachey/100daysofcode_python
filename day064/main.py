from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from sqlalchemy import create_engine, desc, exc
import os
from sqlalchemy.sql import exists
from sqlalchemy.orm.query import Query
import requests

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(THIS_FOLDER, 'movie-list.db')
db_path = f"sqlite:///{db_file}"
print(db_path)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'
# engine = create_engine()

Bootstrap(app)
db = SQLAlchemy(app)

time_choice = [n / 2 for n in list(range(20, -1, -1))]


class EditForm(FlaskForm):
    rating = SelectField(label="Edit Rating", choices=time_choice, validators=[DataRequired()])
    review = StringField(label="Edit Review", validators=[DataRequired()],
                         render_kw={'width': '400px', 'height': '200%'})
    submit = SubmitField()


class AddForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()],
                        render_kw={'width': '400px', 'height': '200%'})
    submit = SubmitField(render_kw={'width': '400px', 'height': '200%'})


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=True)
    description = db.Column(db.String(250), unique=False, nullable=True)
    rating = db.Column(db.Float, unique=False, nullable=True)
    ranking = db.Column(db.Integer, unique=False, nullable=True)
    review = db.Column(db.String(250), unique=False, nullable=True)
    img_url = db.Column(db.String(250), unique=False, nullable=True)


try:
    db.create_all()
except:
    pass


@app.route("/delete")
def delete():
    movie_id = request.args['id']
    print(movie_id)
    delete_movie = Movie.query.get(movie_id)
    db.session.delete(delete_movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        movie_name = request.form['title']
        page_num = 1
        TMDB_SEARCH_MOVIE_URL = f'https://api.themoviedb.org/3/search/movie?api_key=77c0cc86efb75e423f479ee500e542a6&language=en-US&query={movie_name}&page={page_num}'
        response_json = requests.get(TMDB_SEARCH_MOVIE_URL).json()
        total_pages = response_json["total_pages"]
        results = response_json['results']

        while page_num <= total_pages:
            page_num += 1
            TMDB_SEARCH_MOVIE_URL = f'https://api.themoviedb.org/3/search/movie?api_key=77c0cc86efb75e423f479ee500e542a6&language=en-US&query={movie_name}&page={page_num}'
            response_json = requests.get(TMDB_SEARCH_MOVIE_URL).json()
            results += response_json['results']

        # session['movies_list'] = results
        # print(f"Add Method:\n\n\n\n{movies_list}\n\n\n")
        return render_template('select.html', movies_list=results)

    add_form = AddForm()
    return render_template("add.html", form=add_form)


@app.route("/select/", methods=['POST', 'GET'])
def select():
    # if request.method == 'POST':
    movie_id = request.args['id']
    TMDB_GET_MOVIE_URL = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=77c0cc86efb75e423f479ee500e542a6&language=en-US'
    response_json = requests.get(TMDB_GET_MOVIE_URL).json()
    print(response_json)
    new_movie = Movie(
        title=response_json['original_title'],
        year=response_json['release_date'].split('-')[0],
        description=response_json['overview'],
        img_url=f"https://image.tmdb.org/t/p/w500{response_json['poster_path']}"
    )
    print(f"https://image.tmdb.org/t/p/w500{response_json['poster_path']}")
    print(f"Adding Movie: {new_movie.__dict__['title']}")
    db.session.add(new_movie)
    print("Committing to movie")
    db.session.commit()

    movie = Movie.query.filter(Movie.title == response_json['original_title']).first()
    print(f"Movie ID: {movie.id}")
    return redirect(url_for('edit', id=movie.id))


@app.route("/edit", methods=['POST', 'GET'])
def edit():
    if request.method == 'POST':
        movie_id = request.args['id']
        edit_movie = Movie.query.get(movie_id)
        edit_movie.review = request.form['review']
        edit_movie.rating = request.form['rating']
        db.session.commit()

        return redirect(url_for('home'))

    edit_form = EditForm()
    return render_template("edit.html", form=edit_form)


@app.route("/")
def home():
    q = Query(Movie)
    # movies = db.session.query(Movie).order_by(desc(Movie.rating)).all()
    movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()

    return render_template("index.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)
