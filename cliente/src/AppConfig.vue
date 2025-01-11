<script setup lang="ts">
import { ref, markRaw, onMounted, watch } from 'vue';
import { Cancion } from './modelo/cancion';
import { Contexto } from './modelo/contexto';
import { Reproductor } from './modelo/reproductor';
import Menu from './components/menu.vue';


import ComponenteMusicalAcordesEdit from './components/ComponenteMusicalAcordesEdit.vue';
import ComponenteMusicalAcordes from './components/ComponenteMusicalAcordes.vue';
import ComponenteMusicalAcordesSeguidos from './components/ComponenteMusicalAcordesSeguidos.vue';
import ComponenteMusicalLetra from './components/ComponenteMusicalLetra.vue';
import ComponenteMusical from './components/ComponenteMusical.vue';
import ComponenteMusicalPartitura from './components/ComponenteMusicalPartitura.vue';
import ComponenteMusicalMetronomo from './components/ComponenteMusicalMetronomo.vue';
import ControladorTiempo from './components/ControladorTiempo.vue';
import { Acordes, Parte } from './modelo/acordes';
import { Letra } from './modelo/letra';

// Definir la canción y el contexto

const cancion  = ref(new Cancion("", "", new Acordes([], []), new Letra([])));
const mostrando_compas_parte = ref(-1)
import { Almacenado } from './modelo/Almacenado';
const almacen = new Almacenado();
const banda = localStorage.getItem("editar_banda") || '';
const tema = localStorage.getItem("editar_cancion") || '';

cancion.value = almacen.obtenerCancion(tema, banda);
console.log("Canción", cancion.value);



let vista = ref({
   cargando_cancion: false
});
let contexto = new Contexto("Lista", 10);
const compas = ref(-1);

const editando = ref(-1)
const mostrando_parte = ref(-1)
const currentCompas = ref(0);


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



// Vector de componentes musicales
const componentesMusicales = ref([
    markRaw(ComponenteMusicalAcordesEdit),
    markRaw(ComponenteMusicalAcordesSeguidos)
]);


function onPause() {
    reproductor.pausar();
    console.log("Pause event received");
}

function onPlay() {
    reproductor.iniciar();
    console.log("Play event received");

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
    compas.value = parseInt(newCompas)
    console.log(`Esto se actualiza: ${newCompas}`);
}

function guardarCancion() {
    almacen.agregarCancion(cancion.value);
}

    // Llamar a la función iniciarCompasEnComponentes cuando sea necesario 
    onMounted(() => { 
        console.log("APP MONTADA")
    });

</script>

<template>
    <div>
        
  <Menu titulo="config"></Menu>
        Config
</div>
</template>

<style scoped></style>
