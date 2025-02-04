<script setup lang="ts">


import { ref, onMounted } from 'vue';


import Menu from './components/menu.vue';
import Tocar from './pages/tocar.vue';
import Listas from './pages/listas.vue';
import Editar from './pages/editar.vue';
import Buscar from './pages/buscar.vue';
import Bus from './pages/listas.vue';
import Configuracion from './pages/configuracion.vue';
import { ModeloConfiguracion  } from './modelo/modeloconfiguracion';
import { Cancion } from './modelo/cancion';
import { Letra } from './modelo/letra';
import { Acordes, Parte } from './modelo/acordes';
import { EstadoSesion } from './modelo/estadosesion';
import { Cliente }  from './modelo/client_socketio';
import { Director } from './modelo/director';
import { item_lista } from './modelo/item_lista';
import { AdminListasTocables } from './modelo/AdminIndiceListas';
import { findSourceMap } from 'module';
import { GetCanciones } from './modelo/GetCanciones';

// EDITAR
const editando_item = ref(new item_lista("no song name", "no band name"));
const editando_cancion = ref(new Cancion("no song name", "no band name", new Acordes([new Parte("p1", ["C"])], [0]), new Letra([[""]]), 120, 4, 4, 4, "C"));
//editando_cancion.value = JSON.parse(localStorage.getItem("editando_cancion") || "{}");


const viendo = ref("tocar");
viendo.value = localStorage.getItem("viendo") || "tocar";

// LISTAS

const admin_indiceslista = new AdminListasTocables();

// CANCIONES
const canciones_Actual = ref([] as item_lista[]);
canciones_Actual.value = admin_indiceslista.GetIndice("default");
const cancion_ref  = ref(new Cancion("Cancion no cargada", "sin banda", new Acordes([], []), new Letra([])));
const sesion_ref = ref(new EstadoSesion());
const compas_ref = ref(-2);


///// LLEGO EL DIRECTOR

let cliente = new Cliente("http://10.31.129.71:8080/")

let config_load: string | null = localStorage.getItem("configuracion")
if (!config_load)
  config_load = ""

let configuracionObj: ModeloConfiguracion | null = null;

try {
  configuracionObj = JSON.parse(config_load);
} catch (error) {
}

if (configuracionObj == null) {
  viendo.value = "config";
  configuracionObj = new ModeloConfiguracion()
  configuracionObj.sesion = new EstadoSesion()
  configuracionObj.sesion.nombre = "default"
  configuracionObj.nombre = "default"
  localStorage.setItem("configuracion", JSON.stringify(configuracionObj))
}

let director = new Director(configuracionObj, cliente);
const director_ref = ref(director);




  sesion_ref.value = configuracionObj.sesion;
  director.Iniciar();
  director.setcambiosHandler((directornuevo: Director) => {
    console.log("cambios", directornuevo.configuracion.sesion.estado);
    sesion_ref.value = directornuevo.configuracion.sesion;
  });
  director.setcambiosCancionHandler((cancion: Cancion) => {
    cancion_ref.value = cancion;
  });
  director.setcambiosCompasHandler((compas: number) => {
    compas_ref.value = parseInt(compas.toString());
});
  

onMounted(() => { 
    console.log("APP MONTADA")
});

function cargar_edit() {
  let item = JSON.parse(localStorage.getItem("editando_cancion") || "{}");
  
  GetCanciones.obtenerCancion(item).then((cancion_get: Cancion) => {
      editando_cancion.value = cancion_get;
      
    });
}

function acciono(valor: string, compas: number = 0) {

  switch (valor) {
    case 'next':
      director.click_siguiente();
      break;
    case 'previous':
      director.click_anterior();
      break;
    case 'play':
      director.click_play();
      break;
    case 'pause':
      director.click_pause();
      break;
    case 'update-compas':
      director.update_compas(compas);
      break;
    case 'conectar':
      console.log("conectar");
      director_ref.value.Conectar();
      break;
    case 'tocar':
    case 'listas':
    case 'config':
    case 'editar':
    case 'buscar':

      if (valor == 'editar') 
      {
        if (viendo.value == 'tocar') 
        {
          editando_item.value = director.getitemActual();
          localStorage.setItem("editando_cancion", JSON.stringify(editando_item.value));
          
        }
        
        cargar_edit();
      }

      viendo.value = valor;
      localStorage.setItem("viendo", valor);
      
      break;
    default:
      console.warn(`Acción no reconocida: ${valor}`);
  }
  
}
if (viendo.value == 'editar') {
  cargar_edit();
}


</script>

<template>
    <div>

       

  <Menu :viendo_vista="viendo" :nro_cancion="director_ref.nro_cancion" :sesion="sesion_ref" 
  :total_canciones="director_ref.total_canciones" @acciono="acciono" 
  :compas="compas_ref" :cancion="cancion_ref" 
  ></Menu>
  <div class="pantalla">
    <Tocar v-if="viendo=='tocar'"  @acciono="acciono" :compas="compas_ref" :cancion="cancion_ref"></Tocar>
    <Listas v-if="viendo=='listas'"  @acciono="acciono"></Listas>
    <Configuracion v-if="viendo=='config'"></Configuracion>
    <Editar v-if="viendo=='editar'"  @acciono="acciono" :cancion="editando_cancion" :item="editando_item"></Editar>
    <Buscar v-if="viendo=='buscar'"  @acciono="acciono"></Buscar>

    
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
