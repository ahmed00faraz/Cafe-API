import random

from main import Cafe, db

cafes = db.session.query(Cafe).all()
random_cafe = random.choice(cafes)
print(type(random_cafe))