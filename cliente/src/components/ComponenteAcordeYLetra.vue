<script setup lang="ts">
import { ref, onMounted, onUnmounted, watchEffect } from 'vue';

const props = defineProps<{ texto: string, acorde: string  }>()
</script>
<template>
  <Fragment>
  <div v-for="(linea, linea_id) in props.texto.split('/n')" :key="linea">
    <span v-if="linea_id != 0"><br></span> {{ linea }}
  </div>
    
  </Fragment>
  <!-- Este bloque se renderiza si la condición es verdadera -->
  
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
