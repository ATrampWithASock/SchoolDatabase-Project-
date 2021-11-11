from flask import Flask, request, redirect, render_template
from application import app, db
from application.forms import AddStudent, EditStudent, Marks, EditMarks
from application.models import Student, Marks

@app.route("/")
def home():
    students = Student.query.all()
    return render_template("Homepage.html", records=students)
