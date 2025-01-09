<script setup lang="ts">
import { ref, markRaw, onMounted } from 'vue';
import { Almacenado } from './modelo/Almacenado';

const almacen = new Almacenado();
const indice = ref(almacen.indice());

const canciones = localStorage.getItem("canciones");

function editarCancion(cancion: string, banda: string) {
    console.log("Editar canción", cancion, banda);
    localStorage.setItem("editar_cancion", cancion);
    localStorage.setItem("editar_banda", banda);
    window.location.href = '/edit';
}

</script>

<template>
    <div>
        
        <div>
            <h1>Almacenado</h1>
        <div v-for="cancion in indice" :key="cancion.cancion" class="cancion">
            {{ cancion.cancion }},  {{ cancion.banda }}
            <button @click="editarCancion(cancion.cancion, cancion.banda)">Editar</button>
        </div>
    </div>

        <div>
            <h1>Almacenado</h1>
        <div v-for="cancion in indice" :key="cancion.cancion" class="cancion">
            {{ cancion.cancion }},  {{ cancion.banda }}
            <button @click="editarCancion(cancion.cancion, cancion.banda)">Editar</button>
        </div>
    </div>
</div>
</template>

<style scoped>
#contenedor-musical {
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
