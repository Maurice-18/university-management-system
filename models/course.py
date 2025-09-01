from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    code = Column(String, unique=True, nullable=False)

    assignments = relationship("CourseAssignment", back_populates="course")
    enrollments = relationship("Student", back_populates="course")
