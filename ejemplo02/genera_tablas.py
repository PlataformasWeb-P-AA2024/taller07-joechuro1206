from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Importar cadena de conexión desde un archivo de configuración
from configuracion import cadena_base_datos

# Crear el motor de la base de datos
engine = create_engine(cadena_base_datos)

# Declarar una base para las clases ORM
Base = declarative_base()

# Definir la relación entre Club y Jugador (One-to-Many)
class Club(Base):
    __tablename__ = 'clubes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    deporte = Column(String(100))
    fundacion = Column(Integer, nullable=False)
    # Establecer la relación inversa con la clase Jugador
    jugadores = relationship("Jugador", back_populates="club")

    def __repr__(self):
        return f"Club: nombre={self.nombre} deporte={self.deporte} fundación={self.fundacion}"

class Jugador(Base):
    __tablename__ = 'jugadores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    dorsal = Column(Integer)
    posicion = Column(String(100))
    # Clave foránea para establecer la relación con Club
    club_id = Column(Integer, ForeignKey('clubes.id'))
    # Establecer la relación con Club
    club = relationship("Club", back_populates="jugadores")

    def __repr__(self):
        return f"Jugador: {self.nombre} - dorsal:{self.dorsal} - posición: {self.posicion}"

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)
