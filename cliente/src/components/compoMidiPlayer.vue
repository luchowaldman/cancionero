<script setup lang="ts">
import { ref } from 'vue';
import { MidiPlayer} from '../modelo/midiplayer';
import Pianocontrol from './pianocontrol.vue';

const ref_instrumentocargado = ref(false)
let midiplayer: MidiPlayer | null = null;
let archivos_instrumentos = ['acordion', 'bateria', 'guitarra', 'guitarraelectrica', 'harmonica', 'piano', 'trompeta']
let nombres_instrumentos = ['acordion', 'bateria', 'guitarra', 'guitarra electrica', 'harmonica', 'piano', 'trompeta']

function iniciar_midi(id_instrumeto: number) {
  console.log("iniciar_midi") 

fetch('data/notas_midi/' + archivos_instrumentos[id_instrumeto]  +'.json')
  .then(response => response.json())
  .then(samples => {
    midiplayer = new MidiPlayer(samples);
    midiplayer.initialize();

    ref_instrumentocargado.value = true;
    // Puedes establecer el handler aquí si lo necesitas:
    midiplayer.setConectadoHandler((resultado: string) => {
      console.log(resultado);
    });

    // Ejemplo para tocar una nota:
    
  })
  .catch(error => {
    console.error("Error loading samples:", error);
  });
    }

    function tocar_nota(nota: string) {
      
      midiplayer?.tocarNota(nota);
    }

    function soltar_nota(nota: string) {
     
      midiplayer?.soltarNota(nota);
    }

</script>
<template>
    <div>
      <div class="row">
        <div class="col-4">
          <button v-for="(nombre, id) in nombres_instrumentos" :key="id" @click="iniciar_midi(id)" > {{ nombre }}</button>
          
        </div>

      </div>
      <Pianocontrol @toco="tocar_nota" @solto="soltar_nota" v-if="ref_instrumentocargado"></Pianocontrol>

</div>
</template>

<style scoped>



</style>
