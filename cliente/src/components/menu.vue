<script setup lang="ts">

import { Cancion } from '../modelo/cancion';
import ControladorTiempo from './ControladorTiempo.vue';
import ControladorSesion from './ControladorSesion.vue';
import { Cliente } from '../modelo/client_socketio';



const emit = defineEmits(['acciono']);
function acciono(valor: string) {
    emit('acciono', valor);
    
}
const props = defineProps<{ titulo: string, viendo_vista: string, compas: number, cancion: Cancion, cliente: Cliente  }>()
if (props.viendo_vista == undefined) 
  console.log("Viendo vista no definida")
</script>

<template>
  <div class="navbar">
    <div class="marca">
      <a class="navbar-brand" href="#">Cancionero</a>
    </div>

    
          <div class="marca-item">
            <p class="nav-link" :class="{active: viendo_vista == 'tocar'}" aria-current="page"  @click="acciono('tocar')">Tocar</p>	
          </div>

          <ControladorTiempo :compas=compas :cancion="cancion">
        </ControladorTiempo> 

          <div class="nav-item">
            <p class="nav-link" :class="{active: viendo_vista == 'listas'}" aria-current="page"  @click="acciono('listas')">Listas</p>
          </div>
          
          <ControladorSesion :compas=compas :cancion="cancion" :cliente="cliente">
        </ControladorSesion>
          
          <div class="nav-item">
            <p class="nav-link" :class="{active: viendo_vista == 'config'}" aria-current="page" @click="acciono('config')">Configuración</p>
          </div>
    
    </div>
</template>

<style scoped>
body {
  font-size: 20px; /* Hacer las letras más grandes */
  background-color: #F5DEB3; /* Color claro, como un papel viejo */
  color: #333; /* Color de texto gris oscuro para mejor contraste */
  font-family: 'Arial', sans-serif; /* Cambiar a una fuente moderna */
}

.navbar {
  background-color: #FFF;
  padding: 10px;
}

.navbar-brand {
  color: #8B4513; /* Color marrón para un estilo de papel viejo */
  font-size: 42px; /* Aumentar tamaño de la marca */
  text-decoration: none;
}

.nav-link {
  color: #8B4513;
  text-decoration: none;
  padding: 5px 10px;
}

.nav-link.active {
  font-weight: bold;
  font-size: 22px; /* Aumentar el tamaño de la letra para el enlace activo */
}

.navbar-toggler {
  border: none;
  background-color: transparent;
}

.navbar-toggler-icon {
  display: inline-block;
  width: 30px;
  height: 30px;
  background-color: #8B4513;
}

.navbar-collapse {
  display: flex;
  flex-direction: column;
}

.nav-item {
  list-style: none;
}

.navbar-nav {
  display: flex;
  flex-direction: column;
}

.dropdown-menu {
  display: none;
  flex-direction: column;
  padding: 0;
  margin: 0;
}

.nav-item.dropdown:hover .dropdown-menu {
  display: flex;
}

.dropdown-item {
  padding: 5px 10px;
  color: #8B4513;
  text-decoration: none;
}
</style>
