from sqlalchemy import String, Integer, Column, ForeignKey,Float
from sqlalchemy.orm import relationship
from conexion import Base  

class Registro(Base):
    __tablename__ = 'usuarios'
    documento = Column(String(50), primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    ciudad = Column(String(50),nullable=False)
    descripcion=Column(String(160),nullable=False)
    celular = Column(String(50), nullable=False)
    correo = Column(String(50), nullable=False)
    contraseña = Column(String(100), nullable=False)
    fecha_nacimiento = Column(String(50), nullable=False)
    imagen = Column(String(255),nullable=True)
    Edad = Column(String(10), nullable=True)
    posicion = Column(String(50),nullable=False)
    
class Contacto(Base):
    __tablename__ = 'PQRS_Usuarios' 
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    queja_reclamo_quest = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    celular = Column(String(50), nullable=False)
    comentario = Column(String(150), nullable=False)
    fecha_radicacion = Column(String(50),nullable=False)
    ciudad = Column(String(50),nullable=False)

class Contacto_usuarios(Base):
    __tablename__ = 'contactos_Usuarios' 
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    celular = Column(String(50), nullable=False)


class Jugador(Base):
        __tablename__ = 'Solicitud_de_jugadores'  
        id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        nombre = Column(String(100), nullable=False)
        posicion = Column(String(50), nullable=False)
        email = Column(String(100), nullable=False)
        celular = Column(String(15), nullable=False)
        equipo = Column(String(50), nullable=False)
        Edad = Column(String(10), nullable=False)




class UserVideos(Base):
    __tablename__ = "uservideos"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(250),nullable=False)
    documento_usuario = Column(String(250),nullable=False)

class Equipos(Base):
     __tablename__ = 'Equipos_Barrio_Gol'
     Id_team = Column(Integer, primary_key=True, index=True)
     nombreteam = Column(String(50),nullable=False)
     Descripcion = Column(String(100),nullable=False)
     numeropeople = Column(Integer,nullable=False)
     capitanteam = Column(String(100),nullable=False)
     requisitos_join = Column(String(100),nullable=False)
     location = Column(String(150),nullable=False)
     logoTeam = Column(String(255),nullable=False)



class Torneos(Base):
    __tablename__ = 'Torneos'
    id_evento = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(50), nullable=False)
    nombre = Column(String(100), nullable=False)
    fecha = Column(String(50), nullable=False) 
    ubicacion = Column(String(150), nullable=False)
    numPartidos = Column(Integer, nullable=False)
    apuestaTorneo = Column(Float, nullable=False)  # Cambiar float por Float
    precioArbitrajeTorneo = Column(Float, nullable=False)  # Cambiar float por Float
    precioInscripcion = Column(Float, nullable=False)  # Cambiar float por Float
    reglasTorneo = Column(String(255), nullable=False)  
    numeroparticipantes = Column(Integer,nullable=False)
    logoTeam = Column(String(255),nullable=False)

