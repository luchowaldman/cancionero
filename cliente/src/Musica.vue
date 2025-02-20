<script setup lang="ts">
import { MidiPlayer} from './modelo/midiplayer';
import Pianocontrol from './components/pianocontrol.vue';
import Pentagrama from './components/pentagrama.vue';

import Nota from './modelo/Midi/nota';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import 'bootstrap-icons/font/bootstrap-icons.css';

const ref_instrumentocargado = ref(false)
const ref_viendoacorde = ref(0);
let midiplayer: MidiPlayer | null = null;
let archivos_instrumentos = ['acordion', 'bateria', 'guitarra', 'guitarraelectrica', 'harmonica', 'piano', 'trompeta']
let nombres_instrumentos = ['acordion', 'bateria', 'guitarra', 'guitarra electrica', 'harmonica', 'piano', 'trompeta']

const notas: number[] = [1, 2, 4, 8, 16, 32];
const musicaref = ref([] as Nota[][])

import { ref } from 'vue';


function nombre_nota(numero: number) 
    {

      const rn = 51 - numero;
      const toan = rn % 7;
      let modif = "";
      let escala = Math.floor((rn - 1) / 7);
      switch (toan) {
        case 1: return "C" + modif + escala;
        case 2: return "D" + modif + escala;
        case 3: return "E" + modif + escala;
        case 4: return "F" + modif + escala;
        case 5: return "G" + modif + escala;
        case 6: return "A" + modif + escala;
        case 0: return "B" + modif + escala;

      }
      return "N/A";
    }



const numeros: number[] = Array.from({ length: 53 }, (_, i) => i);
let notas_pentagrama: string[] = [];
for (let i = 1; i < 53; i++) {
  notas_pentagrama.push(nombre_nota(i));
}
const drageandoref = ref(false);


musicaref.value = [[]];

function clase(numero: number) {
  if (numero < 10 || numero > 32) {
    return "noseve";
  }
  // DO CENTRAL
  if (numero == 22 || numero == 23) {
      return "espacio";
  }

  if (numero % 2 == 1 && numero < 20) {
    return "linea";
  } 
  if (numero % 2 == 0 && numero > 22) {
    return "linea";
  } 
  return "espacio";
}

function duracionnota(acordes: Nota[], numero: number) {
  const nota = nombre_nota(numero);
  for (let i = 0; i < acordes.length; i++) {
    if (acordes[i].nota == nota) {
      return acordes[i].duracion
    }
  }
  return -1;
}


const pordrop_acorde = ref(-1);
const pordrop_nronota = ref(-1);

function onDragOver(event: DragEvent, acordeid: number, numero: number) {
      event.preventDefault();
      pordrop_acorde.value = acordeid;
      pordrop_nronota.value = numero;      
      }

function drop(acordeid: number, numero: number) {
  console.log("Drop", acordeid, numero);
  if (acordeid == -1) {
    //musicaref.value[acordeid].push([new Nota(nombre_nota(numero), agregando_duracion.value)]);

  }
  else {
   
    let acorde = musicaref.value[acordeid];
    const notaExistente = acorde.find(nota => nota.nota === nombre_nota(numero));
    if (notaExistente) {
      notaExistente.duracion = agregando_duracion.value;
    } else {
      acorde.push(new Nota(nombre_nota(numero), agregando_duracion.value));
    } 
  }
  pordrop_acorde.value = -1;
  pordrop_nronota.value = -1;
}
const agregando_duracion = ref(4);
function click_duracion(duracion: number) {

  agregando_duracion.value = duracion;
}

function dragend() {
  drageandoref.value = false;
  agregando_duracion.value = 0;

}

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
      if (ref_instrumentocargado.value) {
        midiplayer?.tocarNota(nota);
      }
      // Agrego la nota
      if (ref_viendoacorde.value != -1) {
        let acorde = musicaref.value[ref_viendoacorde.value];

        const notaExistente = acorde.find(notaf => notaf.nota === nota);
        if (notaExistente) 
        {
            acorde.splice(acorde.indexOf(notaExistente), 1); 
        } else 
        {
          musicaref.value[ref_viendoacorde.value].push(new Nota(nota, agregando_duracion.value));
          ref_viendoacorde.value++;
          if (ref_viendoacorde.value >= musicaref.value.length) {
            musicaref.value.push([]);

        } 
      }
        }
      
    }

    function soltar_nota(nota: string) {
     
      if (ref_instrumentocargado.value) {
        midiplayer?.soltarNota(nota);
      }
   }

    function tocar() 
    {
      const bpm = 120;
      const duracion_blanca = 60 / bpm;
      let delay = 0;
      for (let i = 0; i < musicaref.value.length; i++) {
        const acorde = musicaref.value[i];
        let menor_del_acorde = 11111;
        for (let j = 0; j < acorde.length; j++) {
          const nota = acorde[j];
          const duracion = duracion_blanca / nota.duracion;
          if (duracion < menor_del_acorde) {
            menor_del_acorde = duracion;
          }
          const notanom = nota.nota;
          console.log("Tocar", notanom, duracion, delay); 
          midiplayer?.play(notanom, duracion, delay);
        }
        delay += menor_del_acorde;
      }
      //midiplayer?.play("C4", 1, 0);
    }


    function ver_acorde(acordeid: number) {
      ref_viendoacorde.value = acordeid;
    }


</script>

<template>
    <div class="contMusica">
      <Pentagrama></Pentagrama>
      

      <div class="cabecera">
        <div style="display: flex;"> 
          <div style="display: flex;">
            <div class="notaadd titnotas">Notas: </div> 
            <div class="notaadd" v-for="nota in notas" :key="nota" 
            @click="click_duracion(nota)" :class="{'seleccionada' : nota == agregando_duracion}"> {{ nota }} </div>
          </div> 
          <div v-if="drageandoref"> 
            <div>Va a agregar</div>
            <div>{{  agregando_duracion }} - {{ pordrop_acorde }} - {{ pordrop_nronota }}</div>
          </div>

          <div>
            

            <button v-for="(nombre, id) in nombres_instrumentos" :key="id" @click="iniciar_midi(id)" > {{ nombre }}</button>
            
      <button @click="tocar()"  v-if="ref_instrumentocargado">TOCAR</button>


          </div>
        </div>


      </div>


      <div style="display: flex; width: 100%;" :class="{ 'drageando': drageandoref }">
     


            <div v-for="(acordes, acordeid) in musicaref" :key="acordeid">
              <div class="parte_pentagrama" :class="{'acorde_viendo': ref_viendoacorde == acordeid} ">
                <div @click="ver_acorde(acordeid)">
                <i class="bi bi-eye"></i>
                </div>
                <div v-for="numero in numeros" :key="numero" class="linea_pentagrama" :class="[clase(numero), { 'lineadrageando': pordrop_nronota == numero }]"  >
                    <div class="nota">
                      
                      <div v-if="!drageandoref">
                        <template v-if="duracionnota(acordes, numero) != -1">
                          <span>{{ duracionnota(acordes, numero) }} - {{ nombre_nota(numero)  }}</span>
                        </template>
                        <template v-else>
                          <span>&nbsp;</span>
                        </template>
                      
                      </div>
                      <div v-if="drageandoref" @dragover="onDragOver($event, acordeid, numero)" 
                      @drop="drop(acordeid, numero)"
                      :class="{'xDrag': pordrop_acorde == acordeid && pordrop_nronota == numero }">
                      x
                    
                    </div>
                    </div>
                  </div>
              </div>
            </div>

              <!-- Pa Agregar-->
              <div class="parte_pentagrama"  v-if="drageandoref">
                <div>+</div>
                <div v-for="numero in numeros" :key="numero" :class="[clase(numero), { 'lineadrageando': pordrop_nronota == numero }]">
                  <div class="nota">
                    <span @dragover="onDragOver($event, -1, numero)" 
                                  @drop="drop(-1, numero)"
                                  class="linea_pentagrama"
                                  :class="{'xDrag': pordrop_acorde == -1 && pordrop_nronota == numero }">N</span></div>
                  </div>
            </div>




    </div>
    <Pianocontrol @toco="tocar_nota" @solto="soltar_nota" escala="C" acorde="C" :notas_seleccionadas="musicaref[ref_viendoacorde]" ></Pianocontrol>

</div>
</template>

<style scoped>

.noseve {
  display: none;
}

.linea {
  border-bottom: 1px solid;
  height: 16px;
}

.espacio {
  height: 16px;
}

.lineadrageando {
  background-color: yellow;
}
.xDrag {
  border-color: red ;
  border: 1px solid;

}

.notaadd {
  padding: 12px;
  font-size: xxx-large;
  border: 1px solid;
}

.acorde_viendo {
  border: 1px solid red;

}

.seleccionada {
  background-color: red;
  color: white;
}


</style>
