from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Importar cadena de conexión desde un archivo de configuración
from configuracion import cadena_base_datos

# Crear el motor de la base de datos
engine = create_engine(cadena_base_datos)

# Declarar una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Importar las clases después de crear el motor y la sesión
from genera_tablas import Club, Jugador


# Crear el motor de la base de datos
engine = create_engine(cadena_base_datos)

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Crear objetos Club a partir de datos de un archivo
clubs = {}
with open('../ejemplo02/data/datos_clubs.txt', 'r', encoding='utf-8') as file:
    for line in file:
        nombre, deporte, fundacion = line.strip().split(';')
        fundacion = int(fundacion)
        club = Club(nombre=nombre, deporte=deporte, fundacion=fundacion)
        session.add(club)
        clubs[nombre] = club

# Leer datos de jugadores desde un archivo y relacionarlos con los clubes
with open('../ejemplo02/data/datos_jugadores.txt', 'r', encoding='utf-8') as file:
    for line in file:
        nombre_club, posicion, dorsal, nombre = line.strip().split(';')
        dorsal = int(dorsal)
        club = clubs.get(nombre_club)
        if club:
            # Crear el jugador y asignar el club utilizando la relación
            jugador = Jugador(nombre=nombre, dorsal=dorsal, posicion=posicion, club=club)
            session.add(jugador)

# Confirmar los cambios en la base de datos
session.commit()
