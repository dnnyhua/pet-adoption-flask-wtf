from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, NumberRange, Optional, URL

class PetForm(FlaskForm):
  "Form for adding a new pet to the database"

  name = StringField("Pet Name", validators=[InputRequired(message="Please enter pet's name")])
  species = StringField("Species",validators=[InputRequired(message="Please enter specie")])
  photo_url = StringField("Photo Url")
  age = IntegerField("Age", validators=[Optional(), NumberRange(min=1, max=30, message="Enter age between 1 to 30")])
  notes = TextAreaField("Notes")
  available = SelectField("Available?", choices=[(True, 'True'), (False, 'False')])


class EditForm(FlaskForm):
  """Edit pet information"""

  photo_url = StringField("Photo Url", validators=[URL()])
  notes = TextAreaField("Notes")
  available = SelectField("Available?", choices=[(True, 'True'), (False, 'False')])


