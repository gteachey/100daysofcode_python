from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["POST"])
def login_page():
    return render_template('login.html', username=request.form['name'], password=request.form['password'])


if __name__ == '__main__':
    app.run(debug=True)
