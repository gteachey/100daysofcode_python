from flask import Flask, render_template, request
from datetime import date, datetime
import requests
from smtplib import SMTP
from email.message import EmailMessage

app = Flask(__name__)
response = requests.get('https://api.npoint.io/bebc3e16f13e73d3f31c')
json_out = response.json()
fromEmail = "gt100daysofcode@gmail.com"
toEmail = 'gteachey@outlook.com'


@app.route('/post/<id>')
def post(id):
    year = datetime.now().year
    post = json_out[int(id) - 1]
    return render_template("post.html", title="Blog Post", blog_post=post, date=year)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    error = None
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        tele = request.form['tel']
        message = f"Name: {username}\nEmail: {email}\nTelephone: {tele}\nMessage: {request.form['message']}"
        smtp_provider = "smtp.gmail.com"

        with SMTP(host=smtp_provider) as smtp_send:
            smtp_send.starttls()
            smtp_send.login(user=fromEmail, password="T..h7RP#tz;G[t27bC,y")
            email_message = EmailMessage()
            email_message['Subject'] = "Contact Me"
            email_message['From'] = fromEmail
            email_message['To'] = toEmail
            email_message.set_content(message)

            smtp_send.send_message(email_message)
        return render_template('contact.html',
                               page_text="Successfully Sent Your Message"
                               )
    else:
        year = datetime.now().year
        return render_template("contact.html", title="Contact Me", page_text="Contact Me", date=year)


@app.route('/about')
def about():
    year = datetime.now().year
    return render_template("about.html", title="About", date=year)


@app.route('/')
def start_page():
    year = datetime.now().year
    return render_template("index.html", title="Welcome to the Blog", date=year, posts=json_out)


if __name__ == "__main__":
    app.run(debug=True)
