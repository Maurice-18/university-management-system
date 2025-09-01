from database import SessionLocal, init_db
from models import Student, Professor, Course, CourseAssignment

def seed_data():
    init_db()
    session = SessionLocal()

    professor1 = Professor(name="Dr. Smith", department="Math", rank="Associate")
    professor2 = Professor(name="Dr. Johnson", department="CS", rank="Full")

    course1 = Course(title="Calculus", code="MATH101", credits=4)
    course2 = Course(title="Algorithms", code="CS201", credits=3)

    student1 = Student(name="Alice", email="alice@example.com", major="Math")
    student2 = Student(name="Bob", email="bob@example.com", major="CS")

    assignment1 = CourseAssignment(professor=professor1, course=course1, semester="Fall 2024")
    assignment2 = CourseAssignment(professor=professor2, course=course2, semester="Spring 2025")

    session.add_all([professor1, professor2, course1, course2, student1, student2, assignment1, assignment2])
    session.commit()
    session.close()

if __name__ == "__main__":
    seed_data()
