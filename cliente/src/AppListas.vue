<script setup lang="ts">
import { ref, markRaw, onMounted } from 'vue';
import { Almacenado } from './modelo/Almacenado';
import { item_lista } from './modelo/item_lista';
import { Banda } from './modelo/banda';
import { Cancion } from './modelo/cancion';
import { Acordes, Parte } from './modelo/acordes';
import { Letra } from './modelo/letra';

const almacen = new Almacenado();

const refindice_almacen = ref([]);
const muy_faciles = ref(false);
const indice_disponible = ref([]);
const indice_disponible_filtro = ref([]);
const fil_can = ref("");
const fil_ban = ref("");
const max_registros = ref(50);

const todo_almacen = almacen.indice();
let indice_almacen = [];
for (let i = 0; i < todo_almacen.length; i++) {
    console.log("Canción", todo_almacen[i]);
    indice_almacen.push(new item_lista(todo_almacen[i].cancion, todo_almacen[i].banda));
}
refindice_almacen.value = indice_almacen;


getIndice().then((indice) => {
    indice_disponible.value = indice;
    cancionesFiltradas() 
});


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

async function getIndice(): Promise<item_lista[]> {
        const response = await fetch(`/public/data/indice.json`);
        const data = await response.json();
        
        let items_lista = []
        for (let i = 0; i < data.length; i++) {
            items_lista.push(new item_lista(data[i].cancion, data[i].banda, data[i].total_partes, data[i].total_orden_partes));
        }
        return items_lista;

}

function cancionesFiltradas() 
{
    let indices_ret = [];
    let indice = 0;
    console.log("Ejec")
    console.log(indice_disponible.value.length)
    
    while ((indices_ret.length < max_registros.value) && (indice < indice_disponible.value.length)) 
    {
        if (indice_disponible.value[indice].cancion.toLowerCase().includes(fil_can.value.toLowerCase())
         && indice_disponible.value[indice].banda.toLowerCase().includes(fil_ban.value.toLowerCase()))
        {
            if (muy_faciles.value)
            {
                if (
                    (indice_disponible.value[indice].total_partes < 3)
                    && (indice_disponible.value[indice].total_orden_partes > 3)
             ) {
                    indices_ret.push(indice_disponible.value[indice]);
                }
            }
            else {

                indices_ret.push(indice_disponible.value[indice]);
            }
        }
        indice = indice + 1;
    }
    indice_disponible_filtro.value = indices_ret;

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
        refindice_almacen.value = almacen.indice();
    }); 
}



let canciones_lista: item_lista[] = [];
    const canciones_editando = ref(canciones_lista);
    canciones_lista = JSON.parse(localStorage.getItem("canciones_lista") || "[]");
    if (canciones_lista.length == 0)
    {
        canciones_lista = [
        
        ];
        localStorage.setItem("canciones_lista", JSON.stringify(canciones_lista));
    }
    canciones_editando.value = canciones_lista;


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

        <div v-if="1 == 0">
            <h1>Almacenado</h1>
        <div v-for="cancion in refindice_almacen" :key="cancion.cancion" class="cancion">
            {{ cancion.cancion }},  {{ cancion.banda }}
            <button @click="editarCancion(cancion.cancion, cancion.banda)">Editar</button>
            <button @click="agregarCancion(cancion.cancion, cancion.banda)">Agregar</button>
        </div>
    </div>
    <div>
        <h1>En indice disponible</h1>
        <div>
        Maximo: <input type="text" v-on:change="cancionesFiltradas()" v-model="max_registros" />
        </div>
        <div>
        Muy faciles: <input type="checkbox" v-on:change="cancionesFiltradas()" v-model="muy_faciles" />
        </div>
        <table>
            <thead>
                <tr>
                    <th>Canción</th>
                    <th>Banda</th>
                    <th>Acciones</th>
                    
                    <th>partes</th>                    
                    <th>uso partes</th>
                </tr>
                
                <tr>
                    <td><input type="text" v-on:change="cancionesFiltradas()" v-model="fil_can" /></td>
                    <td><input type="text" v-on:change="cancionesFiltradas()" v-model="fil_ban" /></td>
                    <td></td>
                </tr>

            </thead>
            <tbody>
            <tr v-for="cancion in indice_disponible_filtro" :key="cancion.cancion">
                <td>{{ cancion.cancion }}</td>
                <td>{{ cancion.banda }}</td>
                <td>
                        <button @click="editarCancion(cancion.cancion, cancion.banda)">Ver</button>
                        <button @click="agregarCancion_disponible(cancion.cancion, cancion.banda)">Agregar</button>
                    </td>
                <td> {{  cancion.total_partes }}</td>
                <td> {{  cancion.total_orden_partes }}</td>
            </tr>
            </tbody>
        </table>
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
