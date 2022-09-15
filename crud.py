"""CRUD operations."""
from model import db, User, Location, Booking, Amenity, LocationAmenity, connect_to_db
#TODAY
  #add samply bookings to seed

  #in general, think about the info i'll need and how to get it, then start formulating crud
    #i want to add some bookings functions
    #i want to change my hompage so there is a link to login/create user on the navbar and that renders a login.html template
    #i want to add a login html template

#Qs
  #do i need to add my locations in a JSON file? NO
  #someone in scrum mentioned competing their crud file? will change as i go


#LATER
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
#should i add a get booking by email? Other ones i should add?
#should i create sample bookings to test?
def create_booking(availability, arrival, departure, user, location):
  """Create and return a new booking."""
  booking = Booking(availability = availability, arrival = arrival, departure = departure, user = user, location = location)
  #do i need to do this here?
  db.session.add(booking)
  db.session.commit()

  return booking

def get_booking_by_id(booking_id):
  """Return booking by id"""

  return Booking.query.get(booking_id)

#FIX ME
def get_booking_by_user_email(email):
  """Return the booking by the users id."""
  #is this right? how do i test this?
  return Booking.query.filter(User.email == email).first()

  #display booking related to a specific user






#dunder name dunder main syntax from crup in movie ratings project
if __name__ == '__main__':
    from server import app
    connect_to_db(app)

