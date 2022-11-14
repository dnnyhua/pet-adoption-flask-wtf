from flask import Flask, request, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm, EditForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():

  pets = Pet.query.all()
  return render_template('home.html', pets=pets)


@app.route('/pets/new', methods=['GET','POST'])
def add_pet():
  """Add Pet"""

  form = PetForm()

  if form.validate_on_submit():
    name = form.name.data
    species = form.species.data
    photo_url = form.photo_url.data
    age = form.age.data
    notes = form.notes.data
    available = bool(form.available.data)
    
    # add data from form to database
    pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
    db.session.add(pet)
    db.session.commit()
    flash(f'{pet.name} added.')
    return redirect('/')
  else:
    return render_template('add_pet.html', form=form)


@app.route('/pets/<int:pet_id>/display')
def display_pet_info(pet_id):
  """Display information about the pet"""
  
  pet = Pet.query.get(pet_id) 
  return render_template('display_pet.html', pet=pet)


@app.route('/pets/<int:pet_id>/edit', methods=['GET', 'POST'])
def edit_form(pet_id):
  """Edit the info of a pet"""

  pet = Pet.query.get(pet_id)

  # populate form with current data
  form = EditForm(obj=pet)

  if form.validate_on_submit():
    pet.name = form.name.data
    pet.species = form.species.data
    pet.photo_url = form.photo_url.data
    pet.age = form.age.data
    pet.notes = form.notes.data
    pet.available = bool(form.available.data)
    db.session.commit()
    return redirect('/')
  else:
    return render_template('edit_pet_form.html', form=form, pet=pet)




