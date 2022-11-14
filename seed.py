"""Seed file to make sample data"""

from models import Pet, db
from app import app


db.drop_all()
db.create_all()


p1 = Pet(name="Hammy", species="hamster", age="2", notes="big sleeper")
p2 = Pet(name="Shadow", species="dog", age="3", notes="timid", available=False)
p3 = Pet(name="Bun-Bun", species="rabbit", age="1")
p4 = Pet(name="Leo", species="cat", age="5", notes="likes to go on walks", available=False)


db.session.add_all([p1, p2, p3, p4])
db.session.commit()