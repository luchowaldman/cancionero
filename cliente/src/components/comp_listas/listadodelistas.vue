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
    
<div class="listado">
  <div v-for="n in props.listas" :key="n"  >
    {{ n }}
    <button @click="ver_lista(n)">
      <i class="bi bi-eye"></i>
    </button>
  </div>
  <div>
    
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
</template>

<style scoped>
.listado {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  
  margin-top: 20px;
  font-size: 50px;
}
</style>





