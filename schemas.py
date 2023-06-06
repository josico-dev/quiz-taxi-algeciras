from pydantic import BaseModel, Field
from typing import List, Optional, Union

## Question schemas

class QuestionBase(BaseModel):
    text: str = Field(..., unique=True)
    options: str
    answer: str


class QuestionCreate(QuestionBase):
    pass


class Question(QuestionBase):
    id: int

    class Config:
        orm_mode = True

## UserResponse schemas

class UserResponseBase(BaseModel):
    user_id: int
    question_id: int
    selected_option: str


class UserResponseCreate(UserResponseBase):
    exam_id: Optional[Union[int, None]] = None


class UserResponse(UserResponseBase):
    id: int
    exam_id: Union[int, None]  # Optional[Union[int, None]] = None

    class Config:
        orm_mode = True

## User schemas

class UserBase(BaseModel):
    email: str
    hashed_password: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    user_responses: List[UserResponse]

    class Config:
        orm_mode = True

## Exam schemas

class ExamBase(BaseModel):
    questions: str  # all the questions will be codified as a json string
    user_id: int
    grade: int


class ExamCreate(ExamBase):
    pass


class Exam(ExamBase):
    id: int

    class Config:
        orm_mode = True
