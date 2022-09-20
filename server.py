"""Server for work travel co-living app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from datetime import datetime
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev" # fixme
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """Show homepage"""

    return render_template("homepage.html")

@app.route("/locations")
def show_all_locations():
    """Show all locations"""
    all_locations = crud.get_all_locations()
    return render_template("all_locations.html", locations = all_locations)

@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")

@app.route("/login", methods = ['POST'])
def process_login():
    """Show login"""
    input_email = request.form.get('email')
    input_password = request.form.get('password')
    #will retrieve a user obj or none.
    potential_user = crud.get_user_by_email(input_email)
    #if user is none
    if not potential_user:
        flash('user not found!')
    #if user is found check pw
    elif potential_user.password == input_password:
        session['user_id'] = potential_user.user_id
        session['email'] = potential_user.email
        flash('Logged in!')
        return redirect("/locations")
    #user was found but pw didnt match
    else:
        flash('Not logged in!')
    return render_template("login.html")


@app.route("/locations/<location_id>")
def location_details(location_id):
    """Show details of a location."""
    location = crud.get_location_by_id(location_id)
    return render_template("location_details.html", location = location)


@app.route("/locations/<location_id>", methods = ['POST'])
def book_location(location_id):
    """book a location."""

    arrival = request.json.get("arrival")
    departure = request.json.get("departure")
    booked_location = request.json.get("location")

    #change input string to global format
    input_date_format = "%Y-%m-%d"
    global_data_format = "%m-%d-%Y"

    arrival_datetime = datetime.strptime(arrival, input_date_format).strftime(global_data_format)
    departure_datetime = datetime.strptime(departure, input_date_format).strftime(global_data_format)
    print(arrival_datetime)
    print(departure_datetime)

    return jsonify({
        "sucess": True,
        "status": f"Your booking from {arrival_datetime} to {departure_datetime} in {booked_location} is confirmed!"
    })

@app.route("/book-now", methods=["GET"])
def show_book_now():
    """Show booking page."""
    all_locations = crud.get_all_locations()

    return render_template("book_now.html", locations = all_locations)







#dunder main syntax from movie ratings server.py file
if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)