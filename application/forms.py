from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class WorkoutForm(FlaskForm):
    workout_muscle_group = StringField(
        'Workout', 
        validators=[DataRequired(), Length(max=30)]
    )
    duration = StringField(
        'Duration', 
        validators=[DataRequired(), Length(max=30)]
    )
    submit = SubmitField('Submit')

class ExerciseForm(FlaskForm):
    exercise_name = StringField(
        'Exercise', 
        validators=[DataRequired(), Length(max=30)]
    )
    sets_per_exercise = StringField(
        'Sets per exercise', 
        validators=[DataRequired(), Length(max=30)]
    )
    reps_per_set = StringField(
        'Reps per set', 
        validators=[DataRequired(), Length(max=30)]
    )
    
    workout_id = IntegerField(
        'Workout ID', 
        validators=[DataRequired(), Length(max=30)]
    )

    submit = SubmitField('Submit')