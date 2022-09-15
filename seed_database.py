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
#SAMPLE LOCATIONS


location_1 = create_location('Boulder, CO', 400, "right next to the mountains")
location_2 = create_location('San Francisco, CA', 600, "right next to the ocean")
location_3 = create_location('Manhattan, NY', 800, "right next to central park")


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

user_check_1 = get_user_by_email('user1@email.com')
user_check_2 = get_user_by_email('user2@email.com')
user_check_3 = get_user_by_email('user3@email.com')

print(user_check_1)
print(user_check_2)
print(user_check_3)