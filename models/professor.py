from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Professor(Base):
    __tablename__ = "professors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    rank = Column(String, nullable=False)

    assignments = relationship("CourseAssignment", back_populates="professor")
