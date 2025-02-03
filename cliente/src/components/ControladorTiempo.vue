<script setup lang="ts">
import { ref } from 'vue';
import { Cancion } from '../modelo/cancion';
import { Musica } from '../modelo/musica';
import { Tiempo } from '../modelo/tiempo';

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
    <div class="titulocontorltiempo">
    {{ nro_cancion + 1 }} / {{ total_canciones }} {{ cancion.cancion }} - {{ cancion.banda }}
  </div>
    
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
    
    <div class="controls">
      <div style="display: flex; flex-wrap: wrap;">
        <div style="display: flex; flex-wrap: wrap;"><button style="font-size: larger;" class="boton_controller boton_controllerplay" @click="play">
              <i class="bi bi-play-fill"></i>
            </button>
            <div><span class="spnTiempo">{{ tiempo.formatSegundos(segundos_actuales) }} / {{ tiempo.formatSegundos(segundos_totales) }} </span></div>
          </div>
        
        <div>
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
            </button></div>
          
        
            
            
            
      </div>
      <div style="margin-left: auto">
        <div style="margin-right: 10px;">
        <Metronomo ref="metronomeRef" :cancion="cancion"></Metronomo>
      </div>
      </div>


    </div>
    
    

    

    
</div>

</template>

<style scoped>
.controls {
    display: flex;
    
}

.titulocontorltiempo {
  border: 1px solid;
  font-size: 38px;
  padding-left: 12px;
  margin: 4px;
  border-radius: 8px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.boton_controller {
  width: 46px;
  height: 46px;
  
  border-radius: 3px;
  color: #a9a8f6;
  background-color: black;
  font-size: 20px;
  border: 1px solid #a9a8f6;
  width: 56px;
  height: 56px;
}

.boton_controllerplay {
  font-size: 30px !important;
}

.spnTiempo {
  border: 1px solid;
  font-size: 40px;
  margin: 14px;
  border-radius: 8px;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
