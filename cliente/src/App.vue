<script setup lang="ts">


import { ref, onMounted } from 'vue';


import Menu from './components/menu.vue';
import Tocar from './pages/tocar.vue';
import Listas from './pages/listas.vue';
import Editar from './pages/editar.vue';
import Buscar from './pages/buscar.vue';
import Configuracion from './pages/configuracion.vue';
import { Reproductor } from './modelo/reproductor';

import { ModeloConfiguracion  } from './modelo/modeloconfiguracion';
import { Cancion } from './modelo/cancion';
import { Letra } from './modelo/letra';
import { Aplicacion } from './modelo/aplicacion';

import { Acordes, Parte } from './modelo/acordes';
import { EstadoSesion } from './modelo/estadosesion';
import { Director } from './modelo/director';
import { item_lista } from './modelo/item_lista';
import { GetCanciones } from './modelo/GetCanciones';
import { DirectorOffline } from './modelo/directoroffline';
import { DirectorOnline } from './modelo/directoronline';



const aplicacion: Aplicacion = new Aplicacion();




// VISTA
const cancion_ref  = ref(new Cancion("Cancion no cargada", "sin banda", new Acordes([], []), new Letra([])));
const sesion_ref = ref(new EstadoSesion());
const compas_ref = ref(-2);
const editando_item = ref(new item_lista("no song name", "no band name"));
const editando_cancion = ref(new Cancion("no song name", "no band name", new Acordes([new Parte("p1", ["C"])], [0]), new Letra([[""]]), 120, 4, 4, 4, "C"));

const bpm_encompas = ref(0);

let reproductor = new Reproductor(2200);


function startReproduccion() 
{

  console.log("Iniciando reproduccion");
   const seg = 60 / cancion_ref.value.bpm;
   console.log("Duracion:", seg);
   reproductor.setDuracion(seg * 1000);
   reproductor.iniciar();
}




reproductor.setIniciaCicloHandler(() => {
  faltan_parainicio.value = faltan_parainicio.value - 1;
  bpm_encompas.value = (bpm_encompas.value + 1) % cancion_ref.value.compas_cantidad;
});



//viendo.value = "config";


// CONTROLES
const ctrlMenu = ref();



let director: Director = new DirectorOffline(aplicacion.configuracionObj);
  director.setcambiosHandler((directornuevo: Director) => {
    
    
    sesion_ref.value = directornuevo.configuracion.sesion;
    if (estado_ref.value == 'pausado' && directornuevo.estado != 'pausado') {
      faltan_parainicio.value = cancion_ref.value.compas_cantidad; 
      startReproduccion();
      
    }
    director.set_nro_cancion(directornuevo.nro_cancion);
    
    estado_ref.value = directornuevo.estado;
    ctrlMenu.value?.actualizar_vista();
  });

const director_ref = ref(director);
const faltan_parainicio = ref(-1);
const estado_ref = ref(director.estado);
const conectado = localStorage.getItem("conectado") || "no";


function Conectar() {

  director = new DirectorOnline(aplicacion.configuracionObj);
  director.setcambiosHandler((directornuevo: Director) => {
    
    console.log("Estado _red")
    sesion_ref.value = directornuevo.configuracion.sesion;
    estado_ref.value = directornuevo.estado;
    ctrlMenu.value?.actualizar_vista();
  });

  director.Iniciar();if (director instanceof DirectorOnline) {
  // Haz un casting al tipo DirectorOnline y llama al método exclusivo
  (director as DirectorOnline).Conectar();
} else {
  console.log("El objeto no es una instancia de DirectorOnline");
  }
  vincular_director();
}
function Desconectar() {
  if (director instanceof DirectorOnline) {
  // Haz un casting al tipo DirectorOnline y llama al método exclusivo
  (director as DirectorOnline).Desconectar();
} else {
  console.log("El objeto no es una instancia de DirectorOnline");
  }
  director = new DirectorOffline(aplicacion.configuracionObj);
  director.Iniciar();
  vincular_director();
}


function vincular_director() {
  director_ref.value = director;
  sesion_ref.value = director.configuracion.sesion;

  director.setcambiosCancionHandler((cancion: Cancion) => {
      cancion_ref.value = cancion;
  });

  director.setcambiosCompasHandler((compas: number) => {
    compas_ref.value = parseInt(compas.toString());
    });
  }

  director.Iniciar();
  vincular_director();

onMounted(() => { 
    console.log("APP MONTADA")
    
    aplicacion.Iniciar();
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
      
    case 'setcancion':
      director.set_nro_cancion(compas);
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
      Conectar();
      break;
    case 'desconectar':
      console.log("conectar");
      Desconectar();
      break;
      
    case 'tocar_cancion':
      director.set_nro_cancion(compas);
      break;
    case 'tocar':
    case 'listas':
    case 'config':
    case 'editar':
    case 'buscar':

      if (valor == 'editar') 
      {
        if (aplicacion.viendo.value == 'tocar') 
        {
          editando_item.value = director.getitemActual();
          localStorage.setItem("editando_cancion", JSON.stringify(editando_item.value));
          
        }
        
        cargar_edit();
      }
      
      if (valor == 'tocar') 
      {
        director.CargarLista();

      }

      aplicacion.viendo.value  = valor;
      localStorage.setItem("viendo", valor);
      
      break;
    default:
      console.warn(`Acción no reconocida: ${valor}`);
  }
  
}
if (aplicacion.viendo.value  == 'editar') {
  cargar_edit();
}


</script>

<template>




<div id="contenedor-musical" class="pantalla">

  <Menu 
  :viendo_vista="aplicacion.viendo.value" :nro_cancion="director_ref.nro_cancion" :sesion="sesion_ref" 
  :total_canciones="director_ref.total_canciones" @acciono="acciono" 
  :compas="compas_ref" :cancion="cancion_ref" :ref="ctrlMenu"
  :editando_cancion="editando_cancion" :estado="estado_ref" :conectado="conectado" :director="director_ref"
   :bpm_encompas="bpm_encompas"
  ></Menu>



  <div class="carteliniciando" v-if="estado_ref=='iniciando'">
        {{ faltan_parainicio }}
   </div>    

    <Tocar v-if="aplicacion.viendo.value =='tocar'"  @acciono="acciono" :compas="compas_ref" :cancion="cancion_ref"></Tocar>
    <Listas v-if="aplicacion.viendo.value =='listas'" :nro_cancion="director.nro_cancion"  @acciono="acciono"></Listas>
    <Configuracion v-if="aplicacion.viendo.value =='config'"></Configuracion>
    <Editar v-if="aplicacion.viendo.value =='editar'"  @acciono="acciono" :cancion="editando_cancion" :item="editando_item"></Editar>
    <Buscar v-if="aplicacion.viendo.value =='buscar'"  @acciono="acciono"></Buscar>
</div>
</template>

<style scoped>
#contenedor-musical {
  height: 100vh; /* Altura completa de la ventana */
  width: 100%;
}
.pantalla {
  width: 100%;
}
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
.carteliniciando {
  position: absolute;
  top: 20px;
  font-size: 500px;
  border: 5px solid #a9a8f6;
  margin-left: 300px;
  padding-left: 40px;
  padding-right: 40px;
  border-radius: 60px;
}
</style>
