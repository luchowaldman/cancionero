<script setup lang="ts">
import { ref } from 'vue';
import { Cancion } from '../modelo/cancion';
import { Contexto } from '../modelo/contexto';

const props = defineProps<{ compas: number, cancion: Cancion, contexto: Contexto }>();
const emit = defineEmits(['play', 'pause', 'stop', 'next', 'previous', 'update-compas']);
const currentCompas = ref(0);
const tempo = ref(props.cancion.tempo);
import { watch } from 'vue';

watch(() => props.compas, (newCompas) => {
  currentCompas.value = newCompas;
});

function play() {
    emit('play');
}

function pause() {
  emit('pause');
}

function stop() {
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
        <button @click="play">Play</button>
        <button @click="pause">Pause</button>
        <button @click="stop">Stop</button>
        <button @click="previous">Anterior</button>
        <button @click="next">Siguiente</button>
    </div>
    <div class="col-2">Compás: {{ currentCompas }} </div>
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
