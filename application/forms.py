from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField

class AddStudent(FlaskForm):
    student_firstname = StringField("First Name")
    student_surname = StringField("Surname")
    phone = StringField("Mobile Number")
    email = StringField("Email Address")
    address = StringField("Address")
    submit = SubmitField("Add Student")


class Marks(FlaskForm):
    student_ID = IntegerField("Student ID")
    subject = StringField("Subject", choices=[("physics","Physics"), ("chemistry","Chemistry"), ("biology","Biology"), ("maths","Maths"), ("english","English"), ("spanish","Spanish"), ("french","French"), ("geography","Geography"), ("history","History"), ("IT","IT"), ("sport_science","Sport Science")])
    marks = IntegerField("Marks")
    submit = SubmitField("Add Marks")


class EditStudent(FlaskForm):
    student_firstname = StringField("First Name")
    student_surname = StringField("Surname")
    phone = IntegerField("Mobile Number")
    email = StringField("Email Address")
    address = StringField("Address")
    submit = SubmitField("Edit Student")


class EditMarks(FlaskForm):
    student_ID = IntegerField("Student ID")
    subject = SelectField("Subject", choices=[("physics","Physics"), ("chemistry","Chemistry"), ("biology","Biology"), ("maths","Maths"), ("english","English"), ("spanish","Spanish"), ("french","French"), ("geography","Geography"), ("history","History"), ("IT","IT"), ("sport_science","Sport Science")])
    marks = IntegerField("Marks")
    submit = SubmitField("Edit Marks")