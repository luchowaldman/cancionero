<script setup lang="ts">
import { ref, markRaw, onMounted } from 'vue';
import { Cancion } from './modelo/cancion';
import { Contexto } from './modelo/contexto';
import { Reproductor } from './modelo/reproductor';

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
const cancion = ref(new Cancion(
    'Fuiste lo mejor', 
    'Intoxicados', 
    new Acordes([
        new Parte("verso", ["sol", "do sol", "MIm", "LaM", "Do"]),
        new Parte("estribilllo", ["SIm", "Sol", "Mim","DO", "RE", "SIm", "Sol", "DO", "RE"])
    ], [0, 0, 1, 0, 1, 0]),

    new Letra([
    ["", "", "", ""],
    ["", "", "", ""],
    ["aca", "llego a buscarte"],
        ["en la playa", "bajo el sol"],
        ["con la brisa", "del mar"],
        ["y el sonido", "de las olas"],
        [],
        ["aca", "llego a buscarte"],
        ["en la playa", "bajo el sol"],
        ["con la brisa", "del mar"],
        ["y el sonido", "de las olas"]
    ]    )
    
));
let vista = ref({
   cargando_cancion: false
});
let contexto = new Contexto("Lista", 10);
const compas = ref(-1);
let reproductor = new Reproductor(2200, 50);

reproductor.setIniciaHandler(() => {
    console.log("Iniciando reproductor");
});

reproductor.setIniciaCompasHandler((newCompas: number) => {
    console.log("Tocando compas", newCompas);
    compas.value = parseInt(newCompas)
});

reproductor.setFinalizaHandler(() => {
    console.log("Deteniendo reproductor");
});



// Vector de componentes musicales
const componentesMusicales = ref([
    markRaw(ComponenteMusicalLetra),
    markRaw(ComponenteMusicalAcordesSeguidos),
    markRaw(ComponenteMusicalAcordes)
    
    //markRaw()
    //
    //markRaw(ComponenteMusicalLetra),
    //markRaw(ComponenteMusicalMetronomo),
    //markRaw(ComponenteMusical),
    //markRaw(ComponenteMusical),
    
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

    // Llamar a la función iniciarCompasEnComponentes cuando sea necesario 
    onMounted(() => { 
        console.log("APP MONTADA")
    });

</script>

<template>
    
<div id="barra_navegacion">
  <div>Cancionero</div>
  <div id="barra_control">
      <div>{{ cancion.titulo }} </div>
  </div>
  <ControladorTiempo :compas=compas :cancion="cancion" :contexto="contexto"
  @play="onPlay" @pause="onPause" @stop="onStop" @next="onNext" @previous="onPrevious" @update-compas="onUpdateCompas">

  </ControladorTiempo>

  {{ compas }}
  <div style="margin-left: auto;">Configuración</div>
</div>
<div id="vistas">
</div>
<div id="contenedor-musical">
    <div v-for="(Componente, index) in componentesMusicales" :key="index">
        <component :is="Componente" :compas="compas" :cancion="cancion" :contexto="contexto"></component>
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
