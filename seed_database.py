"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server


from crud import *
connect_to_db(server.app)
db.drop_all()
db.create_all()


## run this when i make changes to model or crud to make sure they are working


#SAMPLE AMENITIES  - probably going to have 30 ish total


amenity_1 = create_amenity('Free WIFI')
amenity_2 = create_amenity('Dedicated Workspace')
amenity_3 = create_amenity('Well-equipped Kitchen')
amenity_4 = create_amenity('Printer')
amenity_5 = create_amenity('Room Door Locks')
amenity_6 = create_amenity('Bedroom Linens')
amenity_7 = create_amenity('Soaps and Shampoo')
amenity_8 = create_amenity('Desks in all Rooms')
amenity_9 = create_amenity('Hairdryer')
amenity_10 = create_amenity('Outdoor Space')
amenity_11 = create_amenity('Parking Avaliable')
amenity_12 = create_amenity('Self Check-in')
amenity_13 = create_amenity('Convertable Workspace and Work Nook')
amenity_14 = create_amenity('Smart TV')
amenity_15 = create_amenity('Secure Building Entry')
amenity_16 = create_amenity('On-street parking')
amenity_17 = create_amenity('Laundry on-site')
amenity_18 = create_amenity('Local gym membership')
amenity_19 = create_amenity('A/C')
amenity_20 = create_amenity('Walking Distance to sites')
amenity_21 = create_amenity('Public Transportation closeby')


amenity_check_1 = get_amenity_by_id(1)
amenity_check_2 = get_amenity_by_id(2)
amenity_check_3 = get_amenity_by_id(3)
amenity_check_4 = get_amenity_by_id(4)
amenity_check_5 = get_amenity_by_id(5)


# print(amenity_check_1)
# print(amenity_check_2)
# print(amenity_check_3)
# print(amenity_check_4)
# print(amenity_check_5)

#SAMPLE LOCATIONS


location_1 = create_location(
  'Boulder, CO',
  1869,
  "Classic Craftsman in Colorado.",
  "Made for a cozy mountain getaway, Boulder University Hill maintains its original wooden banister, fireplaces, and wooden floorboards. It has a wine cellar downstairs, and its large back deck is perfect for relaxing with your housemates. The neighborhood is known for its hilly roads, Victorian houses, and its close proximity to UC Boulder. It's a very bikeable area, and just minutes from the Boulder Farmer's Market or Pearl Street, where you'll find great restaurants, cafes, and shopping. Outsite Boulder - University Hill is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
  "/static/img/boulder.jpeg",
  [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_10, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20]
  )
location_2 = create_location(
  "Lisbon, Portugal",
  1365,
  "Comfortable coliving inside a historic building.",
  "Outsite Lisbon is a traditional Lisbon building,- you’ll recognize it from it’s blue and white azulejos on the outside from Rua Sao Paulo. Pick a sea view on the south facing side of the building, or select a room with a balcony for the ultimate people-watching perch. There are 25 rooms in total, with a shared kitchen facility between every 5 rooms, and a large coworking space on the ground floor. Outsite Lisbon - Cais do Sodre is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
  "/static/img/lisbon.jpeg",
  [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
  )
location_3 = create_location(
  'San Francisco, CA',
  2968,
  "A modern San Francisco home on California Street.",
  "Make yourself at home in this four-floor house in Pacific Heights, San Francisco. There are 9 private bedrooms total, 6 of which have a shared bathroom, and 3 of which have their own en-suite. There's a backyard for summer barbecues, a modern, fully equipped kitchen and workspace in-house. Outsite San Francisco - Pacific Heights is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
  "/static/img/sanfrancisco.jpeg",
  [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
  )
location_4 = create_location(
  'Manhattan, NY',
  3003,
  "Beautiful 5-story brownstone made for city living.",
  "This is the spot for posting-up in New York - this traditional brownstone has a lounge room, fully equipped kitchen and large windows to let as much light in as possible. Work from the space, and head to one of Manhattan's coffee shops for a day's work. Outsite New York - Manhattan Midtown is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
  "/static/img/manhattan.jpeg",
  [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
  )
location_5 = create_location(
  'Puerto Rico, San Juan',
  1491,
  "Airy, Spanish Style Home on the Beach.",
  "Outsite Puerto Rico is your invite into island life. This ocean view home has plenty of outdoor space for making the most of San Juan's temperate climate, including a rooftop terrace. Hang out in the newly renovated kitchen when dining with friends, or explore the bay from your front doorstep. This space has beach access, so you can wake up and hit the water all before your morning calls. Outsite Puerto Rico - Ocean Park is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
  "/static/img/puerto_rico.jpg",
  [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
  )
location_6 = create_location(
  'Morocco, North Africa',
  1052,
  "Restored Berber riad in the centre of Marrakesh.",
  "A traditional riad complete with pool, hammam and rooftop terrace. Make use of the shared kitchen, indoor patios, outdoor terraces and the workspace, all furnished with ornate Moroccan textiles and crafts.  Outsite Marrakesh is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
  "/static/img/morocco.jpg",
  [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
  )
location_7 = create_location(
  'Bidart, France',
  1535,
  "A traditional French country house, overlooking the Pyrenees.",
  "This is a dreamy French country house dating back to 1870, finished with traditional tiles and stone interiors. There are 7 bedrooms, a kitchen, lounge and indoor pool, spread out between 2 floors. Private rooms are available with private and shared bathrooms. There's a heated pool on the ground floor, a tennis court, and an outdoor area for lounging in the sun - or setting up an enviable Zoom background. You'll have access to the tennis rackets, balls and e-bikes on-site for exploring during your stay. Outsite Bidart is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
  "/static/img/france.jpeg",
  [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
  )
location_8 = create_location(
  'Canggu, Bali',
  1407,
  "Open, spacious villa with jungle views.",
  "This is a true Balinese paradise, surrounded by palm trees and rice terraces. The garden and pool area sit at the center of the complex - the perfect outdoor place to workout, relax, or throw a get-together. When the heat gets too much, there's an air conditioned workspace, and shared kitchen for family dinners. There's an additional outdoor shelter for organising sound baths, meditations and massages too. Outsite Bali - Pererenan is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
  "/static/img/bali.jpg",
  [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
  )
location_9 = create_location(
  'Fuerteventura, Canary Islands',
  1240,
  "An open plan space, designed to bring the outdoors in.",
  "Wake up to volcano views and a dip in the pool in Outsite Canary Islands. This space is shouldered by 2 dormant volcanoes, and you can reach major surf beaches in 15 minutes drive. All rooms face an open, decked pool area, peppered with palm trees and native plants. Use the lounge or desk in your room for a few hours of focus, or meditate in the designated yoga room on-site. Outsite Canary Islands is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
  "/static/img/canary_islands.jpeg",
  [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
  )
location_10 = create_location(
  'Santa Teresa, Costa Rica',
  1375,
  "Quality workspace meets ocean views in Costa Rica.",
  "Nestled in the middle of Costa Rica's blue zone is Outsite Santa Teresa, a jungle villa. There are plenty of communal spaces to work from and unwind in, all of which are open-air and offer panoramic views of the Pacific. Sunsets are magical here - opt to watch them from the living room, or from your own private terrace. The house is in a gated community at the top of a hill. You'll find a pool just before the gate to cool off in on your way into town. Outsite Santa Teresa is a serviced coliving space designed to be the perfect hub for digital nomads, flexible professionals, and business travellers looking to live, work, and connect.",
  "/static/img/costa_rica.jpeg",
  [amenity_1, amenity_2, amenity_3, amenity_4, amenity_5, amenity_6, amenity_7, amenity_8, amenity_9, amenity_10, amenity_11, amenity_12, amenity_13, amenity_14, amenity_15, amenity_16, amenity_17, amenity_18, amenity_19, amenity_20, amenity_21]
  )




check_1 = get_location_by_id(1)
check_2 = get_location_by_id(2)
check_3 = get_location_by_id(3)

# print(check_1)
# print(check_2)
# print(check_3)

#SAMPLE USERS

user_1 = create_user('user1@email.com', "1234")
user_2 = create_user('user2@email.com', "5678")
user_3 = create_user('user3@email.com', "9101112")

# user_check_1 = get_user_by_email('user1@email.com')
# user_check_2 = get_user_by_email('user2@email.com')
# user_check_3 = get_user_by_email('user3@email.com')

# print(user_check_1)
# print(user_check_2)
# print(user_check_3)

#SAMPLE BOOKINGS

global_date_format = "%m-%d-%Y"

booking_1 = create_booking(datetime.strptime('12-25-2022', global_date_format), datetime.strptime('01-01-2023', global_date_format), user_1, location_1)
booking_2 = create_booking(datetime.strptime('01-01-2023', global_date_format), datetime.strptime('01-30-2023', global_date_format), user_2, location_2)
booking_3 = create_booking(datetime.strptime('02-21-2023', global_date_format), datetime.strptime('02-28-2022', global_date_format), user_3, location_3)

# booking_check_1 = get_booking_by_id(1)
# booking_check_2 = get_booking_by_id(2)
# booking_check_3 = get_booking_by_id(3)

# print(booking_check_1)
# print(booking_check_2)
# print(booking_check_3)

