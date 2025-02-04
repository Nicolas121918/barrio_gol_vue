<template>

  <header>
    <headerapp></headerapp>
  </header>
  <h1 class="titulo_torneo">Lista de Torneos y Partidos</h1>

    <div class="main-container">
      <div class="buscador_torneo">
      
      
      <!-- Barra de búsqueda y botón "Ver Juegos" -->
      <div class="search-container">
        <input 
          v-model="searchQuery" 
          type="text" 
          placeholder="Buscar torneos o partidos..." 
          class="search-input"
        />
        <router-link to="/crearpartido"><button @click="viewGames" class="view-games-button">Crear Partido</button></router-link>
        
        <router-link class="view-games-button" to="/creartorneo">
        crear Torneo
      </router-link>
      <router-link to="/torneo_creados"><button @click="" class="view-games-button2">creados..</button></router-link>
      </div>
    </div>
      <div class="card-list">
        <div v-for="(item, index) in filteredList" :key="index" class="card3">
          <!-- Si es un torneo -->
          <div v-if="item.tipo === 'torneo'">
            <div class="card-header-tor">
              <img :src="getImagenUrl(item.logoTeam)" alt="Logo del Torneo" class="logo-img">
              <div class="card-info-tor">
                <h2 class="titu">{{ item.nombre }}</h2>
                <p>Participantes: {{ item.numeroparticipantes }}</p>
                <p>Precio de Inscripción: ${{ item.precioInscripcion }}</p>
                <p>Precio de Arbitraje por partido: ${{ item.precioArbitrajeTorneo }}</p>
              </div>
            </div>
            <div class="uno_solo">
            <div class="rules-container">
              <button @mouseover="showRules('torneo', index)" @mouseleave="hideRules('torneo', index)" class="torn_boton">Ver Reglas</button>
              <div v-if="activeRules.torneo === index" class="rules-info-tor">
                <p class="reglas">Reglas del Torneo {{ item.reglasTorneo }}</p>
                <!-- Agrega aquí el contenido de las reglas -->
              </div>
            </div>
            <button class="action-button-tor" @click="inscribirTorneo(index)">Inscribir</button>
          </div>
        </div>
          
          <!-- Si es un partido -->
          <div v-if="item.tipo === 'partido'" class="card4">
            <div class="card-header-match">
              <div class="card-info-match">
                <h2 class="titu2">Torneo {{ index + 1 }}</h2>
                <p>Hora: {{ item.hora }}</p>
                <p>Lugar: {{ item.lugar }}</p>
                <p>Número de partidos: {{ item.numeroPartidos }}</p>
                <p>Apuesta: ${{ item.apuesta }}</p>
              </div>
            </div>
            <div class="uno_solo">
            <div class="rules-container">
              <button @mouseover="showRules('partido', index)" @mouseleave="hideRules('partido', index)" class="torn_boton">Ver Reglas</button>
              <div v-if="activeRules.partido === index" class="rules-info-match">
                <p class="reglas">Reglas del Partido {{ index + 1 }}</p>
                <!-- Agrega aquí el contenido de las reglas -->
              </div>
            </div>
            <button class="action-button-match" @click="unirPartido(index)">Unir</button>
          </div>
        </div>
      </div>
      </div>
    </div>
  </template>
  
  
  <script setup>
  import { ref, computed, onMounted } from 'vue';
  import axios from 'axios'; // Importar Axios
  import Headerapp from './Headerapp.vue';
  
  const torneos = ref([]);  // Lista vacía para almacenar los torneos obtenidos del API
  const partidos = ref([   // Aquí mantendremos los datos de los partidos como ya lo tenías
  
    {
      tipo: "partido",
      hora: "15:00",
      lugar: "Estadio Nacional",
      numeroPartidos: 5,
      apuesta: 100000
    },
    {
      tipo: "partido",
      hora: "18:00",
      lugar: "Campo de Juego",
      numeroPartidos: 3,
      apuesta: 50000
    }
    // Otros partidos...
  ]);
  const getImagenUrl = (path) =>{
      return `http://127.0.0.1:8000/${path}`;
    };
    
  
  const combinedList = ref([...torneos.value, ...partidos.value]);  // Lista combinada de torneos y partidos
  
  // Obtener torneos del API
  const getTorneos = async () => {
    try {
      const response = await axios.get('http://localhost:8000/listartorneos');
      torneos.value = response.data; // Asignar los torneos obtenidos a la variable `torneos`
      combinedList.value = [...torneos.value, ...partidos.value]; // Actualizar la lista combinada
    } catch (error) {
      console.error('Error al obtener los torneos:', error);
    }
  };
  
  onMounted(() => {
    getTorneos();  // Llamar la función para obtener los torneos cuando el componente se monte
  });
  
  // Función para mezclar la lista de manera aleatoria
  const shuffleArray = (array) => {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  };
  
  // Mezclar la lista combinada al cargar la página
  combinedList.value = shuffleArray(combinedList.value);
  
  const activeRules = ref({ torneo: null, partido: null });
  
  const showRules = (type, index) => {
    activeRules.value[type] = index;
  };
  
  const hideRules = (type, index) => {
    if (activeRules.value[type] === index) {
      activeRules.value[type] = null;
    }
  };
  
  const inscribirTorneo = (index) => {
    alert(`Inscripción al torneo ${index + 1}`);
  };
  
  const unirPartido = (index) => {
    alert(`Unirse al partido ${index + 1}`);
  };
  
  // Buscador
  const searchQuery = ref('');
  const filteredList = computed(() => {
    const query = searchQuery.value.toLowerCase();
    return combinedList.value.filter(item => {
      if (item.tipo === 'torneo') {
        return item.nombre.toLowerCase().includes(query);
      } else if (item.tipo === 'partido') {
        return item.lugar.toLowerCase().includes(query) || item.hora.toLowerCase().includes(query);
      }
      return false;
    });
  });
  
  </script>
  
  
  
  <style scoped>
  .search-container{
    display: flex;
    flex-direction: row;
    width: 100%;
    align-content: space-between;
  
    justify-content: space-between;
  }

.uno_solo{
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
}
  .main-container {
  padding: 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-top: 2%;
  margin-left: -10%;
  width: 100%;
  text-align: center;
}

.buscador_torneo{
  display: flex;
  flex-direction: row;
  margin-bottom: 2%;
}

.header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
  
}

.search-bar {
  width: 40%;
  padding: 10px;
  font-size: 16px;
  position: relative;
  left: 100%;
}

.view-games-button {
  
  background-color: #0c0452;
  color: white;
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
  border: 2px solid white;

}
.view-games-button2{
  background-color: #0099ff;
  color: rgb(0, 0, 0);
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
  left: 40%;
  border: 2px solid black
}
.view-games-button2:hover{
  background-color: #2f00ff;
  color: white;
} 

.view-games-button:hover {
  background-color:  #00ccff;
  color: black;
}


.card-list {
  display: flex;
  flex-direction: column; /* Mostrar en vertical */
  gap: 20px;
}

.card3 {
  width: 60vw; /* 60% del ancho de la vista del usuario */
  min-height: 100%;
  min-width: 150%;
  background-color: #000000;
  padding: 15px;
  box-shadow: 0px 4px 2px rgb(255, 255, 255);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border: none; /* Sin bordes redondeados */
  box-sizing: border-box; /* Asegura que el padding no aumente el ancho total */
  overflow: hidden; /* Asegura que no haya bordes redondeados */
  position: relative;
  right: 10%;
}

.card-header-tor, .card-header-match {
  display: flex;
  align-items: center;
  gap: 15px;
}

.logo-img {
  width: 80px; /* Ajusta el tamaño del logo */
  height: 80px; /* Ajusta el tamaño del logo */
  object-fit: cover;
}

.card-info-tor, .card-info-match {
  flex-grow: 1;
  
  text-align: left;
  font-size: 120%;
  width: 10%;
  display: inline;
}

.rules-container {
  margin-right: 35%;
  height: auto;
  font-size: 90%;
}

.card-info-tor, .card-info-match {
  flex-grow: 0; /* Elimina el crecimiento del elemento */
  text-align: left;
  font-size: 120%;
  width: auto; /* Elimina la ocupación total del ancho */
  display: inline-block; /* Solo ocupa el ancho del contenido */
}

.titulo_torneo {
margin-top: 20%;
text-align: center;
  text-shadow: 0 0 6px rgb(255, 255, 255);
  color: #ffffff;
  font-size: 250%;
}

.action-button-tor, .action-button-match {
  margin-top: 10px;
  background-image: url("https://static.vecteezy.com/system/resources/thumbnails/000/549/015/small/vector-apr-2018-19.jpg");
  height: auto;
  color: white;
  padding: 10px;
  font-size: 300%;
  cursor: pointer;

  left: 70%;
  bottom: 35%;
  font-family: 'Times New Roman', Times, serif;
  text-shadow: 0 0 5px black;
  font-weight: bold;
  transition: all 0.3s ease; /* Transición suave */
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
}

.torn_boton {
  color: rgb(0, 0, 0);
  position: relative;
  border-radius: 10px;
  font-size: 150%;
  font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;

}

.reglas {
  background-color: rgb(90, 90, 90);
  width: 15%;
  height: auto;
  position: absolute;
}

.titu {
  font-size: 170%;
  font-weight: bold;
  text-align: center;
  
  background-image: url("https://static.vecteezy.com/system/resources/thumbnails/000/549/015/small/vector-apr-2018-19.jpg");
  background-size: cover; /* Ajusta el tamaño de la imagen para que cubra todo el texto */
  background-clip: text;
  -webkit-background-clip: text; /* Para navegadores que requieren prefijo */
  color: transparent; /* Hace el texto transparente para mostrar el fondo */
  text-shadow: none; /* Elimina sombras en el texto si hay */
}
.search-input{
  font-size: 140%;
  border: 2px solid transparent;
  width: 15em;
  height: 2.5em;
  padding-left: 0.8em;
  outline: none;
  overflow: hidden;
  background-color: #f3f3f3;
  border-radius: 10px;
  transition: all 0.5s;
}

.search-input:hover,
.search-input:focus {
  border: 2px solid #4a9dec;
  box-shadow: 0px 0px 0px 7px rgb(74, 157, 236, 20%);
  background-color: white;
}

.titu2 {
  font-size: 170%;
  font-weight: bold;

  left: 300%;
  background-image: url("https://static.vecteezy.com/system/resources/thumbnails/000/549/015/small/vector-apr-2018-19.jpg");
  background-size: cover; /* Ajusta el tamaño de la imagen para que cubra todo el texto */
  background-clip: text;
  -webkit-background-clip: text; /* Para navegadores que requieren prefijo */
  color: transparent; /* Hace el texto transparente para mostrar el fondo */
  text-shadow: none;
}

@media (max-width: 320px) {
  /* Estilos para pantallas con un ancho máximo de 320px */
  .titulo_torneo {
margin-top: 20%;
text-align: center;
  text-shadow: 0 0 6px rgb(255, 255, 255);
  color: #ffffff;
  font-size: 160%;
  width: 100%;
  margin-left: 20%;
}
.main-container {
  padding: 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-top: 2%;
  margin-left: 33%;
  width: 65%;
  text-align: center;
}
  
}


@media (min-width: 321px) and (max-width:480px) {
  /* Estilos para pantallas con un ancho máximo de 320px */
  .titulo_torneo {
margin-top: 20%;
text-align: center;
  text-shadow: 0 0 6px rgb(255, 255, 255);
  color: #ffffff;
  font-size: 160%;
  width: 100%;
  margin-left: 20%;
}
.main-container {
  padding: 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-top: 2%;
  margin-left: 28%;
  width: 70%;
  text-align: center;
}
  
}




@media (min-width: 481px) and (max-width: 600px) {
  /* Estilos para pantallas entre 481px y 600px */
  .titulo_torneo {
margin-top: 20%;
  text-shadow: 0 0 6px rgb(255, 255, 255);
  color: #000000;
  font-size: 160%;
  margin-left: 40%;
}
.main-container {
  padding: 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-top: 2%;
  margin-left: 17%;
  width: 60%;
  text-align: center;
}
}







@media (min-width: 601px) and (max-width: 768px) {
  /* Estilos para pantallas entre 601px y 768px */
  .titulo_torneo {
margin-top: 20%;
  text-shadow: 0 0 6px rgb(255, 255, 255);
  color: #000000;
  font-size: 160%;
  margin-left: 40%;
}
.main-container {
  padding: 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-top: 2%;
  margin-left: 6%;
  width: 70%;
  text-align: center;
}
}


@media (min-width: 769px) and (max-width: 1024px) {
  /* Estilos para pantallas entre 769px y 1024px */
  .titulo_torneo {
margin-top: 20%;
  text-shadow: 0 0 6px rgb(255, 255, 255);
  color: #000000;
  font-size: 205%;
  margin-left: 20%;
}
.main-container {
  padding: 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-top: 2%;
  margin-left: 5%;
  width: 100%;
  text-align: center;
}
}


@media (min-width: 1025px) and (max-width: 1280px) {
  /* Estilos para pantallas entre 1025px y 1280px */
  .titulo_torneo {
margin-top: 20%;
  text-shadow: 0 0 6px rgb(255, 255, 255);
  color: #000000;
  font-size: 205%;
  margin-left: 20%;
}
.main-container {
  padding: 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-top: 2%;
  margin-right: 0%;
  width: 100%;
  text-align: center;
}
}

@media (min-width: 1281px) and (max-width: 1440px) {
  /* Estilos para pantallas entre 1281px y 1440px */
  .titulo_torneo {
margin-top: 20%;
  text-shadow: 0 0 6px rgb(255, 255, 255);
  color: #000000;
  font-size: 205%;
  margin-left: 20%;
}
.main-container {
  padding: 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-top: 2%;
  margin-right: 0%;
  width: 100%;
  text-align: center;
}
}



@media (min-width: 1441px) and (max-width: 1920px) {
  /* Estilos para pantallas entre 1441px y 1920px */
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
  