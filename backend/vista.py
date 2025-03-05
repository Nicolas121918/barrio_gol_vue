from fastapi import FastAPI,UploadFile,File ,Form , Depends, HTTPException, Query
from sqlalchemy.orm import Session
import bcrypt
from conexion import engine, get_db
from modelo import Base, Registro, Contacto,Jugador,Contacto_usuarios,Equipos,UserVideos,Torneos,partidos 
from schemas import RegistroBase as clie,LoginRequest
from schemas import ContactForm
from schemas import Contactousuers
from schemas import JugadorForm
from schemas import DatosTeams
from schemas import videos
from schemas import Torneo,Partidos
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi.staticfiles import StaticFiles
from fastapi import HTTPException


app = FastAPI()
app.mount("/micarpeta", StaticFiles(directory="micarpeta"), name="micarpeta")
app.mount("/logosteams", StaticFiles(directory="logosteams"), name="logosteams")
app.mount("/videos", StaticFiles(directory="videos"), name="videos")
app.mount("/logosteams", StaticFiles(directory="logosteams"), name="logosteams")
app.mount("/logostorneos", StaticFiles(directory="logostorneos"), name="logostorneos")
app.mount("/logospartidos", StaticFiles(directory="logospartidos"), name="logospartidos")



## permisos endpoints
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

Base.metadata.create_all(bind=engine)



## Endpoint Para Login
@app.post("/iniciar")
async def iniciar_sesion(login: LoginRequest, db: Session = Depends(get_db)):
    cliente = db.query(Registro).filter(Registro.correo == login.correo).first()
    
    if not cliente:     
        raise HTTPException(status_code=400, detail="Usuario no existe")
    
    if not bcrypt.checkpw(login.contraseña.encode('utf-8'), cliente.contraseña.encode('utf-8')):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    
    return {
        "id": cliente.documento,
        "nombreUsuario": cliente.nombre,
        "correo": cliente.correo,
        "ciudad": cliente.ciudad,
        "descripcion": cliente.descripcion,
        "fechaNacimiento": cliente.fecha_nacimiento,
        "imagen" : cliente.imagen,
        "celular" : cliente.celular,
        "Edad" : cliente.Edad,
        "posicion" : cliente.posicion,
    }

## Endpoint Para Registrar usuarios
@app.post("/insertarc", response_model=clie)
async def registrar_cliente(
    documento: int = Form(...),
    fecha_nacimiento : str = Form(...),
    nombre: str = Form(...),
    ciudad : str = Form(...),
    descripcion : str = Form(...),
    correo: str = Form(...),
    contraseña: str = Form(...),
    file: UploadFile = File(None),
    celular : str = Form(...),
    Edad : int = Form(...),
    posicion : str = Form(...),
    db: Session = Depends(get_db)
):
    cliente_existente = db.query(Registro).filter(Registro.correo == correo).first()
    documento_existente = db.query(Registro).filter(Registro.documento == documento).first()

    if cliente_existente:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")
    if documento_existente:
        raise HTTPException(status_code=400, detail="El documento ya está registrado")
    if file and file.content_type not in ["image/jpeg", "image/png", "image/gif", "image/bmp", "image/svg+xml", "image/webp"]:
        raise HTTPException(status_code=400, detail="Formato de archivo no soportado")
    
    if file:
        file_location = f"micarpeta/{file.filename}"
        os.makedirs("micarpeta", exist_ok=True)
        with open(file_location, "wb") as buffer:
            buffer.write(await file.read())
        ruta_Imagen = f"micarpeta/{file.filename}"

    encriptacion = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())

    nuevo_cliente = Registro(
        descripcion=descripcion,
        documento=documento,
        celular=celular,
        fecha_nacimiento=fecha_nacimiento,
        nombre=nombre,
        correo=correo,
        ciudad=ciudad,
        Edad=Edad,
        posicion=posicion,
        contraseña=encriptacion.decode('utf-8'),
        imagen=ruta_Imagen if file else None
    )
    # Crear el registro en la tabla de datos de contacto del usuario
    datos_contacto_usuario = Contacto_usuarios(
        nombre=nombre,
        email=correo,
        celular=celular,
        usuario_documento=documento  # Relacionamos con el usuario creado
    )
    
    db.add(nuevo_cliente)
    db.add(datos_contacto_usuario)
    db.commit()
    db.refresh(nuevo_cliente)

    return nuevo_cliente







#endpoint para ver los videos
@app.get("/listarvideos", response_model=list[videos])  
async def listar_videos(db: Session = Depends(get_db)):
    lista_videos = db.query(UserVideos).all()
    if not lista_videos:
        raise HTTPException(status_code=404, detail="No Videos Todavia")
    return lista_videos



## Endpoint para lista los equipos
@app.get("/listarteams", response_model=list[DatosTeams])
async def listar_clientes(db: Session=Depends(get_db)):
    lista_Equipos=db.query(Equipos).all()
    if not lista_Equipos:
        raise HTTPException(status_code=404, detail="No hay Equipos Todavia")
    return lista_Equipos



## Endpoint Para Crear los Equipos 
@app.post("/Teams")
async def registrar_cliente(
    nombreteam: str = Form(...),
    Descripcion : str = Form(...),
    numeropeople : int = Form(...),
    capitanteam: str = Form(...),
    requisitos_join : str = Form(...),
    location : str = Form(...),
    logoteam: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    file_location = f"logosteams/{logoteam.filename}"
    os.makedirs("logosteams", exist_ok=True)
    with open(file_location, "wb") as buffer:
        buffer.write(await logoteam.read())

    ruta_Imagen = f"logosteams/{logoteam.filename}"
     # Buscar al capitán en la base de datos por su nombre
    capitan = db.query(Registro).filter(Registro.nombre == capitanteam).first()

    if not capitan:
        raise HTTPException(status_code=404, detail="Capitán no encontrado en la base de datos")



    nuevo_Team = Equipos(
        nombreteam=nombreteam,
        Descripcion = Descripcion,
        numeropeople =numeropeople,
        capitanteam=capitanteam,
        requisitos_join=requisitos_join,
        location=location,
        logoTeam=ruta_Imagen,
        capitan_documento=capitan.documento,  # Asociar el documento del capitán
    )

    db.add(nuevo_Team)
    db.commit()
    db.refresh(nuevo_Team)
    return nuevo_Team



## Endpoint Para Enviar el Formulario De contacto
@app.post("/contacto/")
async def crear_contacto(form_data: ContactForm, db: Session = Depends(get_db)):

    nuevo_contacto = Contacto(
        nombre=form_data.nombre,
        queja_reclamo_quest=form_data.queja_reclamo_quest,
        email=form_data.email,
        celular=form_data.celular,
        comentario=form_data.comentario,
        fecha_radicacion = form_data.fecha_radicacion,
        ciudad = form_data.ciudad
    )


    db.add(nuevo_contacto)
    db.commit()
    db.refresh(nuevo_contacto)  
    
    return {"message": "Formulario enviado correctamente", "data": nuevo_contacto}





## Endpoint Para Crear la tabla de datos basicos apartir de las pqrs del usuario
@app.post("/contactos/")
async def crear_contacto(form_data: Contactousuers, db: Session = Depends(get_db)):

    nuevo_contacto = Contacto_usuarios(
        nombre=form_data.nombre,
        email=form_data.email,
        celular=form_data.celular,
    )
  
    db.add(nuevo_contacto)
    db.commit()
    db.refresh(nuevo_contacto) 
    
    return {"message": "Formulario enviado correctamente", "data": nuevo_contacto}


@app.post("/jugadores/")
async def crear_jugador(form_data: JugadorForm, db: Session = Depends(get_db)):
    nuevo_jugador = Jugador(
        nombre=form_data.nombre,
        Edad=form_data.Edad,
        posicion=form_data.posicion,
        email=form_data.email,
        celular=form_data.celular,
        equipo=form_data.equipo,
    )
    db.add(nuevo_jugador)
    db.commit()
    db.refresh(nuevo_jugador)
    
    return {"message": "Formulario Enviado correctamente En pocas horas Recibira Notificaciones de su Solicitud", "data": nuevo_jugador}


@app.get("/api/usuario/{user_id}", response_model=clie) 
def obtener_usuario(user_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Registro).filter(Registro.documento == user_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


from typing import List
## endpoint para listar nombre de  equipos
@app.get("/equipo/lista", response_model=List[str])
async def listar_equipos(db: Session = Depends(get_db)):
    lista_Equipos = db.query(Equipos.nombreteam).all() 
    if not lista_Equipos:
        raise HTTPException(status_code=404, detail="No hay Equipos Todavia")
    return [equipo.nombreteam for equipo in lista_Equipos]  




@app.put("/usuario/actualizar-foto")
async def actualizar_foto_perfil(
    correo: str,  # El correo se enviará en el cuerpo de la solicitud
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Busca el usuario por correo
    usuario = db.query(Registro).filter(Registro.correo == correo).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    # Verifica el formato de archivo
    if file.content_type not in ["image/jpeg", "image/png", "image/gif", "image/bmp", "image/svg+xml", "image/webp"]:
        raise HTTPException(status_code=400, detail="Formato de archivo no soportado")
    # Guarda el archivo
    file_location = f"micarpeta/{file.filename}"
    os.makedirs("micarpeta", exist_ok=True)
    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())

    # Actualiza la foto de perfil
    usuario.imagen = file_location
    db.commit()
    db.refresh(usuario)
    return {"message": "Foto de perfil actualizada", "ruta": file_location}


@app.put("/usuario/actualizar-nombre")
async def actualizar_nombre(
    correo: str = Query(...),
    nombre: str = Form(...),  # Recibimos el nombre como parámetro en el cuerpo del formulario
    db: Session = Depends(get_db)
):
    # Buscar el usuario por correo
    usuario = db.query(Registro).filter(Registro.correo == correo).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Actualizar el nombre del usuario
    usuario.nombre = nombre
    db.commit()
    db.refresh(usuario)

    return {"message": "Nombre actualizado", "nombre": usuario.nombre}


## Endpoint Para Actualizar la ciudad sin ID en la URL
@app.put("/usuario/actualizar-ciudad")
async def actualizar_ciudad(
    correo: str = Query(...),
    ciudad: str = Form(...),
    db: Session = Depends(get_db)
):
    # Busca el usuario por correo
    usuario = db.query(Registro).filter(Registro.correo == correo).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Actualiza la ciudad
    usuario.ciudad = ciudad
    db.commit()
    db.refresh(usuario)

    return {"message": "Ciudad actualizada", "ciudad": usuario.ciudad}


## Endpoint Para Actualizar la descripción sin ID en la URL
@app.put("/usuario/actualizar-descripcion")
async def actualizar_descripcion(
    correo: str = Query(...),
    descripcion: str = Form(...),
    db: Session = Depends(get_db)
):
    # Busca el usuario por correo
    usuario = db.query(Registro).filter(Registro.correo == correo).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Actualiza la descripción
    usuario.descripcion = descripcion
    db.commit()
    db.refresh(usuario)
    return {"message": "Descripción actualizada", "descripcion": usuario.descripcion}



# Endpoint para crear torneos
@app.post("/crearTorneo")
async def crear_evento(
    correo_usuario : str = Form(...),
    nombre: str = Form(...),
    fecha: str = Form(...),
    ubicacion: str = Form(...),
    numPartidos:int = Form(...),  
    apuestaTorneo: float = Form(...),  
    precioArbitrajeTorneo: float = Form(...),
    precioInscripcion: float = Form(...), 
    reglasTorneo: str = Form(...),
    numeroparticipantes : int = Form(...),
    logoTeam: UploadFile = File(...),
    db: Session = Depends(get_db)
):
     # Buscar al usuario en la base de datos por su email
    usuario = db.query(Registro).filter(Registro.correo == correo_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    


    file_location = f"logostorneos/{logoTeam.filename}"
    os.makedirs("logostorneos", exist_ok=True)
    with open(file_location, "wb") as buffer:
        buffer.write(await logoTeam.read())

    ruta_Imagen = f"logostorneos/{logoTeam.filename}"

    # Crear una instancia de Torneos con los datos recibidos
    nuevo_evento = Torneos(
        nombre=nombre,
        fecha=fecha,
        ubicacion=ubicacion,
        numPartidos=numPartidos,
        apuestaTorneo=apuestaTorneo,
        precioArbitrajeTorneo=precioArbitrajeTorneo,
        precioInscripcion=precioInscripcion,
        reglasTorneo=reglasTorneo,
        numeroparticipantes=numeroparticipantes,
        Documento_Creador_Torneo = usuario.documento,
        Nombre_Creador_Torneo = usuario.nombre,
        logoTeam=ruta_Imagen if logoTeam else None
    )

    # Agregar el nuevo evento a la base de datos
    db.add(nuevo_evento)
    db.commit()

    # Devolver el evento creado como respuesta
    return nuevo_evento






# Endpoint para crear Partidos
@app.post("/crearPartidos")
async def crear_partidos(
    correo_usuario : str = Form(...),
    hora: str = Form(...),
    name: str = Form(...),
    apuesta: float = Form(...),
    ubicacionpartido: str = Form(...),
    logomatch: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Buscar al usuario en la base de datos por su email
    usuario = db.query(Registro).filter(Registro.correo == correo_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    file_location = f"logospartidos/{logomatch.filename}"
    os.makedirs("logospartidos", exist_ok=True)
    with open(file_location, "wb") as buffer:
        buffer.write(await logomatch.read())

    ruta_Imagen = f"logospartidos/{logomatch.filename}"

    # Crear una instancia de Torneos con los datos recibidos
    nuevo_partido = partidos(
        hora=hora,
        name=name,
        apuesta=apuesta,
        ubicacionpartido=ubicacionpartido,
        Documento_Creador_P = usuario.documento,
        Nombre_Creador_Partido = usuario.nombre,
        logomatch=ruta_Imagen if logomatch else None
    )

    # Agregar el nuevo evento a la base de datos
    db.add(nuevo_partido)
    db.commit()
    db.refresh(nuevo_partido)








## Endpoint Para Subir Video
@app.post("/subirvideo", response_model=dict)
async def subir_video(
    correo: str = Form(...),  
    video: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    # Verificar si el formato del video es válido
    if video.content_type not in ["video/mp3", "video/mp4", "video/mkv", "video/avi", "video/mov", "video/webm"]:
        raise HTTPException(status_code=400, detail="Formato de video no soportado")

    # Buscar al usuario en la base de datos por su email
    usuario = db.query(Registro).filter(Registro.correo == correo).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Guardar el video en la carpeta
    video_location = f"videos/{video.filename}"
    os.makedirs("videos", exist_ok=True)
    with open(video_location, "wb") as buffer:
        buffer.write(await video.read())

    # Guardar la ruta del video en la base de datos
    ruta_video = f"videos/{video.filename}"
    nuevovideo2 = UserVideos(
        url=ruta_video,
        usuario_documento=usuario.documento  # Relacionamos el video con el usuario
    )

    db.add(nuevovideo2)
    db.commit()
    db.refresh(nuevovideo2)

    return {"mensaje": "Video subido correctamente", "ruta": ruta_video}






## Endpoint para lista los Torneos
@app.get("/listartorneos", response_model=List[Torneo])
async def listar_clientes(db: Session=Depends(get_db)):
    lista_Equipos=db.query(Torneos).all()
    if not lista_Equipos:
        raise HTTPException(status_code=404, detail="No hay Equipos Todavia")
    return lista_Equipos




@app.get("/listarpartidos", response_model=List[Partidos])  # ✅ Usa el modelo Pydantic
async def listar_partidos(db: Session = Depends(get_db)):
    listar_partidos = db.query(partidos).all()
    if not listar_partidos:
        raise HTTPException(status_code=404, detail="No hay partidos todavía")

    return listar_partidos  # ✅ FastAPI convierte los objetos SQLAlchemy en JSON




@app.get('/verificar-equipo/{id_usuario}')
def verificar_equipo(id_usuario: int, db: Session = Depends(get_db)):
    equipo = db.query(Equipos).filter(Equipos.id_usuario == id_usuario).first()
    if equipo:
        return {"asociado": True, "Id_team": equipo.Id_team, "nombreteam": equipo.nombreteam}
    return {"asociado": False}




# Endpoint GET para obtener todos los usuarios
@app.get("/usuarios", response_model=list[clie])
async def obtener_usuarios(db: Session = Depends(get_db)):
    
    # Consultar todos los registros de usuarios en la base de datos
    usuarios = db.query(Registro).all()

    # Si no hay usuarios registrados, lanzar un error 404
    if not usuarios:
        raise HTTPException(status_code=404, detail="No se encontraron usuarios")

    # Devolver los usuarios encontrados
    return usuarios


    
