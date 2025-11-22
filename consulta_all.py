from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion
from configuracion import base  

engine = create_engine(base)
Session = sessionmaker(bind=engine)
session = Session() 

instituciones = session.query(Institucion).all()
print("Instituciones:")
for institucion in instituciones:
    print(institucion) 

departamentos = session.query(Departamento).all()
print("\nDepartamentos:")
for departamento in departamentos:
    print(departamento) 

investigadores = session.query(Investigador).all()  
print("\nInvestigadores:")
for investigador in investigadores:
    print(investigador) 

publicaciones = session.query(Publicacion).all()
print("\nPublicaciones:")
for publicacion in publicaciones:
    print(publicacion)  