from application import db
from application.models import Exercises, Workouts

db.drop_all()
db.create_all()
