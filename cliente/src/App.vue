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
import { item_lista } from './modelo/item_lista';
import { AdminListasTocables } from './modelo/AdminIndiceListas';
import { GetCanciones } from './modelo/GetCanciones';

const nro_cancion = ref(0);
const compas = ref(-1);
const cancion_ref  = ref(new Cancion("no song name", "no band name", new Acordes([], []), new Letra([])));
const width = ref(window.innerWidth); 
const height = ref(window.innerHeight);
const viendo = ref("config");
let cliente = new Cliente("http://192.168.0.202:8080/")
const updateDimensions = () => { width.value = window.innerWidth; height.value = window.innerHeight; };

const generadorlistasURL = new AdminListasURL('/data/canciones');

const ref_lista_actual = ref("default");
const canciones_Actual = ref([] as item_lista[]);
const admin_indiceslista = new AdminListasTocables();
canciones_Actual.value = admin_indiceslista.GetIndice(ref_lista_actual.value);



GetCanciones.obtenerCancion(canciones_Actual.value[0]).then((cancion_get: Cancion) => {
    cancion_ref.value = cancion_get;
});

    
    

onMounted(() => { 
    console.log("APP MONTADA")
    window.addEventListener('resize', updateDimensions);
});

function acciono(valor: string) {
    viendo.value = valor;    
}


</script>

<template>
    <div>

       

  <Menu :viendo_vista="viendo" @acciono="acciono" :compas="compas" :cancion="cancion_ref" :cliente="cliente"></Menu>
  <div class="pantalla">
    <Tocar v-if="viendo=='tocar'" :compas="compas" :cancion="cancion_ref"></Tocar>
    <Listas v-if="viendo=='listas'" :lista_actual="ref_lista_actual" ></Listas>
    <Configuracion v-if="viendo=='config'"></Configuracion>

    
  </div>

  <h1><p>Anchura: {{ width }} px</p> <p>Altura: {{ height }} px</p>
  </h1>
  
  
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
