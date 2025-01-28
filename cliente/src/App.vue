<script setup lang="ts">


import { ref, markRaw, onMounted } from 'vue';


import Menu from './components/menu.vue';
import Tocar from './pages/tocar.vue';
import Listas from './pages/listas.vue';
import Configuracion from './pages/configuracion.vue';
import { Cancion } from './modelo/cancion';
import { Letra } from './modelo/letra';
import { Acordes } from './modelo/acordes';
import { EstadoSesion } from './modelo/estadosesion';
import { Cliente }  from './modelo/client_socketio';
import { Director } from './modelo/director';
import { AdminListasURL } from './modelo/AdminListasURL';
import { item_lista } from './modelo/item_lista';
import { AdminListasTocables } from './modelo/AdminIndiceListas';
import { GetCanciones } from './modelo/GetCanciones';


// ENTORNO
const width = ref(window.innerWidth); 
const height = ref(window.innerHeight);
const updateDimensions = () => { width.value = window.innerWidth; height.value = window.innerHeight; };
const viendo = ref("tocar");

// LISTAS
const ref_lista_actual = ref("default");
const admin_indiceslista = new AdminListasTocables();

// CANCIONES
const nro_cancion = ref(0);
const total_canciones = ref(0);
const canciones_Actual = ref([] as item_lista[]);
canciones_Actual.value = admin_indiceslista.GetIndice(ref_lista_actual.value);
const compas = ref(-1);
const cancion_ref  = ref(new Cancion("no song name", "no band name", new Acordes([], []), new Letra([])));
const sesion_ref = ref(new EstadoSesion());

GetCanciones.obtenerCancion(canciones_Actual.value[0]).then((cancion_get: Cancion) => {
    cancion_ref.value = cancion_get;
});

///// LLEGO EL DIRECTOR
let cliente = new Cliente("http://192.168.0.202:8080/")

let config_load: string | null = localStorage.getItem("configuracion")
if (!config_load)
  config_load = ""
let configuracionObj: Configuracion | null = JSON.parse(config_load)
if (configuracionObj == null) {
  viendo.value = "config";
} 
sesion_ref.value = configuracionObj.sesion;
let director = new Director(configuracionObj, cliente);
director.Iniciar();
const director_ref = ref(director);
director.setcambiosHandler((directornuevo: Director) => {
  console.log("cambios", directornuevo.configuracion.sesion.estado)
  sesion_ref.value = directornuevo.configuracion.sesion;
});


onMounted(() => { 
    console.log("APP MONTADA")
    window.addEventListener('resize', updateDimensions);
});

function acciono(valor: string) {
  if (valor == 'conectar') {
    console.log("conectar")
    director_ref.value.Conectar();
  }
  else {
    viendo.value = valor;    
  }
    
}


</script>

<template>
    <div>

       

  <Menu :viendo_vista="viendo" :nro_cancion="director_ref.nro_cancion" :sesion="sesion_ref" 
  :total_canciones="director_ref.total_canciones" @acciono="acciono" 
  :compas="director_ref.nro_compas" :cancion="cancion_ref" 
  ></Menu>
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
