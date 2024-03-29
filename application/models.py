from application import db


class Student(db.Model):
    """Students"""
    ___tablename___ = "students"
    student_ID = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    subject = db.Column(db.String(50))
    phone = db.Column(db.String(11))
    email = db.Column(db.String(50))
    address = db.Column(db.String(50))
    marks = db.relationship('Marks', backref='student')


class Marks(db.Model):
    """Marks"""
    ___tablename___ = "marks"
    mark_ID = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(50))
    marks = db.Column(db.Integer)
    student_ID = db.Column(db.Integer, db.ForeignKey(Student.student_ID))