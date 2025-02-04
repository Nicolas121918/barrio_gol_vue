<template>
  <header>
    <headerapp></headerapp>
  </header>

  <!-- Mostrar si no hay equipos disponibles -->
  <div v-if="teams.length <= 0">
    <div class="caja_contiene">
      <div class="caja_contiene_hijo">
        <div id="main">
          <input
            class="input"
            name="text"
            type="text"
            v-model="buscar"
            placeholder="Busca o Crea Tu Team"
          />
          <div class="search-icon">
            <svg
              stroke-linejoin="round"
              stroke-linecap="round"
              stroke-width="2"
              stroke="url(#cosmic-search)"
              fill="none"
              height="24"
              width="24"
              viewBox="0 0 24 24"
            >
              <circle r="8" cy="11" cx="11"></circle>
              <line y2="16.65" x2="16.65" y1="21" x1="21"></line>
              <defs>
                <linearGradient gradientTransform="rotate(40)" id="cosmic-search">
                  <stop stop-color="#a9c7ff" offset="0%"></stop>
                  <stop stop-color="#6e8cff" offset="100%"></stop>
                </linearGradient>
              </defs>
            </svg>
          </div>
          <button class="boton_formulario_join">
            <span><router-link to="/creacionequipo">Crear</router-link></span>
          </button>
        </div>
      </div>

      <div class="container_equipo">
        <!-- Lógica de búsqueda -->
        <div v-if="buscar">
          <div v-for="(i, index) in teams.filter(team => team.nombreteam.toLowerCase().includes(buscar.toLowerCase()) && team.capitanteam !== usuario.nombreUsuario)" :key="index">
            <li>
              <div id="fil-custom" class="container-custom">
                <div class="card-custom">
                  <img :src="getImagenUrl(i.logoTeam)" class="card-img-top-custom" alt="Imagen de tarjeta">
                  <div class="card-body-custom">
                    <p class="card-text-custom">Nombre: {{ i.nombreteam }}</p>
                    <p class="card-text-custom">Capitán: {{ i.capitanteam }}</p>
                    <p class="card-text-custom">Ubicación: {{ i.location }}</p>
                    <a href="#" @click.prevent="seleccionarEquipo(i.nombreteam)" class="btn-custom">UNIRSE</a>
                  </div>
                </div>
              </div>
            </li>
          </div>
        </div>

        <!-- Mostrar mensaje si no hay equipos disponibles -->
        <div v-else>
          <div class="terminal-loader">
            <div class="terminal-header">
              <div class="terminal-title">Status</div>
              <div class="terminal-controls">
                <div class="control close"></div>
                <div class="control minimize"></div>
                <div class="control maximize"></div>
              </div>
            </div>
            <div class="text">No Hay Equipos Disponibles...</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Mostrar todos los equipos si no hay búsqueda activa y el capitán no es el usuario -->
  <div v-else>
    <div v-if="teams.length > 0">
      <div v-for="(i, index) in teams.filter(team => team.capitanteam !==usuario.nombreUsuario)" :key="index" class="card-custom">
        <img :src="getImagenUrl(i.logoTeam)" class="card-img-top-custom" alt="Imagen de tarjeta">
        <div class="card-body-custom">
          <h5 class="card-title-custom"><strong>Nombre Equipo: {{ i.nombreteam }}</strong></h5>
          <p class="card-text-custom"><strong>Descripción: {{ i.Descripcion }}</strong></p>
          <p class="card-text-custom"><strong>Número De Integrantes: {{ i.numeropeople }}</strong></p>
          <p class="card-text-custom"><strong>Capitán Del Equipo: {{ i.capitanteam }}</strong></p>
          <p class="card-text-custom"><strong>Requisitos: {{ i.requisitos_join }}</strong></p>
          <p class="card-text-custom"><strong>Ubicación: {{ i.location }}</strong></p>
          <a href="#" @click.prevent="seleccionarEquipo(i.nombreteam)" class="btn-custom">
            <router-link to="/formulario">UNIRSE</router-link>
          </a>
        </div>
      </div>
    </div>
  </div>

  <!-- Mostrar componente si el capitán del equipo es el mismo que el usuario -->
  <div v-for="(i, index) in teams" :key="index">
    <div v-if="i.capitanteam === usuario.nombreUsuario">
      <componente></componente>
    </div>
  </div>

  <div class="galaxy"></div>
  <div id="search-container">
    <div class="nebula"></div>
    <div class="starfield"></div>
    <div class="cosmic-dust"></div>
    <div class="cosmic-dust"></div>
    <div class="cosmic-dust"></div>
    <div class="stardust"></div>
    <div class="cosmic-ring"></div>
  </div>
</template>


<script>
import { ref, onMounted } from 'vue';
import Swal from 'sweetalert2';
import axios from 'axios';
import Headerapp from './Headerapp.vue';
import Componente from './componente.vue';

export default {
  components: {
    Headerapp,
    Componente,
  },
  setup() {
    const url = ref('');
    const buscar = ref('');
    const teams = ref([]);
    const tiene = ref(false);
    const id = ref(["1", "2", "3", "4", "6", "7", "8", "9", "10", "11", "12", "13", "14"]);
    const getImagenUrl = (path) => {
      return `http://127.0.0.1:8000/${path}`;
    };
    const usuario = ref(JSON.parse(localStorage.getItem('usuario')));

    // Métodos
    const fetchTeams = async () => {
      try {
        const response = await axios.get('http://localhost:8000/listarteams');
        teams.value = response.data;
      } catch (error) {
        console.error("Error al obtener los datos", error);
      }
    };

    const seleccionarEquipo = (equipo) => {
      Swal.fire({
        icon: 'success',
        title: `¡Equipo ${equipo} seleccionado!`,
        text: 'Verifica tus Datos antes de Enviarlos.',
        timer: 3000,
        showConfirmButton: false,
      });
    };

    // Llamada inicial
    onMounted(fetchTeams);

    // Retornamos todas las variables y métodos
    return {
      teams,
      tiene,
      id,
      url,
      buscar,
      seleccionarEquipo,
      getImagenUrl,
      Headerapp,
      usuario,
    };
  },
};
</script>


<style scoped>
.caja_contiene_hijo{
  display: flex;
  flex-direction: row;
  margin: 40%;
}
#main{
  display: flex;
}
.caja_contiene{
  width: 90%;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: center;
  align-items: flex-start;
  margin-left: -20%;
}

.search-icon{
  height: 20%;
  margin-right: 90%;
}
.container_equipo{
  display: flex;
  flex-direction:row;
  flex-wrap: wrap;
  width: 90%;
  margin-left: 10%;
  padding: 0;
  
}
@keyframes blinkCursor {
  50% {
    border-right-color: transparent;
  }
}

@keyframes typeAndDelete {
  0%,
  10% {
    width: 0;
  }
  45%,
  55% {
    width: 6.2em;
  } 
  90%,
  100% {
    width: 0;
  }
}

.terminal-loader {
  border: 0.1em solid #333;
  background-color: #1a1a1a;
  font-family: "Courier New", Courier, monospace;
  font-size: 2em;
  padding: 1.5em 1em;
  width: 180%;
  margin: 0 0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  border-radius: 4px;
  overflow: hidden;
  box-sizing: border-box;
}

.terminal-header {

  top: 0;
  left: 0;
  right: 0;
  height: 1.5em;
  background-color: #333;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  padding: 0 0.4em;
  box-sizing: border-box;
}

.terminal-controls {
  float: right;
}

.control {
  display: inline-block;
  width: 0.6em;
  height: 0.6em;
  margin-left: 0.4em;
  border-radius: 50%;
  background-color: #777;
}

.control.close {
  background-color: #e33;
}

.control.minimize {
  background-color: #ee0;
}

.terminal-title {
  float: left;
  line-height: 1.5em;
  color: #eee;
}

.text {
  display: inline-block;
  white-space: nowrap;
  border-right: 0.2em solid green; /* Cursor */
  animation: typeAndDelete 4s steps(11) infinite,
    blinkCursor 0.5s step-end infinite alternate;
  margin-top: 1.5em;
}

#text-conditional{
  align-items: center;
  background-color:black;
}
.boton_formulario_join{
  background-color: #05071b;
  width: 20%;
  color: wheat;
  width: 20%;
}

.boton_formulario_join:hover {
  animation: sh0 0.5s ease-in-out both;
}

@keyframes sh0 {
  0% {
    transform: rotate(0deg) translate3d(0, 0, 0);
  }

  25% {
    transform: rotate(7deg) translate3d(0, 0, 0);
  }

  50% {
    transform: rotate(-7deg) translate3d(0, 0, 0);
  }

  75% {
    transform: rotate(1deg) translate3d(0, 0, 0);
  }

  100% {
    transform: rotate(0deg) translate3d(0, 0, 0);
  }
}

.boton_formulario_join:hover span {
  animation: storm 0.7s ease-in-out both;
  animation-delay: 0.06s;
}

.boton_formulario_join::before,
.boton_formulario_join::after {
  content: '';
  right: 0;
  bottom: 0;
  width: 5%;
  height: 5%;
  border-radius: 50%;
  background: #fff;
  opacity: 0;
  transition: transform 0.15s cubic-bezier(0.02, 0.01, 0.47, 1), opacity 0.15s cubic-bezier(0.02, 0.01, 0.47, 1);
  z-index: -1;
  transform: translate(100%, -25%) translate3d(0, 0, 0);
}

.boton_formulario_join:hover::before,
.boton_formulario_join:hover::after {
  opacity: 0.15;
  transition: transform 0.2s cubic-bezier(0.02, 0.01, 0.47, 1), opacity 0.2s cubic-bezier(0.02, 0.01, 0.47, 1);
}

.boton_formulario_join:hover::before {
  transform: translate3d(50%, 0, 0) scale(0.9);
}

.boton_formulario_join:hover::after {
  transform: translate(50%, 0) scale(1.1);
}

#card2-custom {
  background-color: black;
  color: #ffffff;
  border-color: rgb(0, 0, 0);
  border-style: solid;
  border-radius: 0%;
  background-image: url("https://media.istockphoto.com/id/1293988714/es/foto/fondo-dorado-metal-pulido-dorado-con-textura-de-acero.jpg?s=612x612&w=0&k=20&c=dYBE-ZrxpIsKbkVgbSFkUvYcymSjyjTr9j61tQKsoXI=");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
 
  left: 500%;
  height: 50%;
}

#fil-custom {
  display: flex;
  flex-direction: column;
  align-items:center ;
  margin-left: 60%;
  top: 22%;
  width: 10%;
  font-size: 20px;
}

.container-custom {
  
  display: flex;
  flex-wrap: wrap;
  height: 100%;
  max-height: 110%;
  width: 300%;
  max-width: 100%;
  gap: 5rem;

  color: rgb(255, 0, 0);
  height: 100%;
  width: 100%;
  background-image: radial-gradient(#ffffff 1px, transparent 1px),
    radial-gradient(#ffffff 1px, transparent 1px);
  background-size: 50px 50px;
  background-position:
    0 0,
    25px 25px;
    flex-direction: row;
  
  
}

.card-custom {
  width: 18rem;
  background-color: rgb(21, 21, 21);
  transition: transform 0.5s;
  border-color: rgba(98, 96, 96, 0.278);
  border-style: solid;
  color: white;
  border-width: 1px;
  margin-bottom: 5%;
  height: 70%;
}

.card-custom:hover {
  transform: scale(1.05);
  box-shadow: 0 0 40px rgb(255, 230, 0);
}

.card-img-top-custom {
  width: 100%;
  border: 5px solid transparent;
  border-image: linear-gradient(to right, #FFD700, #FFFFFF) 1;
  border-style: solid;
}

.btn-custom {
  margin-top: 1rem;
  background-color: rgba(255, 255, 255, 0.71);
  text-shadow: 0 0 2px #FFD700;
  border-color: black;
  font-size: 20px;
  color: black;
  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
}

.galaxy {
  height: 60%;
  width: 100%;
  background-image: radial-gradient(#ffffff 1px, transparent 1px),
    radial-gradient(#ffffff 1px, transparent 1px);
  background-size: 50px 50px;
  background-position:
    0 0,
    25px 25px;
  z-index: -1;
  animation: twinkle 5s infinite;
  background-attachment: fixed; 
  display: inline-block;
  transform: translate(-25%, 0%);
};

@keyframes twinkle {
  0%,
  100% {
    opacity: 0.5;
  }
  50% {
    opacity: 1;
  }
}

.stardust,
.cosmic-ring,
.starfield,
.nebula {
  max-height: 70px;
  max-width: 314px;
  height: 100%;
  width: 100%;
 
  overflow: hidden;
  z-index: -1;
  border-radius: 12px;
  filter: blur(3px);
}

.input {
  background-color: #05071b;
  border: none;
  width: auto;
  height: 60px;
  border-radius: 10px;
  color: #c9b037;
  padding-inline: 59px;
  font-size: 20px;
 
}

#search-container {
  display: flex;
  justify-content:flex-end;
  align-items: flex-end;
  transform: translate(-20%, 35%);
}

.input::placeholder {
  color: #c9b037;
}

.input:focus {
  outline: none;
}

  
#input-mask {
  pointer-events: none;
  width: 100px;
  height: 20px;
 
  background: linear-gradient(90deg, transparent, #00000000);

}

#cosmic-glow {
  pointer-events: none;
  width: 30px;
  height: 20px;
 
  background:#c9b037;
  top: 10px;
  left: 5px;
  filter: blur(20px);
  opacity: 0.8;
  transition: all 2s;
}



.stardust {
  max-height: 63px;
  max-width: 307px;
  border-radius: 10px;
  filter: blur(2px);
}

.stardust::before {
  content: "";
  z-index: -2;
  text-align: center;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) rotate(83deg);
 
  width: 600px;
  height: 600px;
  background-repeat: no-repeat;
  background-position: 0 0;
  filter: brightness(1.4);
  background-image: conic-gradient(
    45deg, 
  rgb(253, 253, 253), 
  #d4af37, /* Dorado */
  rgb(255, 255, 255) 50%, 
  rgb(0, 0, 0) 50%, 
  #c9b037, /* Dorado más oscuro */
  rgba(0, 0, 0, 0) 100%
  );
  transition: all 2s;
}

.cosmic-ring {
  max-height: 59px;
  max-width: 303px;
  border-radius: 11px;
  filter: blur(0.5px);
}

.cosmic-ring::before {
  content: "";
  z-index: -2;
  text-align: center;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) rotate(80deg);
 
  width: 600px;
  height: 600px;
  filter: brightness(1.3);
  background-repeat: no-repeat;
  background-position: 0 0;
  background-image: conic-gradient(

  rgba(255, 255, 255, 0.847), 
  #d4af37, /* Dorado */
  rgb(255, 255, 255) 50%, 
  rgba(0, 0, 0, 0) 50%, 
  #c9b037, /* Dorado más oscuro */
  rgba(0, 0, 0, 0) 100%
  );
  transition: all 2s;
}

.starfield {
  max-height: 65px;
  max-width: 312px;
}

.starfield::before {
  content: "";
  z-index: -2;
  text-align: center;
  top: 50%;
   left: 50%;
  transform: translate(-50%, -50%) rotate(82deg);
 
  width: 600px;
  height: 600px;
  background-repeat: no-repeat;
  background-position: 0 0;
  background-image: conic-gradient(
    rgba(0, 0, 0, 0),
    #c9b037,
    rgba(0, 0, 0, 0) 10%,
    rgba(0, 0, 0, 0) 50%,
    #c9b037,
    rgba(0, 0, 0, 0) 60%
  );
  transition: all 1ms;
}

#search-container:hover > .starfield::before {
  transform: translate(-50%, -50%) rotate(-98deg);
}

#search-container:hover > .nebula::before {
  transform: translate(-50%, -50%) rotate(-120deg);
}

#search-container:hover > .stardust::before {
  transform: translate(-50%, -50%) rotate(-97deg);
}

#search-container:hover > .cosmic-ring::before {
  transform: translate(-50%, -50%) rotate(-110deg);
}

#search-container:focus-within > .starfield::before {
  transform: translate(-50%, -50%) rotate(442deg);
  transition: all 4s;
}

#search-container:focus-within > .nebula::before {
  transform: translate(-50%, -50%) rotate(420deg);
  transition: all 4s;
}

#search-container:focus-within > .stardust::before {
  transform: translate(-50%, -50%) rotate(443deg);
  transition: all 4s;
}

#search-container:focus-within > .cosmic-ring::before {
  transform: translate(-50%, -50%) rotate(430deg);
  transition: all 4s;
}

.nebula {
  overflow: hidden;
  filter: blur(30px);
  opacity: 0.4;
  max-height: 130px;
  max-width: 354px;
}

.nebula:before {
  content: "";
  z-index: -2;
  text-align: center;
 
 
  transform: translate(-50%, -50%) rotate(60deg);
  
  width: 999px;
  height: 999px;
  background-repeat: no-repeat;
  background-position: 0 0;
  background-image: conic-gradient(
  rgba(0, 0, 0, 0), 
  #d4af37, /* Dorado */
  rgba(0, 0, 0, 0) 50%, 
  rgba(0, 0, 0, 0) 50%, 
  #c9b037, /* Dorado más oscuro */
  rgba(0, 0, 0, 0) 100%
  );
  transition: all 2s;
}

#wormhole-icon {
 
  top: 8px;
  right: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2;
  max-height: 40px;
  max-width: 38px;
  height: 100%;
  width: 100%;
  isolation: isolate;
  overflow: hidden;
  border-radius: 10px;
  background: linear-gradient(180deg, #c9b13743, #05071b, #c9b13750);
  border: 1px solid transparent;
}

.wormhole-border {
  height: 42px;
  width: 40px;
 
  overflow: hidden;
  top: 7px;
  right: 7px;
  border-radius: 10px;
}

.wormhole-border::before {
  content: "";
  text-align: center;

  transform: translate(-50%, -50%) rotate(90deg);

  width: 600px;
  height: 600px;
  background-repeat: no-repeat;
  background-position: 0 0;
  filter: brightness(1.35);
  background-image: conic-gradient(
  rgba(0, 0, 0, 0), 
  #d4af37, /* Dorado */
  rgba(0, 0, 0, 0) 50%, 
  rgba(0, 0, 0, 0) 50%, 
  #c9b037, /* Dorado más oscuro */
  rgba(0, 0, 0, 0) 100%
  );
  animation: rotate 4s linear infinite;
}



@keyframes rotate {
  100% {
    transform: translate(-50%, -50%) rotate(450deg);
  }
}

.card-text-custom, .card-title-custom {
  font-size: 100%;
  font-family: "Ubuntu", sans-serif;
  font-weight: 300;
  font-style: normal;
  text-align: center;
  color: rgb(255, 255, 255);
  background-color: rgba(0, 0, 0, 0.6); 
  padding: 2%; 
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); 
  transition: transform 1s ease, background-color 1s ease; 
}

.card-text-custom:hover, .card-title-custom:hover {
  background-color: rgba(255, 0, 0, 0.666); 
  transform: translateY(-5px); 
}

.btn {
  padding: 0.7em 1em;
  background: transparent;
  outline: none;
  border: 0;
  color: #d4af37;
  letter-spacing: 0.1em;
  font-family: monospace;
  font-size: 100%;
  font-weight: bold;
  cursor: pointer;
  z-index: 1;

  transform: translate(100%, 45%); /* Mueve verticalmente */
}

.cube {
  
  transition: all 0.5s;
}

.cube .bg-top {
  
  height: 10px;
  background: #d4af37;
  transform: skew(-45deg, 0);
  margin: 0;
  transition: all 0.4s;
}


.cube .bg {
  

  background: #d4af37;
  transition: all 0.4s;
}

.cube .bg-right {
  
  background: #d4af37;
  top: -5px;
  z-index: 0;

  width: 10px;

  transform: skew(0, -45deg);
  transition: all 0.4s;
}



.cube .bg-inner {
  background: #28282d;

}

.cube .text {
 
  transition: all 0.4s;
}

.cube:hover .bg-inner {
  background: #d4af37;
  transition: all 0.4s;
}

.cube:hover .text {
  color: #28282d;
  transition: all 0.4s;
}

.cube:hover .bg-right,
.cube:hover .bg,
.cube:hover .bg-top {
  background: #28282d;
}

.cube:active {
  z-index: 9999;
}

@keyframes bounce {
  50% {
    transform: scale(0.9);
  }
}
</style>
