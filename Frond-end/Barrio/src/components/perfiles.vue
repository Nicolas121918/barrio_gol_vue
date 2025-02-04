<template>
  <header>
    <Headerapp></Headerapp>
  </header>
  <div class="profile-container">
    <!-- Botón de Volver -->
    <button class="back-button" @click="goBack">Volver</button>

    <div class="usuario">
      <!-- Información del equipo o mensaje de 'Jugador sin equipo' -->
      <div class="team-info" v-if="team.name" @mouseover="isTeamInfoVisible = true" @mouseleave="isTeamInfoVisible = false">
        <img class="team-logo" :src="team.logo" alt="Logo del equipo" />
        <div class="team-hover-info" v-if="isTeamInfoVisible || isTeamInfoClicked" @click="toggleTeamInfo">
          <p><span class="label">Nombre:</span> <strong class="value">{{ team.name }}</strong></p>
          <p><span class="label">Ciudad:</span> <strong class="value">{{ team.city || 'N/A' }}</strong></p>
          <p><span class="label">Descripción:</span> <strong class="value">{{ team.description || 'N/A' }}</strong></p>
          <button v-if="team.name" @click.stop="sendJoinRequest" class="join-button">Enviar solicitud al equipo</button>
        </div>
      </div>
      <div v-else class="no-team-info">
        <p><strong>Jugador sin equipo</strong></p>
      </div>

      <!-- Perfil del usuario -->
      <div class="profile-info">
        <div class="profile-header">
          <!-- Foto de perfil que se puede hacer clic para mostrar en grande -->
          <img 
            class="profile-picture" 
            :src="userProfile.picture" 
            alt="Foto de perfil" 
            @click="showImage = true" 
          />
          <div class="user-details">
            <h2>{{ userProfile.name }}</h2>
            <p>Ciudad: {{ userProfile.city }}</p>
            <p>Edad: {{ userProfile.age }}</p>
            <p>Posición: {{ userProfile.position }}</p>
            <p>Email: {{ maskedEmail }}</p>
            <p><strong>Descripción:</strong> {{ userProfile.description }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal para mostrar la foto en grande -->
    <div v-if="showImage" class="image-modal" @click="showImage = false">
      <img :src="userProfile.picture" alt="Foto de perfil grande" class="large-image" />
    </div>

    <!-- Videos del usuario -->
    <div class="videos-section">
      <h3>Videos del Usuario</h3>
      <div class="videos-grid">
        <div class="video-card" v-for="video in userProfile.videos" :key="video.id">
          <div class="video-content">
            <router-link id="letra" class="link perfil" to="/Perfil">
              <!-- Video sin botones, solo el video que inicia/pausa al pasar el mouse -->
              <video
                ref="video"
                :src="video.url"
                class="video"
                @mouseover="playVideo($event)"
                @mouseleave="pauseVideo($event)"
                :title="video.title"
              >
                Tu navegador no soporta el video.
              </video>
              <p>{{ video.title }}</p>
            </router-link>
          </div>
        </div>
      </div>
    </div>  
  </div>
</template>

<script>
import Headerapp from './Headerapp.vue';
export default {
  components :{
    Headerapp
  },
  data() {
    return {
      isTeamInfoVisible: false,
      isTeamInfoClicked: false,
      showImage: false, // Variable para controlar si el modal se muestra
      userProfile: {
        picture: 'https://dthezntil550i.cloudfront.net/f4/latest/f41908291942413280009640715/1280_960/1b2d9510-d66d-43a2-971a-cfcbb600e7fe.png',
        name: 'Sebastián Barrantes',
        city: 'Bogotá',
        age: 26,
        position: 'Delantero',
        email: 'barrantessebastian261@gmail.com',
        description: 'Jugador apasionado con grandes sueños y metas en el mundo del deporte.',
        videos: [
          { id: 1, url: 'https://www.w3schools.com/html/movie.mp4', title: 'Gol en el partido contra equipo X' },
          { id: 2, url: 'https://www.w3schools.com/html/movie.mp4', title: 'Entrenamiento con el equipo' },
          { id: 3, url: 'https://www.w3schools.com/html/movie.mp4', title: 'Gol en el partido contra equipo Y' },
        ]
      },
      team: {
        logo: 'https://www.designevo.com/res/templates/thumb_small/brown-badge-and-white-football.webp',
        name: "null",
        city: 'Medellín',
        description: "los mejores jaja"
      }
    };
  },
  computed: {
    maskedEmail() {
      const emailParts = this.userProfile.email.split('@');
      const maskedName = emailParts[0].slice(0, 8) + '*******';
      return `${maskedName}@${emailParts[1]}`;
    }
  },
  methods: {
    playVideo(event) {
      event.target.play();
    },
    pauseVideo(event) {
      event.target.pause();
    },
    toggleTeamInfo() {
      this.isTeamInfoClicked = !this.isTeamInfoClicked;
    },
    sendJoinRequest(event) {
      event.stopPropagation();
      alert('Solicitud enviada al equipo');
    },
    goBack() {
      this.$router.go(-1);
    },
    showProfileImage() {
      this.showImage = true;
    },
    closeProfileImage() {
      this.showImage = false;
    }
  }
};
</script>


<style scoped>
.profile-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
  background-color: rgb(0, 0, 0);
  width: 155%;
  margin-left: -24%;
  border: solid white;
  box-shadow: 0 0 30px rgb(0, 0, 0);
  margin-top: 17%;
}

.back-button {
  padding: 10px 20px;
  background-image: url("https://static.vecteezy.com/system/resources/thumbnails/000/549/015/small/vector-apr-2018-19.jpg");
  color: rgb(0, 0, 0);  
  border: 3px solid white;
  text-shadow: rgb(223, 0, 0) 0 0 40px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  z-index: 10;
  margin-right: 100%;
}

.back-button:hover {
  font-size: 1.2rem;
  color: white;
  transform: scale(1);
  box-shadow: 0 0 40px white;
}
.team-hover-info {
  position: absolute;
  color: #201f1f;
  text-align: left;
  top: 0;
  right: 70px;
  background-color: white;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.2);
  width: 230px;
  font-size: 1rem;
  transition: all 0.4s ease-in-out;
  animation: fadeIn 0.6s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.team-hover-info p {
  margin: 10px 0;
  line-height: 1.6;
}

.team-hover-info .label {
  font-weight: bold;
  color: black;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}

.team-hover-info .value {
  color: rgb(48, 48, 48);
  font-weight: normal;
}

.team-hover-info .join-button {
  display: block;
  margin-top: 15px;
  background-color: gold;
  color: black;
  border: none;
  padding: 12px 18px;
  font-size: 1rem;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.team-hover-info .join-button:hover {
  background-color: #d4af37;
  transform: scale(1.05);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}

.team-hover-info:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
}

.profile-info {
  width: 100%;
  display: flex;
  justify-content: center;
  margin-bottom: 30px;
}

.profile-header {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 20px;
}

.profile-picture {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  border: solid rgb(255, 166, 2);
  box-shadow: 0 0 10px white;
}
.profile-picture:hover{
    transform: scale(1.1);
    box-shadow: 0 0 20px rgb(255, 230, 9);
    
}

.user-details h2 {
  margin: 0;
  color: white;
  font-size: 220%;
  font-family: Georgia, 'Times New Roman', Times, serif;
  text-align: center;
  border-bottom: 0.5px solid white;
  text-shadow: 0 0 10px rgb(255, 174, 0);
}
.user-details h2:hover {
    transform: scale(1.2);
    text-shadow: 0 0 20px rgb(255, 255, 255);
}

.user-details p {
  margin: 5px 0;
  font-size: 1.1rem;

  
}

.team-info {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  position: relative;
  margin-bottom: 30px;
  cursor: pointer;
  width: 20%;
  margin-left: 100%
}

.team-logo {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  object-fit: cover;
  border: solid black;
  box-shadow: 0 0 20px white;
}
.team-logo:hover{
    transform: scale(1.1);
}


.no-team-info {
  font-size: 1.5rem;
  color: #949494;
  margin-left: 70%;
}

.videos-section {
    border-top: 0.5px solid white;
  width: 100%;
  margin-top: 2%;
  display: flex;
  flex-direction: column;
  align-items: center;
  
}
.usuarios{
    display: flex;
    flex-direction: row;
}
.videos-section h3 {
  font-size: 2.2rem;
  margin-bottom: 20px;
  
  font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
  color: white;
  text-shadow: 0 0 10px white;
  border: 2px solid white;
  margin-bottom: 3%;
  padding: 1%;
  box-shadow: 0 0 4px #ddd;
}

.videos-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  width: 100%;
}
.video-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 5px;
  background-color: #030303;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s;
  border: solid white;
  box-shadow: 0 0 10px#949494;
}

.video-card:hover {
  transform: scale(1.05);
  box-shadow: 0 0 20px#ffc400;
}

.video-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  
}
.image-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.image-modal .large-image {
  max-width: 90%;
  max-height: 90%;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  animation: fadeIn 0.3s ease-in-out;
}

/* Animación para que el modal aparezca suavemente */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
video {
  width: 100%;
  height: 200px;
  border-radius: 8px;
  margin-bottom: 10px;
  object-fit: cover;
  border: 1px solid white;
  box-shadow: 0 0 5px#949494;
}

#letra {
  font-size: 1rem;
  color: #ffffff;
}
#letra:hover{
    color: #ffffff; /* Cambia el color del enlace al pasar el ratón */
    background-color: transparent; 
}


#letra-link:focus {
  outline: none; /* Asegura que no aparezca el borde en el foco */
}

</style>
