from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import Institucion, Departamento, Investigador, Publicacion   
from configuracion import base 

engine = create_engine(base)
Session = sessionmaker(bind=engine)
session = Session()

# Crear y agregar instituciones
inst1 = Institucion(nombre='UTPL', ciudad='Loja', pais='Ecuador')
inst2 = Institucion(nombre='ESPOL', ciudad='Guayaquil', pais='Ecuador')

# Crear y agregar departamentos
dept1 = Departamento(nombre='Ciencias de la Computación', codigo='CC101', institucion_id=1)
dept2 = Departamento(nombre='Ingeniería en Sistemas', codigo='IS202', institucion_id=2)
dept3 = Departamento(nombre='Matemáticas', codigo='MA303', institucion_id=1)
dept4 = Departamento(nombre='Física', codigo='FI404', institucion_id=2)

# Crear y agregar investigadores
inv1 = Investigador(nombre='Carlos', apellido='Juca', email='carlos.juca@utpl.edu.ec', area_investigacion='Inteligencia Artificial', departamento_id=1)
inv2 = Investigador(nombre='Luis', apellido='Torval', email='luis.torval@espol.edu.ec', area_investigacion='Sistemas Distribuidos', departamento_id=2)    
inv3 = Investigador(nombre='Diego', apellido='Rodríguez', email='diego.rodriguez@utpl.edu.ec', area_investigacion='Matemáticas Aplicadas', departamento_id=3)
inv4 = Investigador(nombre='Anahi', apellido='López', email='anahi.lopez@espol.edu.ec', area_investigacion='Física Teórica', departamento_id=4)
inv5 = Investigador(nombre='Paula', apellido='Martínez', email='paula.martinez@utpl.edu.ec', area_investigacion='Física Aplicada', departamento_id=4)
inv6 = Investigador(nombre='Jorge', apellido='González', email='jorge.gonzalez@utpl.edu.ec', area_investigacion='Redes', departamento_id=2)

# Crear y agregar publicaciones
pub1 = Publicacion(titulo='Avances en IA', fecha_publicacion='2022-05-10', doi='10.1000/182', tipo_publicacion='Artículo', investigador_id=1)
pub2 = Publicacion(titulo='Sistemas Distribuidos Modernos', fecha_publicacion='2021-11-15', doi='10.1000/183', tipo_publicacion='Conferencia', investigador_id=2)
pub3 = Publicacion(titulo='Modelos Matemáticos en la Ciencia', fecha_publicacion='2023-01-20', doi='10.1000/184', tipo_publicacion='Tesis', investigador_id=3)
pub4 = Publicacion(titulo='Nuevas Perspectivas en Física', fecha_publicacion='2022-08-30', doi='10.1000/185', tipo_publicacion='Tesis', investigador_id=4)

session.add_all([inst1, inst2, dept1, dept2, dept3, dept4, inv1, inv2, inv3, inv4, inv5, inv6, pub1, pub2, pub3, pub4])  
session.commit()
session.close() 
print("Base de datos poblada")