<script setup lang="ts">
import { ref } from 'vue';
import { Almacenado } from '../modelo/Almacenado';
import { item_lista } from '../modelo/item_lista';
import { Cancion } from '../modelo/cancion';
import ListadoTemas from '../components/listadotemassimples.vue';
import ListadoListas from '../components/listadodelistas.vue';
import { Acordes } from '../modelo/acordes';
import { Letra } from '../modelo/letra';
import { AdminListasURL } from '../modelo/AdminListasURL';
import { AdminListasLocalStorage } from '../modelo/AdminListasStorage';
import { GetCanciones } from '../modelo/GetCanciones';
import { AdminListasTocables } from '../modelo/AdminIndiceListas';
import ComponenteMusicalEditar from '../components/ComponenteMusicalEditar.vue';

const props = defineProps<{ nro_cancion: number }>();

const emit = defineEmits(['acciono']);
const ctrlguardados = ref();
const ctrlviendolista = ref();
const editando_cancion = ref(false);
const cancion_ver  = ref(new Cancion("no song name", "no band name", new Acordes([], []), new Letra([])));
const itemindice_ref = ref(new item_lista("no song name", "no band name"));

editando_cancion.value = (localStorage.getItem("editando") == "si");
if (editando_cancion.value) {
    let item = JSON.parse(localStorage.getItem("editando_cancion") || "{}");
    click_editar_item(item);
}




const canciones_Actual = ref([] as item_lista[]);
let canciones_url = ref([] as item_lista[]);
// INICIALIZA LAS LISTAS DE CANCIONES GENERADAS
const generadorlistasURL = new AdminListasURL('/data/canciones');
const almacen = new Almacenado();
const generadorlistasLS = new AdminListasLocalStorage(almacen);

const canciones_Storage = ref(almacen.indice());

const listas = ref([] as string[]);
listas.value = generadorlistasLS.listas();
const admin_indiceslista = new AdminListasTocables();

canciones_Actual.value = admin_indiceslista.GetIndice("default");
ctrlviendolista.value?.cancionesFiltradas();
ctrlguardados.value?.cancionesFiltradas();

generadorlistasURL.getIndice().then((indice: item_lista[]) => {
    canciones_url.value = indice;
});





function click_editar_item(item: item_lista) {
    
    localStorage.setItem("editando_cancion", JSON.stringify(item));
    emit('acciono', 'editar');
}



function click_tocar_item(item: item_lista) {
    console.log("tocar item", item);
    emit('acciono', 'tocar_cancion', item);
}


function click_borrar_viendolista(item: item_lista) {
    admin_indiceslista.BorrarCancion("default", item);
    canciones_Actual.value = admin_indiceslista.GetIndice(reflista_actual.value)
    ctrlviendolista.value?.cancionesFiltradas();
}


function click_agregar_guardadas(item: item_lista) {
    canciones_Actual.value = admin_indiceslista.GetIndice(reflista_actual.value)
    canciones_Actual.value.push(item);
    admin_indiceslista.SaveIndice(reflista_actual.value, canciones_Actual.value);
    ctrlguardados.value?.cancionesFiltradas();
}


function click_borrar_guardadas(item: item_lista) {
    generadorlistasLS.BorrarCancion(item);
    console.log(ctrlguardados.value)
    ctrlguardados.value?.cancionesFiltradas();
    
}

</script>

<template>
    <div class="divListas">
        

    
        <div style="font-size: xx-large;">Reproduciendo</div>
    <ListadoTemas :ref="ctrlviendolista" titulo="" :indice="canciones_Actual" :muestra_renglones=10
    :nro_cancion="props.nro_cancion"
    :btnVer=true v-on:click_ver="click_editar_item" :btnDescargar=false :btnBorrar=true :btnAgregar=false
    @click_borrar="click_borrar_viendolista"
    @click_tocar="click_tocar_item"
    ></ListadoTemas>

    <div style="font-size: xx-large;">Guardadas</div>
    <ListadoTemas :ref="ctrlguardados" titulo="Guardadas" :indice="canciones_Storage" :muestra_renglones=10
    :btnVer=true v-on:click_ver="click_editar_item" :btnDescargar=false :btnAgregar=true :btnBorrar=true
    @click_agregar="click_agregar_guardadas" @click_borrar="click_borrar_guardadas"
    ></ListadoTemas>

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

.divListas {
    border: 1px solid ;
    padding: 15px;
    margin: 10px;
    border-radius: 8px;
}
</style>
