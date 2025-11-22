from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion
from configuracion import base

engine = create_engine(base)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta las publicaciones de tipo 'Tesis' publicadas por UTPL

publicaciones = session.query(Publicacion).filter(
    Publicacion.tipo_publicacion == 'Tesis').filter(
    Publicacion.investigador.has(Investigador.departamento.has(Departamento.institucion.has(Institucion.nombre=='UTPL')))
).all() 

print("Publicaciones de tipo 'Tesis' publicadas por UTPL:")
for publicacion in publicaciones:
    print(publicacion)  
session.close()