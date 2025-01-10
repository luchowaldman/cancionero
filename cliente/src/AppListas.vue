<script setup lang="ts">
import { ref, markRaw, onMounted } from 'vue';
import { Almacenado } from './modelo/Almacenado';
import { item_lista } from './modelo/item_lista';
import { Banda } from './modelo/banda';
import { Cancion } from './modelo/cancion';
import { Acordes, Parte } from './modelo/acordes';
import { Letra } from './modelo/letra';

const almacen = new Almacenado();
const indice = ref(almacen.indice());


const mascanciones: Banda[]  = [
    new Banda("andres Calamaro", ["flaca", "cuando no estas", "te quiero igual", "crimenes perfectos", "paloma", "cartas sin marcar", "donde manda marinero", "pasemos a otro tema", "mi gin tonic", "loco", "soy tuyo", "el salmon", "alta suciedad", "media veronica", "bohemio"]),
    new Banda("Intoxicados", ["esta saliendo el sol", "fuiste lo mejor","casi sin pensar", "fuego", "necesito", "no tengo ganas", "pila pila", "volver a casa"])
   // new Banda("Viejas Locas", ["esta saliendo el sol", "fuiste lo mejor","casi sin pensar", "fuego", "necesito", "no tengo ganas", "pila pila", "volver a casa"]),
   // new Banda("Beatles", ["esta saliendo el sol", "fuiste lo mejor","casi sin pensar", "fuego", "necesito", "no tengo ganas", "pila pila", "volver a casa"]),

]


async function getCancion(banda: string, tema: string): Promise<Cancion> {
        const response = await fetch(`/public/data/${banda.replace(/\s+/g, '-')}_${tema.replace(/\s+/g, '-')}.json`);
        const data = await response.json();
        
        let partes = []
        for (let i = 0; i < data.acordes.partes.length; i++) {
            partes.push(new Parte(data.acordes.partes[i].nombre, data.acordes.partes[i].acordes));
        }

        
        const acordes = new Acordes(partes, data.acordes.orden_partes);
    
        return new Cancion(
            data.cancion,
            data.banda,
            acordes,
            new Letra(data.letras) 
        );
    }

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



function cargarTodo() {
    for (let i = 0; i < mascanciones.length; i++) {
        for (let j = 0; j < mascanciones[i].canciones.length; j++) {
            getCancion(mascanciones[i].nombre, mascanciones[i].canciones[j]).then((cancion) => {
                console.log("Canción obtenida", cancion);
                almacen.agregarCancion(cancion);
                indice.value = almacen.indice();
            }); 
        }
    }
    
}


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

function agregarCancion_disponible(cancion: string, banda: string) {
    getCancion(banda, cancion).then((cancion) => {
        console.log("Canción obtenida", cancion);
        almacen.agregarCancion(cancion);
        indice.value = almacen.indice();
    }); 
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

    
    <div>
            <h1>Disponibles   </h1><button @click="cargarTodo()">Cargar todo</button>
        <div v-for="banda in mascanciones" :key="banda.nombre" class="cancion">
            <h1>{{ banda.nombre }}</h1>
            <div v-for="cancion in banda.canciones" :key="cancion" class="cancion">
                {{ cancion }}
                <button @click="agregarCancion_disponible(cancion, banda.nombre)">Agregar</button>
            </div>
            
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
