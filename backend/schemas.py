from pydantic import BaseModel
from fastapi import Form
from typing import Optional

class RegistroBase(BaseModel):
    documento: str = Form(...)
    nombre: str = Form(...)
    ciudad :str = Form(...)
    descripcion:str = Form(...)
    celular: str = Form(...)
    correo: str = Form(...)
    contraseña: str = Form(...)
    fecha_nacimiento: str = Form(...)
    Edad : int = Form(...)
    posicion : str = Form(...)
    imagen : Optional[str]=None
    

class LoginRequest(BaseModel):
    correo: str
    contraseña: str

    

class ContactForm(BaseModel):
    nombre: str
    queja_reclamo_quest: str
    email: str 
    celular: str
    comentario: str
    fecha_radicacion : str
    ciudad : str
    
class Contactousuers(BaseModel):
    nombre : str
    email : str 
    celular : str


class JugadorForm(BaseModel):
    nombre : str
    posicion : str
    email : str 
    celular : str 
    equipo : str
    Edad : str

class DatosTeams(BaseModel):
    nombreteam : str
    Descripcion : str
    numeropeople : int
    capitanteam : str
    requisitos_join : str
    location : str
    logoTeam : Optional[str]=None

class videos(BaseModel):
    id : int
    url : str


     
class Torneo(BaseModel):
    id_Torneo: int
    nombre: str
    fecha: str
    ubicacion: str
    numPartidos: int
    apuestaTorneo: float
    precioArbitrajeTorneo: float
    precioInscripcion: float
    reglasTorneo: str
    numeroparticipantes : int
    logoTeam : str
    Nombre_Creador_Torneo : str


class Partidos(BaseModel):
    id_Partido: int
    name : str                   
    hora: str
    apuesta: float
    ubicacionpartido: str
    logomatch  :   str
    Nombre_Creador_Partido : str
    class Config:
        from_attributes = True  # ✅ Convierte objetos SQLAlchemy a JSON                                                                                         
    