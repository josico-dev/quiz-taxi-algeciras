import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, engine
from models import Question

# Import the necessary models and database configuration

# Create the database tables
Base.metadata.create_all(bind=engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create sample users

raw_questions = [
    {
        "text": "¿Puede una persona física ser titular de más de una licencia de taxi?",
        "options": [
            "Sí",
            "Sí, siempre que sean licencias de distintos municipios",
            "No, sólo podrá ser titular de una licencia de taxi o autorizacion de transporte interurbano de vehículo de turismo",
        ],
        "answer": "No, sólo podrá ser titular de una licencia de taxi o autorizacion de transporte interurbano de vehículo de turismo",
        "tag": "ordenanzas",
    },
    {
        "text": "¿Corresponde a la Consejería de Transportes en materia de transportes la adjudicación de licencias de autotaxi mediante concurso?",
        "options": [
            "No, corresponde al Consejo Andaluz del Taxi",
            "Sí",
            "No, corresponden a los Ayuntamientos o entes que asuman sus funciones",
        ],
        "answer": "No, corresponden a los Ayuntamientos o entes que asuman sus funciones",
        "tag": "ordenanzas",
    },
    {
        "text": "A efectos de las Ordenanzas, ¿cuál sería la definición correcta de SERVICIO DE TAXI O AUTOTAXI?",
        "options": [
            "Servicio de transporte público discrecional de viajeros en automóviles de turismo con una capacidad máxima de diez plazas, prestados en régimen de actividad pública",
            "Servicio de transporte público discrecional de viajeros en automóviles de turismo con una capacidad máxima de nueve plazas, prestados en régimen de actividad privada",
            "Servicio de transporte privado discrecional de viajeros en automóviles de turismo con una capacidad máxima de nueve plazas, prestados en régimen de actividad pública",
        ],
        "answer": "Servicio de transporte público discrecional de viajeros en automóviles de turismo con una capacidad máxima de nueve plazas, prestados en régimen de actividad privada",
        "tag": "ordenanzas",
    },
    {
        "text": "A efectos de las Ordenanzas, ¿cuál sería la definición correcta de SERVICIO URBANO?",
        "options": [
            "Servicio prestado dentro del término municipal de Algeciras",
            "Servicio prestado entre dos términos municipales colindantes",
            "Servicio prestado dentro de una misma provincia",
        ],
        "answer": "Servicio prestado dentro del término municipal de Algeciras",
        "tag": "ordenanzas",
    },
    {
        "text": "A efectos de las Ordenanzas, ¿cuál sería la definición correcta de SERVICIO INTERURBANO?",
        "options": [
            "Servicio que se realiza en el ámbito territorial metropolitano",
            "Servicio prestado dentro de un mismo término municipal",
            "Servicio que excede del ámbito municipal",
        ],
        "answer": "Servicio que excede del ámbito municipal",
        "tag": "ordenanzas",
    },
    {
        "text": "A efectos de las ordenanzas, ¿cuál sería la definición correcta de licencia?",
        "options": [
            "Autorización municipal otorgada para la prestación del servicio privado no reglamentado.",
            "Autorización municipal otorgada para la prestación del servicio urbano de taxi como actividad privada reglamentada.",
            "Tarjeta otorgada para la prestación del servicio de taxi como actividad pública.",
        ],
        "answer": "Autorización municipal otorgada para la prestación del servicio urbano de taxi como actividad privada reglamentada.",
        "tag": "ordenanzas",
    },
    {
        "text": "A efectos de las ordenanzas, ¿cuál sería la definición correcta de autorización de transporte interurbano?",
        "options": [
            "Autorización administrativa otorgada por la Administración Autonómica competente, de conformidad con la normativa estatal de transportes terrestres, que habilita a su titular para la realización de servicios de taxi de ámbito interurbano.",
            "Autorización administrativa otorgada de conformidad con la normativa estatal para la prestación del servicio privado interurbano de taxi.",
            "Autorización administrativa otorgada de conformidad con la normativa estatal para la prestación del servicio público urbano.",
        ],
        "answer": "Autorización administrativa otorgada por la Administración Autonómica competente, de conformidad con la normativa estatal de transportes terrestres, que habilita a su titular para la realización de servicios de taxi de ámbito interurbano.",
        "tag": "ordenanzas",
    },
    {
        "text": "Según las ordenanzas, ¿cuál sería la definición correcta de titular?",
        "options": [
            "Persona autorizada como autónoma colaboradora.",
            "Única persona que puede conducir el taxi.",
            "Persona autorizada para la prestación de servicios de taxi.",
        ],
        "answer": "Persona autorizada para la prestación de servicios de taxi.",
        "tag": "ordenanzas",
    },
    {
        "text": "Según las ordenanzas, ¿cuál es la definición correcta de licencia como título habilitante?",
        "options": [
            "La licencia es el título jurídico que habilita a su titular para la prestación de los servicios que regula esta ordenanza.",
            "La licencia es el título jurídico que habilita a su titular para la prestación de los servicios que regula esta ordenanza, y además se expedirá solo a una persona jurídica.",
            "La licencia es el título jurídico que habilita a su titular para la prestación de los servicios que regula esta ordenanza, y se podrá arrendar, traspasar o ceder por cualquier título la explotación de la misma y el vehículo afecto...",
        ],
        "answer": "La licencia es el título jurídico que habilita a su titular para la prestación de los servicios que regula esta ordenanza.",
        "tag": "ordenanzas",
    },
    {
        "text": "¿Quién establece los requisitos exigibles a los conductores y conductoras para la obtención de licencias de autotaxi?",
        "options": [
            "Las ordenanzas regionales.",
            "Las ordenanzas comarcales.",
            "Las ordenanzas municipales.",
        ],
        "answer": "Las ordenanzas municipales.",
        "tag": "ordenanzas",
    },
    {
        "text": "Las ordenanzas municipales establecen las características e identificación de los vehículos.",
        "options": [
            "Falso",
            "Verdadero",
            "Verdadero, pero con el consentimiento del titular de la licencia.",
        ],
        "answer": "Verdadero",
        "tag": "ordenanzas",
    },
    {
        "text": "Las competencias municipales de ordenación de la actividad comprenden las actuaciones siguientes:",
        "options": [
            "Reglamentación de la actividad, de los vehículos y su equipamiento, de las relaciones de los prestadores con los usuarios del servicio, sus derechos y deberes y las tarifas urbanas, del régimen de las licencias, requisitos para la adjudicación y transmisión.",
            "Requisitos para ser conductor, de la oferta del taxi, del régimen de descansos, turnos para la prestación del servicio, especialmente para los vehículos adaptados para discapacitados, del régimen sancionador y extinción de la licencia, inspección, control y seguimiento respecto a las condiciones del servicio, incluido el visado de las licencias.",
            "Ambas son correctas.",
        ],
        "answer": "Ambas son correctas.",
        "tag": "ordenanzas",
    },
    {
        "text": "El titular de las licencias de taxi tendrá plena y exclusiva dedicación a la profesión.",
        "options": [
            "Sí.",
            "Sí, siempre y cuando no esté dado de alta en la seguridad social.",
            "No, salvo que figure en régimen general como asalariado de otra actividad.",
        ],
        "answer": "Sí.",
        "tag": "ordenanzas",
    },
    {
        "text": "Se define el coeficiente de licencia de taxi...",
        "options": [
            "El coeficiente de licencias de taxis en este municipio como el resultado de multiplicar por cien el cociente entre el número de licencias existentes y la población usuaria en su ámbito territorial.",
            "El coeficiente de licencias de taxis en este municipio como el resultado de multiplicar por mil el cociente entre el número de licencias existentes y la población usuaria en su ámbito territorial.",
            "El coeficiente de licencias de taxis en este municipio como el resultado de multiplicar por cien mil el cociente entre el número de licencias existentes y la población usuaria en su ámbito territorial.",
        ],
        "answer": "El coeficiente de licencias de taxis en este municipio como el resultado de multiplicar por mil el cociente entre el número de licencias existentes y la población usuaria en su ámbito territorial.",
        "tag": "ordenanzas",
    },
    {
        "text": "En los municipios en los que están implantados los servicios de taxi, ¿quién establece las condiciones de prestación del servicio?",
        "options": [
            "El titular de la licencia.",
            "El consejo andaluz del taxi.",
            "Las ordenanzas municipales.",
        ],
        "answer": "Las ordenanzas municipales.",
        "tag": "ordenanzas",
    },
    {
        "text": "La persona titular de la licencia puede arrendar, ceder o traspasar la explotación del título habilitante y el vehículo adscrito a la misma.",
        "options": [
            "Sí, siempre que el servicio se preste por personas contratadas a tal fin por el titular de la licencia.",
            "No, en ningún caso.",
        ],
        "answer": "No, en ningún caso.",
        "tag": "ordenanzas",
    },
    {
        "text": "Para la prestación de servicios de transporte urbano en autotaxi, ¿será necesaria la obtención de licencia expedida por el Ayuntamiento?",
        "options": ["Sí.", "No, solo autorización de transportes."],
        "answer": "Sí.",
        "tag": "ordenanzas",
    },
    {
        "text": "Para la prestación de servicio de transporte interurbano en autotaxi, ¿será necesaria la obtención de autorización expedida por el órgano correspondiente de la consejería de transportes?",
        "options": ["Sí.", "No."],
        "answer": "Sí.",
        "tag": "ordenanzas",
    },
    {
        "text": "Para la determinación del número de licencias, ¿cuáles de los siguientes aspectos deben tenerse en cuenta?",
        "options": [
            "Los niveles de oferta y demanda del servicio existentes.",
            "La evolución de las actividades comerciales, industriales, turísticas, económicas en general.",
            "Ambas son correctas.",
        ],
        "answer": "Ambas son correctas.",
        "tag": "ordenanzas",
    },
    {
        "text": "Las licencias de autotaxi serán transmisibles",
        "options": [
            "Por actos “inter vivos”.",
            "Por actos “mortis causa”.",
            "Ambas son correctas.",
        ],
        "answer": "Ambas son correctas.",
        "tag": "ordenanzas",
    },
    {
        "text": "En caso de transmisión “mortis causa”, ¿los herederos disponen de plazo desde el fallecimiento para determinar la persona titular?",
        "options": [
            "No, solo por 'inter vivos'.",
            "Sí, disponen de un plazo de treinta meses desde el fallecimiento para determinar la persona titular.",
        ],
        "answer": "Sí, disponen de un plazo de treinta meses desde el fallecimiento para determinar la persona titular.",
        "tag": "ordenanzas",
    },
    {
        "text": "La persona titular de la licencia que se proponga transmitirla “inter vivos”...",
        "options": [
            "Solicitará la autorización del Ayuntamiento señalando la persona a la que pretenda transmitir la licencia y el precio por el que se fija la operación para que así, en un plazo de 2 meses, el Ayuntamiento ejerza el derecho del tanteo.",
            "Solicitará la autorización de la Consejería de Transportes señalando la persona a la que pretenda transmitir la licencia y el precio por el que se fija la operación para que así, en un plazo de 2 meses, la Consejería de Transportes ejerza el derecho del tanteo.",
        ],
        "answer": "Solicitará la autorización del Ayuntamiento señalando la persona a la que pretenda transmitir la licencia y el precio por el que se fija la operación para que así, en un plazo de 2 meses, el Ayuntamiento ejerza el derecho del tanteo.",
        "tag": "ordenanzas",
    },
    {
        "text": "Se aplicará el derecho de tanteo por:",
        "options": ["'Inter vivos'.", "'Mortis causa'.", "Ambas son correctas."],
        "answer": "'Inter vivos'.",
        "tag": "ordenanzas",
    },
    {
        "text": "¿La nueva persona titular de la licencia puede iniciar el ejercicio de la actividad urbana hasta que se haya obtenido la autorización interurbana?",
        "options": [
            "No, deberá comunicar antes la transmisión de titularidad a la Consejería de Transportes y solicitar la autorización de transporte interurbano.",
            "Sí, el Ayuntamiento comunicará la transmisión de titularidad a la Consejería de Transportes y después solicitará la autorización de transporte interurbano.",
        ],
        "answer": "Sí, el Ayuntamiento comunicará la transmisión de titularidad a la Consejería de Transportes y después solicitará la autorización de transporte interurbano.",
        "tag": "ordenanzas",
    },
    {
        "text": "Las licencias de autotaxi se otorgarán por tiempo...",
        "options": [
            "Indefinido.",
            "Por tiempo determinado hasta cumplir la edad de jubilación.",
        ],
        "answer": "Indefinido.",
        "tag": "ordenanzas",
    },
    {
        "text": "La extinción de las licencias de autotaxi se extinguirá por:",
        "options": [
            "Renuncia, fallecimiento del titular.",
            "Caducidad, revocación y anulación del acto administrativo de su otorgamiento.",
            "Ambas son correctas.",
        ],
        "answer": "Ambas son correctas.",
        "tag": "ordenanzas",
    },
    {
        "text": "¿Constituye motivo de revocación la extinción de uno de los títulos habilitantes, tanto licencia municipal como autorización de transporte interurbano?",
        "options": ["Sí.", "No."],
        "answer": "Sí.",
        "tag": "ordenanzas",
    },
    {
        "text": "En el supuesto de accidente o avería, enfermedad o cualquier circunstancia que impida la continuidad en la prestación del servicio, ¿puede solicitar el titular la suspensión de la licencia?",
        "options": [
            "No, deberá contratar, en lugar de la suspensión, personas asalariadas o autónomas colaboradoras para la continuidad de la actividad.",
            "Sí, y el Ayuntamiento podrá autorizar la suspensión por un máximo de 24 meses y comunicará a la Consejería de Transportes la suspensión simultánea de la autorización de transportes.",
            "Sí, y el Ayuntamiento podrá autorizar la suspensión por un máximo de 5 años.",
        ],
        "answer": "Sí, y el Ayuntamiento podrá autorizar la suspensión por un máximo de 24 meses y comunicará a la Consejería de Transportes la suspensión simultánea de la autorización de transportes.",
        "tag": "ordenanzas",
    },
    {
        "text": "¿Cuál es el periodo máximo y mínimo que puede conceder el Ayuntamiento en caso de suspensión de las licencias por solicitud del titular?",
        "options": [
            "24 meses como máximo y 6 meses como mínimo.",
            "3 años como máximo y 3 meses como mínimo.",
            "5 años como máximo y 6 meses como mínimo.",
        ],
        "answer": "5 años como máximo y 6 meses como mínimo.",
        "tag": "ordenanzas",
    },
    {
        "text": "Verdadero o Falso:",
        "options": [
            "Procederá la declaración de caducidad por incumplimiento del deber de visado periódico de la licencia.",
            "Procederá la declaración de caducidad por no iniciación de la prestación del servicio o abandono del mismo por un plazo superior al establecido.",
            "Ambas son correctas.",
        ],
        "answer": "Ambas son correctas.",
        "tag": "ordenanzas",
    },
    {
        "text": "Registro de Licencias:",
        "options": [
            "Los municipios, o entes que ejerzan sus funciones en esta materia, podrán llevar un Registro de las licencias concedidas por orden, anotando las diferentes incidencias, vehículos afectos a las mismas, infracciones cometidas y sanciones impuestas y además comunicarán a la Consejería de Transportes sus incidencias cada seis meses.",
            "Los municipios, o entes que ejerzan sus funciones en esta materia, podrán llevar un Registro de las licencias concedidas por orden, anotando las diferentes incidencias, vehículos afectos a las mismas, infracciones cometidas y sanciones impuestas.",
            "Los municipios, o entes que ejerzan sus funciones en esta materia, podrán llevar un Registro de las licencias concedidas por orden, anotando las diferentes incidencias, vehículos afectos a las mismas, infracciones cometidas y sanciones impuestas y además comunicarán a la Consejería de Transportes sus incidencias cada doce meses.",
        ],
        "answer": "Los municipios, o entes que ejerzan sus funciones en esta materia, podrán llevar un Registro de las licencias concedidas por orden, anotando las diferentes incidencias, vehículos afectos a las mismas, infracciones cometidas y sanciones impuestas.",
        "tag": "ordenanzas",
    },
    {
        "text": "Las personas titulares de licencias de auto taxi deben iniciar el ejercicio de la actividad en un plazo máximo de:",
        "options": [
            "60 días hábiles siendo ampliado cuando exista causa justificadas, pero no podrá dejar de prestarlo por periodos iguales o superiores a 60 días consecutivos o sesenta días alternos, en el plazo de un año sin causa justificada, siendo justificados los descansos que rijan el Reglamento y Ordenanzas.",
            "50 días naturales siendo ampliado cuando exista causa justificadas, pero no podrá dejar de prestarlo por periodos iguales o superiores a 30 días consecutivos o sesenta días alternos, en el plazo de un año sín causa justificada siendo justificados los descansos que rijan el Reglamento y Ordenanzas.",
            "No tengo plazo para iniciar el ejercicio de la actividad hasta obtener el vehículo afecto a la misma.",
        ],
        "answer": "50 días naturales siendo ampliado cuando exista causa justificadas, pero no podrá dejar de prestarlo por periodos iguales o superiores a 30 días consecutivos o sesenta días alternos, en el plazo de un año sín causa justificada siendo justificados los descansos que rijan el Reglamento y Ordenanzas.",
        "tag": "ordenanzas",
    },
]


def make_question(raw_question):
    questions = []
    for question in raw_questions:
        for option in question["options"]:
            if option == question["answer"]:
                questions.append(
                    Question(
                        text=question["text"],
                        options=json.dumps(question["options"]),
                        answer=question["answer"],
                        tag=question["tag"],
                    )
                )
    return questions


##dump and array into

questions = make_question(raw_questions)

session.add_all(questions)
session.commit()

# Close the session
session.close()
