from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from application import app, db
from application.models import Workouts

from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db", 
        SECRET_KEY="Test_Secret_Key",
        WTF_CSRF_ENABLED=False
        )
        return app

    def setup(self):
        db.create_all()
        Test = Workouts(workout_muscle_group='Test', 
        duration='Test' 
        )
        db.session.add(Test)
        db.session.commit()

    def teardown(self):
        db.session.remove()
        db.drop.all()

class TestViews(TestBase):
    def test_new_workout_get(self):
        response = self.client.get(url_for('new_workout'))
        self.assertEqual(response.status_code, 200)

    
class TestCreate(TestBase):
    def test_workouts_add(self):
        with self.client:
            response = self.client.post(
                '/new_workout',
                data=dict(
                   workout_muscle_group = "test1",
                   duration = "test1"
                ),
            )

class TestRead(TestBase): #might delete
    def test_workouts_read(self):
        response = self.client.get(url_for('index'))

class TestDelete(TestBase): 
    def test_workout_delete(self):
        response = self.client.get(url_for('delete_workout', id=1))
        self.assertNotIn(response.data, b'Test Delete')

