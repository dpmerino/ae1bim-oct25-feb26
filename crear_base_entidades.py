from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship

# creacion de la base de datos y el motor importando de configuracion.py
from configuracion import base
engine = create_engine(base)
Base = declarative_base()

# Definicion de las entidades
class Institucion(Base):
    __tablename__ = 'instituciones'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    ciudad = Column(String(), nullable=False)
    pais = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Institucion(nombre='{self.nombre}', ciudad='{self.ciudad}', pais='{self.pais}')>"
    
class Departamento(Base):
    __tablename__ = 'departamentos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(10), nullable=False)
    institucion_id = Column(Integer, ForeignKey('instituciones.id'))
    institucion = relationship("Institucion", back_populates="departamentos")

    def __repr__(self):
        return f"<Departamento(nombre='{self.nombre}', codigo='{self.codigo}')>"
    
Institucion.departamentos = relationship("Departamento", back_populates="institucion")
    
class Investigador(Base):
    __tablename__ = 'investigadores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    area_investigacion = Column(String(200), nullable=False)
    departamento_id = Column(Integer, ForeignKey('departamentos.id'))
    departamento = relationship("Departamento", back_populates="investigadores")

    def __repr__(self):
        return f"<Investigador(nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}', area_investigacion='{self.area_investigacion}')>"
    
Departamento.investigadores = relationship("Investigador", back_populates="departamento")
class Publicacion(Base):
    __tablename__ = 'publicaciones'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(200), nullable=False)
    fecha_publicacion = Column(String(20), nullable=False)
    doi = Column(String(100), nullable=False)
    tipo_publicacion = Column(String(50), nullable=False)
    investigador_id = Column(Integer, ForeignKey('investigadores.id'))
    investigador = relationship("Investigador", back_populates="publicaciones")

    def __repr__(self):
        return f"<Publicacion(titulo='{self.titulo}', fecha_publicacion='{self.fecha_publicacion}', doi='{self.doi}', tipo_publicacion='{self.tipo_publicacion}')>"
    
Investigador.publicaciones = relationship("Publicacion", back_populates="investigador")
# Crear las tablas en la base de datos
Base.metadata.create_all(engine)