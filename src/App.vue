<script setup lang="ts">
import { ref } from 'vue';
import { Cancion } from './modelo/cancion';

const cancion = ref(new Cancion(
    'Despacito', 
    'Luis Fonsi', 
    'Vamos a hacerlo en una playa en Puerto Rico...'
));

let vista = ref( {
   cargando_cancion: false
});
</script>

<template>

<div class="app">
    <h1>{{ cancion.titulo }}</h1>
    <h3>{{ cancion.artista }}</h3>
    <div class="cancion">
        
        <p>{{ cancion.letra }}</p>
    </div>
</div>



</template>

<style scoped>
.app {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.cancion {
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
}
</style>
