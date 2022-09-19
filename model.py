""" Models for work travel co-living app. """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()



class User(db.Model): #one user has many bookings
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    bookings = db.relationship("Booking", back_populates="user")

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'



#took syntax from rating in the movie ratings project
class Booking(db.Model):
    """A booking."""

    __tablename__ = 'bookings'

    booking_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    location_id = db.Column(db.Integer, db.ForeignKey("locations.location_id"))
    arrival= db.Column(db.DateTime)
    departure = db.Column(db.DateTime)

    user = db.relationship("User", back_populates="bookings")
    location = db.relationship("Location", back_populates="bookings")

    def __repr__(self):
        return f'<Booking booking_id={self.booking_id} arrival={self.arrival} departure = {self.departure}>'



class Location(db.Model): #one location has many amenity per location
    """A location."""

    __tablename__ = 'locations'

    location_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    location_title = db.Column(db.String)
    price = db.Column(db.Integer)
    overview = db.Column(db.String)
    description = db.Column(db.String)
    # capacity = db.Column(db.Integer)
    img = db.Column(db.String)

    bookings = db.relationship("Booking", back_populates="location")

    #set up relationship to amenities and location_amenties middle table
    amenities = db.relationship("Amenity", secondary = "location_amenities", back_populates = "locations")

    def __repr__(self):
        return f'<Location location_id={self.location_id} location_title={self.location_title} price={self.price} amenities= {self.amenities}>'



class Amenity(db.Model): #one amenity is related to a location with many amenities
    """A amenity."""

    __tablename__ = 'amenities'

    amenity_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    amenity_title = db.Column(db.String)

    #set up relationship to locations and location_amenties middle table
    locations = db.relationship("Location", secondary = "location_amenities", back_populates = "amenities")

    def __repr__(self):
        return f'<Amenity amenity_id={self.amenity_id} amenity_title={self.amenity_title}>'



#took syntax from BookGenre in many to many demo
class LocationAmenity(db.Model): #middle table - do not need to save additional info here
    """An amenity of a specific location."""

    __tablename__ = "location_amenities"

    location_amenity_id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.location_id"), nullable=False)
    amenity_id = db.Column(db.Integer, db.ForeignKey("amenities.amenity_id"), nullable=False)

    def __repr__(self):
        return f"<LocationAmenity location_id={self.location_id} amenity_id={self.amenity_id}>"



#connect to db took syntax from many to many lecture demo
def connect_to_db(app):
    """Connect to database."""

    #stating which db to connect to
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///projectdb"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # this would output the raw SQL, currently off as it can be noisy
    # app.config["SQLALCHEMY_ECHO"] = True

    db.app = app
    db.init_app(app)



#dunder main statement
if __name__ == "__main__":
    import os

    #need to change text here
    os.system("dropdb projectdb --if-exists")
    os.system("createdb projectdb")

    connect_to_db(app)

    # Make our tables
    db.create_all()