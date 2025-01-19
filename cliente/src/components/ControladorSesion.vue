<script setup lang="ts">
import { ref } from 'vue';
import { Cancion } from '../modelo/cancion';
import { watch } from 'vue';
import { Cliente } from '../modelo/client_socketio';
import 'bootstrap-icons/font/bootstrap-icons.css';
const props = defineProps<{ compas: number, cancion: Cancion, cliente: Cliente }>();
const currentCompas = ref(0);


watch(() => props.compas, (newCompas) => {
  currentCompas.value = newCompas;
});

</script>

<template>

  <div>
      Desconectado
  </div>
    

</template>

<style scoped>
.controls {
    display: flex;
    
}
</style>
