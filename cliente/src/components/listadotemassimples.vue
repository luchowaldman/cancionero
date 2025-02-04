<script setup lang="ts">
import { ref, watch } from 'vue';
import { item_lista } from '../modelo/item_lista';
import { Musica } from '../modelo/musica';
import { Tiempo } from '../modelo/tiempo';

const emit = defineEmits(['click_ver', 'click_descargar', 'click_agregar', 'click_borrar']);
const props = defineProps<{ indice: item_lista[], titulo: string, muestra_renglones: number
    ,  btnVer: boolean, btnDescargar: boolean, btnAgregar: boolean, btnBorrar: boolean, nro_cancion: number
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

                
                <tr v-for="(cancion, cancionid) in indice" :key="cancionid" :class="{ 'tocando-cancion': nro_cancion === cancionid }">

                
                   <td >
                      <span style="font-size: 24px;">{{ FormatearNombre(cancion.cancion) }}</span> -                        <span style="font-size: 15px;">{{ FormatearNombre(cancion.banda) }}</span>
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
            
            </tbody>
        </table>
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

.tocando-cancion {
    color: #d2ab46;
}

.viendodetalles {
    background-color: #d2ab46;
    color: white;
}

.origen {
    font-size: 14px;
    border: 4px solid;
    padding: 6px;
    border-radius: 5px;
}


.duracion {
    font-size: 20px;
    padding: 6px;
    border-radius: 5px;
}


.escala {
    font-size: 20px;
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
    padding: 1px;
}

.tablaListas td {
    padding: 1px;
}

.tablaListas tbody tr:nth-child(odd) {
    background-color: black;
}

.tablaListas tbody tr:nth-child(even) {
    background-color: black;
    border: 1px solid;
}

.btnGrilla {
    display: inline-block;
    border: 1px solid;
    font-size: xx-large;
    padding: 3px;
    margin: 5px;
    cursor: pointer;
}

</style>






