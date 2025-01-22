<script setup lang="ts">
import { ref } from 'vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import 'bootstrap-icons/font/bootstrap-icons.css';
const props = defineProps<{ listas: string[] }>();
const vista_agregando = ref(false);
const nueva_lista = ref("");

const emit = defineEmits(['agrego_lista', 'ver_lista']);

function click_agregar() {
  vista_agregando.value = true;
}

function cancelarAgregar() {
  vista_agregando.value = false;
}

function confirmarAgregar() {
  vista_agregando.value = false;
  emit('agrego_lista', nueva_lista.value);
  nueva_lista.value = "";
}

function ver_lista(n: string) {
  emit('ver_lista', n);
}

</script>

<template>
  <div>
    
<div class="row">
  <div v-for="n in props.listas" :key="n" class="col-3" >
    {{ n }}
    <button @click="ver_lista(n)">
      <i class="bi bi-eye"></i>
    </button>
  </div>
  <div class="col-3">
    
    <button @click="click_agregar">
    <i class="bi bi-plus" ></i>
    </button>
    <input text="text"  v-if="vista_agregando"  v-model="nueva_lista" />
    <button  v-if="vista_agregando" @click="confirmarAgregar">
      <i class="bi bi-check"></i>
    </button>
    <button v-if="vista_agregando"  @click="cancelarAgregar">
      <i class="bi bi-x"></i>
    </button>
  </div>
  
</div>
  </div>
</template>

<style scoped>
</style>









function emit(arg0: string, value: string) {
  throw new Error('Function not implemented.');
}
