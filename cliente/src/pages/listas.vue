<script setup lang="ts">
import { ref } from 'vue';
import { Almacenado } from '../modelo/Almacenado';
import { item_lista } from '../modelo/item_lista';
import { Cancion } from '../modelo/cancion';
import ListadoTemas from '../components/listadotemas.vue';
import { Acordes } from '../modelo/acordes';
import { Letra } from '../modelo/letra';
import { AdminListasURL } from '../modelo/AdminListasURL';
import { AdminListasLocalStorage } from '../modelo/AdminListasStorage';
import { GetCanciones } from '../modelo/GetCanciones';
import { AdminListasTocables } from '../modelo/AdminListasTocables';
import ComponenteMusicalEditar from '../components/ComponenteMusicalEditar.vue';

const editref = ref();
const editando_cancion = ref(false);
const cancion_ver  = ref(new Cancion("no song name", "no band name", new Acordes([], []), new Letra([])));

const almacen = new Almacenado();
const generadorlistasLS = new AdminListasLocalStorage(almacen);
const generadorlistasTocables = new AdminListasTocables(almacen);
const canciones_Storage = ref([] as item_lista[]);
const canciones_tocables = ref([] as item_lista[]);
let canciones_url = ref([] as item_lista[]);

// INICIALIZA LAS LISTAS DE CANCIONES GENERADAS
const generadorlistasURL = new AdminListasURL('/data');

generadorlistasURL.getIndice().then((indice: item_lista[]) => {
    canciones_url.value = indice;
});



generadorlistasLS.getIndice().then((indi_get: item_lista[]) => {
    canciones_Storage.value = indi_get;
});


function click_editar_URL(item: item_lista) {
    
    GetCanciones.obtenerCancion(item).then((cancion_get: Cancion) => {
        editando_cancion.value = true;
        cancion_ver.value = cancion_get;
        //editref.value?.reload_song();   
    });
}

function cerro_editar() {
    editando_cancion.value = false;
}




</script>

<template>
    <div>
       <div>
        <ComponenteMusicalEditar @cerrar="cerro_editar" :editando_cancion="editando_cancion" :compas="-1" :cancion="cancion_ver"  ref="editref"></ComponenteMusicalEditar>
    </div>
    <div v-if="!editando_cancion">

    <ListadoTemas titulo="En data generada por Luis Waldman" :indice="canciones_url" :muestra_renglones=10
    :btnVer=true v-on:click_ver="click_editar_URL" :btnDescargar=true :btnAgregar=false :btnBorrar=false
    ></ListadoTemas>
  
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
