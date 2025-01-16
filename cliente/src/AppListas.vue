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


const almacen = new Almacenado();

// INICIALIZA LAS LISTAS DE CANCIONES GENERADAS
const generadorlistas = new AdminListasURL('/data');
const generadorlistasLS = new AdminListasLocalStorage(almacen);
const generadorlistasTocables = new AdminListasTocables(almacen);
const canciones_listaURL = ref([] as item_lista[]);
const canciones_Storage = ref([] as item_lista[]);
const canciones_tocables = ref([] as item_lista[]);

generadorlistas.getIndice().then((indi_get: item_lista[]) => {
    canciones_listaURL.value = indi_get;
});

generadorlistasLS.getIndice().then((indi_get: item_lista[]) => {
    canciones_Storage.value = indi_get;
});



/*
getIndice().then((indice) => {
    indice_disponible.value = indice;
    cancionesFiltradas() 
});
*/




</script>

<template>
    <div>
        
  <Menu titulo="Listas"></Menu>
        
  <ListadoTemas titulo="En la lista de reproduccion" @click_descargar="click_descargar_URL()" :indice="canciones_tocables"></ListadoTemas>
  <ListadoTemas titulo="Almacenadas" :indice="canciones_listaURL"></ListadoTemas>
  <ListadoTemas titulo="En data generada por Luis Waldman" @click_descargar="click_descargar_URL()" :indice="canciones_Storage"></ListadoTemas>
  
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
