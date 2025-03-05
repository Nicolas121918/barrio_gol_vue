<template>

  <header>
    <headerapp></headerapp>

  </header>

  
  <form  @submit.prevent="Insertar_team" class="crear_equipo_form">
    <div class="crear_equipo_form-title"><span>CREA TU EQUIPO</span></div>

    <div class="crear_equipo_input-container">
      <input v-model="nombreteam" class="crear_equipo_input" type="text" placeholder="Nombre del equipo" required />
    </div>

    <div class="crear_equipo_input-container">
      <textarea v-model="Descripcion" class="crear_equipo_input" placeholder="Descripcion del equipo" required></textarea>
    </div>

    <div class="crear_equipo_input-container">
      <input v-model="numeropeople" class="crear_equipo_input" type="number" required placeholder="Numero de Integrantes" />
    </div>

    <div class="crear_equipo_input-container">
      <input v-model="capitanteam" class="crear_equipo_input" type="text" required placeholder="Capitan Del equipo" />
    </div>

    <div class="crear_equipo_input-container">
      <input v-model="requisitos_join" class="crear_equipo_input" type="text" required placeholder="Requisitos del equipo" />
    </div>

    <div class="crear_equipo_input-container">
      <input v-model="location" class="crear_equipo_input" type="text" placeholder="Ciudad del equipo" required />
    </div>

   
    <div class="crear_equipo_input-container">
      <label class="logotext">Logo del equipo</label>
      <input type="file" @change="onFileChange" accept="image/jpeg, image/png" />
  </div>


 
  <button class="contacto_boton" type="submit">Enviar</button>
  </form>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import Swal from 'sweetalert2';
import Headerapp from './Headerapp.vue';

// Variables reactivas
const nombreteam = ref('');
const Descripcion = ref('');
const numeropeople = ref('');
const capitanteam = ref('');
const requisitos_join = ref('');
const location = ref('');
const logoTeam = ref('');

// Obtener los datos del usuario desde localStorage al cargar el componente
onMounted(() => {
  const datosusuario = JSON.parse(localStorage.getItem('usuario'));
  console.log(datosusuario); // Verifica la estructura del objeto almacenado
  if (datosusuario && datosusuario.nombreUsuario) {
    capitanteam.value = datosusuario.nombreUsuario;  // Asigna el nombre del usuario al campo de capitanteam
  }
});


const onFileChange = (event) => {
  logoTeam.value = event.target.files[0];
};

const Insertar_team = async () => {
  const formData = new FormData();
  formData.append('nombreteam', nombreteam.value);
  formData.append('Descripcion', Descripcion.value);
  formData.append('numeropeople', numeropeople.value);
  formData.append('capitanteam', capitanteam.value);
  formData.append('requisitos_join', requisitos_join.value);
  formData.append('location', location.value);

  if (logoTeam.value) {
    formData.append('logoteam', logoTeam.value);
  }
  if (!nombreteam.value || !Descripcion.value || !numeropeople.value && numeropeople.value==0  || !capitanteam.value || !requisitos_join.value || !location.value) {
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'Por favor, completa todos los campos antes de enviar.',
      });
      return;
    }
  try {
    const insertar = await axios.post('http://localhost:8000/Teams', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    const Equipos = {
      nombreteam: insertar.data.nombreteam,
      Descripcion: insertar.data.Descripcion,
      numeropeople: insertar.data.numeropeople,
      capitanteam: insertar.data.capitanteam,
      requisitos_join: insertar.data.requisitos_join,
      location: insertar.data.location,
      logoTeam: insertar.data.logoTeam,
    };

    console.log('Respuesta del servidor:', insertar);
    localStorage.setItem('Equipos', JSON.stringify(Equipos));

    

    if (insertar.status == 200) {
      Swal.fire({
        timer: 2000,
        icon: 'success',
        title: 'PERFECTO',
        text: 'Tu Equipo Se ha Creado Correctamente',
      });
    }

    // Limpiar los campos después de enviar el formulario
    nombreteam.value = '';
    Descripcion.value = '';
    numeropeople.value = '';
    capitanteam.value = '';
    requisitos_join.value = '';
    location.value = '';
    logoTeam.value = '';
  } catch (error) {
    console.error(error);
  }
};
</script>

<style scoped>
/* Fondo y estilo general del formulario */
.crear_equipo_form {
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  display: block;
  padding: 1.5rem; /* Reduce el padding para que sea más pequeño */
  max-width: 350px; /* Ajusta el máximo ancho del formulario */
  background: linear-gradient(135deg, #1695c049 0%, rgba(104, 169, 180, 0.612) 100%); /* Gradiente dorado suave con naranja oscuro */
  border-radius: 10px;
  border: none;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
  z-index: 1;
  margin-top: 20%; /* Reduce el margen superior para centrar mejor */
  margin-left: 20%;
  text-align: center; /* Centrado del contenido dentro del formulario */
  width: 200%; /* Asegura que ocupe todo el ancho disponible pero con el max-width limitado */
  max-width: 350px; /* Ajusta el máximo ancho del formulario */
  backdrop-filter: blur(6px); /* Agrega un desenfoque suave al fondo */
  background-size: cover; /* Asegura que el fondo ocupe toda el área */
  color: #fff; /* Asegura que el texto sea blanco para un buen contraste */
}


/* Efecto adicional de brillo suave */
.crear_equipo_form::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 140, 0, 0.1); /* Añade un filtro dorado suave para no sobrecargar */
  border-radius: 10px;
  z-index: -1;
}



/* Título del formulario */
.crear_equipo_form-title {
  text-align: center;
  color: #000000;
  font-size: 28px;
  font-weight: bold;
  margin-bottom: 20px;
}

/* Contenedor de los inputs */
.crear_equipo_input-container {
  position: relative;
  margin-bottom: 15px;
  color: #000000  ;
}


/* Estilo para todos los inputs y textarea */
.crear_equipo_input {
  outline: none;
  border: 2px solid #000000;
  border-radius: 5px;
  padding: 10px;
  font-family: 'Arial', sans-serif;
  font-size: 1rem;
  width: 100%;
  box-sizing: border-box;
  background-color: rgb(255, 255, 255);
  transition: all 0.3s ease-in-out;
}

/* Efecto de hover y foco para los inputs */
.crear_equipo_input:focus {
  border-color: #d4c600;
  background-color: #fff;
  box-shadow: 0 0 8px rgba(255, 251, 0, 0.6);
}
/* Estilo del botón de envío */
.contacto_boton {
  background-color: #ff4d00; /* Azul fuerte */
  color: rgb(0, 0, 0);
  padding: 12px;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: bold;
  width: 100%;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.contacto_boton:hover {
  background-color: #0056b3; /* Azul más oscuro al pasar el cursor */
  transform: translateY(-3px);
}

.contacto_boton:active {
  background-color: #004085; /* Azul aún más oscuro al hacer clic */
  transform: translateY(0);
}


/* Estilo del campo de archivo */
.crear_equipo_input[type="file"] {
  background-color: transparent;
  padding: 5px;
  border: none;
}

.crear_equipo_input[type="file"]:focus {
  outline: none;
  box-shadow: none;
}

/* Estilo del label para el logo */
.crear_equipo_input-container label {
  color: #fff;
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 8px;
  display: block;
  text-align: left;
}

/* Estilo para el mensaje de notificación */
.notification {
  text-align: center;
  color: #fff;
  font-size: 1rem;
  margin-top: 20px;
}

</style>
