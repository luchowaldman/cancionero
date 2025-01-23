<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { Cancion } from './modelo/cancion';
import { Contexto } from './modelo/contexto';
import { Reproductor } from './modelo/reproductor';

import Menu from './components/menu.vue';

import ComponenteMusicalAcordesEdit from './components/ComponenteMusicalAcordesEdit.vue';
import ControladorTiempo from './components/ControladorTiempo.vue';
import { Acordes } from './modelo/acordes';
import { Letra } from './modelo/letra';

import { AdminListasLocalStorage } from './modelo/AdminListasStorage';
import { AdminListasURL } from './modelo/AdminListasURL';
import { Almacenado } from './modelo/Almacenado';



function onPlay() {
    reproductor.iniciar();
    console.log("Play event received");

}

const almacen = new Almacenado();

// INICIALIZA LAS LISTAS DE CANCIONES GENERADAS
const generadorlistasURL = new AdminListasURL('/data');
const generadorlistasLS = new AdminListasLocalStorage(almacen);
// Definir la canción y el contexto

const cancion  = ref(new Cancion("", "", new Acordes([], []), new Letra([])));

const origen = localStorage.getItem("origen") || 'almacenada';
const banda = localStorage.getItem("editar_banda") || 'intoxicados';
const tema = localStorage.getItem("editar_cancion") || 'esta-saliendo-el-sol';
if (origen == 'almacenada') {

    generadorlistasLS.GetCancionxTema(banda, tema).then((cancion_obtenida) => {
    cancion.value = cancion_obtenida;
    
    });
} else if (origen == 'URL') {
    generadorlistasURL.GetCancionxTema(banda, tema).then((cancion_obtenida) => {
    cancion.value = cancion_obtenida;
    
    }); 
    
}


let contexto = new Contexto("Lista", 10);
const compas = ref(-1);


let reproductor = new Reproductor(2200, 50);

reproductor.setIniciaHandler(() => {
    console.log("Iniciando reproductor");
});

reproductor.setIniciaCompasHandler((newCompas: number) => {
    console.log("Tocando compas", newCompas);
    compas.value = newCompas;
});

reproductor.setFinalizaHandler(() => {
    console.log("Deteniendo reproductor");
});





function onPause() {
    reproductor.pausar();
    console.log("Pause event received");
}


function onStop() {
    reproductor.parar();
    console.log("Stop event received");
}

function onNext() {
    console.log("Next event received");
}

function onPrevious() {
    console.log("Previous event received");
}

function onUpdateCompas(newCompas: number) {
    compas.value = newCompas;
    console.log(`Esto se actualiza: ${newCompas}`);
}

function guardarCancion() {
    generadorlistasLS.GuardarCancion(cancion.value, null);
}

    // Llamar a la función iniciarCompasEnComponentes cuando sea necesario 
    onMounted(() => { 
        console.log("APP MONTADA")
    });




</script>

<template>
     

<div >
    
  <Menu :titulo="cancion.cancion" viendo_vista="tocar"></Menu>
     <div class="row">
      <div class="col-6">
            <ControladorTiempo :compas=compas :cancion="cancion" :contexto="contexto"
                @play="onPlay" @pause="onPause" @stop="onStop" @next="onNext" @previous="onPrevious" @update-compas="onUpdateCompas">
        </ControladorTiempo>
      </div>    
      <div class="col-6">
        SIN CONECTARSE
      </div>
  
     </div>

     <h1>{{ cancion.cancion }}</h1>
     <h2>{{ cancion.banda }}</h2>
    <ComponenteMusicalAcordesEdit :compas="compas" :cancion="cancion" :contexto="contexto"></ComponenteMusicalAcordesEdit>
    <button @click="guardarCancion">Guardar</button>
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
</style>
