from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "mysecretKey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        employee = Data.query.get(request.form['id'])
        employee.name = request.form['name']
        employee.email = request.form['email']
        employee.phone = request.form['phone']
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    employee = Data.query.get(id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/')
def index():
    employees = Data.query.all()
    return render_template('index.html', employees=employees)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
