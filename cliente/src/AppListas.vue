<script setup lang="ts">
import { ref, markRaw, onMounted } from 'vue';
import { Almacenado } from './modelo/Almacenado';
import { item_lista } from './modelo/item_lista';

const almacen = new Almacenado();
const indice = ref(almacen.indice());




/*
localStorage.setItem("canciones_lista", JSON.stringify([
    new item_lista("Esta saliendo el sol", "Intoxicados"),
    new item_lista("Fuego", "Intoxicados"),
    new item_lista("fuiste lo mejor", "Intoxicados"),
    ]));

*/
    let canciones_lista: item_lista[] = [];
    const canciones_editando = ref(canciones_lista);
    canciones_lista = JSON.parse(localStorage.getItem("canciones_lista") || "[]");
    if (canciones_lista.length == 0)
    {
        canciones_lista = [
        new item_lista("Esta saliendo el sol", "Intoxicados"),
        new item_lista("Fuego", "Intoxicados"),
        new item_lista("fuiste lo mejor", "Intoxicados"),
        ];
        localStorage.setItem("canciones_lista", JSON.stringify(canciones_lista));
    }
    canciones_editando.value = canciones_lista;


function editarCancion(cancion: string, banda: string) {
    console.log("Editar canción", cancion, banda);
    localStorage.setItem("editar_cancion", cancion);
    localStorage.setItem("editar_banda", banda);
    window.location.href = '/edit';
}

function agregarCancion(cancion: string, banda: string) {
    console.log("Agregar canción", cancion, banda);
    canciones_editando.value.push(new item_lista(cancion, banda));
    localStorage.setItem("canciones_lista", JSON.stringify(canciones_lista));
}

function borrarCancion(indice: number) {
    console.log("Borrar canción", indice);
    canciones_editando.value.splice(indice, 1);
    localStorage.setItem("canciones_lista", JSON.stringify(canciones_lista));
}


</script>

<template>
    <div>
        
        <div>
            <h1>Lista actual</h1>
        <div v-for="(cancion, cancion_id) in canciones_editando" :key="cancion.cancion" class="cancion">
            {{ cancion.cancion }}, {{ cancion.banda }}
            <button @click="borrarCancion(cancion_id)">Borrar</button>
            
        </div>
    </div>

        <div>
            <h1>Almacenado</h1>
        <div v-for="cancion in indice" :key="cancion.cancion" class="cancion">
            {{ cancion.cancion }},  {{ cancion.banda }}
            <button @click="editarCancion(cancion.cancion, cancion.banda)">Editar</button>
            <button @click="agregarCancion(cancion.cancion, cancion.banda)">Agregar</button>
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
