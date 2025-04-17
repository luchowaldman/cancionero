<script setup lang="ts">


import { ref, onMounted } from 'vue';


import Menu from './components/menu.vue';
import Tocar from './pages/tocar.vue';
import Listas from './pages/listas.vue';
import Editar from './pages/editar.vue';
import Buscar from './pages/buscar.vue';
import Configuracion from './pages/configuracion.vue';

import { Reproductor } from './modelo/reproductor';

import { Cancion } from './modelo/cancion';
import { Aplicacion } from './modelo/aplicacion';
import { EstadoSesion } from './modelo/estadosesion';
import { Director } from './modelo/director';
import { DirectorOffline } from './modelo/directoroffline';


const aplicacion: Aplicacion = new Aplicacion();




// VISTA

const sesion_ref = ref(new EstadoSesion());
const bpm_encompas = ref(0);

let reproductor = new Reproductor(2200);


function startReproduccion() 
{

  console.log("Iniciando reproduccion");
   const seg = 60 / aplicacion.cancion.value.bpm;
   console.log("Duracion:", seg);
   reproductor.setDuracion(seg * 1000);
   reproductor.iniciar();
}


reproductor.setIniciaCicloHandler(() => {
  faltan_parainicio.value = faltan_parainicio.value - 1;
  bpm_encompas.value = (bpm_encompas.value + 1) % aplicacion.cancion.value.compas_cantidad;
});



//viendo.value = "config";


// CONTROLES
const ctrlMenu = ref();



let director: Director = new DirectorOffline(aplicacion.configuracionObj);
  director.setcambiosHandler((directornuevo: Director) => {
    
    
    sesion_ref.value = directornuevo.configuracion.sesion;
    if (estado_ref.value == 'pausado' && directornuevo.estado != 'pausado') {
      faltan_parainicio.value = aplicacion.cancion.value.compas_cantidad; 
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



function vincular_director() {
  director_ref.value = director;
  sesion_ref.value = director.configuracion.sesion;

  director.setcambiosCancionHandler((cancion: Cancion) => {
    aplicacion.cancion.value = cancion;
  });

  director.setcambiosCompasHandler((compas: number) => {
    aplicacion.compas.value = parseInt(compas.toString());
    });
  }

  director.Iniciar();
  vincular_director();

onMounted(() => { 
    console.log("APP MONTADA")
    
    aplicacion.Iniciar();
});



function acciono(valor: string, compas: number = 0) {
  aplicacion.acciono(valor, compas);
}



</script>

<template>




<div id="contenedor-musical" class="pantalla">

  <Menu 
  :viendo_vista="aplicacion.viendo_pagina.value" :nro_cancion="director_ref.nro_cancion" :sesion="sesion_ref" 
  :total_canciones="director_ref.total_canciones" @acciono="acciono" 
  :compas="aplicacion.compas.value" :cancion="aplicacion.cancion.value" :ref="ctrlMenu"
  :editando_cancion="aplicacion.editando_cancion.value" :estado="estado_ref" :conectado="conectado" :director="director_ref"
   :bpm_encompas="bpm_encompas"
  ></Menu>
  <div class="carteliniciando" v-if="estado_ref=='iniciando'">
        {{ faltan_parainicio }}
   </div>    

    <Tocar v-if="aplicacion.viendo_pagina.value =='tocar'"  @acciono="acciono" :compas="aplicacion.compas.value" 
    :width="aplicacion.width" :height="aplicacion.height" 
    :cancion="aplicacion.cancion.value"></Tocar>
    <Listas v-if="aplicacion.viendo_pagina.value =='listas'" :nro_cancion="director.nro_cancion"  @acciono="acciono"></Listas>
    <Configuracion v-if="aplicacion.viendo_pagina.value =='config'"></Configuracion>
    <Editar v-if="aplicacion.viendo_pagina.value =='editar'"  @acciono="acciono" :cancion="aplicacion.editando_cancion.value" :item="aplicacion.editando_item.value"></Editar>
    <Buscar v-if="aplicacion.viendo_pagina.value =='buscar'"  @acciono="acciono"></Buscar>

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
