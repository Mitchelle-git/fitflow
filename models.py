from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# ================= WORKOUT =================
class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))

    workout_exercises = db.relationship(
        "WorkoutExercise",
        backref="workout",
        cascade="all, delete-orphan"
    )

    def __init__(self, title, description=None):
        if len(title) < 3:
            raise ValueError("Title must be at least 3 characters")
        self.title = title
        self.description = description


# ================= EXERCISE =================
class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    workout_exercises = db.relationship(
        "WorkoutExercise",
        backref="exercise",
        cascade="all, delete-orphan"
    )

    def __init__(self, name, category):
        allowed = ["strength", "cardio", "flexibility"]

        if category not in allowed:
            raise ValueError("Invalid category")

        self.name = name
        self.category = category


# ================= JOIN TABLE =================
class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)

    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"))
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"))

    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer)
    duration = db.Column(db.Integer)

    __table_args__ = (
        db.CheckConstraint("sets > 0", name="check_sets_positive"),
        db.CheckConstraint("reps >= 0", name="check_reps_non_negative"),
    )