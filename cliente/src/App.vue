<script setup lang="ts">
import { ref, markRaw, onMounted } from 'vue';
import { Cancion } from './modelo/cancion';
import { Contexto } from './modelo/contexto';
import { Reproductor } from './modelo/reproductor';

import ComponenteMusicalAcordes from './components/ComponenteMusicalAcordes.vue';
import ComponenteMusicalAcordesSeguidos from './components/ComponenteMusicalAcordesSeguidos.vue';
import ComponenteMusicalLetra from './components/ComponenteMusicalLetra.vue';
import ControladorTiempo from './components/ControladorTiempo.vue';
import Menu from './components/menu.vue';
import { Acordes } from './modelo/acordes';
import { Letra } from './modelo/letra';
import { Almacenado } from './modelo/Almacenado';
import { item_lista } from './modelo/item_lista';

// Definir la canción y el contexto

    


import { AdminListasTocables } from './modelo/AdminListasTocables';

const almacen = new Almacenado();
const generadorlistasTocables = new AdminListasTocables(almacen);

const cancion  = ref(new Cancion("", "", new Acordes([], []), new Letra([])));
const nro_cancion = ref(0);

let canciones_sesion: Cancion[] = [];
let canciones_lista: item_lista[] = []
generadorlistasTocables.getIndice().then((value: item_lista[]) => {
    canciones_lista = value;
    //console.log("Canciones", canciones_lista);
    for (const tema of canciones_lista) 
    {
        generadorlistasTocables.GetCancionxTema(tema.banda, tema.cancion).then((cancion_obtenida: Cancion) => {
            canciones_sesion.push(cancion_obtenida);
            cancion.value = canciones_sesion[nro_cancion.value];
        });        
    }

});
    






let contexto = new Contexto("Lista", 10);
const compas = ref(-1);
let reproductor = new Reproductor(2200, 70);

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
    markRaw(ComponenteMusicalAcordesSeguidos),
    markRaw(ComponenteMusicalLetra),
    markRaw(ComponenteMusicalAcordes)
]);


function onPause() {
    reproductor.pausar();
    console.log("Pause event received");
}

function onPlay() {
    console.log("Play Cancion", cancion.value.tempo, cancion.value.compas_unidad, cancion.value.compas_cantidad);
    const seg = (60) * (cancion.value.compas_cantidad / cancion.value.tempo);
    console.log("Duracion:", seg);
    reproductor.setDuracion(seg * 1000);
    reproductor.iniciar();
    console.log("Play event received");

}

function onStop() {
    reproductor.parar();
    console.log("Stop event received");
}

function onNext() {
    console.log("Next event received");
    nro_cancion.value = (nro_cancion.value + 1) % canciones_sesion.length;
    cancion.value = canciones_sesion[nro_cancion.value];
}

function onPrevious() {
    console.log("Previous event received");
    nro_cancion.value = (nro_cancion.value - 1 + canciones_sesion.length) % canciones_sesion.length;
    cancion.value = canciones_sesion[nro_cancion.value];
}

function onUpdateCompas(newCompas: number) {
    compas.value = newCompas
    console.log(`Esto se actualiza: ${newCompas}`);
}

    // Llamar a la función iniciarCompasEnComponentes cuando sea necesario 
    onMounted(() => { 
        console.log("APP MONTADA")
    });

</script>

<template>
    <div>

       

  <Menu :titulo="cancion.cancion" viendo_vista="tocar"></Menu>

  <div class="pantalla">

    <div class="row">
      <div class="col-6">
            <ControladorTiempo :compas=compas :cancion="cancion" :contexto="contexto"
                @play="onPlay" @pause="onPause" @stop="onStop" @next="onNext" @previous="onPrevious" @update-compas="onUpdateCompas">
        </ControladorTiempo>
      </div>    
      <div class="col-3">
        Escala: G
        Tempo: {{  cancion.tempo }} bpm
      </div>
  
     </div>

        
<div class="row">
    <div v-for="(Componente, index) in componentesMusicales" :key="index" class="col-3">
        <component :is="Componente" :compas="compas" :cancion="cancion" :contexto="contexto"></component>
    </div>
</div>



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
</style>
