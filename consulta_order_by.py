from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion
from configuracion import base

engine = create_engine(base)
Session = sessionmaker(bind=engine)
session = Session()

# Ordenar investigadores por apellido ascendente
investigadores_asc = session.query(Investigador).order_by(Investigador.apellido.asc()).all()
print("Investigadores ordenados por apellido (ascendente):")
for investigador in investigadores_asc:
    print(investigador)