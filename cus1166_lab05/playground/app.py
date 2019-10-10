{% extends 'layout.html' %}
import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#This module defines that database parameters.
from config import Config
#Load the models (i.e. Flights, Passenger model classes)
from models import *

# Load the models (i.e. Flights, Passenger model classes)

# Define an instance of flask application, load database parameters.
app = Flask(__name__)
app.config.from_object(Config)

# SQLAlchemy class need an instance of the flask app to know of the application model.
db.init_app(app)

# Define a route
@app.route("/")
def index():
    # Equivalent to: "SELECT * from flights" SQL statement.
    Course = Course.query.all()
    return render_template('index.html', courses = courses)

@app.route("/add_course",methods=['POST'])

def add_course():
    # Get information from the form.
    id = request.form.get("id")
    Course_number = request.form.get("Course_Number")
    Course_title = request.form.get("Course_Title")
    # Equivalent to:
    # INSERT INTO flights (flight_number, origin, destination, durations) VALUES (origin,...)
    new_course = Course(Course_number = Course_number, Course_title = Course_title)
        db.session.add(new_course)
        db.session.commit()
    # Query database.
        courses = course.query.all()
    return render_template('index.html', courses=courses)

@app.route('/course_details/<int:course_id>')
def course_students(course_id):
    students = student.query.all()
    return render_template("course_details.html", students=students, course_id=course_id)

@app.route("/register_student/<int:Course_id>", methods=["GET", "POST"])
def register_student(Course_id):
    #
    # Equivalent to "SELECT * from flights where id=flight_id"
    course = course.query.get(Course_id)
    # If this is a post request = Add the passenger.
    if request.method == 'POST':
        course_number = request.form.get("student_name")
        course_title = request.form.get("student_grade")
        new_Student= student(name=course_number,grade=course_title, course_id=Course_id)
        db.session.add(new_student)
        db.session.commit()
        Students = student.query.all ()
return render_template("course_details.html", students= students, Course_id = Course_id)

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
