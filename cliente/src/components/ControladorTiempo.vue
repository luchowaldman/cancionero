<script setup lang="ts">
import { ref } from 'vue';
import { Cancion } from '../modelo/cancion';
import { Musica } from '../modelo/musica';
import { Tiempo } from '../modelo/tiempo';

import 'bootstrap-icons/font/bootstrap-icons.css';
const props = defineProps<{ compas: number, cancion: Cancion,  nro_cancion: number, total_canciones: number, viendo_vista: string, editando_cancion: Cancion }>();
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
    <div style="display: inline;">
      
    <div class="titulocontorltiempo">
      
            
            <div v-if="viendo_vista=='editar'">

              <input type="text" v-model="editando_cancion.cancion"/> -
      <input type="text" v-model="editando_cancion.banda" /> 
            </div>
            
            <div v-if="viendo_vista=='tocar'"> 
              {{ nro_cancion + 1 }} / {{ total_canciones }} 
          {{ cancion.cancion }} - {{ cancion.banda }}

          
        <div style="display: flex; flex-wrap: wrap;">
          
        
          <input 
    type="range" 
    min="0" 
    :max="musica.total_compases(cancion)" 
    v-model="currentCompas" 
    @input="updateCompas(currentCompas)" 
    style="accent-color: #a9a8f6;"
/>

    
          <span class="spnTiempo">{{ tiempo.formatSegundos(segundos_actuales) }} / {{ tiempo.formatSegundos(segundos_totales) }} </span>
          <button  class="boton_controller boton_controllerplay" @click="play">
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
        
          </div>
          
      </div>
      
            
            
            
      
      
        

    </div>
  </div>
  <div>


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
  border-radius: 3px;
  color: #a9a8f6;
  background-color: black;
  font-size: 20px;
  border: 1px solid #a9a8f6;
  width: 46px;
  height: 46px;
}

.boton_controllerplay {
  font-size: 30px !important;
}

.spnTiempo {
  border: 1px solid;
  font-size: 16px;
  margin: 14px;
  border-radius: 8px;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
