<script setup lang="ts">
import { ref } from 'vue';
import { Cancion } from '../modelo/cancion';
import { watch } from 'vue';
import 'bootstrap-icons/font/bootstrap-icons.css';
import { EstadoSesion } from '../modelo/estadosesion';
const props = defineProps<{ sesion: EstadoSesion }>();
const currentCompas = ref(0);
const refSesion = ref(props.sesion.estado);


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

  <div class="controlador_session">
      
      <div class="iniciado" v-if="refSesion=='Inic. s/conexion'">
        <select style="margin-right: 10px;" v-model="sesion.nombre">
          <option value="default">default</option>
          <option value="default2">default2</option>
          <option value="default3">default3</option>
          <option value="fogoneando">fogoneando</option>
          <option value="juntada">juntada</option>
          <option value="nuestra">nuestra</option>
          <option value="aca vamos">aca vamos</option>
        </select>
        <button @click="conectar" class="btnconectar">Conectarse</button>
      </div>
      <div v-if="refSesion!='Inic. s/conexion'">{{ refSesion }} </div>
     
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
  padding: auto;
}

.btnconectar {
  
  color: #a9a8f6;
  background-color: black;
  padding: 10px;
  font-size: x-large;
  border: 2px solid #a9a8f6;
}
</style>

