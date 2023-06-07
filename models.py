from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY
from sqlalchemy.orm import relationship

from database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    options = Column(String) # The options will be codified as a json string
    answer = Column(String)
    tag = Column(String)

    responses = relationship("UserResponse", back_populates="question")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    

class UserResponse(Base):
    __tablename__ = "user_responses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=True)
    selected_option = Column(String)
    
    
    question = relationship("Question", back_populates="responses")
    user = relationship("User", back_populates="user_responses")
    exam = relationship("Exam", back_populates="user_responses")
    


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    user_responses = relationship("UserResponse", back_populates="user")
    exams = relationship("Exam", back_populates="user")

class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True, index=True)
    questions = Column(String)  ## The questions will be codified as a json string
    grade = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    user_responses = relationship("UserResponse", back_populates="exam")
    user = relationship("User", back_populates="exams")

