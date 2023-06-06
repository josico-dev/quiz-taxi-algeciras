import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, engine
from models import User, Exam, Question, UserResponse

# Import the necessary models and database configuration

# Create the database tables
Base.metadata.create_all(bind=engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create sample users
user1 = User(email="user1@example.com", hashed_password="password1")
user2 = User(email="user2@example.com", hashed_password="password2")
session.add_all([user1, user2])
session.commit()

raw_questions = [
    {
        "text": "¿PUEDE UNA PERSONA FÍSICA SER TITULAR DE MÁS DE UNA LICENCIA DE TAXI?",
        "options": [
            "Sí",
            "Sí, siempre que sean licencias de distintos municipios",
            "No, sólo podrá ser titular de una licencia de taxi o autorizacion de transporte interurbano de vehículo de turismo",
        ],
        "answer": "No, sólo podrá ser titular de una licencia de taxi o autorizacion de transporte interurbano de vehículo de turismo",
    },
    {
        "text": "CORRESPONDE A LA CONSEJERÍA DE TRANSPORTES EN MATERIA DE TRANSPORTES LA ADJUDICACIÓN DE LICENCIAS DE AUTOTAXI MEDIANTE CONCURSO?",
        "options": [
            "No, corresponde al Consejo Andaluz del Taxi",
            "Sí",
            "No, corresponden a los Ayuntamientos o entes que asuman sus funciones",
        ],
        "answer": "No, corresponden a los Ayuntamientos o entes que asuman sus funciones",
    },
    {
        "text": "A efectos de las Ordenanzas, ¿cuál sería la definición correcta de SERVICIO DE TAXI O AUTOTAXI?",
        "options": [
            "Servicio de transporte público discrecional de viajeros en automóviles de turismo con una capacidad máxima de diez plazas, prestados en régimen de actividad pública",
            "Servicio de transporte público discrecional de viajeros en automóviles de turismo con una capacidad máxima de nueve plazas, prestados en régimen de actividad privada",
            "Servicio de transporte privado discrecional de viajeros en automóviles de turismo con una capacidad máxima de nueve plazas, prestados en régimen de actividad pública",
        ],
        "answer": "Servicio de transporte público discrecional de viajeros en automóviles de turismo con una capacidad máxima de nueve plazas, prestados en régimen de actividad privada",
    },
    {
        "text": "A efectos de las Ordenanzas, ¿cuál sería la definición correcta de SERVICIO URBANO?",
        "options": [
            "Servicio prestado dentro del término municipal de Algeciras",
            "Servicio prestado entre dos términos municipales colindantes",
            "Servicio prestado dentro de una misma provincia",
        ],
        "answer": "Servicio prestado dentro del término municipal de Algeciras",
    },
    {
        "text": "A efectos de las Ordenanzas, ¿cuál sería la definición correcta de SERVICIO INTERURBANO?",
        "options": [
            "Servicio que se realiza en el ámbito territorial metropolitano",
            "Servicio prestado dentro de un mismo término municipal",
            "Servicio que excede del ámbito municipal",
        ],
        "answer": "Servicio que excede del ámbito municipal",
    },
]


def make_question(raw_question):
    questions = []
    for question in raw_questions:
        questions.append(
            Question(
                text=question["text"],
                options=json.dumps(question["options"]),
                answer=question["answer"],
            )
        )
    return questions


##dump and array into

questions = make_question(raw_questions)

session.add_all(questions)
session.commit()

# Close the session
session.close()
