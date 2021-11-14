from flask import url_for
from flask_testing import TestCase
from app import app
from create import db
from application.models import Student

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        sample = Student(firstname="Jake", surname="Lindop", subject="IT", phone="07742040823", email="J.lindop98@gmail.com", address="8 Albert Road")
        db.session.add(sample)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
    def test_students_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Jake", response.data)

    def test_add_students(self):
        response = self.client.post(
            url_for('addStudent'),
            data = dict(firstname="Sofie", surname="Llugiqi", subject="Biology", phone="14789632541", email="email@gmail.com", address="64 Zoo Lane"),
            follow_redirects = True
        )
        self.assertIn(b"Sofie", response.data)

    def test_edit_students(self):
        response = self.client.post(
            url_for('editStudent', student_ID=1),
            data = dict(firstname="John", surname="Lindop", subject="French", phone="07742040823", email="J.lindop98@gmail.com", address="8 Albert Road"),
            follow_redirects = True
        )
        self.assertIn(b"John", response.data)

    def test_del_student(self):
        response = self.client.get(url_for('deleteStudent', student_ID=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Student Information", response.data)

    def test_student_info(self):
        response = self.client.get(url_for("studentInformation", student_ID=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Jake", response.data)

    def test_view_edit(self):
        response = self.client.get(url_for('editStudent', student_ID=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Edit Student Record", response.data)

    def test_view_add(self):
        response = self.client.get(url_for('addStudent'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Input Student Information", response.data)

    def test_filter_records(self):
        response = self.client.post(url_for('filterRecords'),
        data = dict(subject="IT"))
        self.assertIn(b"Jake", response.data)

    def test_filter_records_all(self):
        response = self.client.post(url_for('filterRecords'),
        data = dict(subject="all"),
        follow_redirects=True)
        self.assertIn(b"Jake", response.data)