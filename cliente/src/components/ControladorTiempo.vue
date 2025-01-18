<script setup lang="ts">
import { ref } from 'vue';
import { Cancion } from '../modelo/cancion';
import { Contexto } from '../modelo/contexto';
import Metronomo from './metronomo.vue';
const props = defineProps<{ compas: number, cancion: Cancion, contexto: Contexto }>();
const emit = defineEmits(['play', 'pause', 'stop', 'next', 'previous', 'update-compas']);
const currentCompas = ref(0);
const metronomeRef = ref();

import { watch } from 'vue';

watch(() => props.compas, (newCompas) => {
  currentCompas.value = newCompas;
});

function play() {
    emit('play');
    metronomeRef.value?.startMetronome();
    
}

function pause() {
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
<div class="row">
  <div class="row">
    <div class="controls col-6">
      <button @click="play">
  <i class="bi bi-play-fill"></i>
</button>
<button @click="pause">
  <i class="bi bi-pause-fill"></i>
</button>
<button @click="stop">
  <i class="bi bi-stop-fill"></i>
</button>
<button @click="previous">
  <i class="bi bi-skip-backward-fill"></i>
</button>
<button @click="next">
  <i class="bi bi-skip-forward-fill"></i>
</button>

    </div>
    <div class="col-2">Compás: {{ currentCompas }} 
    <Metronomo ref="metronomeRef" :cancion="cancion"></Metronomo>

    </div>
    <div class="col-2">Tempo: <input type="number" v-model="props.cancion.tempo"> </div>
  <div class="row">

    <div class="progress-bar">
        <input 
            type="range" 
            min="0" 
            max="100" 
            v-model="currentCompas" 
            @input="updateCompas(currentCompas)" 
        />
        
    </div>

  </div>

    
</div>
</div>
</template>

<style scoped>
.controls {
    display: flex;
    
}
</style>
