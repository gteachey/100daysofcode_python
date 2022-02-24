import re
from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests
from werkzeug.wrappers import response

app = Flask(__name__)
'''
https://api.agify.io?name=michael
https://api.genderize.io?name=peter
https://api.nationalize.io?name=michael
'''


@app.route('/guess/<name>')
def guess_name(name):
    response_agify = requests.get(f"https://api.agify.io?name={name}")
    agify_out = response_agify.json()
    response_genderize = requests.get(f"https://api.genderize.io?name={name}")
    genderize_out = response_genderize.json()
    response_nationalize = requests.get(f"https://api.nationalize.io?name={name}")
    nationalize_out = response_nationalize.json()['country']
    year = datetime.now().year

    return render_template("guess.html",
                           guess_name=genderize_out['name'].title(),
                           age=agify_out['age'],
                           gender=genderize_out['gender'],
                           nationality=nationalize_out, year=year, my_name="Glenn Teachey Inc"
                           )


@app.route('/blog')
def get_blog():
    blog_url = 'https://api.npoint.io/a3eeda432421be4c5518'
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


@app.route('/')
def home():
    num = randint(1, 6)
    year = datetime.now().year
    return render_template("index.html", num=num, year=year, my_name="Glenn Teachey Inc")


if __name__ == "__main__":
    app.run(debug=True)
