<script setup lang="ts">


import { ref, markRaw, onMounted } from 'vue';


import Menu from './components/menu.vue';
import Tocar from './pages/tocar.vue';
import Listas from './pages/listas.vue';
import Configuracion from './pages/configuracion.vue';
import { Cancion } from './modelo/cancion';
import { Acordes } from './modelo/acordes';
import { Letra } from './modelo/letra';
import { Cliente } from './modelo/client_socketio';

import { AdminListasURL } from './modelo/AdminListasURL';

const nro_cancion = ref(0);
const compas = ref(-1);
const cancion  = ref(new Cancion("no song name", "no band name", new Acordes([], []), new Letra([])));

const width = ref(window.innerWidth); 
const height = ref(window.innerHeight);
const viendo = ref("tocar");
let cliente = new Cliente("http://192.168.0.202:8080/")
const updateDimensions = () => { width.value = window.innerWidth; height.value = window.innerHeight; };

const generadorlistasURL = new AdminListasURL('/data');
generadorlistasURL.GetCancionxTema('intoxicados', 'casi-sin-pensar').then((cancion_obtenida) => {
    cancion.value = cancion_obtenida;
    
    }); 
    

onMounted(() => { 
    console.log("APP MONTADA")
    window.addEventListener('resize', updateDimensions);
});

function acciono(valor: string) {
    console.log("ACCIONO", valor);
    viendo.value = valor;    
}


</script>

<template>
    <div>

       

  <Menu :titulo="cancion.cancion" :viendo_vista="viendo" @acciono="acciono" :compas="compas" :cancion="cancion" :cliente="cliente"></Menu>

  <div class="pantalla">
    <Tocar v-if="viendo=='tocar'" :titulo="cancion.cancion" :viendo_vista="viendo" :compas="compas" :cancion="cancion"></Tocar>
    <Listas v-if="viendo=='listas'" :titulo="cancion.cancion" :viendo_vista="viendo" :compas="compas" :cancion="cancion"></Listas>
    <Configuracion v-if="viendo=='config'"></Configuracion>

    
  </div>
  <div class="fixed-bottom-right"><p>Anchura: {{ width }} px</p> <p>Altura: {{ height }} px</p>
  </div>
</div>
</template>

<style scoped>

#contenedor-musical {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.cancion {
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
}

.fixed-bottom-right {
  position: fixed;
  bottom: 0;
  right: 0;
  z-index: 9999; /* Asegura que se muestre encima de otros elementos */
}

</style>
