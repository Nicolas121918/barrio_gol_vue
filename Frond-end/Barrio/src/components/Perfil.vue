<template>
  <header>
    <headerapp></headerapp>
  </header>

  <div class="caja_perfil">
    <h1 id="datos">Datos De su Perfil</h1>
    <section class="fondo" v-if="isUserLoaded">
      <router-link class="actualizar_perfil" to="/actualizar_perfil">Actualizar Datos</router-link>
      <router-link class="link equipo" to="/equipos">
        <img class="clan" src="../assets/iconos header/clan.png" alt="" />
      </router-link>
      <div class="container_profile">
        <div class="card_profile">
          <div class="front">
            <div class="card-top">
              <p class="card-top-para">Barrio Gol</p>
            </div>
            <div class="circle-container">
              <img :src="getImagenUrl(url)" alt="Fondo de perfil" />
            </div>
            <p class="heading">
              Nombre: {{ nombre?.split(' ')[0] }} {{ nombre?.split(' ')[2] }}
            </p>
            <p class="follow">Ciudad: {{ ciudad }}</p>
            <p class="follow">Edad: {{ Edad }}</p>
            <p class="follow">Posicion: {{ posicion }}</p>
            <p class="follow">
              Email: {{ correo.slice(0, 5) + '******' + correo.slice(correo.indexOf('@')) }}
            </p>
          </div>

          <div class="back">
            <p class="heading_2">Descripcion: {{ descripcion }}</p>
            

          </div>
        </div>
      </div>
    </section>
  </div>


</template>

  <script setup>
  import Headerapp from './Headerapp.vue';
  import { ref, onMounted } from 'vue';
import { RouterLink } from 'vue-router';
  const url = ref('');
  const nombre = ref('');
  const ciudad = ref('');
  const correo = ref('');
  const descripcion = ref('');
  const fecha_nacimiento = ref('');
  const isUserLoaded = ref(false);
  const Edad = ref('');
  const posicion = ref('');
  const fecha = ref('');

  const getImagenUrl = (path) =>{
    return `http://127.0.0.1:8000/${path}`;
  }
  

  const loadProfileFromStorage = () => {
    const datosusuario = JSON.parse(localStorage.getItem('usuario'));
    if (datosusuario) {
      nombre.value = datosusuario.nombreUsuario || 'Sin nombre';
      correo.value = datosusuario.correo || 'Sin correo';
      ciudad.value = datosusuario.ciudad || 'Sin ciudad';
      descripcion.value = datosusuario.descripcion || 'Sin descripción';
      fecha_nacimiento.value = datosusuario.fechaNacimiento || 'Sin descripción';
      Edad.value = datosusuario.Edad || 'Sin Edad';
      posicion.value = datosusuario.posicion || ' Sin posicion';
      url.value = datosusuario.fileInput || 'Sin Foto de perfil'; 

      isUserLoaded.value = true; // Cambia el estado a true una vez cargado el perfil
    } else {
      console.error('No se encontró usuario en localStorage');
    }
  };


  onMounted(() => {
    loadProfileFromStorage();
    // Actualizar la fecha cada segundo
    const interval = setInterval(() => {
      fecha.value = new Date().toLocaleString();
    }, 1000);
    onMounted(() => {
      clearInterval(interval);
    });
  });


  </script>


<style scoped>
/* Quita Los estilos Predefinidos de las rutas color verde*/
a.router-link-active, a.router-link-exact-active {
    color: inherit;
    text-decoration: none;
    background-color: none;
  }
  

  .link {
    display: inline-block;
    margin: 0;
    padding: 0;
  }
  .link:hover {
  background: none;
}




.caja_perfil{
  display: flex;
  flex-direction: column;
  justify-content:center;
  margin-top: 40%;
  width: 400%;
  text-align: center;
  margin-left: -150%;
}



.circle-container {
width: 150px; 
height: 100px;
border-radius: 50%; 
overflow: hidden; 
display: flex;
justify-content: center; 
align-items: center; 
background-color: rgb(255, 251, 251);
}


.circle-container img {
width: 100%; 
height: 100%; 
object-fit: cover; 
}



.card_profile {
width: 50%;
height: auto;
margin-left: 24%;
background: rgb(0, 0, 0);
border-radius: 2rem;
transition: transform 1500ms;
transform-style: preserve-3d;

}


.card-top-para {
font-size: 20px;
font-weight: bold;
}

.container_profile:hover > .card_profile {
cursor: pointer;
transform: rotateX(180deg) rotateZ(-180deg);
}
.container_profile{
  display: flex;
  flex-direction:column;

}

.front,
.back {
height: 50%;
width: 100%;
border-radius: 2rem;
box-shadow: 0px 0px 10px 5px rgba(255, 255, 0, 0.7);
backface-visibility: hidden;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
gap:15px;
}

.back {
transform: rotateX(180deg) rotateZ(-180deg);
position: absolute;
top: 0%; 
}

.heading {
font-size: 15px;
font-weight: bold;
}
.heading_2 {
font-size: 20px;
font-weight: bold;
text-align: center;
width: auto;
}

.follow {
font-size: 15px;
font-weight: 500;
}

.icons {
display: flex;
flex-direction: row;
gap: 20px;
margin-top: 20px;

}


.texto-2 {
  margin: 10px 0; 
  color: white;
  text-shadow: 0 0 4px rgb(0, 0, 0);
  font-family: monospace;
  font-size: 20px;
}

.clan {
  height: 70px;
  width: 70px; /* Asegurar que sea un círculo */
  margin-top: 50%;
  background-color: rgb(255, 255, 255);
  border-radius: 50%;
  border: 4px solid rgba(255, 255, 255, 0.986);
  transition: all 0.3s ease-in-out;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
}

.clan:hover {
  transform: scale(1.2);
  border-color: #ffcc00;
  box-shadow: 0px 0px 50px rgba(255, 204, 0, 0.8), 0px 0px 40px rgba(255, 136, 0, 0.6);
}


.link  {
margin-left: 80%;
color: rgb(0, 0, 0);
font-family: monospace;
}
.link:hover {
box-shadow: 0 0 100% rgb(255, 2, 2);
transform: scale(1.05);
}


.actualizar_perfil {
background: linear-gradient(45deg, #bdbebe, #575757); 
color: rgb(255, 255, 255);
border: none;
padding: 2% 2%;
border-radius: 5%;
margin-right: 70%;
font-family: 'Arial', sans-serif;
font-size: 100%;
font-weight: bold;
cursor: pointer;
transition: all 0.5s ease; 
}

.actualizar_perfil {
  position: absolute;
  left: 5%;
  width: 180px;
  height: 50px;
  background: linear-gradient(45deg, #3a3a3a, #6e6e6e);
  border: none;
  border-radius: 10px;
  font-family: 'Arial', sans-serif;
  font-size: 14px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  text-transform: uppercase;
  letter-spacing: 2px;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.actualizar_perfil:hover {
  background: linear-gradient(45deg, #575757, #bdbebe);
  transform: scale(1.1);
  box-shadow: 0px 5px 25px rgba(255, 255, 255, 0.3);
}

.actualizar_perfil:active {
  transform: scale(0.95);
}


@import url('https://fonts.googleapis.com/css2?family=Anton&display=swap');

#datos {
  font-family: 'Anton', sans-serif; /* Fuente gruesa y de impacto */
  color: #00ffea; /* Azul neón estilo sci-fi */
  text-align: center;
  text-transform: uppercase;
  display: inline-block;
  background: black;
  border: 5px solid #00ffea;
  border-radius: 15px;
  box-shadow: 0px 0px 15px #00ffea, 0px 0px 30px #0077ff;
  text-shadow: 4px 4px 10px #0077ff, 8px 8px 20px #00ffea;
  animation: pulseGlow 1.5s infinite alternate, shake 0.3s infinite alternate;
}

@keyframes pulseGlow {
  0% { text-shadow: 4px 4px 10px #0077ff, 8px 8px 20px #00ffea; }
  100% { text-shadow: 6px 6px 15px #00ffea, 12px 12px 30px #00ffff; }
}

@keyframes shake {
  0% { transform: translateX(0px) rotate(-0deg); }
  100% { transform: translateX(-1px) rotate(1deg); }
}
.texto-2:hover, #datos:hover {
color: rgb(255, 251, 0);
text-shadow: 0 0 4px rgb(0, 0, 0);

}

.linea {
position: absolute;
background-color: rgb(255, 255, 255);
width: 1535px;
height: 5px;
right: 0;
top: 550px;
}

.videos {
width: 100%;
height: 100%; 
display: flex;
justify-content: center;
align-items: center;
top: 600px;
right: 5px;
}

video {
width: 500px;
height: 800px;
}


@media (max-width: 320px) {
  /* Estilos para pantallas muy pequeñas */
.card_profile {
width: 50%;
height: auto;
border-radius: 2rem;
transition: transform 1500ms;
transform-style: preserve-3d;
margin-left: 40%;
}
  .caja_perfil{
  display: flex;
  flex-direction: column;
  justify-content:center;
  text-align: center;
  margin-top: 0%;
}

.front,
.back {
height: 100%;
width: 100%;
border-radius: 2rem;
backface-visibility: hidden;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
gap:15px;
}
#datos {
color: rgb(255, 255, 255);
font-size: 160%;
margin-top:15%;
margin-left: 30%;
font-family: Arial, Helvetica, sans-serif;
text-align: center;
}
@keyframes pulseGlow {
  0% { text-shadow: 4px 4px 10px #0077ff, 8px 8px 20px #00ffea; }
  100% { text-shadow: 6px 6px 15px #00ffea, 12px 12px 30px #00ffff; }
}

@keyframes shake {
  0% { transform: translateX(0px) rotate(-0deg); }
  100% { transform: translateX(-1px) rotate(1deg); }
}
.actualizar_perfil {
  margin-top: 5%;
position: absolute;
left: 5%;
width: 60%;
background: linear-gradient(45deg, #bdbebe, #575757); 
color: rgb(255, 255, 255);
border: none;
padding: 2% 2%;
border-radius: 5%;
font-family: 'Arial', sans-serif;
font-size:20px;
font-weight: bold;
cursor: pointer;
transition: all 0.5s ease; 
}
}
@media (max-width: 480px) {
   /* Estilos para pantallas muy pequeñas */
.card_profile {
width: 50%;
height: auto;
border-radius: 2rem;
transition: transform 1500ms;
transform-style: preserve-3d;
margin-left: 40%;
}
  .caja_perfil{
  display: flex;
  flex-direction: column;
  justify-content:center;
  text-align: center;
  margin-top: 0%;
}
.front,
.back {
height: 100%;
width: 100%;
border-radius: 2rem;
backface-visibility: hidden;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
gap:15px;
}
#datos {
color: rgb(255, 255, 255);
font-size: 160%;
margin-top:20%;
margin-left: 30%;
font-family: Arial, Helvetica, sans-serif;
text-align: center;
}
.actualizar_perfil {
  margin-top: 2%;
position: absolute;
left: 5%;
width: 40%;
background: linear-gradient(45deg, #bdbebe, #575757); 
color: rgb(255, 255, 255);
border: none;
padding: 2% 2%;
border-radius: 5%;
font-family: 'Arial', sans-serif;
font-size:15px;
font-weight: bold;
cursor: pointer;
transition: all 0.5s ease; 
}

}


@media (min-width: 481px) and (max-width: 600px) {
  /* Estilos para pantallas entre 481px y 600px */
   /* Estilos para pantallas muy pequeñas */
.card_profile {
width: 50%;
height: auto;
border-radius: 2rem;
transition: transform 1500ms;
transform-style: preserve-3d;
margin-left: 35%;
}
  .caja_perfil{
  display: flex;
  flex-direction: column;
  justify-content:center;
  text-align: center;
  margin-top: 0%;
}
.front,
.back {
height: 100%;
width: 100%;
border-radius: 2rem;
backface-visibility: hidden;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
gap:15px;
}
#datos {
color: rgb(255, 255, 255);
font-size: 160%;
margin-top:35%;
margin-left: 20%;
font-family: Arial, Helvetica, sans-serif;
text-align: center;
}
.actualizar_perfil {
  margin-top: 2%;
position: absolute;
left: 5%;
width: 25%;
background: linear-gradient(45deg, #bdbebe, #575757); 
color: rgb(255, 255, 255);
border: none;
padding: 2% 2%;
border-radius: 5%;
font-family: 'Arial', sans-serif;
font-size:10px;
font-weight: bold;
cursor: pointer;
transition: all 0.5s ease; 
}
}

@media (min-width: 601px) and (max-width: 768px) {
   /* Estilos para pantallas muy pequeñas */
.card_profile {
width: 40%;
height: auto;
border-radius: 2rem;
transition: transform 1500ms;
transform-style: preserve-3d;
margin-left: 35%;
}
  .caja_perfil{
  display: flex;
  flex-direction: column;
  justify-content:center;
  text-align: center;
}
.front,
.back {
height: 100%;
width: 100%;
border-radius: 2rem;
backface-visibility: hidden;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
gap:15px;
}
#datos {
color: rgb(255, 255, 255);
font-size: 160%;
margin-top:6%;
margin-left: 10%;
font-family: Arial, Helvetica, sans-serif;
text-align: center;
}
.actualizar_perfil {
  margin-top: 0%;
position: absolute;
left: 5%;
width: 20%;
background: linear-gradient(45deg, #bdbebe, #575757); 
color: rgb(255, 255, 255);
border: none;
padding: 2% 2%;
border-radius: 5%;
font-family: 'Arial', sans-serif;
font-size:10px;
font-weight: bold;
cursor: pointer;
transition: all 0.5s ease; 
}
}

@media (min-width: 769px) and (max-width: 1024px) {
     /* Estilos para pantallas muy pequeñas */
.card_profile {
width: 40%;
height: auto;
border-radius: 2rem;
transition: transform 1500ms;
transform-style: preserve-3d;
margin-left: 35%;
}
  .caja_perfil{
  display: flex;
  flex-direction: column;
  justify-content:center;
  text-align: center;
}
.front,
.back {
height: 100%;
width: 100%;
border-radius: 2rem;
backface-visibility: hidden;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
gap:15px;
}
#datos {
color: rgb(255, 255, 255);
font-size: 160%;
margin-top:6%;
margin-left: 10%;
font-family: Arial, Helvetica, sans-serif;
text-align: center;
}
.actualizar_perfil {
  margin-top: 0%;
position: absolute;
left: 5%;
width: 20%;
background: linear-gradient(45deg, #bdbebe, #575757); 
color: rgb(255, 255, 255);
border: none;
padding: 1%;
border-radius: 5%;
font-family: 'Arial', sans-serif;
font-size:10px;
font-weight: bold;
cursor: pointer;
transition: all 0.5s ease; 
}
  
}
  


@media (min-width: 1025px) and (max-width: 1280px) {
  /* Estilos para pantallas entre 1025px y 1280px */
.card_profile {
width: 50%;
height: auto;
border-radius: 2rem;
transition: transform 1500ms;
transform-style: preserve-3d;
margin-left: 40%;
}
  .caja_perfil{
  display: flex;
  flex-direction: column;
  justify-content:center;
  text-align: center;
}
.front,
.back {
height: 100%;
width: 100%;
border-radius: 2rem;
backface-visibility: hidden;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
gap:15px;
}
#datos {
color: rgb(255, 255, 255);
font-size: 160%;
margin-top:6%;
margin-left: 30%;
font-family: Arial, Helvetica, sans-serif;
text-align: center;
}
.actualizar_perfil {
  margin-top: 0%;
position: absolute;
left: 5%;
width: 30%;
background: linear-gradient(45deg, #bdbebe, #575757); 
color: rgb(255, 255, 255);
border: none;
padding: 2% 2%;
border-radius: 5%;
font-family: 'Arial', sans-serif;
font-size:100%;
font-weight: bold;
cursor: pointer;
transition: all 0.5s ease; 
}
  
  
}

@media (min-width: 1281px) and (max-width: 1440px) {
  /* Estilos para pantallas entre 1281px y 1440px */
   /* Estilos para pantallas muy pequeñas */
.card_profile {
width: 60%;
height: auto;
border-radius: 2rem;
transition: transform 1500ms;
transform-style: preserve-3d;
margin-left: 20%;
}
  .caja_perfil{
  display: flex;
  flex-direction: column;
  justify-content:center;
  text-align: center;
}
.front,
.back {
height: 100%;
width: 100%;
border-radius: 2rem;
backface-visibility: hidden;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
gap:15px;
}
#datos {
color: rgb(255, 255, 255);
font-size: 160%;
margin-top:6%;
margin-left: 0%;
font-family: Arial, Helvetica, sans-serif;
text-align: center;
}

}

@media (min-width: 1025px) and (max-width: 2000px) {
  .actualizar_perfil {
  margin-top: 0%;
position: absolute;
left: 5%;
width: 12%;
background: linear-gradient(45deg, #bdbebe, #575757); 
color: rgb(255, 255, 255);
border: none;
padding: 1%;
border-radius: 5%;
font-family: 'Arial', sans-serif;
font-size:13px;
font-weight: bold;
cursor: pointer;
transition: all 0.5s ease; 
}
.card_profile {
width: 60%;
height: auto;
border-radius: 2rem;
transition: transform 1500ms;
transform-style: preserve-3d;
margin-left: 22%;
}
#datos {
color: rgb(255, 255, 255);
font-size: 160%;
margin-top:6%;
margin-left: 5%;
font-family: Arial, Helvetica, sans-serif;
text-align: center;
}

}
@media (min-width: 1441px) and (max-width: 2000px) {
  /* Estilos para pantallas entre 1441px y 1920px */
  .card_profile {
width: 60%;
height: auto;
border-radius: 2rem;
transition: transform 1500ms;
transform-style: preserve-3d;
margin-left: 20%;
}
  .caja_perfil{
  display: flex;
  flex-direction: column;
  justify-content:center;
  text-align: center;
}
.front,
.back {
height: 100%;
width: 100%;
border-radius: 2rem;
backface-visibility: hidden;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
gap:15px;
}

.actualizar_perfil {
margin-top: 0%;
position: absolute;
left: 5%;
width: 12%;
background: linear-gradient(45deg, #bdbebe, #575757); 
color: rgb(255, 255, 255);
border: none;
padding: 1%;
border-radius: 5%;
font-family: 'Arial', sans-serif;
font-size:10px;
font-weight: bold;
cursor: pointer;
transition: all 0.5s ease; 
}
  
}

@media (min-width: 1921px) and (max-width: 2560px) {
  /* Estilos para pantallas entre 1921px y 2560px */
}

@media (min-width: 2561px) and (max-width: 3840px) {
  /* Estilos para pantallas entre 2561px y 3840px */
}


@media (min-width: 3841px) and (max-width: 5120px) {
  /* Estilos para pantallas entre 3841px y 5120px */
}




</style>
