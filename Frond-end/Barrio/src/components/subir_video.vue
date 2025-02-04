<template>

  <header>
    <headerapp></headerapp>
  </header>
      <router-link to="/videos" class="volver">
      <button class="volver-button">Volver</button>
    </router-link>
  <div class="video">
    <h1>¡Sube Aquí Tu Video!</h1>
    <form @submit.prevent="subirVideo">
      <input class="selectvideo" type="file" accept="video/*" @change="seleccionarVideo" />
      <input type="hidden" v-model="documento_user_video" />
      <button type="submit" class="subirboton">Subir Video</button>
    </form>
    <div v-if="mensaje" class="mensaje">
      {{ mensaje }}
    </div>
  </div>
</template>

<script setup>
import Headerapp from "./Headerapp.vue";
import { ref, onMounted } from "vue";
import axios from "axios";

// Variables reactivas
const videoSeleccionado = ref(null);
const documento_user_video = ref('');
const mensaje = ref("");




onMounted(() => {
  const documents = JSON.parse(localStorage.getItem('documents'));
  if (documents) {
    documento_user_video.value = documents.id;
  } else {
    console.error('No se encontró usuario en localStorage');
  }
});

const seleccionarVideo = (event) => {
  videoSeleccionado.value = event.target.files[0];
};

const subirVideo = async () => {
  if (!videoSeleccionado.value) {
    mensaje.value = "Por favor selecciona un video.";
    return;
  }

  const formData = new FormData();
  formData.append("video", videoSeleccionado.value);
  formData.append("documento_usuario", documento_user_video.value);

  try {
    const response = await axios.post("http://localhost:8000/subirvideo", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    mensaje.value = response.data.mensaje;
  } catch (error) {
    console.error(error);
    mensaje.value = "Ocurrió un error al subir el video.";
  }
};
</script>

<style scoped>
/* Estilo para el contenedor del video */
.video {
  background: linear-gradient(135deg, #54524c88, #12120436, #4e4d4aa7); /* Gradiente de colores vibrantes */
  border-radius: 12px; /* Bordes redondeados */
  padding: 2.5rem; /* Espaciado interno */
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2); /* Sombra sutil */
  max-width: 500px; /* Ancho máximo */
  width: 100%; /* Asegura que ocupe todo el ancho disponible */
  position: absolute; /* Posicionamiento absoluto */
  top: 50%; /* Centrado vertical */
  left: 50%; /* Centrado horizontal */
  transform: translate(-50%, -50%); /* Ajusta el contenedor para centrarlo perfectamente */
  text-align: center; /* Centrado del contenido */
  backdrop-filter: blur(6px); /* Desenfoque suave al fondo */
  display: flex;
  flex-direction: column;
  gap: 20px; /* Espaciado entre los elementos */
  box-sizing: border-box; /* Asegura que el padding no afecte el tamaño total */
  color: #000000ea; /* Texto blanco para buen contraste */
}


/* Estilo para el título */
h1 {
  font-size: 2rem; /* Tamaño de fuente más grande */
  color: #ffffff; /* Color oscuro para el título */
  margin-bottom: 20px; /* Espacio debajo del título */
  font-weight: 600; /* Negrita para el título */

}

.selectvideo{
  background-color: #847d20;
}

/* Estilo para el formulario */
form {
  display: flex;
  flex-direction: column; /* Alineación vertical */
  gap: 20px; /* Espaciado entre los campos */
  width: 100%; /* Asegura que el formulario ocupe el ancho completo */
}

/* Estilo para el campo de archivo */
input[type="file"] {
  padding: 14px; /* Relleno para el input */
  border-radius: 8px; /* Bordes redondeados */
  border: 2px solid #ccc; /* Borde gris claro */
  background-color: #f7f7f7; /* Fondo gris claro */
  font-size: 16px; /* Tamaño de fuente adecuado */
  width: 100%; /* Asegura que ocupe todo el ancho */
  box-sizing: border-box; /* Para que el padding no afecte el tamaño total */
  transition: border-color 0.3s ease; /* Transición suave para el borde */
}

/* Estilo para el botón */
.subirboton {
  padding: 14px 20px; /* Relleno adecuado para el botón */
  background-color: #000000; /* Color de fondo negro (si quieres mantenerlo como fondo de reserva) */
  background-image: url('https://i.pinimg.com/736x/82/77/8d/82778d6d72c05cf2808e3bd2bcaeb823.jpg'); /* Imagen de fondo */
  background-size: cover; /* Asegura que la imagen cubra todo el fondo del botón */
  background-position: center; /* Centra la imagen dentro del botón */
  color: rgb(0, 0, 0); /* Color del texto blanco */
  border: none; /* Sin borde */
  border-radius: 8px; /* Bordes redondeados */
  cursor: pointer; /* Cursor de puntero */
  font-size: 16px;
  transition: background-color 0.3s ease; /* Transición suave para el color de fondo */
  width: 50%; /* Asegura que el botón ocupe el 50% del ancho del contenedor */
  box-sizing: border-box; /* Para que el padding no afecte el tamaño total */
  margin: 0 auto; /* Centrado horizontal */
  display: block; /* Asegura que el margen de auto funcione */
}

.subirboton:hover{
  transform: scale(1.1); /* Aumenta el tamaño del botón un 10% */
}




button:disabled {
  background-color: #ccc; /* Color gris cuando el botón está deshabilitado */
  cursor: not-allowed; /* Cursor de "no permitido" */
}

/* Estilo para el mensaje */
.mensaje {
  margin-top: 20px;
  padding: 12px;
  border-radius: 8px; /* Bordes redondeados */
  background-color: #f7e0e0; /* Fondo verde claro */
  color: #000000; /* Texto verde */
  text-align: center; /* Centrado del mensaje */
  font-size: 14px;
}

/* Estilo para el mensaje de error */
.mensaje.error {
  background-color: #f8d7da; /* Fondo rojo claro para errores */
  color: #842029; /* Texto rojo */
  border-color: #842029; /* Borde rojo para el mensaje de error */
}


.volver {
  position: absolute;
  top: 150px; /* Ajustamos la distancia desde la parte superior */
  left: 10px; /* Pegamos a la izquierda */
  z-index: 1000; /* Aseguramos que esté por encima de otros elementos */
}

.volver-button {
  padding: 10px 20px;
  background-color: #ff04008b;
  font-weight: bold;
  color: rgb(255, 255, 255);
  border: none;
  width: 100px;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

.volver-button:hover{
  transform: scale(1.1); /* Aumenta el tamaño del botón un 10% */
}



</style>
