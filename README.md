# FitFlow API 

##  Project Description
FitFlow API is a Flask REST backend for tracking workouts and exercises. It allows creation of workouts, exercises, and linking exercises to workouts with sets, reps, and duration.

---

## ⚙️ Tech Stack
- Flask
- Flask-SQLAlchemy
- Flask-Migrate (Alembic)
- Marshmallow
- SQLite

---

##  Project Structure
fitflow-api/
│
├── app.py
├── models.py
├── schemas.py
├── seed.py
├── requirements.txt
└── migrations/

---

##  Installation & Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Flask app
```bash
export FLASK_APP=app.py
```

### 3. Initialize migrations
```bash
flask db init
```

### 4. Create migration
```bash
flask db migrate -m "initial migration"
```

### 5. Apply migration
```bash
flask db upgrade
```

### 6. Seed database
```bash
python seed.py
```

### 7. Run server
```bash
python app.py
```

---

## API Endpoints

### Workouts
- GET /workouts → Get all workouts
- GET /workouts/<id> → Get single workout
- POST /workouts → Create workout
- DELETE /workouts/<id> → Delete workout

### Exercises
- GET /exercises → Get all exercises
- POST /exercises → Create exercise
- DELETE /exercises/<id> → Delete exercise

### Workout Exercises
- POST /workouts/<workout_id>/exercises → Add exercise to workout

---

##  Seeding Data
Run:
```bash
python seed.py
```

This creates sample workouts and exercises.

---

##  Example Payload

### Add exercise to workout
```json
{
  "exercise_id": 1,
  "sets": 4,
  "reps": 10,
  "duration": 30
}
```

---

## Features
- CRUD for workouts & exercises
- Many-to-many relationship with extra fields
- Schema validation (Marshmallow)
- Model validation
- Table constraints
- Database migrations (Flask-Migrate)
- Seed file included

---


FitFlow API - Flask Backend Project
