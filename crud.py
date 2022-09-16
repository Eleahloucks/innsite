"""CRUD operations."""
from model import db, User, Location, Booking, Amenity, LocationAmenity, connect_to_db
#MVP
# Guests can see the features and locations where they can book
# When booking they will be asked to create login so they have confirmation of booking
# Home and about page will have photos and information about why they should work and travel and where.

#TODAY
  #add photo by adding to location class
  #add amenities to each page -
    #create crud functions
    #seed the data

  # think about booking flow
  # create each locations page by have server route that can display each location see movies for example

#Qs for staff
  #availability:
    #should availibility be under my location class instead of booking?
    #How should i format all available dates?
    #I'll need to blackout booked dates also.
  #locations & amenities
    #would it make sense to put these into their own json files to populate my 10 locations?
    #how is my google maps going to come into play with locations?



#GENERAL Q's for myself
  # what do i want my user to be able to accompish? What is in my MVP? What is most important?


#LATER
  #i want to change my hompage so there is a link to login/create user on the navbar and that renders a login.html template
  #i want to add a login html template
  #when i'm ready to work with api:
    #outside of server.py, make a playground.py(maybe in .gitignore)

#USER FUNCTIONS
def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return user

def get_all_users():
    """Return a list of all users in the database."""

    return User.query.all()

def get_user_by_email(email):
    """Return user by looking up their email."""

    return User.query.filter(User.email == email).first()


#LOCATION FUNCTIONS
def get_all_locations():
    """Return a list of all locations in the database."""

    return Location.query.all()

def create_location(location_title, price, overview):
  """Create a location instance."""

  location = Location(location_title = location_title, price = price, overview = overview)
  db.session.add(location)
  db.session.commit()

  return location

def get_location_by_id(location_id):
  """Get location by id."""

  return Location.query.get(location_id)


#BOOKING FUNCTIONS
def create_booking(availability, arrival, departure, user, location):
  """Create and return a new booking."""
  booking = Booking(availability = availability, arrival = arrival, departure = departure, user = user, location = location)
  db.session.add(booking)
  db.session.commit()

  return booking

def get_booking_by_id(booking_id):
  """Return booking by id"""

  return Booking.query.get(booking_id)

def get_booking_by_user_id(user_id):
  """Return the booking by the users id."""

  return Booking.query.filter(User.user_id == user_id).first()







#dunder name dunder main syntax from crup in movie ratings project
if __name__ == '__main__':
    from server import app
    connect_to_db(app)

