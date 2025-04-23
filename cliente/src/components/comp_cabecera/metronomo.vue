<script setup lang="ts">

import { ref, watch } from 'vue';
import { Reproductor } from '../../modelo/reproductor';
import { Cancion } from '../../modelo/cancion';
const props = defineProps<{ cancion: Cancion, compas: number, estado: string, bpm_encompas: number }>();


</script>

<template>
  <div>
  <div class="divPrevia" v-if="estado == 'tocando' && compas < 0">Empieza en {{  4 - bpm_encompas   }} </div>
  <div class="metronono">


<div style="display: flex;">
<div v-for="n in props.cancion.compas_cantidad" :key="n" class="beat" :class="{ beat_activo: n - 1  === bpm_encompas }">
    
    {{ n }}
  </div>
</div>

  </div>
</div>
</template>

<style scoped>
.controls {
    display: flex;
    
}

.metronono {
  border: 1px solid #a9a8f6;
  border-radius: 10px;
  font-size: 27px;
  margin: 4px;
}

.beat {
  border: 1px solid #a9a8f6;
  border-radius: 10px;
  margin: 4px;
  padding-left: 14px;
  padding-right: 14px;

}
.beat_activo {
  background-color: rgb(235, 67, 16);
}
.divPrevia {
  position: absolute;
  top: 200px ;
  left: 90px;
  color: red;
  font-size: 80px;
  padding: 20px;
  border: 1px solid red ;
 }
</style>








