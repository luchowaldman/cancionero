<script setup lang="ts">
import { ref, watch } from 'vue';
import { item_lista } from '../modelo/item_lista';

const emit = defineEmits(['click_ver', 'click_descargar', 'click_agregar', 'click_borrar']);
const props = defineProps<{ indice: item_lista[], titulo: string, muestra_renglones: number
    ,  btnVer: boolean, btnDescargar: boolean, btnAgregar: boolean, btnBorrar: boolean
 }>();

const indice_disponible = ref(props.indice);
const indice_disponible_filtro = ref([] as item_lista[]);

watch(() => props.indice, (newindice: item_lista[]) => {
  indice_disponible.value = newindice;
  cancionesFiltradas() 
});

function click_ver(item: item_lista) {
    emit('click_ver', item);
}

function click_descargar(indice: item_lista) {
    emit('click_descargar', indice);
}

function click_agregar(indice: item_lista) {
    emit('click_agregar', indice);
}

function click_borrar(indice: item_lista) {
    emit('click_borrar', indice);
}


const muy_faciles = ref(false);
const fil_can = ref("");
const fil_ban = ref("");
const max_registros = ref(3000);

const con_buenaspropos = ref(false);

function cancionesFiltradas() 
{
    //console.log("Filtrando", indice_disponible.value);
    let indices_ret = [];
    let indice = 0;    
    while ((indices_ret.length < max_registros.value) && (indice < indice_disponible.value.length)) 
    {
        let incluye = true

        if (fil_can.value != "") {
            if (!indice_disponible.value[indice].cancion.toLowerCase().includes(fil_can.value.toLowerCase()))
            {
                incluye = false;
            }
        }
        if (fil_ban.value != "") {
            if (!indice_disponible.value[indice].banda.toLowerCase().includes(fil_ban.value.toLowerCase()))
            {
                incluye = false;
            }
        }
        
        
            if (muy_faciles.value)
            {
                if (!((indice_disponible.value[indice].total_partes < 3)
                    && (indice_disponible.value[indice].total_orden_partes > 3)))
                {
                    
                    incluye = false;
                }
            }
            if (con_buenaspropos.value)
            {
            }


            if (incluye) {
                indices_ret.push(indice_disponible.value[indice]);
            }
        indice = indice + 1;
    }
    indice_disponible_filtro.value = indices_ret;

}
cancionesFiltradas();


function FormatearNombre(nombre: string) {
    return nombre.replace(/-/g, ' ').toLowerCase().replace(/^\w/, c => c.toUpperCase());
}

defineExpose({  cancionesFiltradas });

</script>

<template>
  
  
  <div >
    <div class="overflow-auto" style="max-height: 300px;">

        <table class="tablaListas">
            <thead>
                <tr>
                    <th>Canción</th>
                    <th>Banda</th>
                    <th>Origen</th>
                    <th>Escala</th>
                    <th>BPM</th>
                    <th>compas</th>
                    <th>calidad</th>
                    <th>Acciones</th>  
                </tr>
                
            </thead>
            <tbody>
                <tr v-for="(cancion, cancionid) in indice_disponible_filtro" :key="cancionid" >
                    <td style="font-size: x-large;">{{ FormatearNombre(cancion.cancion) }}</td>
                    <td>{{ FormatearNombre(cancion.banda) }}</td>
                    <td>{{ cancion.origen }}</td>

                    <td> {{  cancion.escala }}</td>
                        <td> {{  cancion.bpm }}</td>
                        <td> {{  cancion.compases_tiempo }} / {{ cancion.compases_tiempo }}</td>
                        <td> {{  cancion.calidad }}</td>
                    
                    <td>
                                            
                                            <button v-if="btnVer" @click="click_ver(cancion)" class="btn btn-primary">
                                            <i class="bi bi-eye"></i>
                                            </button>
                                            
                                            <button v-if="btnDescargar" @click="click_descargar(cancion)" class="btn btn-warning">
                                            <i class="bi bi-download"></i>
                                            </button>
                                            <button v-if="btnAgregar" @click="click_agregar(cancion)" class="btn btn-success">
                                            <i class="bi bi-plus"></i>
                                            </button>
                                            <button v-if="btnBorrar" @click="click_borrar(cancion)" class="btn btn-danger">
                                            <i class="bi bi-trash"></i>
                                            </button>
                                        </td>
                </tr>
            
            </tbody>
        </table>
    </div>
    
    
    <div class="controls">
        <div>{{  indice_disponible_filtro.length }} de <input type="text" v-on:change="cancionesFiltradas()" v-model="max_registros" /></div>
        <div>
        Muy faciles: <input type="checkbox" v-on:change="cancionesFiltradas()" v-model="muy_faciles" />
        Con buenas propos: <input type="checkbox" v-on:change="cancionesFiltradas()" v-model="con_buenaspropos" />
        </div>
        
        <div>
            
             Cancion <input type="text" v-on:change="cancionesFiltradas()" v-model="fil_can" />
             Banda <input type="text" v-on:change="cancionesFiltradas()" v-model="fil_ban" />
        </div>
                    
    </div>
        
    </div>


</template>

<style scoped>
.controls {
    display: flex;
    
}

.beat_activo {
    background-color: rgb(235, 67, 16);
}

.controls {
    display: flex; border: 1px solid;
    padding: 3px;
}


.controls div {
    border: 1px solid;
    margin: 3px;
    padding: 3px;
}

.tablaListas {
    width: 100%;
    font-size: large;
    border-collapse: collapse;
}

.tablaListas th {
    background-color: #a9a8f6;
    color: white;
    font-size: larger;
    padding: 10px;
}

.tablaListas td {
    padding: 10px;
}

.tablaListas tbody tr:nth-child(odd) {
    background-color: #f0f8ff; /* Light blue */
}

.tablaListas tbody tr:nth-child(even) {
    background-color: white;
}



</style>






