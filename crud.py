"""CRUD operations."""
from model import db, User, Location, Booking, Amenity, LocationAmenity, connect_to_db
from datetime import datetime
#MVP - Innsite
# Guests can see the amenities and locations where they can book - DONE
# When booking they will be asked to create login so they have confirmation of booking - done
# Home and about pages will have photos and information about why they should work and travel and where. -

#TODAY -

  # create profile page that shows the user's info and places they have booked.
    #new html template query the db for their bookings
  # make a sign out button -
    #ajax route that can log the user out and redirects to login page
    #make a helper function, they may need to be logged out bc of a timeout etc
  # finish MVP! create about page -
  # brainstorm reviews feature - association table


  # WORKING - make fetch reqest that hits route i am about to make  -  index.JS  -
  #in hande booking route, print statements that shows it was sucessful
    #make a route to handle booking request
      #if they are logged in they can sucessfully book
      #if not they need to log in - can still save that data in session temporarily so they dont have to retype
  #get data from form so that they can sucessfully book if they are logged in


#Qs for staff




#GENERAL Q's for myself
  #Login flow
    #wondering if it would be the simplest to make everyone log in before starting to book
  #Booking flow
    #any book now button would reroute to login
      #if they are already logged in then show booking form

    #option to book on each location page if logged in
      #form that requests arrival & departure and a book now button
      #flash message for successful booking and maybe reroute to their profile, could show their bookings
      #maybe create a your bookings

    #link to book on navbar that routes to a booking page
      #this shows all locations and has a map to the right with everything on the map

#LATER
  #i want to change my hompage so there is a link to login/create user on the navbar and that renders a login.html template
  #i want to add a login html template
  #when i'm ready to work with api:
    #outside of server.py, make a playground.py(maybe in .gitignore)

#AFTER MVP
  #use react in booking feature
  #add capacity feature
    #store capacity in location class
    #create crud function to
      #query bookings table for records with location id
        # show arrival and departure dates that overlap
        # select all from bookings where loc id = location 1 and arrival date is less that date a and/or departure date is greater than date b
  #make gallery class that is one to many with location,
    #each main photo will be the main phot and galleries will show on each locaton detail page
  #make SQL locations and amenitites dump file

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

def get_user_by_id(user_id):
    """Return user by looking up their id."""

    return User.query.get(user_id)


#LOCATION FUNCTIONS
def get_all_locations():
    """Return a list of all locations in the database."""

    return Location.query.all()

def create_location(location_title, price, overview, description, img, amenities):
  """Create a location instance."""

  location = Location(location_title = location_title, price = price, overview = overview, description = description, img = img, amenities = amenities)
  db.session.add(location)
  db.session.commit()

  return location

def get_location_by_id(location_id):
  """Get location by id."""

  return Location.query.get(location_id)

#store capacity in location
#query bookings table for records with location id and
  #arrival and departure dates that overlap
  # select all from bookings where loc id = location 1 and arrival date is less that date a and/or departure date is greater than date b


#BOOKING FUNCTIONS
#global_date_format = "%m-%d-%Y"
#"%Y-%m-%d"
#import datetime to server temporarily
#try making datetime objs in server based on what i get from user
#use those to create booking objs
#decide if i want it in the crud function or not.
def create_booking(arrival, departure, user, location):
  """Create and return a new booking."""
  booking = Booking(arrival = arrival, departure = departure, user = user, location = location)
  db.session.add(booking)
  db.session.commit()

  return booking

def get_booking_by_id(booking_id):
  """Return booking by id"""

  return Booking.query.get(booking_id)

def get_booking_by_user_id(user_id):
  """Return the booking by the users id."""

  return Booking.query.filter(User.user_id == user_id).first()


#AMENITIES FUNCTIONS

def create_amenity(amenity_title):
  """Create and return a new amenity."""
  amenity = Amenity(amenity_title = amenity_title)
  db.session.add(amenity)
  db.session.commit()

  return amenity

def get_all_amenities():
  """Return a list of all amenities."""

  return Amenity.query.all()

def get_amenity_by_id(amentiy_id):
  """Return and amenity by its id."""

  return Amenity.query.get(amentiy_id)












#dunder name dunder main syntax from crup in movie ratings project
if __name__ == '__main__':
    from server import app
    connect_to_db(app)

