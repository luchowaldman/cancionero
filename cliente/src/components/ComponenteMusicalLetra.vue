<script setup lang="ts">
import { ref } from 'vue'
import { watch } from 'vue';

import { Cancion } from '../modelo/cancion';
import { Contexto } from '../modelo/contexto';

const props = defineProps<{ compas: number, cancion: Cancion, contexto: Contexto }>()

const mostrando_renglon = ref(-1);
const mostrando_palabra = ref(-1);

watch(() => props.compas, (newCompas) => {
  let totalCompases = 0;
  for (let i = 0; i < props.cancion.letra.renglones.length; i++) 
  {
    let compases_x_parte = 0;
    if (props.cancion.letra.renglones[i])
      compases_x_parte = props.cancion.letra.renglones[i].length;

    props.cancion.letra.renglones[i].length; 
    if (newCompas < totalCompases + compases_x_parte) {
      mostrando_renglon.value = i;
      mostrando_palabra.value = newCompas - totalCompases;
      totalCompases += compases_x_parte;
      break;
    }
    totalCompases += compases_x_parte;
  }
  console.log("Compas", newCompas, "totalCompases", totalCompases , "Renglon", mostrando_renglon.value, "Palabra", mostrando_palabra.value);

  if (newCompas >= totalCompases) {
    mostrando_renglon.value = -1;
    mostrando_palabra.value = -1;
  }
});



</script>

<template>
<div id="letra">
  <div v-for="(linea, index) in cancion.letra.renglones" :key="index" class="linea">
    <span v-for="(palabra, index_palabra) in linea" :key="index_palabra" class="palabra" 
        :class="{ compas_actual: mostrando_renglon === index && mostrando_palabra === index_palabra }">
        {{ palabra }}&nbsp;
      </span>
  </div>

</div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
