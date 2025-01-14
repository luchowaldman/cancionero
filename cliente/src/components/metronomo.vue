<script setup lang="ts">
import { ref } from 'vue';
import { Cancion } from '../modelo/cancion';
const props = defineProps<{ cancion: Cancion }>();
const activeBeat = ref(-1)
import { Reproductor } from '../modelo/reproductor';

let reproductor = new Reproductor(2200, 99999999);

function startMetronome() {
   const seg = 60 / props.cancion.tempo;
   console.log("Duracion:", seg);
   reproductor.setDuracion(seg * 1000);
   reproductor.iniciar();
}

function stopMetronome() {
  reproductor.parar()
  activeBeat.value = -1;
  
}


reproductor.setIniciaCompasHandler((newCompas: number) => {
    console.log("Cambio compas  --Z", newCompas);
    activeBeat.value = (activeBeat.value + 1) % (props.cancion.compas_cantidad);
});

defineExpose({ startMetronome, stopMetronome });
</script>

<template>
  <div>
    
<div class="row">
  <div v-for="n in props.cancion.compas_cantidad" :key="n" class="col-3" :class="{ beat_activo: n - 1 === activeBeat }">
    {{ n }}
  </div>
</div>
  </div>
</template>

<style scoped>
.controls {
    display: flex;
    
}

.beat_activo {
  background-color: greenyellow;
}
</style>








