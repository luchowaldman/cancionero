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
import { AdminListasTocables } from '../modelo/AdminIndiceListas';





const props = defineProps<{ lista_actual: string }>();



const BandasFavoritasref = ref([] as string[]);
const bandas_seleccionadas = ref("" as string);
const bandasFavoritasKey = 'bandas_favoritas';
const bandasFavoritasSeleccionadaKey = 'bandas_favoritas_seleccionadas';
const ctrlListaURL = ref();
const defaultBandas = ['viejas-locas', 'intoxicados', 'sabina', 'beatles'];

function selecciono_banda(banda: string) {
    if (bandas_seleccionadas.value.includes('|' +banda)) {
        bandas_seleccionadas.value = bandas_seleccionadas.value.replace('|' + banda, '').trim();
    } else {
        bandas_seleccionadas.value += `|${banda}`.trim();
    }
    console.log("bandas_seleccionadas", bandas_seleccionadas.value);
    buscar_cancion();
    localStorage.setItem(bandasFavoritasSeleccionadaKey, bandas_seleccionadas.value);
    ctrlListaURL.value?.cancionesFiltradas();

}


function buscar_cancion() {
    let filtro_canciones = bandas_seleccionadas.value.split('|').filter((banda) => banda.length > 0);
    console.log("filtro_canciones", filtro_canciones);
    if (filtro_canciones.length == 0) {
        canciones_filtradas.value = canciones_url.value;
        return;
    }
    canciones_filtradas.value = canciones_url.value.filter((item) => {
        return filtro_canciones.some((banda) => item.banda.toLowerCase().includes(banda));
    });
}

function loadBandasFavoritas() {
    const storedBandas = localStorage.getItem(bandasFavoritasKey);
    
    if (storedBandas) {
        BandasFavoritasref.value = JSON.parse(storedBandas);
        const storedSeleccionados = localStorage.getItem(bandasFavoritasSeleccionadaKey);
        console.log("storedSeleccionados", storedSeleccionados);
        if (storedSeleccionados) {
            bandas_seleccionadas.value = storedSeleccionados;
        }
        
    } else {
        BandasFavoritasref.value = defaultBandas;
        bandas_seleccionadas.value = "";
    }
}
const banda_nombre_agregar = ref('');
function agregarBanda() {
    if (!BandasFavoritasref.value.includes(banda_nombre_agregar.value)) {
        BandasFavoritasref.value.push(banda_nombre_agregar.value);
        localStorage.setItem(bandasFavoritasKey, JSON.stringify(BandasFavoritasref.value));
    }
}

function quitarBandaPorIndice(indice: number) {
    if (indice >= 0 && indice < BandasFavoritasref.value.length) {
        BandasFavoritasref.value.splice(indice, 1);
        localStorage.setItem(bandasFavoritasKey, JSON.stringify(BandasFavoritasref.value));
    }
}

loadBandasFavoritas();



const ctrlguardados = ref();
const ctrlviendolista = ref();
const editando_cancion = ref(false);
const cancion_ver  = ref(new Cancion("no song name", "no band name", new Acordes([], []), new Letra([])));
const itemindice_ref = ref(new item_lista("no song name", "no band name"));

const reflista_actual = ref(props.lista_actual);
const canciones_Storage = ref([] as item_lista[]);
const canciones_Actual = ref([] as item_lista[]);
let canciones_url = ref([] as item_lista[]);
let canciones_filtradas = ref([] as item_lista[]);
// INICIALIZA LAS LISTAS DE CANCIONES GENERADAS
const generadorlistasURL = new AdminListasURL('/data/canciones');
const almacen = new Almacenado();
const generadorlistasLS = new AdminListasLocalStorage(almacen);

const listas = ref([] as string[]);
listas.value = generadorlistasLS.listas();
const admin_indiceslista = new AdminListasTocables();

canciones_Actual.value = admin_indiceslista.GetIndice(reflista_actual.value);
ctrlviendolista.value?.cancionesFiltradas();


generadorlistasURL.getIndice().then((indice: item_lista[]) => {
    canciones_url.value = indice;
    buscar_cancion();

});

function click_descargar_URL(item: item_lista) {
    generadorlistasURL.GetCancion(item).then((canciondesc: Cancion) => {
        generadorlistasLS.GuardarCancion(item, canciondesc);
        ctrlguardados.value?.cancionesFiltradas();
        
    });
}


generadorlistasLS.getIndice().then((indi_get: item_lista[]) => {
    canciones_Storage.value = indi_get;
});


function click_editar_URL(item: item_lista) {
    localStorage.setItem("editando", "si");
    localStorage.setItem("editando_cancion", JSON.stringify(item));
    
    GetCanciones.obtenerCancion(item).then((cancion_get: Cancion) => {
        itemindice_ref.value = item;
        editando_cancion.value = true;
        cancion_ver.value = cancion_get;
        //editref.value?.reload_song();   
    });
}


function click_agregar_guardadas(item: item_lista) {
    canciones_Actual.value = admin_indiceslista.GetIndice(reflista_actual.value)
    canciones_Actual.value.push(item);
    admin_indiceslista.SaveIndice(reflista_actual.value, canciones_Actual.value);
    ctrlguardados.value?.cancionesFiltradas();
}


</script>

<template>
    <div class="divListas">
        <div class="bandas">
            <div class="titulobandas">BANDAS</div>
            <div v-for="(banda, index) in BandasFavoritasref" class="banda"  :key="index" @click="selecciono_banda(banda)"
            :class="{ banda_seleccionada: bandas_seleccionadas.includes(banda) }" 
            >
                
                    <span>{{ banda }}</span>
                    <button @click="quitarBandaPorIndice(index)">x</button>
                
            </div>
            <div class="bandas">
                <input type="text" v-model="banda_nombre_agregar" :style="{ width: banda_nombre_agregar.length + 3 + 'ch' }" />
                <button @click="agregarBanda()">Agregar</button>
            </div>
        </div>
        <div >
    

    <ListadoTemas titulo="En data generada por Luis Waldman" :indice="canciones_filtradas" :muestra_renglones=15
    :btnVer=true v-on:click_ver="click_editar_URL" 
    @click_agregar="click_agregar_guardadas"
    @click_descargar="click_descargar_URL"
    :filtro_banda="bandas_seleccionadas"
    ref="ctrlListaURL"

    :btnDescargar=true :btnAgregar=true :btnBorrar=false
    ></ListadoTemas>
  
</div>
</div>

</template>

<style scoped>
.bandas {
    display: flex;
    font-size: 40px;
    margin: 3px;
}
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

.banda_seleccionada {
    background-color: rgb(219, 169, 42);
    color: white;
}
.divListas {
    border: 1px solid ;
    padding: 15px;
    margin: 10px;
    border-radius: 8px;
}
.titulobandas {
    padding: 5px;
    margin: 5px;
    border-radius: 8px;
}
.banda {
    border: 1px solid   ;
    padding: 5px;
    margin: 5px;
    border-radius: 8px;
}
</style>
