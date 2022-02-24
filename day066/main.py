import sqlalchemy
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        # dictionary = {}
        # # Loop through each column in the data record
        # for column in self.__table__.columns:
        #     # Create a new dictionary entry;
        #     # where the key is the name of the column
        #     # and the value is the value of the column
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/all")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    cafe_dict = {"cafes": [cafe.to_dict() for cafe in cafes]}
    return cafe_dict


## HTTP GET - Read Record
@app.route("/random")
def get_random():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/search")
def search_cafes():
    query_location = request.args.get("loc")
    cafes = db.session.query(Cafe).filter_by(location=query_location).all()
    [print(column.name) for column in Cafe.__table__.columns]

    if cafes:
        cafe_dict = {"cafes": [cafe.to_dict() for cafe in cafes]}
        return jsonify(cafe_dict)
    else:
        return jsonify(error={"Not Found": "Sorry! No cafes found for that location."})


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    if request.method == "POST":
        post_args = request.args
        print(post_args)
        new_cafe = Cafe()

        for column in new_cafe.__table__.columns:
            if column.name in post_args:
                if type(getattr(Cafe, column.name).type) == sqlalchemy.types.Boolean:
                    # if the field is boolean, evaluate the data to True or False, default is False if nothing entered
                    # This allows for 'true', 'True', '0', and '1' strings to work as expected for boolean
                    setattr(new_cafe, column.name, eval(post_args[column.name].title()) or False)
                else:
                    # Add the data to the new database entry
                    setattr(new_cafe, column.name, post_args[column.name])

        db.session.add(new_cafe)
        db.session.commit()
        return jsonify({"response": {"success": "Successfully added the new cafe"}})


## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_cafe_price(cafe_id):
    try:
        if request.args['new_price'] == "":
            return jsonify(error="New price incorrectly sent."), 400
        else:
            mod_cafe = db.session.query(Cafe).get(cafe_id)
            new_price = request.args['new_price']
            setattr(mod_cafe, 'coffee_price', new_price)
            # print(getattr(mod_cafe, 'coffee_price'))
            # db.session.add(mod_cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the price."}), 200

    except AttributeError:
        return jsonify(error="No cafe with that id found in the database."), 404


## HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args['api-key']
    if api_key == "TopSecretAPIKey":
        del_cafe = db.session.query(Cafe).get(cafe_id)
        if del_cafe is None:
            return jsonify(error="No cafe with that id found in the database."), 404
        else:
            db.session.delete(del_cafe)
            db.session.commit()
            return jsonify(response={"success": f"Successfully deleted the {del_cafe.name} cafe."}), 200
    else:
        return jsonify(error="Invalid API Key provided. Please check your key"), 401


if __name__ == '__main__':
    app.run(debug=True)
