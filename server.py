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
def show_all_movies():
    """Show all locations"""
    all_locations = crud.get_all_movies()
    return render_template("all_locations.html", locations = all_locations)



#dunder main syntax from movie ratings server.py file
if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)