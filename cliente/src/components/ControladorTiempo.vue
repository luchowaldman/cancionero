<script setup lang="ts">
import { ref } from 'vue';
import { Cancion } from '../modelo/cancion';
import { Contexto } from '../modelo/contexto';
import Metronomo from './metronomo.vue';
import 'bootstrap-icons/font/bootstrap-icons.css';
const props = defineProps<{ compas: number, cancion: Cancion }>();
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

  <div>
    1 / 12 {{ cancion.cancion }} - {{ cancion.banda }}
    
    
    
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
            <span>1:23 / 2:13</span>
    </div>
    
    
    <Metronomo ref="metronomeRef" :cancion="cancion"></Metronomo>

    
  <div>

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
