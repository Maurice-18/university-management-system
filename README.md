# University Management System (CLI)

A simple **command-line interface (CLI)** application built with **Python, SQLAlchemy, and Alembic** to manage professors, courses, and assignments in a university.

---

## 📦 Features
- List professors, courses, and course assignments.
- Data is stored in a SQLite database using SQLAlchemy ORM.
- Relationships are modeled between Professors, Courses, and CourseAssignments.
- Alembic used for database migrations.
- Seed script to populate initial data.

---

## 🚀 Setup Instructions

1. Clone this repository.
2. Install dependencies:
   ```bash
# 1. Install dependencies
pipenv install sqlalchemy alembic

# 2. Activate virtualenv
pipenv shell

# 3. Initialize alembic (only once)
alembic init alembic

# 4. Generate migration
alembic revision --autogenerate -m "init"

# 5. Apply migration
alembic upgrade head

# 6. Seed the database
python seed.py

# 7. Run CLI to check data
python cli.py

