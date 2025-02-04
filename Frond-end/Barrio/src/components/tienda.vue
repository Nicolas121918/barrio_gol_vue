<template>
  <header>
    <Headerapp></Headerapp>
  </header>
  <div class="store-container">
    <!-- Header -->
    <header class="store-header">
      <div class="logo">
        <h1>⚽ BarrioStore</h1>
      </div>
      <div class="search-bar">
        <input v-model="searchQuery" type="text" placeholder="Buscar productos..." />
        <button @click="searchProducts" class="search-btn">🔍</button>
      </div>
      <div class="icons">
        <span class="cart-icon" @click="toggleCart">🛒<span class="cart-count">{{ cart.length }}</span></span>
        <span class="favorites-icon" @click="toggleFavorites">❤️</span>
        <span class="settings-icon" @click="toggleSettings">⚙️</span>
      </div>
    </header>

    <!-- Opción para publicar artículos -->
    <div class="publish-item">
      <h2>Publicar nuevo artículo</h2>
      <form @submit.prevent="publishProduct">
        <input v-model="newProduct.name" type="text" placeholder="Nombre del producto" required />
        <textarea v-model="newProduct.description" placeholder="Descripción del producto" required></textarea>
        <input v-model="newProduct.price" type="number" placeholder="Precio" required />
        
        <!-- Input para cargar la imagen -->
        <input type="file" @change="handleImageUpload" required />
        <div v-if="newProduct.image">
          <img :src="newProduct.image" alt="Vista previa de la imagen" class="image-preview" />
        </div>

        <button type="submit" class="btn">Publicar artículo</button>
      </form>
    </div>

    <!-- Configuración -->
    <div v-if="settingsVisible" class="overlay" @click="toggleSettings">
      <div class="settings-panel" @click.stop>
        <h2>Opciones de Cuenta</h2>
        <router-link to="pay"><button @click="recargarCuenta" class="btn">💰 Recargar Cuenta</button></router-link>


        <button @click="verSaldo" class="btn">📊 Ver Saldo</button>
        <button @click="toggleSettings" class="btn close-settings-btn">Cerrar</button>
      </div>
    </div>

    <!-- Carrito de Compras -->
    <div v-if="cartVisible" class="overlay" @click="toggleCart">
      <div class="cart-panel" @click.stop>
        <h2>Carrito de Compras</h2>
        <div v-if="cart.length > 0">
          <div v-for="(product, index) in cart" :key="product.id" class="cart-item">
            <img :src="product.image" :alt="product.name" />
            <div>{{ product.name }} - ${{ product.price }}</div>
            <button @click="removeFromCart(index)" class="btn remove-btn">Eliminar</button>
          </div>
        </div>
        <div v-else>
          <p>Tu carrito está vacío.</p>
        </div>
        <button @click="toggleCart" class="btn close-btn">Cerrar</button>
      </div>
    </div>

    <!-- Favoritos -->
    <div v-if="favoritesVisible" class="overlay" @click="toggleFavorites">
      <div class="favorites-panel" @click.stop>
        <h2>Favoritos</h2>
        <div v-if="favorites.length > 0">
          <div v-for="(product, index) in favorites" :key="product.id" class="favorite-item">
            <img :src="product.image" :alt="product.name" />
            <div>{{ product.name }} - ${{ product.price }}</div>
            <button @click="removeFromFavorites(index)" class="btn remove-btn">Eliminar</button>
          </div>
        </div>
        <div v-else>
          <p>No tienes favoritos.</p>
        </div>
        <button @click="toggleFavorites" class="btn close-btn">Cerrar</button>
      </div>
    </div>

    <!-- Lista de Productos -->
    <div class="product-list">
      <div class="product-card" v-for="product in filteredProducts" :key="product.id">
        <div class="product-image">
          <img :src="product.image" :alt="product.name" />
        </div>
        <div class="product-info">
          <h3>{{ product.name }}</h3>
          <p>{{ product.description }}</p>
          <p class="price">${{ product.price }}</p>
          <div class="actions">
            <button @click="addToCart(product)" class="btn action-btn">🛍️ Agregar al Carrito</button>
            <button @click="addToFavorites(product)" class="btn action-btn">❤️ Favorito</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Headerapp from './Headerapp.vue';

export default {
  components: {
    Headerapp
  },
  data() {
    return {
      searchQuery: '',
      cart: [],
      favorites: [],
      settingsVisible: false,
      cartVisible: false,
      favoritesVisible: false,
      newProduct: {
        name: '',
        description: '',
        price: 0,
        image: ''
      },
      products: [
        { id: 1, name: 'Canilleras Nike', description: 'Protección máxima', price: 25, image: 'canilleras.jpg' },
        { id: 2, name: 'Balón Adidas', description: 'Balón profesional', price: 50, image: 'balon.jpg' },
        { id: 3, name: 'Guantes Puma', description: 'Guantes de portero', price: 30, image: 'guantes.jpg' }
      ],
      filteredProducts: []
    };
  },
  methods: {
    addToCart(product) {
      this.cart.push(product);
    },
    removeFromCart(index) {
      this.cart.splice(index, 1);
    },
    addToFavorites(product) {
      if (!this.favorites.includes(product)) {
        this.favorites.push(product);
      }
    },
    removeFromFavorites(index) {
      this.favorites.splice(index, 1);
    },
    searchProducts() {
      this.filteredProducts = this.products.filter(p => p.name.toLowerCase().includes(this.searchQuery.toLowerCase()));
    },
    toggleSettings() {
      this.settingsVisible = !this.settingsVisible;
    },
    toggleCart() {
      this.cartVisible = !this.cartVisible;
    },
    toggleFavorites() {
      this.favoritesVisible = !this.favoritesVisible;
    },

    verSaldo() {
      alert('Tu saldo actual es: $100');
    },
    publishProduct() {
      if (this.newProduct.name && this.newProduct.description && this.newProduct.price && this.newProduct.image) {
        const newId = this.products.length + 1;
        this.products.push({
          ...this.newProduct,
          id: newId
        });
        this.newProduct = { name: '', description: '', price: 0, image: '' };
        alert('Producto publicado exitosamente');
      } else {
        alert('Por favor complete todos los campos');
      }
    },
    handleImageUpload(event) {
      const file = event.target.files[0];
      const reader = new FileReader();
      reader.onload = () => {
        this.newProduct.image = reader.result; // Almacena la imagen en base64
      };
      reader.readAsDataURL(file);
    }
  },
  watch: {
    searchQuery() {
      this.searchProducts();
    }
  },
  mounted() {
    this.filteredProducts = this.products;
  }
};
</script>


<style scoped>
/* Estilos para la vista previa de la imagen */
.image-preview {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 10px;
  margin-top: 10px;
}
/* Contenedor principal */
.store-container {
  font-family: 'Inter', sans-serif;
  background-color: #121212;
  padding: 30px;
  color: #f5f5f5;
  margin-top: 18%;
}

/* Encabezado */
.store-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #1e1e1e;
  padding: 20px;
  border-radius: 15px;
  box-shadow: 0 4px 10px rgba(255, 255, 255, 0.1);
}

/* Barra de búsqueda */
.search-bar {
  display: flex;
  align-items: center;
  gap: 12px;
}

.search-bar input {
  padding: 12px;
  border: none;
  border-radius: 8px;
  width: 280px;
  font-size: 14px;
  background: #333;
  color: white;
  outline: none;
}

.search-btn {
  background: #ffcc00;
  color: #1e1e1e;
  padding: 12px 15px;
  border: none;
  cursor: pointer;
  border-radius: 8px;
  font-size: 14px;
  transition: background 0.3s, transform 0.2s;
}

.search-btn:hover {
  background: #ffaa00;
  transform: scale(1.1);
}

/* Íconos */
.icons {
  display: flex;
  gap: 20px;
}

.icons span {
  font-size: 1.8rem;
  cursor: pointer;
  transition: transform 0.2s;
}

.icons span:hover {
  transform: scale(1.15);
  color: #ffcc00;
}

/* Lista de productos */
.product-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-top: 30px;
}

/* Tarjeta de producto */
.product-card {
  background: #1e1e1e;
  padding: 20px;
  border-radius: 20px;
  box-shadow: 0 6px 15px rgba(255, 255, 255, 0.05);
  text-align: center;
  transition: transform 0.3s, box-shadow 0.3s;
}

.product-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 10px 20px rgba(255, 255, 255, 0.08);
}

.product-card img {
  max-width: 100%;
  border-radius: 15px;
}

/* Botones de acción */
.actions {
  display: flex;
  justify-content: center;
  gap: 12px;
  margin-top: 15px;
}

.actions button {
  padding: 14px 18px;
  background: #ffcc00;
  color: #1e1e1e;
  border: none;
  cursor: pointer;
  border-radius: 10px;
  font-weight: bold;
  transition: background 0.3s, transform 0.2s;
}

.actions button:hover {
  background: #ffaa00;
  transform: scale(1.08);
}

/* Panel de configuraciones */
.settings-panel {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #1e1e1e;
  padding: 25px;
  border-radius: 12px;
  box-shadow: 0 6px 15px rgba(255, 255, 255, 0.08);
  width: 280px;
  z-index: 1000;
}

.btn {
  background: #ffcc00;
  color: #1e1e1e;
  padding: 12px 15px;
  border: none;
  width: 100%;
  margin-bottom: 10px;
  cursor: pointer;
  border-radius: 8px;
  font-size: 14px;
  transition: background 0.3s;
}

.btn:hover {
  background: #ffaa00;
}

.close-settings-btn {
  background: #e74c3c;
}

.close-settings-btn:hover {
  background: #c0392b;
}

/* Panel de carrito */
.cart-panel, .favorites-panel {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #1e1e1e;
  padding: 25px;
  border-radius: 12px;
  box-shadow: 0 6px 15px rgba(255, 255, 255, 0.08);
  width: 300px;
  max-height: 80%;
  overflow-y: auto;
  z-index: 1000;
}

/* Overlay */
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  z-index: 999;
}

/* Botón de cerrar */
.close-btn {
  background: #e74c3c;
}

.close-btn:hover {
  background: #c0392b;
}

/* Productos en carrito */
.cart-item, .favorite-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 0;
}

.cart-item img, .favorite-item img {
  width: 50px;
  height: 50px;
  margin-right: 15px;
}

/* Botón eliminar */
.remove-btn {
  background: #ff4d4d;
  color: white;
  padding: 8px 12px;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.3s;
}

.remove-btn:hover {
  background: #e74c3c;
}

/* Estilos adicionales */
.publish-item {
  margin-top: 30px;
  background: #1e1e1e;
  padding: 20px;
  border-radius: 15px;
  box-shadow: 0 4px 10px rgba(255, 255, 255, 0.1);
}

.publish-item h2 {
  margin-bottom: 15px;
}

.publish-item input,
.publish-item textarea {
  width: 100%;
  padding: 12px;
  margin-bottom: 15px;
  border-radius: 8px;
  background: #333;
  color: white;
  border: none;
}

.publish-item button {
  background: #ffcc00;
  color: #1e1e1e;
  padding: 12px 15px;
  border: none;
  cursor: pointer;
  border-radius: 8px;
  font-size: 14px;
}

.publish-item button:hover {
  background: #ffaa00;
}
</style>
