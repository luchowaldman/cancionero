<script setup lang="ts">
import { ref, markRaw, onMounted, watch } from 'vue';
import { Cancion } from './modelo/cancion';
import { Contexto } from './modelo/contexto';
import { Reproductor } from './modelo/reproductor';


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

// Definir la canción y el contexto

async function getCancion(banda: string, tema: string): Promise<Cancion> {
        const response = await fetch(`/public/data/${banda.replace(/\s+/g, '-')}_${tema.replace(/\s+/g, '-')}.json`);
        const data = await response.json();
        
        let partes = []
        for (let i = 0; i < data.acordes.partes.length; i++) {
            partes.push(new Parte(data.acordes.partes[i].nombre, data.acordes.partes[i].acordes));
        }

        
        const acordes = new Acordes(partes, data.acordes.orden_partes);
    
        return new Cancion(
            data.cancion,
            data.banda,
            acordes,
            new Letra(data.letras) 
        );
    }
    

const cancion  = ref(new Cancion("", "", new Acordes([], []), new Letra([])));
const mostrando_compas_parte = ref(-1)
import { Almacenado } from './modelo/Almacenado';
const almacen = new Almacenado();
cancion.value = almacen.obtenerCancion('fuego', 'intoxicados');



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
<div id="barra_navegacion">
  <div>Cancionero -EDIT </div>
  <div id="barra_control">
      <div>{{ cancion.cancion }} </div>
      <div><button v-on:click="guardarCancion()">GUARDAR</button></div>
  </div>
  <ControladorTiempo :compas=compas :cancion="cancion" :contexto="contexto"
  @play="onPlay" @pause="onPause" @stop="onStop" @next="onNext" @previous="onPrevious" @update-compas="onUpdateCompas">

  </ControladorTiempo>

  {{ compas }}
  <div style="margin-left: auto;">Configuración</div>
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
