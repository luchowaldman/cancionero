<script setup lang="ts">
import { ref } from 'vue';
import { Cancion } from '../modelo/cancion';
import { Musica } from '../modelo/musica';
import { Tiempo } from '../modelo/tiempo';

import { Contexto } from '../modelo/contexto';
import Metronomo from './metronomo.vue';

import 'bootstrap-icons/font/bootstrap-icons.css';
const props = defineProps<{ compas: number, cancion: Cancion,  nro_cancion: number, total_canciones: number }>();
const emit = defineEmits(['play', 'pause', 'stop', 'next', 'previous', 'update-compas']);
const musica = new Musica();
const tiempo = new Tiempo();
const currentCompas = ref(0);
const segundos_totales = ref(0);
const segundos_actuales = ref(0);
const currentCancion = ref(props.cancion);
const metronomeRef = ref();

import { watch } from 'vue';

watch(() => props.compas, (newCompas) => {
  currentCompas.value = newCompas;
  segundos_actuales.value = musica.duracion_compas(currentCancion.value) * currentCompas.value;
});

watch(() => props.cancion, (newCancion) => {
  
    currentCancion.value = newCancion;
    CalcularCancion(newCancion);


});

function CalcularCancion(newCancion: Cancion) {
  segundos_totales.value = musica.duracion_cancion(newCancion);
  segundos_actuales.value = musica.duracion_compas(newCancion) * currentCompas.value;


}

function play() {
    emit('play');
    metronomeRef.value?.startMetronome();
    
}

function pause() {
  console.log(metronomeRef.value);
  metronomeRef.value?.stopMetronome();
  emit('pause');
}

function stop() {
  metronomeRef.value?.stopMetronome();
  emit('stop');
}

function next() {

  emit('next');
}

function previous() {
  
  emit('previous');
}

function updateCompas(newCompas: number) {
  
  emit('update-compas', newCompas);
}
</script>

<template>

  <div>
    {{ nro_cancion + 1 }} / {{ total_canciones }} {{ cancion.cancion }} - {{ cancion.banda }}
    
    
    
    <div class="controls">
            <button class="boton_controller" @click="play">
              <i class="bi bi-play-fill"></i>
            </button>
            <button class="boton_controller" @click="pause">
              <i class="bi bi-pause-fill"></i>
            </button>
            <button class="boton_controller" @click="stop">
              <i class="bi bi-stop-fill"></i>
            </button>
            <button class="boton_controller" @click="previous">
              <i class="bi bi-skip-backward-fill"></i>
            </button>
            <button class="boton_controller" @click="next">
              <i class="bi bi-skip-forward-fill"></i>
            </button>
            <span>{{ tiempo.formatSegundos(segundos_actuales) }} / {{ tiempo.formatSegundos(segundos_totales) }} </span>
    </div>
    
    
    <Metronomo ref="metronomeRef" :cancion="cancion"></Metronomo>

    
  <div>

    <div class="progress-bar">
        <input 
            type="range" 
            min="0" 
            :max="musica.total_compases(cancion)" 
            v-model="currentCompas" 
            @input="updateCompas(currentCompas)" 
        />
        
    </div>

  </div>

    
</div>

</template>

<style scoped>
.controls {
    display: flex;
    
}

.boton_controller {
  width: 50px;
  height: 50px;
}
</style>
