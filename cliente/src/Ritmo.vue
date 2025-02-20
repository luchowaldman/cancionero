<script setup lang="ts">
import { MidiPlayer} from './modelo/midiplayer';
import { Reproductor } from './modelo/reproductor';

import Nota from './modelo/Midi/nota';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import 'bootstrap-icons/font/bootstrap-icons.css';

const ref_instrumentocargado = ref(false)
const ref_viendoacorde = ref(0);
const ref_repetir = ref(true);
const ref_instrumento = ref("C1");
let midiplayer: MidiPlayer | null = null;
import { ref } from 'vue';
import { transpileModule } from 'typescript';


class ParteBateria {
  nota: string;
  nombre: string;
  constructor(nombre: string, nota: string) {
    this.nota = nota;
    this.nombre = nombre;
  }
}
const partes_bateria = [
  new ParteBateria("Bombo", "C1"),
  new ParteBateria("Caja", "E4"),
  new ParteBateria("Platillo", "B3"),
  new ParteBateria("Platillo cerrado", "C#3"),
  new ParteBateria("Platillo abierto", "D#3"),
  new ParteBateria("Matraca", "A#3"),
  new ParteBateria("Triangulo", "G#4"),
  new ParteBateria("Pito", "C5"),
  new ParteBateria("Pedal", "F6")
]

class Ritmo {
  partes: boolean[][];
  instrumento: string
  constructor(instrumento: string) {
    this.instrumento = instrumento;
    this.partes = [[true], [true], [true], [true]];
  }
}


function iniciar_midi() {
  console.log("iniciar_midi") 

fetch('data/notas_midi/bateria.json')
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

function agregar_instrumento() {
  ref_instrumentos.value.push(new Ritmo("C1"));
}


const ref_instrumentos = ref([new Ritmo("C1")]);
function cambia_ritmo(instrumento: number, index: number) {
  
  let ref_ritmos = ref_instrumentos.value[instrumento].partes[index];
  switch (ref_ritmos.length) {
    case 0:
      ref_ritmos = [true]
      break;
    case 1:
      ref_ritmos = [true, true]
      break;
    case 2:
      ref_ritmos = [true, true, true]
      break;
    case 3:
      ref_ritmos = [true, true, true, true]
      break;
    case 4:
      ref_ritmos = []
      break;
  }
  ref_instrumentos.value[instrumento].partes[index] = ref_ritmos;
}

function cambia_estado(instrumento: number, index: number, tocaindex: number) {
  ref_instrumentos.value[instrumento].partes[index][tocaindex] = !ref_instrumentos.value[instrumento].partes[index][tocaindex];
}
function tocar_instrumento(numero_instrumento: number) {
  midiplayer?.play(ref_instrumentos.value[numero_instrumento].instrumento, 1, 0);
}
const bpm = ref(100);

let reproductor = new Reproductor(200, 200000);

reproductor.setIniciaCicloHandler((newCompas: number) => {  
    if (ref_repetir.value) {
      tocar();
    }
});
function tocar() 
{
    const duracion_negra = 60 / bpm.value;
    for (let index_instrumento = 0; index_instrumento < ref_instrumentos.value.length; index_instrumento++) 
    {
      let delay = 0;
      const ref_ritmos = ref_instrumentos.value[index_instrumento].partes;
      for (let index = 0; index < ref_ritmos.length; index++) 
      {
        if (ref_ritmos[index].length > 0) 
        {
          for (let tocaindex = 0; tocaindex < ref_ritmos[index].length; tocaindex++) 
          {
            if (ref_ritmos[index][tocaindex]) 
            {
              
              const duracion = duracion_negra / ref_ritmos[index].length;
              midiplayer?.play(ref_instrumentos.value[index_instrumento].instrumento, duracion, delay + (duracion * tocaindex));
            }
          }
        }
        delay += duracion_negra;
      }
    }
    reproductor.setDuracion(duracion_negra * 1000 * ref_instrumentos.value[0].partes.length);
    //reproductor.iniciar();

}

function iniciar_reproduccion() {
  reproductor.iniciar();
  tocar();
}
</script>

<template>
    <div class="contMusica">
<div class="cabRitmo">
  <button @click="iniciar_midi">Iniciar</button>
  <button @click="iniciar_reproduccion" v-if="ref_instrumentocargado">Tocar</button>
  <button @click="agregar_instrumento">Agregar instrumento</button>

  BPM: <input type="range" style="background-color: #a9a8f6; color: white;"  v-model="bpm" min="30" max="240" /> {{ bpm }}  
  Repetir: <input type="checkbox" v-model="ref_repetir" />
</div>



<div v-for="(instrumento, index_instrumento) in ref_instrumentos" :key="index_instrumento">

      <div class="seqRitmo"> 
        <div>
<select v-model="instrumento.instrumento">
  <option v-for="parte in partes_bateria" :key="parte.nota" :value="parte.nota">{{ parte.nombre }}</option>
</select>
<div @click="tocar_instrumento(index_instrumento)">TOCAR</div>
        </div>
        <div class="clsParteCompas" v-for="(ritmo, index) in instrumento.partes" :key="index" >
          <div @click="cambia_ritmo(index_instrumento, index)"> &bigstar; </div>
          <div class="claDivParteCompas" v-if="ritmo.length == 0">Sh</div>
          
            <div class="claDivParteCompas" v-for="(toca, tocaindex) in ritmo" @click="cambia_estado(index_instrumento, index, tocaindex)" :key="tocaindex">
              <div v-if="toca">X</div>
              <div v-else>O</div>
          
          

        </div></div>
      </div>

    </div>


    </div>
    

</template>

<style scoped>
.claDivParteCompas {
  width: 20px;
  border: 1px solid;
  border-radius: 5px;
  margin: 3px;
  padding: 4px;

}

.contMusica {
  border: 1px solid;
  border-radius: 5px;
  margin: 10px;
  padding: 10px;
 }
.clsParteCompas {
  width: 200px;
  display: flex;
  border: 1px solid;
  border-radius: 5px;
  margin: 3px;
  padding: 10px;
}
 .seqRitmo {
  display: flex;
 }
</style>
