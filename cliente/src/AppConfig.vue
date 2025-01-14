<script setup lang="ts">
import { ref, markRaw, onMounted, watch } from 'vue';
import Menu from './components/menu.vue';
// Definir la canción y el contexto

const viendo = ref("perfil")
const configuracion = ref(localStorage.getItem("configuracion"))
if (configuracion.value == undefined)
  console.log("SS")
  configuracion.value = "{asd}"




    // Llamar a la función iniciarCompasEnComponentes cuando sea necesario 
    onMounted(() => { 
        console.log("APP CONFIGURACION MONTADA")
    });
    function click_opcion(viendostr: string) {
      viendo.value = viendostr
      
    }

</script>

<template>
    <div>
        
        <Menu titulo="Configuracion"></Menu>
        
  <div class="d-flex flex-column flex-shrink-0 p-3 text-bg-dark" style="width: 280px;">
    <ul class="nav nav-pills flex-column mb-auto">
    
      
      <li @click="click_opcion('perfil')">
        <a href="#" class="nav-link text-white"  :class="{ 'active': viendo==='perfil' }" >
          
          Perfil
        </a>
      </li>
      
      <li @click="click_opcion('sesion')">
        <a href="#" class="nav-link text-white" :class="{ 'active': viendo==='sesion' }" >
          
          Sesion
        </a>
      </li>
    </ul>

    <hr>
    <ul class="nav nav-pills flex-column mb-auto">
      
      <li @click="click_opcion('vistas')">
        <a href="#" class="nav-link text-white"
        :class="{ 'active': viendo==='vistas' }" >
          
          Vistas
        </a>
      </li>
      <li @click="click_opcion('conexiones')">
        <a href="#" class="nav-link text-white"
        :class="{ 'active': viendo==='conexiones' }" >
          
          Conexiones
        </a>
      </li>
      <li @click="click_opcion('datos')">
        <a href="#" class="nav-link text-white"
          :class="{ 'active': viendo==='datos' }" >
          Datos
        </a>
      </li>
      
      
    </ul>
    <hr>
    
  </div>

</div>
</template>

<style scoped></style>
