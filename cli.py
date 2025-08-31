import re
from database import SessionLocal
from models import Professor, Course, CourseAssignment


# ================= HELPERS =================
def get_valid_name(prompt="Enter name: "):
    """Allow only letters, spaces, and dots in names."""
    pattern = re.compile(r"^[A-Za-z .]+$")
    while True:
        name = input(prompt).strip()
        if pattern.match(name):
            return name
        print("❌ Invalid name, try again.")


def get_choice(options, prompt="Enter choice: "):
    """Safe menu choice selection."""
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("❌ Invalid choice, try again.")
        except ValueError:
            print("❌ Enter a number.")


# ================= PROFESSOR MANAGEMENT =================
def add_professor():
    session = SessionLocal()

    name = get_valid_name("Enter professor name: ")

    departments = ["Computer Science", "Data Science", "Cyber Security", "Programming"]
    print("\nChoose Department:")
    for i, dept in enumerate(departments, 1):
        print(f"{i}. {dept}")
    department = get_choice(departments)

    ranks = ["Lecturer", "Senior Lecturer", "Associate Professor", "Professor"]
    print("\nChoose Rank:")
    for i, r in enumerate(ranks, 1):
        print(f"{i}. {r}")
    rank = get_choice(ranks)

    professor = Professor(name=name, department=department, rank=rank)
    session.add(professor)
    session.commit()
    print(f"\n✅ Professor {name} added successfully!\n")
    session.close()


def list_professors():
    session = SessionLocal()
    professors = session.query(Professor).all()
    if not professors:
        print("\n⚠️ No professors found.\n")
    else:
        print("\n--- Professors ---")
        for prof in professors:
            print(f"{prof.id}. {prof.name} - {prof.department} ({prof.rank})")
    print()
    session.close()


def delete_professor():
    session = SessionLocal()
    professors = session.query(Professor).all()
    if not professors:
        print("\n⚠️ No professors to delete.\n")
        session.close()
        return

    print("\nChoose Professor to delete:")
    for i, prof in enumerate(professors, 1):
        print(f"{i}. {prof.name} - {prof.department} ({prof.rank})")
    professor = get_choice(professors)

    session.delete(professor)
    session.commit()
    print(f"✅ Professor {professor.name} deleted successfully!\n")
    session.close()


# ================= COURSE MANAGEMENT =================
def add_course():
    session = SessionLocal()

    title = get_valid_name("Enter course title: ")
    code = input("Enter course code: ").strip()

    credits_options = [2, 3, 4, 5]
    print("\nChoose Credits:")
    for i, c in enumerate(credits_options, 1):
        print(f"{i}. {c}")
    credits = get_choice(credits_options)

    course = Course(title=title, code=code, credits=credits)
    session.add(course)
    session.commit()
    print(f"\n✅ Course {title} added successfully!\n")
    session.close()


def list_courses():
    session = SessionLocal()
    courses = session.query(Course).all()
    if not courses:
        print("\n⚠️ No courses found.\n")
    else:
        print("\n--- Courses ---")
        for course in courses:
            print(f"{course.id}. {course.title} ({course.code}) - {course.credits} credits")
    print()
    session.close()


def delete_course():
    session = SessionLocal()
    courses = session.query(Course).all()
    if not courses:
        print("\n⚠️ No courses to delete.\n")
        session.close()
        return

    print("\nChoose Course to delete:")
    for i, course in enumerate(courses, 1):
        print(f"{i}. {course.title} ({course.code}) - {course.credits} credits")
    course = get_choice(courses)

    session.delete(course)
    session.commit()
    print(f"✅ Course {course.title} deleted successfully!\n")
    session.close()


# ================= ASSIGNMENT MANAGEMENT =================
def assign_course():
    session = SessionLocal()

    professors = session.query(Professor).all()
    if not professors:
        print("⚠️ No professors available. Add one first.\n")
        session.close()
        return

    print("\nChoose Professor:")
    for i, prof in enumerate(professors, 1):
        print(f"{i}. {prof.name} ({prof.department}, {prof.rank})")
    professor = get_choice(professors)

    courses = session.query(Course).all()
    if not courses:
        print("⚠️ No courses available. Add one first.\n")
        session.close()
        return

    print("\nChoose Course:")
    for i, course in enumerate(courses, 1):
        print(f"{i}. {course.title} ({course.code})")
    course = get_choice(courses)

    semesters = ["Fall", "Spring", "Summer"]
    print("\nChoose Semester:")
    for i, s in enumerate(semesters, 1):
        print(f"{i}. {s}")
    semester = get_choice(semesters)

    assignment = CourseAssignment(professor=professor, course=course, semester=semester)
    session.add(assignment)
    session.commit()
    print(f"\n✅ Assigned {course.title} to {professor.name} for {semester} semester.\n")
    session.close()


def list_assignments():
    session = SessionLocal()
    assignments = session.query(CourseAssignment).all()
    if not assignments:
        print("\n⚠️ No assignments found.\n")
    else:
        print("\n--- Assignments ---")
        for assign in assignments:
            print(
                f"{assign.professor.name} teaches {assign.course.title} ({assign.course.code}) in {assign.semester}"
            )
    print()
    session.close()


def delete_assignment():
    session = SessionLocal()
    assignments = session.query(CourseAssignment).all()
    if not assignments:
        print("\n⚠️ No assignments to delete.\n")
        session.close()
        return

    print("\nChoose Assignment to delete:")
    for i, assign in enumerate(assignments, 1):
        print(f"{i}. {assign.professor.name} -> {assign.course.title} ({assign.semester})")
    assignment = get_choice(assignments)

    session.delete(assignment)
    session.commit()
    print("✅ Assignment deleted successfully!\n")
    session.close()


# ================= MENUS =================
def professor_menu():
    while True:
        print("\n--- Professor Management ---")
        print("1. Add Professor")
        print("2. List Professors")
        print("3. Delete Professor")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            add_professor()
        elif choice == "2":
            list_professors()
        elif choice == "3":
            delete_professor()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice, try again.")


def course_menu():
    while True:
        print("\n--- Course Management ---")
        print("1. Add Course")
        print("2. List Courses")
        print("3. Delete Course")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            add_course()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            delete_course()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice, try again.")


def assignment_menu():
    while True:
        print("\n--- Assignment Management ---")
        print("1. Assign Course to Professor")
        print("2. List Assignments")
        print("3. Delete Assignment")
        print("4. Back")
        choice = input("Choose option: ")
        if choice == "1":
            assign_course()
        elif choice == "2":
            list_assignments()
        elif choice == "3":
            delete_assignment()
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice, try again.")


def main_menu():
    while True:
        print("\n=== University Management System ===")
        print("1. Professor Management")
        print("2. Course Management")
        print("3. Assignment Management")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            professor_menu()
        elif choice == "2":
            course_menu()
        elif choice == "3":
            assignment_menu()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    main_menu()
