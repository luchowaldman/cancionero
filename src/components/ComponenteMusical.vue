<script setup lang="ts">
import { ref } from 'vue'
import { Cancion } from '../modelo/cancion';
import { Contexto } from '../modelo/contexto';

defineProps<{ compas: number, cancion: Cancion, contexto: Contexto }>()

const count = ref(0)


function Iniciar_Compas(nro_compas: number) 
{ 
  console.log(`Iniciando compás ${nro_compas} en ComponenteMusicalAcordes`); 
}


</script>

<template>
COMPONENTE MUSICAL
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
