<script setup lang="ts">

import { Cancion } from '../modelo/cancion';
const props = defineProps<{ cancion: Cancion, bpm_encompas: number }>();




</script>

<template>
  <div class="metronono">
    
<div style="display: flex;">
<div v-for="n in props.cancion.compas_cantidad" :key="n" class="beat" :class="{ beat_activo: n - 1 === bpm_encompas }">
    
    {{ n }}
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
</style>








