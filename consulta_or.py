from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion
from sqlalchemy import or_
from configuracion import base

engine = create_engine(base)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta con OR: investigadores que pertenecen a UTPL o al departamento de Física 
investigadores = session.query(Investigador).filter(or_(
    Investigador.departamento.has(Departamento.institucion.has(Institucion.nombre == 'UTPL')),
    Investigador.departamento.has(Departamento.nombre == 'Física')
)).all()    

print("Investigadores que pertenecen a UTPL o al departamento de Física:")
for investigador in investigadores:
    print(investigador)

session.close()