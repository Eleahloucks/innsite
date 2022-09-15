"""CRUD operations."""
from model import db, User, Location, Booking, Amenity, LocationAmenity, connect_to_db
#TODAY
#add search booking by id funtion DONE
#display locations so user can save location or make a booking DONE
#add sample bookings to seed WORKING

# what happens when they click on location ...where should it go?
# what do i want my user to be able to accompish? What is in my MVP? What is most important?
# create each locations page


#Qs


#LATER
#i want to change my hompage so there is a link to login/create user on the navbar and that renders a login.html template
#i want to add a login html template
#vaguely group things together on homepage - minimal css
#wait to connect api until all local stuff is sorted
#work with api outside of server.py, make a playground.py(maybe in .gitignore)

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

