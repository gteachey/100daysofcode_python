from flask_wtf import FlaskForm
from flask import Flask, render_template, request
from wtforms import SubmitField, PasswordField, EmailField
from flask_wtf.csrf import CSRFProtect
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = EmailField('Email address', [InputRequired(), Email()])
    password = PasswordField('Password', [
        InputRequired(),
        Length(min=8, max=20, message=(u'Maximum of 20 characters for the password'))
    ])
    submit = SubmitField('Log In')


app = Flask(__name__)
app.config['SECRET_KEY'] = "FlaskNeedsBetterDocs!"
csrf = CSRFProtect(app)
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = LoginForm()

    if request.method == 'POST' and login_form.validate_on_submit():
        return render_template('success.html')
    elif request.method == 'POST' and not login_form.validate_on_submit():
        print('------ {0}'.format(request.form))
        return render_template('denied.html')
    print('------ {0}'.format(request.form))

    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True, host="localhost")
