<script setup lang="ts">
import { ref } from 'vue';
import { Cancion } from '../modelo/cancion';
const props = defineProps<{ cancion: Cancion, bpm_encompas: number }>();
const activeBeat = ref(-1)
import { Reproductor } from '../modelo/reproductor';


</script>

<template>
  <div class="metronono">
    
<div style="display: flex;">
<div v-for="n in parseInt(props.cancion.compas_cantidad)" :key="n" class="beat" :class="{ beat_activo: n - 1 === bpm_encompas }">
    
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








