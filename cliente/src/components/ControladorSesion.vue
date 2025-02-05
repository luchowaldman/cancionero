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
  <div class="controlador_session" :class="{conectado: sesion.estado == 'conectado'}">
     
    <div class="iniciado" v-if="sesion.estado=='conectado'">
        <i class="bi bi-wifi"></i>
        <button @click="emit('desconectar');" >DESCONECTAR</button>
        <i class="bi bi-magic"></i>
      </div>
      
    
      <div class="iniciado" v-if="sesion.estado=='Desconectado'">
        <select style="margin-right: 10px;" v-model="sesion.nombre">
          <option value="default">default</option>
          <option value="default2">default2</option>
          <option value="default3">default3</option>
          <option value="fogoneando">fogoneando</option>
          <option value="juntada">juntada</option>
          <option value="nuestra">nuestra</option>
          <option value="aca vamos">aca vamos</option>
        </select>
        <button @click="emit('conectar');" class="btnconectar">Conectarse</button>
      </div>
      
     
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

