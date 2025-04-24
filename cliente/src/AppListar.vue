<script setup lang="ts">


import { ref, onMounted } from 'vue';


import Menu from './components/comp_cabecera/menu.vue';
import Tocar from './pages/tocar.vue';
import Listas from './pages/listas.vue';
import Editar from './pages/editar.vue';
import Buscar from './pages/buscar.vue';
import Configuracion from './pages/configuracion.vue';

import { Reproductor } from './modelo/reproductor';

import { Cancion } from './modelo/cancion';
import { Aplicacion } from './modelo/aplicacionespantalla/aplicacionlistas';
import { EstadoSesion } from './modelo/estadosesion';
import { Director } from './modelo/director';
import { DirectorOffline } from './modelo/directoroffline';


const aplicacion: Aplicacion = new Aplicacion();






//viendo.value = "config";


// CONTROLES
const ctrlMenu = ref();
onMounted(() => { 
    console.log("APP MONTADA");
    aplicacion.Iniciar();
});



function acciono(valor: string, compas: number = 0) {
  aplicacion.acciono(valor, compas);
}

const faltan_parainicio = ref(-1);

</script>

<template>




<div id="contenedor-musical" class="pantalla">

  <Menu 
  :viendo_vista="listas" :sesion="aplicacion.sesion.value" 
  :nro_cancion="aplicacion.nro_cancion.value" 
  :listaCanciones="aplicacion.listacanciones.value" @acciono="acciono"
  :compas="aplicacion.compas.value"
  :cancion="aplicacion.cancion.value" 
  :estado="aplicacion.estado.value"
  :ref="ctrlMenu"
   :bpm_encompas="1"
  ></Menu>
  <div class="carteliniciando" v-if="aplicacion.estado.value=='iniciando'">
        {{ faltan_parainicio }}
   </div>    
    <Listas 
      :nro_cancion="aplicacion.nro_cancion.value"  
      :lista_actual="aplicacion.listacanciones.value"
      @acciono="acciono">
    </Listas>
    

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
