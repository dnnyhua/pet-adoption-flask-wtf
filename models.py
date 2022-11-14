from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)


default_image = "https://www.pngkey.com/png/full/842-8429401_pomeranian-02-yappicon-pomeranian-03-yappicon-cartoon.png"

class Pet(db.Model):

  __tablename__ = "pets"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.Text, nullable=False)
  species = db.Column(db.Text, nullable=False)
  photo_url = db.Column(db.Text, default=default_image)
  age = db.Column(db.Integer)
  notes = db.Column(db.Text)
  available = db.Column(db.Boolean, nullable=False, default=True)