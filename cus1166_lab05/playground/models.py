from flask_SQLAlchemy import SQLAlchemy
db = SQLAlchemy()

# Define a Flight model.
class Course(db.Model):
    # Map this model to a flights table
    __tablename__= "Course"

# Specify the columns/ fields of the model.
id = db.Column(db.Integer,primary_key=True)
Course_number = db.Column(db.String, nullable = False)
Course_title = db.Column(db.String, nullable = False)

# Specify any relationship fields.
RegisteredStudent = db.relationship("Student", backref="Course", lazy=True)

# specify any utility methods associated with the model.
def add_Student(self,name,grade):
    # Notice that we set the foreign key for the passenger class.
    new_Student = Student(name=name, grade=grade, Course_id=self.id )
    db.session.add(new_Student)
    db.session.commit()

#Define a Passenger model.
class student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    grade = db.Column(db.Integer, nullable=True)
    # Notice, this field serves as a foreighKey.
    Course_id = db.Column(db.Integer, db.ForeignKey('course.course.id'), nullable=False)
