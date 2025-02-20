<script setup lang="ts">
import { ref } from 'vue';
import { watch } from 'vue';
import 'bootstrap-icons/font/bootstrap-icons.css';
import { EstadoSesion } from '../modelo/estadosesion';
const props = defineProps<{ sesion: EstadoSesion }>();
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
  <i class="bi bi-diagram-2"></i>Conectar
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

