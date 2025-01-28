<script setup lang="ts">

import { Cancion } from '../modelo/cancion';
import { VistaControl } from '../modelo/vista_control';
import { markRaw, ref } from 'vue';


const props = defineProps<{ compas: number, cancion: Cancion }>()


const vist: VistaControl[] = [
 new VistaControl(window.innerHeight / 50, 12, 7, "letra_acordes", "col-9", (window.innerHeight / 1.7)),
 //new VistaControl(window.innerHeight / 50, 12, 7, "detalle", "col-9", (window.innerHeight / 1.7)),
  new VistaControl(30, 12, 7, "acordes", "col-3 d-md-block", 1400)

];
const ref_vista = ref(vist);

</script>

<template>
  
  <div class="pantalla">

<div class="row">
    <div v-for="(Componente, index) in ref_vista" :key="index" 
    :class="Componente.clase">
      <component :is="Componente.getMarkRaw()" :compas="compas" :vista="Componente" :cancion="cancion"></component>
    </div>
</div>



 </div>

</template>

<style scoped>
</style>
