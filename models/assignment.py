from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class CourseAssignment(Base):
    __tablename__ = "course_assignments"

    id = Column(Integer, primary_key=True, index=True)
    professor_id = Column(Integer, ForeignKey("professors.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))

    professor = relationship("Professor", back_populates="assignments")
    course = relationship("Course", back_populates="assignments")
