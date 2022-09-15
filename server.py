"""Server for work travel co-living app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)

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

@app.route("/login", methods = ['POST'])
def login():
    """Show login"""
    email = request.form.get('email')
    password = request.form.get('password')
    potential_user = crud.get_user_by_email(email)

    if potential_user.password == password:
        session['user_id'] = potential_user.user_id
        flash('Logged in!')
    else:
        flash('Not logged in!')
    return redirect("/")






#dunder main syntax from movie ratings server.py file
if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)