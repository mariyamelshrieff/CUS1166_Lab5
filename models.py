# This is the models.py file

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Define a Flight model.
class Flight(db.Model):
    # Map this model to a flights table
    __tablename__= "flights"

# Specify the columns/ fields of the model.
id = db.Column(db.Integer,primary_key=True)
flight_number = db.Column(db.String, nullable = False)
origin = db.Column(db.String, nullable = False)
destination = db.Column(db.String, nullable = False)
duration = db.Column(db.Integer, nullable = False)

# Specify any relationship fields.
passengers = db.relationship("Passenger", backref="flights", lazy=True)

# specify any utility methods associated with the model.
def add_passenger(self,name,seat):
    # Notice that we set the foreign key for the passenger class.
    new_passenger = Passenger(name=name, seat=seat, flight_id=self.id )
    db.session.add(new_passenger)
    db.session.commit()
#Define a Passenger model.
class Passenger(db.Model):
    __tablename__ = "passenger"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    seat = db.Column(db.String, nullable=False)
    # Notice, this field serves as a foreighKey.
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.id'), nullable=False)
