"""CRUD operations."""
from model import db, User, Location, Booking, Amenity, LocationAmenity, connect_to_db



def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)
    return user

def get_all_users():
    """Return a list of all users in the database."""

    return User.query.all()



#dunder name dunder main syntax from crup in movie ratings project
if __name__ == '__main__':
    from server import app
    connect_to_db(app)