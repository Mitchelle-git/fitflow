from app import app
from models import db, Workout, Exercise, WorkoutExercise

with app.app_context():
    db.drop_all()
    db.create_all()

    # Workouts
    w1 = Workout(title="Leg Day", description="Lower body strength")
    w2 = Workout(title="Push Day", description="Upper body strength")

    # Exercises
    e1 = Exercise(name="Squats", category="strength")
    e2 = Exercise(name="Push Ups", category="strength")

    db.session.add_all([w1, w2, e1, e2])
    db.session.commit()

    # Join data
    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=e1.id, sets=4, reps=10)
    we2 = WorkoutExercise(workout_id=w2.id, exercise_id=e2.id, sets=3, reps=15)

    db.session.add_all([we1, we2])
    db.session.commit()

    print("FitFlow DB seeded successfully!")