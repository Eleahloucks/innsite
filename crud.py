"""CRUD operations."""
from model import db, User, Location, Booking, Amenity, LocationAmenity, Review, connect_to_db
from datetime import datetime
#MVP - Innsite
# Guests can see the amenities and locations where they can book - DONE
# When booking they will be asked to create login so they have confirmation of booking - Done
# Home and about pages will have photos and information about why they should work and travel and where. - DONE

#TODAY -
  # populate content on home
  # populate content on profile
  # populate content on about
  # put reviews on locations


#Qs for staff

#GENERAL Q's for myself

#AFTER MVP
  #1 create review feature in react - might need to make a form in react
  #make gallery class that is one to many with location,
    #each main photo will be the main phot and galleries will show on each locaton detail page

  #add capacity feature
    #store capacity in location class
    #create crud function to
      #query bookings table for records with location id
        # show arrival and departure dates that overlap
        # select all from bookings where loc id = location 1 and arrival date is less that date a and/or departure date is greater than date b
  #make SQL locations and amenitites dump file

#USER FUNCTIONS
def create_user(email, password, fname, lname):
    """Create and return a new user."""

    user = User(email=email, password=password, fname = fname, lname = lname)
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

#REVIEW FUNCTIONS

def create_review(title, body, score, user_id, location_id):
  """Create a review."""

  review = Review(title = title, body = body, score = score, user_id = user_id, location_id = location_id)
  db.session.add(review)
  db.session.commit()

  return review

def get_review_by_location_id(location_id):
    """Get review by location id."""

    return Review.query.filter(Review.location_id == location_id).first()

def get_review_by_user_id(user_id):
    """Get review by user id."""

    return Review.query.filter(Review.user_id == user_id).first()

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

#i will call the function for arrival and departure
def get_datetime_format(date_input):
  """get global format arrival and departure"""

  input_date_format = "%Y-%m-%d"
  global_data_format = "%m-%d-%Y"
  return datetime.strptime(date_input, input_date_format).strftime(global_data_format)



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

  return Booking.query.filter(Booking.user_id == user_id).first()


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

