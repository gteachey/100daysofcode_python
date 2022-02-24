from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField, ValidationError
from wtforms.validators import DataRequired, URL, InputRequired
import csv
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
csv_path = os.path.join(app.root_path, 'cafe-data.csv')

coffee = ''
coffee_icons = ['✘']
for cofee in list(range(5)):
    coffee += '☕️'
    coffee_icons.append(coffee)

wifi = ''
wifi_icons = ['✘']
for cofee in list(range(5)):
    wifi += '💪'
    wifi_icons.append(wifi)

power = ''
power_icons = ['✘']
for cofee in list(range(5)):
    power += '🔌'
    power_icons.append(power)

time_choice = ['%s:%s%s' % (h, m, ap) for ap in (' AM', ' PM') for h in ([12] + list(range(1, 12))) for m in
               ('00', '30')]


class CafeForm(FlaskForm):

    def validate_no_dupe(form, field):
        with open(csv_path, newline='', encoding="utf8") as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')
            for row in csv_data:
                if row[0] in field.data:
                    raise ValidationError("Cafe already exists in the database!")

    cafe = StringField('Cafe name', validators=[DataRequired(), validate_no_dupe])

    # location_url = StringField('Location Url', validators=[DataRequired(), URL(message='Must be a valid URL')])
    location_url = URLField(label='Location Url', validators=[DataRequired(), URL(message='Must be a valid URL')])
    open_time = SelectField('Open Time', choices=time_choice, validators=[DataRequired()])
    close_time = SelectField('Close Time', choices=time_choice, validators=[DataRequired()])
    coffee_rating = SelectField(u'☕️ Coffee Rating ☕️', choices=coffee_icons, validators=[DataRequired()])
    wifi_rating = SelectField(u'💪 Wifi Rating 💪', choices=wifi_icons, validators=[DataRequired()])
    power_outlet_rating = SelectField(u'🔌 Power Outlet Rating 🔌', choices=power_icons, validators=[DataRequired()])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------
# all Flask routes below
@app.route("/location")
def location():
    return render_template("index.html")


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")

    if form.validate_on_submit():
        with open(csv_path, mode='a', encoding="utf8") as csv_file:
            entry = "\n" + ",".join(elem for elem in \
                                    [item for item in form.data.values()][0:7]
                                    )
            csv_file.write(entry)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(csv_path, newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    # print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
