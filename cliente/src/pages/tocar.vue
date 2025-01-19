<script setup lang="ts">

import { Cancion } from '../modelo/cancion';
import { Contexto } from '../modelo/contexto';
import ComponenteMusicalLetraAcordes from '../components/ComponenteMusicalLetrayAcordes.vue';
import ComponenteMusicalAcordes from '../components/ComponenteMusicalAcordes.vue';
import { markRaw, ref } from 'vue';


const props = defineProps<{ compas: number, cancion: Cancion }>()


// Vector de componentes musicales
const componentesMusicales = ref([

    markRaw(ComponenteMusicalLetraAcordes),
    markRaw(ComponenteMusicalAcordes)
]);



</script>

<template>
  
  <div class="pantalla">

<h1>{{ cancion.cancion }}</h1>
<h2>{{ cancion.banda }}</h2>
<div class="row">
<div v-for="(Componente, index) in componentesMusicales" :key="index" 
:class="{ 'col-7': index == 0,
         'col-3': index == 1
} ">
   <component :is="Componente" :compas="compas" :cancion="cancion"></component>
</div>
</div>



 </div>

</template>

<style scoped>
</style>
