<script setup lang="ts">
import { ref } from 'vue';
import { Cancion } from '../modelo/cancion';
import { watch } from 'vue';
import 'bootstrap-icons/font/bootstrap-icons.css';
import { EstadoSesion } from '../modelo/estadosesion';
const props = defineProps<{ compas: number, cancion: Cancion, sesion: EstadoSesion }>();
const currentCompas = ref(0);
const refSesion = ref(props.sesion.estado);

watch(() => props.compas, (newCompas) => {
  currentCompas.value = newCompas;
});

watch(() => props.sesion.estado, (newSesion) => {
  refSesion.value = newSesion;
  console.log("Nueva sesion", newSesion);
});

const emit = defineEmits(['conectar']);

function conectar() {
  emit('conectar');
}

</script>

<template>

  <div>
      <div class="tit_estado">{{  refSesion }}</div>
      <div v-if="refSesion=='Inic. s/conexion'">
        <input type="text" v-model="sesion.nombre" />
        
        
        <button @click="conectar">Conectarse</button>
        <input v-model="sesion.iniciar_alcomienzo" type="checkbox">
      Al Iniciar
      </div>
     
</div>

</template>

<style scoped>
.controls {
    display: flex;
    
}
</style>
