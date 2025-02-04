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
import { Musica } from '../modelo/musica';



const emit = defineEmits(['acciono']);
const musica = new Musica()
const BandasFavoritasref = ref([] as string[]);
const bandas_seleccionadas = ref("" as string);
const filtros_seleccionados = ref("" as string);
const bandasFavoritasKey = 'bandas_favoritas';
const bandasFavoritasSeleccionadaKey = 'bandas_favoritas_seleccionadas';
const filtrosSeleccionadaKey = 'filtros_seleccionadas';
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

function selecciono_filtro(filtro: string) {
    if (filtros_seleccionados.value.includes('|' + filtro)) {
        filtros_seleccionados.value = filtros_seleccionados.value.replace('|' + filtro, '').trim();
    } else {
        filtros_seleccionados.value += `|${filtro}`.trim();
    }
    localStorage.setItem(filtrosSeleccionadaKey, filtros_seleccionados.value);
    buscar_cancion();
    ctrlListaURL.value?.cancionesFiltradas();
}
function borrar_filtros() {
    bandas_seleccionadas.value = "";
    filtros_seleccionados.value = "";
    localStorage.setItem(bandasFavoritasSeleccionadaKey, bandas_seleccionadas.value);
    localStorage.setItem(filtrosSeleccionadaKey, filtros_seleccionados.value);
    buscar_cancion();
}
function buscar_cancion() {
    let filtro_canciones = bandas_seleccionadas.value.split('|').filter((banda) => banda.length > 0);
    let filtros = filtros_seleccionados.value.split('|').filter((filtro) => filtro.length > 0);
    if (filtro_canciones.length == 0 &&  filtros.length == 0) {
        canciones_filtradas.value = canciones_url.value;
        return;
    }

    let nuevas_canciones = [] as item_lista[];
    if (filtro_canciones.length > 0) 
    {
        console.log("filtro_canciones", filtro_canciones);
        nuevas_canciones = canciones_url.value.filter((item) => {
            return filtro_canciones.some((banda) => item.banda.toLowerCase().includes(banda));
        });
    }
    else {
        nuevas_canciones = canciones_url.value;
    }

    if (filtros.length > 0) {
        
        const filtros_x_acordes = ['4acordes', '6acordes', '+Acordes'];
        if (filtros.some(filtro => filtros_x_acordes.includes(filtro))) {
         
        nuevas_canciones = nuevas_canciones.filter((item) => {
            return filtros.some((filtro) => {
                if (filtro == '4acordes') {
                    return item.acordes.split('.').length == 4;
                }
                if (filtro == '6acordes') {
                    return item.acordes.split('.').length == 6;
                }
                if (filtro == '+Acordes') {
                    return item.acordes.split('.').length > 6;
                }
                return false;
            });
        });
   
        }

        const filtros_x_modo = ['mayores', 'menores'];
        if (filtros.some(filtro => filtros_x_modo.includes(filtro))) {
        const notas = musica.notas;
        nuevas_canciones = nuevas_canciones.filter((item) => {
            return filtros.some((filtro) => {
                    
                if (filtro == 'mayores') {
                    return notas.includes(item.escala);
                }
                if (filtro == 'menores') {
                    let esMenor = item.escala;
                    if (!esMenor.includes('m')) 
                    {
                        return false;
                    }
                    esMenor = esMenor.replace('m', '');
                    return notas.includes(esMenor);
                    
                }
                return false;
            });
        });
   
        }


/*
if (filtro == 'mayores') {
                return musica.notas.includes(item.escala);
            }
            if (filtro == 'menores') {
                let esMenor = item.escala;
                if (!esMenor.includes('m')) {
                    return false;
                }
                return musica.notas.includes(item.escala);
                
            }
*/ 



    }
    canciones_filtradas.value = nuevas_canciones;
    
}

function loadBandasFavoritas() {
    const storedBandas = localStorage.getItem(bandasFavoritasKey);
    
    if (storedBandas) {
        BandasFavoritasref.value = JSON.parse(storedBandas);
        const storedSeleccionados = localStorage.getItem(bandasFavoritasSeleccionadaKey);
        console.log("storedSeleccionados", storedSeleccionados);
        if (storedSeleccionados) {
            bandas_seleccionadas.value = storedSeleccionados;
            filtros_seleccionados.value = localStorage.getItem(filtrosSeleccionadaKey) || "";
            console.log("filtros_seleccionados", filtros_seleccionados.value);
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



let canciones_url = ref([] as item_lista[]);
let canciones_filtradas = ref([] as item_lista[]);
// INICIALIZA LAS LISTAS DE CANCIONES GENERADAS
const generadorlistasURL = new AdminListasURL('/data/canciones');
const almacen = new Almacenado();
const generadorlistasLS = new AdminListasLocalStorage(almacen);

const listas = ref([] as string[]);
listas.value = generadorlistasLS.listas();
const admin_indiceslista = new AdminListasTocables();



generadorlistasURL.getIndice().then((indice: item_lista[]) => {
    canciones_url.value = indice;
    buscar_cancion();

});

function click_descargar_URL(item: item_lista) {
    generadorlistasURL.GetCancion(item).then((canciondesc: Cancion) => {
        generadorlistasLS.GuardarCancion(item, canciondesc);
    });
}




function click_editar_URL(item: item_lista) {
    localStorage.setItem("editando_cancion", JSON.stringify(item));
    emit('acciono', 'editar');
    
}

function click_tocar(item: item_lista) {
    let indice = admin_indiceslista.GetIndice("default");
    indice.push(item);
    admin_indiceslista.SaveIndice("default", indice);
    
    emit('acciono', 'tocar_cancion', indice.length);
    emit('acciono', 'tocar');
}

function click_agregar_listadefault(item: item_lista) {
    let indice = admin_indiceslista.GetIndice("default");
    indice.push(item);
    admin_indiceslista.SaveIndice("default", indice);
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
            <div class="banda">
                <input type="text" v-model="banda_nombre_agregar" :style="{ width: banda_nombre_agregar.length + 3 + 'ch' }" />
                <button @click="agregarBanda()">Agregar</button>
                <button @click="borrar_filtros()">Borrar Filtros</button>
            </div>
        </div>
        
        <div class="bandas">
            <div class="titulobandas">FILTROS</div>
            <div @click="selecciono_filtro('4acordes')"
            class="banda"
            :class="{ banda_seleccionada: filtros_seleccionados.includes('4acordes') }">
                    <span>De 4 Acordes</span>
            </div>
            <div @click="selecciono_filtro('6acordes')"
            class="banda"
            :class="{ banda_seleccionada: filtros_seleccionados.includes('6acordes') }">
                    <span>A 6 Acordes</span>
            </div><div @click="selecciono_filtro('+Acordes')"
            class="banda"
            :class="{ banda_seleccionada: filtros_seleccionados.includes('+Acordes') }">
                    <span>+ Acordes</span>
            </div> -- 

            <div @click="selecciono_filtro('mayores')"
            class="banda"
            :class="{ banda_seleccionada: filtros_seleccionados.includes('mayores') }">
                    <span>Mayores</span>
            </div><div @click="selecciono_filtro('menores')"
            class="banda"
            :class="{ banda_seleccionada: filtros_seleccionados.includes('menores') }">
                    <span>Menores</span>
            </div> 

        </div>
        <div >
    

    <ListadoTemas titulo="En data generada por Luis Waldman" :indice="canciones_filtradas" :muestra_renglones=15
    :btnVer=true v-on:click_ver="click_editar_URL" 
    @click_tocar="click_tocar"
    @click_agregar="click_agregar_listadefault"
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
    background-color: rgb(206, 145, 4);
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
