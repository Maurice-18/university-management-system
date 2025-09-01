from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Association table for many-to-many relationship between Students and Courses
enrollments_table = Table(
    "enrollments",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True)
)

class Professor(Base):
    __tablename__ = "professors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    rank = Column(String, nullable=False)

    assignments = relationship("CourseAssignment", back_populates="professor")

    def __repr__(self):
        return f"<Professor(id={self.id}, name='{self.name}', department='{self.department}', rank='{self.rank}')>"

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    code = Column(String, nullable=False, unique=True)
    credits = Column(Integer, nullable=False)

    assignments = relationship("CourseAssignment", back_populates="course")
    students = relationship("Student", secondary=enrollments_table, back_populates="courses")

    def __repr__(self):
        return f"<Course(id={self.id}, title='{self.title}', code='{self.code}', credits={self.credits})>"

class CourseAssignment(Base):
    __tablename__ = "course_assignments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    professor_id = Column(Integer, ForeignKey("professors.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    semester = Column(String, nullable=False)

    professor = relationship("Professor", back_populates="assignments")
    course = relationship("Course", back_populates="assignments")

    def __repr__(self):
        return f"<CourseAssignment(id={self.id}, professor_id={self.professor_id}, course_id={self.course_id}, semester='{self.semester}')>"

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    major = Column(String, nullable=False)

    courses = relationship("Course", secondary=enrollments_table, back_populates="students")

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}', major='{self.major}')>"
