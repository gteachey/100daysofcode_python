from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hobbies')
def hobbies_page():
    return render_template("hobbies.html")


@app.route('/connect_with_me')
def connect_with_me_page():
    return render_template("connect_with_me.html")


@app.route('/')
def start_page():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
