from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000",  # Add the URL of your React application here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/questions/", response_model=list[schemas.Question])
def read_questions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    questions = crud.get_questions(db, skip=skip, limit=limit)
    return questions

@app.get("/questions/random", response_model=schemas.Question)
def read_question_random(db: Session = Depends(get_db)):
    db_question = crud.get_question_random(db)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question

@app.get("/questions/{question_id}", response_model=schemas.Question)
def read_question(question_id: int, db: Session = Depends(get_db)):
    db_question = crud.get_question_by_id(db, question_id=question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question

@app.post("/questions/", response_model=schemas.Question)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    db_question = crud.get_question_by_text(db, text=question.text)
    if db_question:
        raise HTTPException(status_code=400, detail="Question already exists")
    return crud.create_question(db=db, question=question)

@app.get("/exam/", response_model=list[schemas.Question])
def get_exam(n_questions: int = 10, db: Session = Depends(get_db)):
    return crud.get_exam(db=db, n_questions=n_questions)

@app.post("/exam/", response_model=schemas.Exam)
def create_exam(exam: schemas.ExamCreate , db: Session = Depends(get_db)):
    return crud.create_exam(db=db, exam=exam)

@app.post("/answer", response_model=schemas.UserResponse)
def create_answer(user_response: schemas.UserResponseCreate, db: Session = Depends(get_db)):
    return crud.create_user_response(db=db, user_response=user_response)