<script setup lang="ts">
import { ref, watch } from 'vue';
import { item_lista } from '../modelo/item_lista';

const emit = defineEmits(['click_editar', 'click_descargar', 'click_agregar', 'click_borrar']);
const props = defineProps<{ indice: item_lista[], titulo: string, muestra_renglones: number }>();
const indice_disponible = ref(props.indice);
const indice_disponible_filtro = ref([] as item_lista[]);
const editando = ref(false);

watch(() => props.indice, (newindice: item_lista[]) => {
  indice_disponible.value = newindice;
  cancionesFiltradas() 
});

function click_editar(indice: item_lista) {
    emit('click_editar', indice);
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
</script>

<template>
  
  
  <div >
    <h1>{{ titulo }}</h1>
    <div>

        <div>
        Maximo: <input type="text" v-on:change="cancionesFiltradas()" v-model="max_registros" />
        </div>
        <div>
        Muy faciles: <input type="checkbox" v-on:change="cancionesFiltradas()" v-model="muy_faciles" />
        Con buenas propos: <input type="checkbox" v-on:change="cancionesFiltradas()" v-model="con_buenaspropos" />
        </div>
        
        <div>
            
             Cancion <input type="text" v-on:change="cancionesFiltradas()" v-model="fil_can" />
             Banda <input type="text" v-on:change="cancionesFiltradas()" v-model="fil_ban" />
        </div>
                    
    </div>
    <div class="overflow-auto" style="max-height: 300px;">

        <table>
            <thead>
                <tr>
                    <th>Canción</th>
                    <th>Banda</th>
                    <th>Acciones</th>
                       
                    <th>escala</th>
                    <th>calidad</th>
                    <th>partes</th>                    
                    <th>uso partes</th>     
                </tr>
                
            </thead>
            <tbody>
                <template v-for="cancion in indice_disponible_filtro" :key="cancion.cancion">
            <tr >
                <td>{{ cancion.cancion }}</td>
                <td>{{ cancion.banda }}</td>
                <td>
                        <button @click="click_editar(cancion)">Editar</button>
                        <button @click="click_agregar(cancion)">Agregar</button>
                        <button @click="click_descargar(cancion)">Descargar</button>
                        <button @click="click_borrar(cancion)">Borrar</button>
                        
                    </td>
                    <td> {{  cancion.escala }}</td>
                    <td> {{  cancion.calidad }}</td>
                <td> {{  cancion.total_partes }} - {{ cancion.len_partes}} </td>
                <td> {{  cancion.total_orden_partes }}</td>
            </tr>
            <tr v-if="editando">
                <td colspan="7">
                    EDIT
                </td>
            </tr>
        </template>
            </tbody>
        </table>
    </div>
    
        
    </div>


</template>

<style scoped>
.controls {
    display: flex;
    
}

.beat_activo {
  background-color: greenyellow;
}

</style>






