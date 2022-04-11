from application import app, db
from application.forms import WorkoutForm, ExerciseForm
from application.models import Workouts, Exercises
from flask import render_template, request, redirect, url_for

@app.route('/')
def index():
    all_workouts = Workouts.query.all()
    all_exercises = Exercises.query.all()
    return render_template('index.html', all_workouts=all_workouts, all_exercises = all_exercises)

@app.route('/new_workout', methods=['GET', 'POST'])
def new_workout():
    form = WorkoutForm()

    if request.method == "POST":
        workoutdata = Workouts(workout_muscle_group = form.workout_muscle_group.data, duration = form.duration.data)
        db.session.add(workoutdata)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('new_workout.html', form=form)

@app.route('/new_exercise/<int:id>', methods=['GET', 'POST'])
def new_exercise(id):
    form = ExerciseForm()
    all_exercises = Exercises.query.all()
    all_workouts = Workouts.query.all()
    workout = Workouts.query.get(id)

    if request.method == "POST":
        exercisedata= Exercises(exercise_name = form.exercise_name.data, sets_per_exercise = form.sets_per_exercise.data, reps_per_set = form.sets_per_exercise.data, workout_id = form.workout_id.data)
        db.session.add(exercisedata)
        db.session.commit()
        

    return render_template('new_exercise.html', form=form)

@app.route('/view_exercise')
def view_exercise():
    all_workouts = Workouts.query.all()
    all_exercises = Exercises.query.all()
    return render_template('view_exercise.html', all_exercises=all_exercises)

@app.route('/complete/<completed>/<int:id>')
def complete_workout(completed, id):
    workout = Workouts.query.get(id)
    if completed == 'True':
        workout.completed = True
        db.session.commit()
    elif completed == 'False':
        workout.completed = False
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_workout(id):
    workout = Workouts.query.get(id)
    form = WorkoutForm()
    
    if request.method == "POST":
        workout.workout_muscle_group = form.workout_muscle_group.data
        workout.duration = form.duration.data
        db.session.commit()
        return redirect(url_for('index'))

    form.workout_muscle_group.data = workout.workout_muscle_group
    form.duration.data = workout.duration

    return render_template('new_workout.html', form=form)

@app.route('/delete/<int:id>')
def delete_workout(id):
    workout = Workouts.query.get(id)
    db.session.delete(workout)
    db.session.commit()
    return redirect(url_for('index'))