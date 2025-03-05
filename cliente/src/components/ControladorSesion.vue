<script setup lang="ts">
import { ref } from 'vue';
import 'bootstrap-icons/font/bootstrap-icons.css';
import { EstadoSesion } from '../modelo/estadosesion';
defineProps<{ sesion: EstadoSesion }>();
const nro = ref(0);
const emit = defineEmits(['conectar', 'desconectar']);

function conectar() {
  emit('conectar');
}

function actualizar_vista() {
  console.log("actualizar_vista");
  nro.value++;
  }

  defineExpose ({ actualizar_vista  });


</script>

<template>
  <div>
    {{ sesion.estado}}
<div @click="conectar" v-if="sesion.estado == 'Desconectado'">
  <i class="bi bi-diagram-2"></i>Conectar {{ sesion.estado}}
</div>

<div @click="conectar" v-if="sesion.estado == 'conectado'">
  <i class="bi bi-diagram-2"></i>Desconectar
</div>
</div>
</template>

<style scoped>
.controls {
    display: flex;
    
}

.iniciado {
  border: 1px solid;
  border-radius: 5%;
  font-size: x-large;
  padding: 20px;
}

.controlador_session {
  border-color: blue;
}

.btnconectar {
  
  color: #a9a8f6;
  background-color: black;
  padding: 10px;
  font-size: x-large;
  border: 2px solid #a9a8f6;
}


.conectado {
  border-color: #f5da09;
}

</style>

