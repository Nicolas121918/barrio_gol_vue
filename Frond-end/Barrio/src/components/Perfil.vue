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
            <svg
              viewBox="0 0 16 16"
              class="bi bi-person-add"
              fill="currentColor"
              height="100"
              width="100"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M12.5 16a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7Zm.5-5v1h1a.5.5 0 0 1 0 1h-1v1a.5.5 0 0 1-1 0v-1h-1a.5.5 0 0 1 0-1h1v-1a.5.5 0 0 1 1 0Zm-2-6a3 3 0 1 1-6 0 3 3 0 0 1 6 0ZM8 7a2 2 0 1 0 0-4 2 2 0 0 0 0 4Z"
              ></path>
              <path
                d="M8.256 14a4.474 4.474 0 0 1-.229-1.004H3c.001-.246.154-.986.832-1.664C4.484 10.68 5.711 10 8 10c.26 0 .507.009.74.025.226-.341.496-.65.804-.918C9.077 9.038 8.564 9 8 9c-5 0-6 3-6 4s1 1 1 1h5.256Z"
              ></path>
            </svg>

            <div class="icons">
              <svg
                viewBox="0 0 16 16"
                class="bi bi-instagram"
                fill="currentColor"
                height="32"
                width="32"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z"
                ></path>
              </svg>
            </div>
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

background-color: rgb(255, 255, 255);
border-radius: 50%;
border: 4px solid rgba(255, 255, 255, 0.986);

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

.actualizar_perfil:hover {
background-color: rgba(127, 255, 212, 0.5);
box-shadow: 0 4% 100% rgba(0, 0, 0, 0.2), 0 2px 6px blue;
text-shadow: 0 0 30% black;
transform: scale(1.1);
}




#datos {
color: white;
font-size: 250%;
font-family: Arial, Helvetica, sans-serif;
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
margin-top:15%;
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
margin-top:15%;
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
.actualizar_perfil {
  margin-top: 0%;
position: absolute;
left: 5%;
width: 15%;
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
#datos {
color: rgb(255, 255, 255);
font-size: 160%;
margin-top:6%;
margin-left: 0%;
font-family: Arial, Helvetica, sans-serif;
text-align: center;
}
.actualizar_perfil {
  margin-top: 0%;
position: absolute;
left: 5%;
width: 10%;
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
