from database import engine, Base
from models import Professor, Course, CourseAssignment

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done!")
