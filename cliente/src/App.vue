<script setup lang="ts">
import { ref, markRaw, onMounted } from 'vue';
import { Cancion } from './modelo/cancion';
import { Contexto } from './modelo/contexto';
import { Reproductor } from './modelo/reproductor';

import ComponenteMusicalAcordes from './components/ComponenteMusicalAcordes.vue';
import ComponenteMusicalAcordesSeguidos from './components/ComponenteMusicalAcordesSeguidos.vue';
import ComponenteMusicalLetra from './components/ComponenteMusicalLetra.vue';
import ComponenteMusical from './components/ComponenteMusical.vue';
import ComponenteMusicalPartitura from './components/ComponenteMusicalPartitura.vue';
import ComponenteMusicalMetronomo from './components/ComponenteMusicalMetronomo.vue';
import ControladorTiempo from './components/ControladorTiempo.vue';
import { Acordes, Parte } from './modelo/acordes';
import { Letra } from './modelo/letra';
import { Almacenado } from './modelo/Almacenado';

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
const almacen = new Almacenado();

/*
const canciones = ['esta saliendo el sol', 'fuiste lo mejor','casi sin pensar', 'fuego', 'necesito', 'no tengo ganas', 'pila pila', 'volver a casa']
for (const tema of canciones) {
    getCancion('Intoxicados', tema).then((cancionret) => {
        console.log("Canción obtenida", cancionret);
        almacen.agregarCancion(cancionret);
    });
}
    */


    let canciones_sesion = [];
    const canciones = ['esta saliendo el sol', 'fuiste lo mejor','casi sin pensar', 'fuego', 'necesito', 'no tengo ganas', 'pila pila', 'volver a casa']
    for (const tema of canciones) {
        canciones_sesion.push(almacen.obtenerCancion(tema, 'intoxicados'));
    }


const nro_cancion = ref(0);
cancion.value = canciones_sesion[nro_cancion.value];



let vista = ref({
   cargando_cancion: false
});
let contexto = new Contexto("Lista", 10);
const compas = ref(-1);
let reproductor = new Reproductor(2200, 70);

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
    markRaw(ComponenteMusicalAcordes),
    markRaw(ComponenteMusicalLetra),
    markRaw(ComponenteMusicalAcordesSeguidos)
    
    //markRaw()
    //
    //markRaw(ComponenteMusicalLetra),
    //markRaw(ComponenteMusicalMetronomo),
    //markRaw(ComponenteMusical),
    //markRaw(ComponenteMusical),
    
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
    nro_cancion.value = (nro_cancion.value + 1) % canciones_sesion.length;
    cancion.value = canciones_sesion[nro_cancion.value];
}

function onPrevious() {
    console.log("Previous event received");
    nro_cancion.value = (nro_cancion.value - 1 + canciones_sesion.length) % canciones_sesion.length;
    cancion.value = canciones_sesion[nro_cancion.value];
}

function onUpdateCompas(newCompas: number) {
    compas.value = parseInt(newCompas)
    console.log(`Esto se actualiza: ${newCompas}`);
}

    // Llamar a la función iniciarCompasEnComponentes cuando sea necesario 
    onMounted(() => { 
        console.log("APP MONTADA")
    });

</script>

<template>
    <div>
<div id="barra_navegacion">
  <div>Cancionero</div>
  <div id="barra_control">
      <div>{{ cancion.cancion }} </div>
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
