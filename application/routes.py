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


@app.route("/editStudent/<int:student_ID>", methods=["GET", "POST"])
def editStudent(student_ID):
    form = EditStudent()
    student = Student.query.filter_by(student_ID = student_ID).first()
    if request.method == "POST":
        student.name = form.student_name.data
        db.session.commit()
        return redirect("/")
    return render_template("EditStudent.html", form=form)


@app.route("/deleteStudent/<int:student_ID>")
def deleteStudent(student_ID):
    student = Student.query.filter_by(student_ID=student_ID).first()
    db.session.delete(student)
    db.session.commit()
    return redirect("/")