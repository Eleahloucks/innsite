"""CRUD operations."""
from model import db, User, Location, Booking, Amenity, LocationAmenity, connect_to_db

#create crud function to add instances of location that ppl might choose to go to
#function to retrive all locations
#template to display all locations
#vaguely group things together on homepage - minimal css
#wait to connect api until all local stuff is sorted

def create_user(email, password):
    """Create and return a new user."""
    user = User(email=email, password=password)

    return user

def get_all_users():
    """Return a list of all users in the database."""

    return User.query.all()

def get_all_locations():
    """Return a list of all locations in the database."""

    return Location.query.all()



#dunder name dunder main syntax from crup in movie ratings project
if __name__ == '__main__':
    from server import app
    connect_to_db(app)