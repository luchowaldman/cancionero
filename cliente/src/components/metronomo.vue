<script setup lang="ts">
import { ref } from 'vue';
import { Cancion } from '../modelo/cancion';
const props = defineProps<{ cancion: Cancion }>();
const activeBeat = ref(-1)
import { Reproductor } from '../modelo/reproductor';

let reproductor = new Reproductor(2200, 99999999);

function startMetronome() {
   const seg = 60 / props.cancion.bpm;
   console.log("Duracion:", seg);
   reproductor.setDuracion(seg * 1000);
   reproductor.iniciar();
}

function stopMetronome() {
  reproductor.parar()
  activeBeat.value = -1;
  
}


reproductor.setIniciaCompasHandler((newCompas: number) => {
  console.log("Nuevo compas:", newCompas);
    activeBeat.value = (activeBeat.value + 1) % (props.cancion.compas_cantidad);
});

defineExpose({ startMetronome, stopMetronome });
</script>

<template>
  <div class="metronono">
    
<div style="display: flex;">
  <div v-for="n in props.cancion.compas_cantidad" :key="n" class="beat" :class="{ beat_activo: n - 1 === activeBeat }">
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
  width: 100%;
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








