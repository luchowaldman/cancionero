<script setup lang="ts">
import { ref, watch } from 'vue';
import { item_lista } from '../modelo/item_lista';
import { Musica } from '../modelo/musica';
import { Tiempo } from '../modelo/tiempo';

const emit = defineEmits(['click_ver', 'click_descargar', 'click_agregar', 'click_borrar']);
const props = defineProps<{ indice: item_lista[], titulo: string, muestra_renglones: number
    ,  btnVer: boolean, btnDescargar: boolean, btnAgregar: boolean, btnBorrar: boolean
 }>();
const musica = new Musica();
const tiempo = new Tiempo();
const indice_disponible = ref(props.indice);
const viendo_detalles = ref([] as number[]);
const indice_disponible_filtro = ref([] as item_lista[]);


function VerDetalle(indice: number) {
    if (viendo_detalles.value.includes(indice)) {
        viendo_detalles.value = viendo_detalles.value.filter((item) => item != indice);
    } else {
        viendo_detalles.value.push(indice);
    }
}

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
const max_registros = ref(100);
const calidad_min = ref(0);
const calidad_max = ref(10);

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

        if (calidad_min.value >= indice_disponible.value[indice].calidad) {
            incluye = false;
        }
        if (calidad_max.value <= indice_disponible.value[indice].calidad) {
            incluye = false;
        }
        
        

            if (incluye) {
                indices_ret.push(indice_disponible.value[indice]);
            }
        indice = indice + 1;
    }
    indice_disponible_filtro.value = indices_ret;

    viendo_detalles.value = [];
}
cancionesFiltradas();


function FormatearNombre(nombre: string) {
    return nombre.replace(/-/g, ' ').toLowerCase().replace(/^\w/, c => c.toUpperCase());
}

defineExpose({  cancionesFiltradas });

</script>

<template>
  
  
  <div >
    <div class="overflow-auto" :style="{'max-height': muestra_renglones * 40 + 'px'}">

        <table class="tablaListas">
            <thead>
                <tr>
                    <th>Canción</th>
                    <th>Origen</th>
                    <th>Duracion</th>
                    <th style="width: 3ch;">Escala</th>
                    <th>Acciones</th>  
                </tr>
                
            </thead>
            <tbody>

                <template v-for="(cancion, cancionid) in indice_disponible_filtro" :key="cancionid" >
                <tr >
                    <td >
                        <p style="font-size: 30px;">{{ FormatearNombre(cancion.cancion) }}</p>
                        <p style="font-size: 20px;">{{ FormatearNombre(cancion.banda) }}</p>
                    </td>
                    
                    <td>
                        <div class="origen" v-if="cancion.origen.startsWith('url')">{{ cancion.origen }}</div>
                        

                    </td>
                    <td> 
                        <div class="duracion">  {{ tiempo.formatSegundos(musica.duracion_cancion_indice(cancion))  }} </div>
                        
                    </td>
                    <td>
                        
                        <div class="escala">  {{   cancion.escala  }} </div>
                        

                    </td>
             
                    
                    <td>
                                    
                        
                                            <div class="btnGrilla" v-if="btnVer" @click="click_ver(cancion)">
                                            <i class="bi bi-fire"></i>
                                            </div>

                                            <div class="btnGrilla" v-if="btnVer" @click="VerDetalle(cancionid)"
                                            :class="{viendodetalles: viendo_detalles.includes(cancionid)}"
                                            >
                                            <i class="bi bi-eye"></i>
                                            </div>


                                                                                        
                                            <div class="btnGrilla" v-if="btnDescargar" @click="click_descargar(cancion)">
                                            <i class="bi bi-save"></i>
                                            </div>
                                            <div class="btnGrilla" v-if="btnVer" @click="click_ver(cancion)">
                                            <i class="bi bi-pencil"></i>
                                            </div>

                                            <div class="btnGrilla" v-if="btnAgregar" @click="click_agregar(cancion)">
                                            <i class="bi bi-plus"></i>
                                            </div>
                                            <div class="btnGrilla" v-if="btnBorrar" @click="click_borrar(cancion)">
                                            <i class="bi bi-trash"></i>
                                            </div>
                                        </td>
                </tr>
                <tr v-if="viendo_detalles.includes(cancionid)">
                    <td colspan="6">
                        
                        <table style="width: 100%;">
                            <thead>
                                <tr>
                                    <th colspan="4">Detalles</th>
                                </tr>
                            </thead>
                            <tr>
                                <td>Compás:</td>
                                <td><strong>{{ cancion.compas_cantidad }} / {{ cancion.compas_unidad }}</strong></td>
          
                                <td>BPM:</td>
                                <td><strong>{{ cancion.bpm }}</strong></td>
                            </tr>
                            <tr>
                                <td>Calidad:</td>
                                <td><strong>{{ cancion.calidad }}</strong></td>
                                <td>Compases:</td>
                                <td><strong>{{ cancion.compases }}</strong></td>
                            </tr>
                            <tr>
                                <td>Longitud de Secuencia:</td>
                                <td><strong>{{ cancion.len_secuencia }}</strong></td>
                                <td>Longitud de Partes:</td>
                                <td><strong>{{ cancion.len_partes }}</strong></td>
                            </tr>
                            <tr>
                                <td>Acordes:</td>
                                <td colspan="3">
                                    <div class="acordes">
                                    <div v-for="(c, i) in cancion.acordes.split('.')" class="acorde"> {{  c }}</div>
                                </div>
                                </td>
                            </tr>
                        </table>
                    </td>

                </tr>
            </template>
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
        <div>
            Rango de calidad: 
            <input type="range" min="0" max="10" v-model="calidad_min" @change="cancionesFiltradas()" />
            <span>{{ calidad_min }}</span>
            -
            <input type="range" min="0" max="10" v-model="calidad_max" @change="cancionesFiltradas()" />
            <span>{{ calidad_max }}</span>
        </div>
    </div>
        
    </div>


</template>

<style scoped>
.controls {
    display: flex;
    
}

.acordes {
    display: flex;
    flex-wrap: wrap;
}

.acorde {
    font-size: 40px;
    border: 4px solid;
    padding: 6px;
    border-radius: 5px;
    margin: 3px;
    width: fit-content;

}

.viendodetalles {
    background-color: #d2ab46;
    color: white;
}

.origen {
    font-size: 20px;
    border: 4px solid;
    padding: 6px;
    border-radius: 5px;
}


.duracion {
    font-size: 40px;
    padding: 6px;
    border-radius: 5px;
}


.escala {
    font-size: 40px;
    padding: 6px;
    border-radius: 5px;
    border: 4px solid;
    padding: 6px;
    border-radius: 5px;
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

.btnGrilla {
    display: inline-block;
    border: 1px solid;
    font-size: xx-large;
    padding: 10px;
    margin: 3px;
    cursor: pointer;
}

</style>






