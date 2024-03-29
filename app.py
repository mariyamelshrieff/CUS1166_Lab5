# Import appropriate libraries,
# Import appropriate libraries,
import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# This module defines that database parameters.
from config import Config
# Load the models (i.e. Flights, Passenger model classes)
from models import *


# Define an instance of flask application, load database parameters.
app = Flask(__name__)
app.config.from_object(Config)

# SQLAlchemy class need an instance of the flask app to know of the application model.
db.init_app(app)

# Define a route
@app.route("/")
def index():
    # Equivalent to: "SELECT * from flights" SQL statement.
    flights = Flight.query.all()
    return render_template('index.html', flights=flights)
@app.route("/add_flight",methods=["post"])
def add_flight():
    # Get information from the form.
    origin = request.form.get("origin")
    destination = request.form.get("destination")
    duration = request.form.get("duration")
    # Equivalent to:
    # INSERT INTO flights (flight_number, origin, destination, durations) VALUES (origin,...)
    flight = Flight(flight_number="LH",origin=origin, destination=destination, duration=duration)
    db.session.add(flight)
    db.session.commit()
    # Query database.
    flights = Flight.query.all()
    return render_template('index.html', flights=flights)
@app.route("/book/<int:flight_id>", methods=["GET", "POST"])
def book_flight(flight_id):
    #
    # Equivalent to "SELECT * from flights where id=flight_id"
    flight = Flight.query.get(flight_id)
    # If this is a post request = Add the passenger.
    if request.method == 'POST':
        name = request.form.get("name")
        seat = request.form.get("seat")
        # Use the utility method to add a new passenger in the database.
        flight.add_passenger(name,seat)
# Use the relationships field in the flights model to retrieve
# all passengers in the current flight.
    passengers = flight.passengers
    return render_template("book.html", flight=flight, passengers=passengers)

def main():
    if (len(sys.argv)==2):
        print(sys.argv)
        if sys.argv[1] == 'createdb':
            db.create_all()
    else:
        print("Run app using 'flask run'")
        print("To create a database use 'python app.py createdb")
# Run the main method in the context of our flass application
# This allows db know about our models.
if __name__ == "__main__":
    with app.app_context():
        main()
