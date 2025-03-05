<script setup lang="ts">
import { ref } from 'vue';
import { Almacenado } from '../modelo/Almacenado';
import { item_lista } from '../modelo/item_lista';
import ListadoTemas from '../components/listadotemassimples.vue';
import { AdminListasURL } from '../modelo/AdminListasURL';
import { AdminListasLocalStorage } from '../modelo/AdminListasStorage';
import { AdminListasTocables } from '../modelo/AdminIndiceListas';


const props = defineProps<{ nro_cancion: number }>();

const emit = defineEmits(['acciono']);
const ctrlguardados = ref();
const ctrlviendolista = ref();
const editando_cancion = ref(false);

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



function click_tocar_item(nro: number) {
    console.log("tocar nro lista",  nro);
    emit('acciono', 'tocar_cancion', nro);
}





function click_borrar_viendolista(item: item_lista) {
    admin_indiceslista.BorrarCancion("default", item);
    canciones_Actual.value = admin_indiceslista.GetIndice("default");
    ctrlviendolista.value?.cancionesFiltradas();
}



function click_agregar_guardadas(item: item_lista) {
    
    let indice = admin_indiceslista.GetIndice("default");
    indice.push(item);
    canciones_Actual.value = indice;
    admin_indiceslista.SaveIndice("default", indice);
    ctrlviendolista.value?.cancionesFiltradas();

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
    :btnTocar="true"
    :btnVer=true v-on:click_ver="click_editar_item" :btnDescargar=false :btnBorrar=true :btnAgregar=false
    @click_borrar="click_borrar_viendolista"
    @click_tocar="click_tocar_item"
    
    ></ListadoTemas>

    <div style="font-size: xx-large;">Guardadas</div>

    <ListadoTemas :ref="ctrlguardados" titulo="Guardadas" :indice="canciones_Storage" :muestra_renglones=10
    :btnVer=true v-on:click_ver="click_editar_item" :btnDescargar=false :btnAgregar=true :btnBorrar=true
    :btnTocar=false
    @click_agregar="click_agregar_guardadas" @click_borrar="click_borrar_guardadas"    
    :nro_cancion="-1"
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
