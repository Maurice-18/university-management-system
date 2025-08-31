from database import SessionLocal, init_db
from models import Professor, Course, CourseAssignment

# Initialize tables
init_db()

# Open a session
session = SessionLocal()

try:
    # Create professors
    p1 = Professor(name="Ken Block", department="Computer Science", rank="Associate Professor")
    p2 = Professor(name="Bobby Johnson", department="Data Science", rank="Lecturer")

    # Create courses
    c1 = Course(title="Computer Science", code="CS101", credits=3)
    c2 = Course(title="Data Science", code="CS102", credits=4)
    c3 = Course(title="Cyber Security", code="MATH201", credits=3)

    session.add_all([p1, p2, c1, c2, c3])
    session.commit()

    # Assign courses
    a1 = CourseAssignment(professor_id=p1.id, course_id=c1.id, semester="First 2025")
    a2 = CourseAssignment(professor_id=p2.id, course_id=c3.id, semester="Second 2025")

    session.add_all([a1, a2])
    session.commit()

    print("✅ Database seeded successfully.")

except Exception as e:
    session.rollback()
    print(f"❌ Error while seeding: {e}")
finally:
    session.close()
