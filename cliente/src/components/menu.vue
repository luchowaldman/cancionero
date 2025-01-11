<script setup lang="ts">
import { ref } from 'vue'
import { Cancion } from '../modelo/cancion';


const props = defineProps<{ titulo: string }>()

</script>

<template>
  
   
  <nav class="navbar navbar-expand-sm navbar-dark bg-dark" aria-label="Third navbar example">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">{{ props.titulo }}</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample03" aria-controls="navbarsExample03" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarsExample03">
        <ul class="navbar-nav me-auto mb-2 mb-sm-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="/">Tocar</a>
          </li>
          
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="/edit">Editar</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="/listas">Listas</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="/config">Configuracion</a>
          </li>
        </ul>
      </div>
      
    </div>
  </nav>

</template>

<style scoped>
</style>
