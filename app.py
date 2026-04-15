from flask import Flask, request
from flask_migrate import Migrate
from models import db, Workout, Exercise, WorkoutExercise
from schemas import (
    workout_schema,
    workouts_schema,
    exercise_schema,
    exercises_schema,
    workout_exercise_schema
)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fitflow.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

migrate = Migrate(app, db)

@app.route("/")
def home():
    return {"message": "FitFlow API running"}


# ================= WORKOUTS =================

@app.route("/workouts", methods=["GET"])
def get_workouts():
    return workouts_schema.dump(Workout.query.all()), 200


@app.route("/workouts/<int:id>", methods=["GET"])
def get_workout(id):
    return workout_schema.dump(Workout.query.get_or_404(id)), 200


@app.route("/workouts", methods=["POST"])
def create_workout():
    data = request.json

    workout = Workout(
        title=data["title"],
        description=data.get("description")
    )

    db.session.add(workout)
    db.session.commit()

    return workout_schema.dump(workout), 201


@app.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):
    db.session.delete(Workout.query.get_or_404(id))
    db.session.commit()
    return {"message": "Workout deleted"}


# ================= EXERCISES =================

@app.route("/exercises", methods=["GET"])
def get_exercises():
    return exercises_schema.dump(Exercise.query.all()), 200


@app.route("/exercises", methods=["POST"])
def create_exercise():
    data = request.json

    exercise = Exercise(
        name=data["name"],
        category=data["category"]
    )

    db.session.add(exercise)
    db.session.commit()

    return exercise_schema.dump(exercise), 201


@app.route("/exercises/<int:id>", methods=["DELETE"])
def delete_exercise(id):
    db.session.delete(Exercise.query.get_or_404(id))
    db.session.commit()
    return {"message": "Exercise deleted"}


# ================= ADD EXERCISE TO WORKOUT =================

@app.route("/workouts/<int:workout_id>/exercises", methods=["POST"])
def add_exercise(workout_id):
    data = request.json

    we = WorkoutExercise(
        workout_id=workout_id,
        exercise_id=data["exercise_id"],
        sets=data["sets"],
        reps=data.get("reps"),
        duration=data.get("duration")
    )

    db.session.add(we)
    db.session.commit()

    return workout_exercise_schema.dump(we), 201


if __name__ == "__main__":
    app.run(debug=True)