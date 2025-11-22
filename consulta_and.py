from operator import and_
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import base
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion

enfine = create_engine(base)
Session = sessionmaker(bind=enfine)
session = Session()

# Consulta con AND: investigadores de ESPOL cuyo apellido contiene la letra 'a'
investigadores = session.query(Investigador).filter(and_(Investigador.email.like('%@espol.edu.ec'), Investigador.apellido.like("%a%"))).all()

print("Investigadores de ESPOL con 'a' en el apellido:")
for investigador in investigadores:
    print(investigador) 