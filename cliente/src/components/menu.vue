<script setup lang="ts">


const props = defineProps<{ titulo: string, viendo_vista: string }>()

</script>

<template>
  
   
  <nav class="navbar navbar-expand-sm navbar-dark bg-dark" aria-label="Third navbar example">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Cancionero</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample03" aria-controls="navbarsExample03" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarsExample03">
        <ul class="navbar-nav me-auto mb-2 mb-sm-0">
          <li class="nav-item">
            <a class="nav-link" :class="{active: viendo_vista == 'tocar'}" aria-current="page" href="/">Tocar</a>
          </li>
          
          <li class="nav-item dropdown " v-if="viendo_vista == 'tocar'">
            <a class="nav-link dropdown-toggle active" href="#" data-bs-toggle="dropdown" aria-expanded="false">Vistas</a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Guitarrista</a></li>
              <li><a class="dropdown-item" href="#">Cantante</a></li>
              <li><a class="dropdown-item" href="#">Multiple</a></li>
            </ul>
          </li>
          
          <li class="nav-item">
            <a class="nav-link " :class="{active: viendo_vista == 'editar'}"  aria-current="page" href="/edit">Editar</a>
          </li>
          <li class="nav-item">
            <a class="nav-link " :class="{active: viendo_vista == 'listas'}"  aria-current="page" href="/listas">Listas</a>
          </li>
          <li class="nav-item">
            <a class="nav-link " :class="{active: viendo_vista == 'config'}"  aria-current="page" href="/config">Configuracion</a>
          </li>
        </ul>
      </div>
      
    </div>
  </nav>

</template>

<style scoped>
</style>
