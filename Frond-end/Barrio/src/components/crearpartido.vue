<template>
    <header>
      <Headerapp></Headerapp>
    </header>
    <div class="form-container">
      <form @submit.prevent="crearPartido">
        <h1>Crear Partido de Fútbol</h1>
  
        <!-- Nombre del partido -->
        <div class="form-group">
          <label for="nombre">Nombre del Partido:</label>
          <input type="text" id="nombre" v-model="form.nombre" placeholder="Nombre del partido" required />
        </div>
  
        <!-- Fecha del partido -->
        <div class="form-group">
          <label for="fecha">Fecha:</label>
          <input type="date" id="fecha" v-model="form.fecha" required />
        </div>
  
        <!-- Hora del partido -->
        <div class="form-group">
          <label for="hora">Hora:</label>
          <input type="time" id="hora" v-model="form.hora" required />
        </div>
  
        <!-- Equipos participantes -->
        <div class="form-group">
          <label for="equipoLocal">Equipo Local:</label>
          <input type="text" id="equipoLocal" v-model="form.equipoLocal" placeholder="Nombre del equipo local" required />
        </div>
        <div class="form-group">
          <label for="equipoVisitante">Equipo Visitante:</label>
          <input type="text" id="equipoVisitante" v-model="form.equipoVisitante" placeholder="Nombre del equipo visitante" required />
        </div>
  
        <!-- Ubicación del partido -->
        <div class="form-group">
          <label for="ubicacion">Ubicación:</label>
          <input type="text" id="ubicacion" v-model="form.ubicacion" placeholder="Ubicación del partido" required />
        </div>
  
        <!-- Arbitro del partido -->
        <div class="form-group">
          <label for="arbitro">Árbitro:</label>
          <input type="text" id="arbitro" v-model="form.arbitro" placeholder="Nombre del árbitro" required />
        </div>
  
        <!-- Costo de entrada -->
        <div class="form-group">
          <label for="costoEntrada">Costo de Entrada ($):</label>
          <input type="number" id="costoEntrada" v-model="form.costoEntrada" min="0" required placeholder="Monto de entrada" />
        </div>
  
        <!-- Estado del partido -->
        <div class="form-group">
          <label for="estado">Estado del Partido:</label>
          <select id="estado" v-model="form.estado" required>
            <option value="programado">Programado</option>
            <option value="en_curso">En curso</option>
            <option value="terminado">Terminado</option>
          </select>
        </div>
  
        <div class="form-group">
            <router-link to="/diego"><button type="submit" class="centered-button">Crear Partido</button></router-link>
          
        </div>
      </form>
    </div>
  </template>
  
  <script>
  import Headerapp from './Headerapp.vue';
  import axios from 'axios';
  
  export default {
    components: {
      Headerapp,
    },
    data() {
      return {
        form: {
          nombre: '',
          fecha: '',
          hora: '',
          equipoLocal: '',
          equipoVisitante: '',
          ubicacion: '',
          arbitro: '',
          costoEntrada: '',
          estado: 'programado',
        },
      };
    },
    methods: {
      async crearPartido() {
        const datosenviar = {
          nombre: this.form.nombre,
          fecha: this.form.fecha,
          hora: this.form.hora,
          equipoLocal: this.form.equipoLocal,
          equipoVisitante: this.form.equipoVisitante,
          ubicacion: this.form.ubicacion,
          arbitro: this.form.arbitro,
          costoEntrada: this.form.costoEntrada,
          estado: this.form.estado,
        };
  
        try {
          const response = await axios.post("http://localhost:8000/crearPartido", datosenviar);
          console.log("Partido creado con éxito:", response.data);
          alert(`Partido creado con éxito!`);
  
          // Limpiar el formulario después de enviar los datos
          this.form = {
            nombre: '',
            fecha: '',
            hora: '',
            equipoLocal: '',
            equipoVisitante: '',
            ubicacion: '',
            arbitro: '',
            costoEntrada: '',
            estado: 'programado',
          };
  
        } catch (error) {
          console.error("Error al crear el partido:", error);
          alert("Hubo un error al crear el partido");
          console.log("Detalles del error:", error.response?.data);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .form-container {
    width: 500px;
    max-width: 600px;
    margin-top: 70px;
    padding: 20px;
    border-radius: 10px;
    border: 2px solid #d4af37; /* Dorado */
    background: linear-gradient(to bottom, #fff8e1, #f0e68c); /* Amarillo suave */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin-bottom: 50px;
    margin-left: 15%;
  }
  
  h1 {
    text-align: center;
    font-size: 24px;
    color: #d4af37; /* Dorado */
  }
  
  .form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
  }
  
  label {
    font-weight: bold;
    margin-bottom: 5px;
    color: #d4af37; /* Dorado */
  }
  
  input,
  select {
    padding: 8px;
    font-size: 16px;
    border-radius: 5px;
    border: 1px solid #d4af37; /* Dorado */
  }
  
  input:focus,
  select:focus {
    border-color: #b8860b; /* Dorado oscuro */
  }
  
  button {
    background-color: #d4af37; /* Dorado */
    color: white;
    padding: 10px 20px;
    font-size: 18px;
    border-radius: 5px;
    cursor: pointer;
    text-align: center;
    width: 100%;
    border: none;
  }
  
  button:hover {
    background-color: #b8860b; /* Dorado oscuro */
  }
  
  .centered-button {
    display: block;
    margin: 10px auto;
  }
  
  @media (max-width: 600px) {
    .form-container {
      width: 90%;
      padding: 15px;
    }
  }
  </style>
  