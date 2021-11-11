from flask import Flask, request, redirect, render_template
from application import app, db
from application.forms import AddStudent, EditStudent, Marks, EditMarks
from application.models import Student, Marks

@app.route("/")
def home():
    students = Student.query.all()
    return render_template("Homepage.html", records=students)


@app.route("/addStudent", methods=["GET","POST"])
def addStudent():
    form = AddStudent()
    if request.method == 'POST':
        name=form.student_name.data
        newstudent = Student(name=name)
        db.session.add(newstudent)
        db.session.commit()
        return redirect("/")
    return render_template("Inputform.html", form=form)