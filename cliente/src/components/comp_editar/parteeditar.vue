<script setup lang="ts">
import { item_lista } from '../../modelo/item_lista';
import { Cancion } from '../../modelo/cancion';
import { ref } from 'vue';



const props = defineProps<{ cancion: Cancion, item: item_lista, parte_indice: number, parte: number }>();
const editando = ref(false);


</script>

<template>
<div>
  
  {{ cancion.acordes.partes[parte].acordes }}

  
  {{  parte_indice  }} {{ parte }}
</div>
          

</template>

<style scoped>
</style>

