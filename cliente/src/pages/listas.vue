<script setup lang="ts">
import { ref } from 'vue';
import { Almacenado } from '../modelo/Almacenado';
import { item_lista } from '../modelo/item_lista';
import { Cancion } from '../modelo/cancion';
import ListadoTemas from '../components/listadotemas.vue';
import ListadoListas from '../components/listadodelistas.vue';
import { Acordes } from '../modelo/acordes';
import { Letra } from '../modelo/letra';
import { AdminListasURL } from '../modelo/AdminListasURL';
import { AdminListasLocalStorage } from '../modelo/AdminListasStorage';
import { GetCanciones } from '../modelo/GetCanciones';
import { AdminListasTocables } from '../modelo/AdminIndiceListas';
import ComponenteMusicalEditar from '../components/ComponenteMusicalEditar.vue';
import { watch } from 'fs';

const props = defineProps<{ lista_actual: string }>();

const editref = ref();
const ctrlcancionesguardadas = ref();
const ctrlviendolista = ref();
const editando_cancion = ref(false);
const cancion_ver  = ref(new Cancion("no song name", "no band name", new Acordes([], []), new Letra([])));




const reflista_actual = ref(props.lista_actual);
const canciones_Storage = ref([] as item_lista[]);
const canciones_Actual = ref([] as item_lista[]);
let canciones_url = ref([] as item_lista[]);
// INICIALIZA LAS LISTAS DE CANCIONES GENERADAS
const generadorlistasURL = new AdminListasURL('/data');
const almacen = new Almacenado();
const generadorlistasLS = new AdminListasLocalStorage(almacen);

const listas = ref([] as string[]);
listas.value = generadorlistasLS.listas();
const admin_indiceslista = new AdminListasTocables();

canciones_Actual.value = admin_indiceslista.GetIndice(reflista_actual.value);
ctrlviendolista.value?.cancionesFiltradas();

generadorlistasURL.getIndice().then((indice: item_lista[]) => {
    canciones_url.value = indice;
});

function click_descargar_URL(item: item_lista) {
    generadorlistasURL.GetCancion(item).then((canciondesc: Cancion) => {
        generadorlistasLS.GuardarCancion(item, canciondesc);
        ctrlcancionesguardadas.value?.cancionesFiltradas();
        
    });
}

function click_cambiolista(new_lista: string) {
    reflista_actual.value = new_lista;  
    
    canciones_Actual.value = admin_indiceslista.GetIndice(new_lista);
    ctrlviendolista.value?.cancionesFiltradas();
    
}



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


function ev_agrego_lista(newlista: string) {
    reflista_actual.value = newlista;
    canciones_Actual.value = admin_indiceslista.GetIndice(reflista_actual.value)
    ctrlcancionesguardadas.value?.cancionesFiltradas();


}


function ev_ver_lista(newlista: string) {
    canciones_Actual.value = admin_indiceslista.GetIndice(newlista);
    ctrlviendolista.value?.cancionesFiltradas();
    
}

function cerro_editar() {
    editando_cancion.value = false;
}


function click_agregar_viendolista(item: item_lista) {
}

function click_borrar_viendolista(item: item_lista) {
    admin_indiceslista.BorrarCancion(reflista_actual.value, item);
    canciones_Actual.value = admin_indiceslista.GetIndice(reflista_actual.value)
    ctrlviendolista.value?.cancionesFiltradas();
}

function click_agregar_guardadas(item: item_lista) {
    canciones_Actual.value = admin_indiceslista.GetIndice(reflista_actual.value)
    canciones_Actual.value.push(item);
    admin_indiceslista.SaveIndice(reflista_actual.value, canciones_Actual.value);
    ctrlcancionesguardadas.value?.cancionesFiltradas();
}

function click_borrar_guardadas(item: item_lista) {
}
</script>

<template>
    <div>
       <div>
        <ComponenteMusicalEditar @cerrar="cerro_editar" :editando_cancion="editando_cancion" :compas="-1" :cancion="cancion_ver"  ref="editref"></ComponenteMusicalEditar>
    </div>
    <div v-if="!editando_cancion">
    
        <h1>{{  reflista_actual }}</h1>
    <ListadoTemas :ref="ctrlviendolista" titulo="" :indice="canciones_Actual" :muestra_renglones=10
    :btnVer=true v-on:click_ver="click_editar_URL" :btnDescargar=false :btnBorrar=true :btnAgregar=false
    @click_agregar="click_agregar_viendolista" @click_borrar="click_borrar_viendolista"
    ></ListadoTemas>


        <ListadoListas :listas="listas" @agrego_lista="ev_agrego_lista" @ver_lista="ev_ver_lista"></ListadoListas>
    <!-- 
const  = ref();
-->

    <ListadoTemas :ref="ctrlcancionesguardadas" titulo="Guardadas" :indice="canciones_Storage" :muestra_renglones=10
    :btnVer=true v-on:click_ver="click_editar_URL" :btnDescargar=false :btnAgregar=true :btnBorrar=true
    @click_agregar="click_agregar_guardadas" @click_borrar="click_borrar_guardadas"
    ></ListadoTemas>

    <ListadoTemas titulo="En data generada por Luis Waldman" :indice="canciones_url" :muestra_renglones=10
    :btnVer=true v-on:click_ver="click_editar_URL" 
    @click_descargar="click_descargar_URL"
    :btnDescargar=true :btnAgregar=false :btnBorrar=false
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
