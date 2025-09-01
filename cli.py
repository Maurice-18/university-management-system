from database import SessionLocal
from models import Professor, Course, Student, CourseAssignment

def list_professors(session):
    professors = session.query(Professor).all()
    for prof in professors:
        print(f"{prof.id}: {prof.name} - {prof.department} ({prof.rank})")

def add_professor(session):
    name = input("Enter professor name: ")

    departments = ["Computer Science", "Mathematics", "Physics", "Biology", "Chemistry"]
    print("\nSelect Department:")
    for i, dept in enumerate(departments, start=1):
        print(f"{i}. {dept}")
    dept_choice = int(input("Enter choice number: "))
    department = departments[dept_choice - 1]

    ranks = ["Assistant", "Associate", "Full"]
    print("\nSelect Rank:")
    for i, rank in enumerate(ranks, start=1):
        print(f"{i}. {rank}")
    rank_choice = int(input("Enter choice number: "))
    rank = ranks[rank_choice - 1]

    new_prof = Professor(name=name, department=department, rank=rank)
    session.add(new_prof)
    session.commit()
    print(f"Professor {name} added successfully!")

def list_courses(session):
    courses = session.query(Course).all()
    for course in courses:
        print(f"{course.id}: {course.title} [{course.code}] ({course.credits} credits)")

def add_course(session):
    title = input("Enter course title: ")
    code = input("Enter course code (e.g., CS101): ")

    credit_options = [2, 3, 4, 5]
    print("\nSelect Credits:")
    for i, c in enumerate(credit_options, start=1):
        print(f"{i}. {c}")
    credit_choice = int(input("Enter choice number: "))
    credits = credit_options[credit_choice - 1]

    new_course = Course(title=title, code=code, credits=credits)
    session.add(new_course)
    session.commit()
    print(f"Course {title} added successfully!")

def list_students(session):
    students = session.query(Student).all()
    for student in students:
        enrolled_courses = [c.title for c in student.courses]
        courses_str = ", ".join(enrolled_courses) if enrolled_courses else "No courses"
        print(f"{student.id}: {student.name}, {student.major}, enrolled in: {courses_str}")

def assign_professor(session):
    list_professors(session)
    prof_id = int(input("Enter professor ID: "))

    list_courses(session)
    course_id = int(input("Enter course ID: "))

    semester = input("Enter semester (e.g., Fall 2025): ")

    assignment = CourseAssignment(professor_id=prof_id, course_id=course_id, semester=semester)
    session.add(assignment)
    session.commit()
    print("Professor assigned to course successfully!")

def main():
    session = SessionLocal()

    while True:
        print("\nUniversity Management CLI")
        print("1. List Professors")
        print("2. Add Professor")
        print("3. List Courses")
        print("4. Add Course")
        print("5. List Students")
        print("6. Assign Professor to Course")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            list_professors(session)
        elif choice == "2":
            add_professor(session)
        elif choice == "3":
            list_courses(session)
        elif choice == "4":
            add_course(session)
        elif choice == "5":
            list_students(session)
        elif choice == "6":
            assign_professor(session)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
