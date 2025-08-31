from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Professor(Base):
    __tablename__ = "professors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    rank = Column(String, nullable=False)

    assignments = relationship("CourseAssignment", back_populates="professor")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    code = Column(String, unique=True, nullable=False)
    credits = Column(Integer, nullable=False)

    assignments = relationship("CourseAssignment", back_populates="course")


class CourseAssignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    professor_id = Column(Integer, ForeignKey("professors.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    semester = Column(String, nullable=False)

    professor = relationship("Professor", back_populates="assignments")
    course = relationship("Course", back_populates="assignments")
