from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.hashed_password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_question_random(db: Session):
    return db.query(models.Question).order_by(func.random()).first()

def get_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Question).offset(skip).limit(limit).all()


def get_question_by_id(db: Session, question_id: int):
    return db.query(models.Item).filter(models.Question.id == question_id).first()


def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(
        text=question.text, options=question.options, answer=question.answer
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def get_exam(db: Session, n_questions: int = 10):
    return db.query(models.Question).order_by(func.random()).limit(n_questions).all()


def create_exam(db: Session, exam: schemas.ExamCreate):
    db_exam = models.Exam(
        questions=exam.questions, user_id=exam.user_id, grade=exam.grade
    )
    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)
    return db_exam


def create_user_response(db: Session, user_response: schemas.UserResponseCreate):
    db_answer = models.UserResponse(
        user_id=user_response.user_id,
        question_id=user_response.question_id,
        exam_id=user_response.exam_id,
        selected_option=user_response.selected_option,
    )
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer
