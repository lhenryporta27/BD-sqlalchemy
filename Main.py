from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# 1. Base para los modelos
Base = declarative_base()


# 2. Modelo Estudiante
class Estudiante(Base):
    __tablename__ = 'estudiantes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    asignaturas = relationship("Asignatura", back_populates="estudiante")


# 3. Modelo Asignatura
class Asignatura(Base):
    __tablename__ = 'asignaturas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id'))
    estudiante = relationship("Estudiante", back_populates="asignaturas")


# 4. Crear base de datos SQLite
engine = create_engine('sqlite:///mi_bd.db')  # Se crea un archivo mi_bd.db
Base.metadata.create_all(engine)

# 5. Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# 6. Insertar datos
est1 = Estudiante(nombre="Luis")
asig1 = Asignatura(nombre="Matemática", estudiante=est1)
asig2 = Asignatura(nombre="Historia", estudiante=est1)

session.add(est1)
session.add_all([asig1, asig2])
session.commit()

# 7. Consultar datos
for estudiante in session.query(Estudiante).all():
    print(f"Estudiante: {estudiante.nombre}")
    for asignatura in estudiante.asignaturas:
        print(f"  Asignatura: {asignatura.nombre}")
