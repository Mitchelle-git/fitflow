from marshmallow import Schema, fields, validates, ValidationError


# ================= EXERCISE =================
class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)

    @validates("name")
    def validate_name(self, value):
        if len(value) < 2:
            raise ValidationError("Name too short")


# ================= WORKOUT =================
class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()


# ================= JOIN =================
class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int()
    exercise_id = fields.Int()
    sets = fields.Int(required=True)
    reps = fields.Int()
    duration = fields.Int()

    @validates("sets")
    def validate_sets(self, value):
        if value <= 0:
            raise ValidationError("Sets must be greater than 0")


# ================= INSTANCES =================
workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()