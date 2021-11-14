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


@app.route("/studentInformation/<int:student_ID>")
def studentInformation(student_ID):
    data = Student.query.filter_by(student_ID=student_ID).first()
    return render_template("StudentInformation.html", record=data)


@app.route("/marksTable")
def marksTable():
    marks = Marks.query.all()
    return render_template("MarksTable.html", records=marks)


@app.route("/addMarks/<int:student_ID>", methods=["GET", "POST"])
def addMarks(student_ID):
    form = Marks()
    student_ID = Student.query.filter_by(student_ID=student_ID).first()
    if request.method == "POST":
        subject=form.subject.data
        marks=form.marks.data
        newmarks=Marks(student = student_ID, subject=subject, marks=marks)
        db.session.add(newmarks)
        db.session.commit()
        return redirect("StudentInformation.html")
    return render_template("InputMarks.html", form=form)


@app.route("/mAddMarks", methods=["GET", "POST"])
def mAddMarks():
    form = Marks()
    if request.method == "POST":
        student_ID=form.student_ID.data
        subject=form.subject.data
        marks=form.marks.data
        newmarks=Marks(student = student_ID, subject=subject, marks=marks)
        db.session.add(newmarks)
        db.session.commit()
        return redirect("MarksTable.html")
    return render_template("InputMarks.html", form=form)


@app.route("/editMarks/<int:mark_ID>", methods=["GET", "POST"])
def editMarks(mark_ID):
    form = EditMarks()
    mark = Marks.query.filter_by(mark_ID-mark_ID).first()
    if request.method == "POST":
        mark.student_ID = form.student_ID.data
        mark.subject = form.subject.data
        mark.mark = form.marks.data
        db.session.commit()
        return redirect("{{ url_for('marksTable') }}")
    return render_template("EditMarks.html", form=form)