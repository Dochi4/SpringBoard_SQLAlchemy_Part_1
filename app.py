"""Blogly application."""

from flask import Flask, request, render_template, redirect 
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db , User
from sqlalchemy import text

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "blogly_key"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

connect_db(app)

with app.app_context():
    db.create_all()

debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """Redirects to user list."""
    return redirect("/users")

@app.route("/users")
def list_page():
    """Shows list of users from the database."""
    users = User.query.all()
    return render_template("list.html", users=users)

@app.route("/users/new")
def add_page():
    """Show new user form."""
    return render_template("add_new.html") 

@app.route("/users/new", methods=['POST'])
def add_new():
    """Adds new user to the database."""
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")

@app.route('/users/<int:user_id>')
def detail_user(user_id):
    """Show detail of a user."""
    user = User.query.get_or_404(user_id)
    return render_template("details.html", user=user)

@app.route('/users/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    """Delete a user."""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")

@app.route('/users/<int:user_id>/edit')
def show_update_page(user_id):
    """Show the form to update a user."""
    user = User.query.get_or_404(user_id)
    return render_template("update.html", user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def update_user(user_id):
    """Update a user."""
    user = User.query.get_or_404(user_id)
    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.image_url = request.form["image_url"]

    db.session.commit()

    return redirect("/users")