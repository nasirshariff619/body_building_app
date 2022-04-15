from application import db
from datetime import datetime

class Workouts(db.Model):
    workout_id = db.Column(db.Integer, primary_key=True)
    workout_muscle_group = db.Column(db.String(30), nullable=False)
    duration = db.Column(db.String(30), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    exercise = db.relationship('Exercises', backref='workoutbr')

class Exercises(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(30), nullable=False)
    sets_per_exercise = db.Column(db.String(30), nullable=False)
    reps_per_set = db.Column(db.String(30), nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.workout_id'))