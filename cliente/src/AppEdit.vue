<script setup lang="ts">
import { ref, markRaw, onMounted } from 'vue';
import { Cancion } from './modelo/cancion';
import { Contexto } from './modelo/contexto';
import { Reproductor } from './modelo/reproductor';

import Menu from './components/menu.vue';

import ComponenteMusicalAcordesEdit from './components/ComponenteMusicalAcordesEdit.vue';
import ComponenteMusicalAcordes from './components/ComponenteMusicalAcordes.vue';
import ComponenteMusicalAcordesSeguidos from './components/ComponenteMusicalAcordesSeguidos.vue';
import ComponenteMusicalLetra from './components/ComponenteMusicalLetra.vue';
import ComponenteMusical from './components/ComponenteMusical.vue';
import ComponenteMusicalPartitura from './components/ComponenteMusicalPartitura.vue';
import ComponenteMusicalMetronomo from './components/ComponenteMusicalMetronomo.vue';
import ControladorTiempo from './components/ControladorTiempo.vue';
import { Acordes, Parte } from './modelo/acordes';
import { Letra } from './modelo/letra';

import { AdminListasLocalStorage } from './modelo/AdminListasStorage';
import { AdminListasTocables } from './modelo/AdminListasTocables';
import { AdminListasURL } from './modelo/AdminListasURL';
import { Almacenado } from './modelo/Almacenado';



const almacen = new Almacenado();

// INICIALIZA LAS LISTAS DE CANCIONES GENERADAS
const generadorlistasURL = new AdminListasURL('/data');
const generadorlistasLS = new AdminListasLocalStorage(almacen);
const generadorlistasTocables = new AdminListasTocables(almacen);
// Definir la canción y el contexto

const cancion  = ref(new Cancion("", "", new Acordes([], []), new Letra([])));
const mostrando_compas_parte = ref(-1)

const banda = localStorage.getItem("editar_banda") || 'intoxicados';
const tema = localStorage.getItem("editar_cancion") || 'esta-saliendo-el-sol';
console.log("Banda", banda);
console.log("Tema", tema);
generadorlistasURL.GetCancionxTema(banda, tema).then((cancion_obtenida) => {
    cancion.value = cancion_obtenida;
    console.log("Canción", cancion.value);
    return cancion;
});
console.log("Canción", cancion.value);



let vista = ref({
   cargando_cancion: false
});


let contexto = new Contexto("Lista", 10);
const compas = ref(-1);
const editando = ref(-1)
const mostrando_parte = ref(-1)
const currentCompas = ref(0);


let reproductor = new Reproductor(2200, 50);

reproductor.setIniciaHandler(() => {
    console.log("Iniciando reproductor");
});

reproductor.setIniciaCompasHandler((newCompas: number) => {
    console.log("Tocando compas", newCompas);
    compas.value = newCompas;
});

reproductor.setFinalizaHandler(() => {
    console.log("Deteniendo reproductor");
});



// Vector de componentes musicales
const componentesMusicales = ref([
    markRaw(ComponenteMusicalAcordesEdit),
    markRaw(ComponenteMusicalAcordesSeguidos)
]);


function onPause() {
    reproductor.pausar();
    console.log("Pause event received");
}

function onPlay() {
    reproductor.iniciar();
    console.log("Play event received");

}

function onStop() {
    reproductor.parar();
    console.log("Stop event received");
}

function onNext() {
    console.log("Next event received");
}

function onPrevious() {
    console.log("Previous event received");
}

function onUpdateCompas(newCompas: number) {
    compas.value = parseInt(newCompas)
    console.log(`Esto se actualiza: ${newCompas}`);
}

function guardarCancion() {
    almacen.agregarCancion(cancion.value);
}

    // Llamar a la función iniciarCompasEnComponentes cuando sea necesario 
    onMounted(() => { 
        console.log("APP MONTADA")
    });

</script>

<template>
    <div>
        <Menu :titulo="cancion.cancion"></Menu>
        <div>
    <ControladorTiempo :compas=compas :cancion="cancion" :contexto="contexto"
    @play="onPlay" @pause="onPause" @stop="onStop" @next="onNext" @previous="onPrevious" @update-compas="onUpdateCompas">

    </ControladorTiempo>
</div>

  
<div id="vistas">
</div>


<div id="contenedor-musical">
    <div v-for="(Componente, index) in componentesMusicales" :key="index">
        <component :is="Componente" :compas="compas" :cancion="cancion" :contexto="contexto"></component>
    </div>
</div>


    
  <div class="componente_acordes">
  
  <div v-for="(parte, index_parte) in cancion.acordes.partes" :key="parte.nombre" >
      <div>
        <h3>{{ parte.nombre }}</h3>
        <input type="text" v-model="parte.nombre" />
      </div>
      <div class="parte">
        <div v-for="(acorde, index) in parte.acordes" class="acorde" :key="acorde">
          <span  :class="{ compas_actual: ((  mostrando_compas_parte === index ) &&
                                           ( index_parte  === cancion.acordes.orden_partes[mostrando_parte]  ))
           }">{{ acorde }}</span>
        </div>
      </div>
  </div>
<h3>Partes</h3>
      <div class="parte">
        <div v-for="(parte, index) in cancion.acordes.orden_partes" :key="index" class="ordenparte">
          <span :class="{ compas_actual: mostrando_parte === index }" >{{ cancion.acordes.partes[parte].nombre }}</span>
        </div>
        
      </div>
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
