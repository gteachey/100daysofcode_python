import requests
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime

## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    posts = db.session.query(BlogPost).all()
    for blog_post in posts:

        if blog_post.id == index:
            print(blog_post.id)
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/edit_post/<int:post_id>", methods=['POST', 'GET'])
def edit_post(post_id):
    post = db.session.query(BlogPost).get(post_id)
    create_post_form = CreatePostForm(obj=post)
    if request.method == "POST":
        edit_blog_post = db.session.query(BlogPost).get(post_id)
        # for key, value in request.form.items():
        #     setattr(edit_blog_post, key, value)
        create_post_form.populate_obj(post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", post=post, form=create_post_form, title="Edit Post")


@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    post = db.session.query(BlogPost).get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/new_post", methods=["POST", "GET"])
def add_new_post():
    if request.method == "POST":
        x = datetime.datetime.now()
        add_blog_post = BlogPost()
        print(request.form)
        for column in add_blog_post.__table__.columns:
            if column.name in request.form:
                setattr(add_blog_post, column.name, request.form[column.name])
            elif column.name == "date":
                setattr(add_blog_post, column.name, x.strftime("%B %d, %Y"))
        try:
            db.session.add(add_blog_post)
            db.session.commit()
            return redirect(url_for('get_all_posts'))
        except:
            print("something went wrong")
        return "Something went wrong"
    else:
        create_post_form = CreatePostForm()
        return render_template("make-post.html", title="New Post", form=create_post_form)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
