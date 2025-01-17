<script setup lang="ts">
import { ref, markRaw, onMounted } from 'vue';
import { Almacenado } from './modelo/Almacenado';
import { item_lista } from './modelo/item_lista';
import { Banda } from './modelo/banda';
import { Cancion } from './modelo/cancion';
import { Acordes, Parte } from './modelo/acordes';
import { Letra } from './modelo/letra';
import Menu from './components/menu.vue';
import ListadoTemas from './components/listadotemas.vue';
import { AdminListasURL } from './modelo/AdminListasURL';
import { AdminListasLocalStorage } from './modelo/AdminListasStorage';
import { AdminListasTocables } from './modelo/AdminListasTocables';
import { it } from 'node:test';


const almacen = new Almacenado();

// INICIALIZA LAS LISTAS DE CANCIONES GENERADAS
const generadorlistasURL = new AdminListasURL('/data');
const generadorlistasLS = new AdminListasLocalStorage(almacen);
const generadorlistasTocables = new AdminListasTocables(almacen);
const canciones_listaURL = ref([] as item_lista[]);
const canciones_Storage = ref([] as item_lista[]);
const canciones_tocables = ref([] as item_lista[]);

generadorlistasURL.getIndice().then((indi_get: item_lista[]) => {
    canciones_listaURL.value = indi_get;
});

generadorlistasLS.getIndice().then((indi_get: item_lista[]) => {
    canciones_Storage.value = indi_get;
});

generadorlistasTocables.getIndice().then((indi_get: item_lista[]) => {
    console.log("Tocables", indi_get);
    canciones_tocables.value = indi_get;
});

function click_descargar_URL(item: item_lista) {
    generadorlistasURL.GetCancion(item).then((cancion: Cancion) => {
        generadorlistasLS.GuardarCancion(item, cancion);
        
    });
}


function click_agregar_almacenada(item: item_lista) {
    console.log("almacenar",item);
    generadorlistasTocables.GuardarCancion(item);
}


function click_editar_almacenada(item: item_lista) {
    console.log("editar",item);
    editarCancion(item.cancion, item.banda, 'almacenada');
}

function click_editar_URL(item: item_lista) {
    console.log("editar",item);
    editarCancion(item.cancion, item.banda, 'URL');
}

function editarCancion(cancion: string, banda: string, origen: string) {
    console.log("Editar canción", cancion, banda);
    localStorage.setItem("origen", origen);
    localStorage.setItem("editar_cancion", cancion);
    localStorage.setItem("editar_banda", banda);
    window.location.href = '/edit';
}

/*
getIndice().then((indice) => {
    indice_disponible.value = indice;
    cancionesFiltradas() 
});
*/




</script>

<template>
    <div>
        
  <Menu titulo="Listas" viendo_vista="listas"></Menu>
        
  <ListadoTemas titulo="En la lista de reproduccion"  
  
  :muestra_renglones=10
  @click_editar="click_editar_almacenada"
  :indice="canciones_tocables"></ListadoTemas>
  <ListadoTemas titulo="Almacenadas"
  :muestra_renglones=10
  @click_agregar="click_agregar_almacenada"
    :indice="canciones_Storage"
    @click_editar="click_editar_almacenada"
    ></ListadoTemas>
  <ListadoTemas titulo="En data generada por Luis Waldman" 
        :muestra_renglones=10
        @click_editar="click_editar_URL"  
        @click_descargar="click_descargar_URL" :indice="canciones_listaURL"></ListadoTemas>
  
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
