import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from '../src/rutas/rutas'


createApp(App)
.use(router)
.mount('#root')
