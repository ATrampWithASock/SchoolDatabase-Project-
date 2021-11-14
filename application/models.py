from application import db


class Student(db.Model):
    """Students"""
    ___tablename___ = "students"
    student_ID = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    marks = db.relationship('Marks', backref='student')


class Marks(db.Model):
    """Marks"""
    ___tablename___ = "marks"
    mark_ID = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(50))
    marks = db.Column(db.Integer)
    student_ID = db.Column(db.Integer, db.ForeignKey(Student.student_ID))