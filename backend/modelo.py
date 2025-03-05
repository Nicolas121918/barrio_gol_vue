from sqlalchemy import String, Integer, Column, ForeignKey, Float
from sqlalchemy.orm import relationship
from conexion import Base  

# Tabla de Usuarios
class Registro(Base):
    __tablename__ = 'usuarios'
    documento = Column(String(50), primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    ciudad = Column(String(50), nullable=False)
    descripcion = Column(String(160), nullable=False)
    celular = Column(String(50), nullable=False)
    correo = Column(String(50), nullable=False)
    contraseña = Column(String(100), nullable=False)
    fecha_nacimiento = Column(String(50), nullable=False)
    imagen = Column(String(255), nullable=True)
    Edad = Column(Integer, nullable=False)
    posicion = Column(String(50), nullable=False)

    # Relaciones
    # Un usuario puede hacer muchas solicitudes a equipos
    solicitudes = relationship("Jugador", back_populates="usuario")
    # Un usuario tiene un solo equipo
    equipo = relationship("Equipos", back_populates="capitan", uselist=False)
    # Un usuario puede subir muchos videos
    videos = relationship("UserVideos", back_populates="usuario")
    # Un usuario puede tener muchos datos de contacto
    contacto = relationship("Contacto_usuarios", back_populates="usuario")
    # Un usuario puede participar en muchos torneos pero sólo en uno
    torneo = relationship("Torneos", back_populates="participantes")


    ## Conexion de registro a partidos
    partido = relationship("partidos", back_populates="creador")
    #conexion de la clase registro a torneos
    Torneos_create= relationship("Torneos",back_populates="creadormatch")


# Tabla de Contacto de Usuario
class Contacto_usuarios(Base):
    __tablename__ = 'datos_para_contactar_users' 
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    celular = Column(String(50), nullable=False)
    # Relación con Usuario
    usuario_documento = Column(String(50), ForeignKey('usuarios.documento'))
    #relacion bidireccional hace una relacion inversa
    usuario = relationship("Registro", back_populates="contacto")


# Tabla de PQRS (Quejas, Reclamos, Solicitudes)
class Contacto(Base):
    __tablename__ = 'PQRS_Usuarios'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    queja_reclamo_quest = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    celular = Column(String(50), nullable=False)
    comentario = Column(String(150), nullable=False)
    fecha_radicacion = Column(String(50), nullable=False)
    ciudad = Column(String(50), nullable=False)

# Tabla de Solicitudes (Jugador en un equipo)
class Jugador(Base):
    __tablename__ = 'solicitud_join_players'  
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    posicion = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    celular = Column(String(15), nullable=False)
    equipo = Column(String(50), nullable=False)
    Edad = Column(String(10), nullable=False)
    # Relación con Usuario
    usuario_documento = Column(String(50), ForeignKey('usuarios.documento'))
    usuario = relationship("Registro", back_populates="solicitudes")


# Tabla de Videos de Usuario
class UserVideos(Base):
    __tablename__ = "uservideos"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(250), nullable=False)
    # Relación con Usuario
    usuario_documento = Column(String(50), ForeignKey('usuarios.documento'))
    usuario = relationship("Registro", back_populates="videos")

# Tabla de Equipos
class Equipos(Base):
     __tablename__ = 'Equipos_de_barrio_gol'
     Id_team = Column(Integer, primary_key=True, index=True)
     nombreteam = Column(String(50), nullable=False)
     Descripcion = Column(String(100), nullable=False)
     numeropeople = Column(Integer, nullable=False)
     capitanteam = Column(String(100), nullable=False)
     requisitos_join = Column(String(100), nullable=False)
     location = Column(String(150), nullable=False)
     logoTeam = Column(String(255), nullable=False)
     # Relación con el usuario que es el capitán del equipo
     capitan_documento = Column(String(50), ForeignKey('usuarios.documento'))
     capitan = relationship("Registro", back_populates="equipo")

# Tabla de Torneos
class Torneos(Base):
    __tablename__ = 'Torneos_Barrio_Gol'
    id_Torneo = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    fecha = Column(String(50), nullable=False)
    ubicacion = Column(String(150), nullable=False)
    numPartidos = Column(Integer, nullable=False)
    apuestaTorneo = Column(Float, nullable=False)  
    precioArbitrajeTorneo = Column(Float, nullable=False)
    precioInscripcion = Column(Float, nullable=False)
    reglasTorneo = Column(String(255), nullable=False)
    numeroparticipantes = Column(Integer, nullable=False)
    logoTeam = Column(String(255), nullable=False)
    # Relación con los participantes (usuarios)
    Documento_Creador_Torneo = Column(String(50), ForeignKey('usuarios.documento'))
    Nombre_Creador_Torneo = Column(String(255),nullable=False)
    
    participantes = relationship("Registro", back_populates="torneo")
    #conexion de torneos a registro
    creadormatch = relationship("Registro",back_populates="Torneos_create")


# Tabla de Partidos
class partidos(Base):
    __tablename__ = 'Partidos_Barrio_Gol'
    id_Partido = Column(Integer, primary_key=True, index=True)
    name = Column(String(100),nullable=False)
    hora = Column(String(100), nullable=False)
    apuesta = Column(Float, nullable=False)
    ubicacionpartido = Column(String(150), nullable=False)
    logomatch = Column(String(255), nullable=True)
    Documento_Creador_P= Column(String(50), ForeignKey('usuarios.documento'))
    ##conexion de partidos a registro
    creador = relationship("Registro", back_populates="partido")
    Nombre_Creador_Partido = Column(String(50),nullable=False)

