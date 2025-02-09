<script setup lang="ts">
import { MidiPlayer} from './modelo/midiplayer';
import Pianocontrol from './components/pianocontrol.vue';
const ref_instrumentocargado = ref(false)
let midiplayer: MidiPlayer | null = null;
let archivos_instrumentos = ['acordion', 'bateria', 'guitarra', 'guitarraelectrica', 'harmonica', 'piano', 'trompeta']
let nombres_instrumentos = ['acordion', 'bateria', 'guitarra', 'guitarra electrica', 'harmonica', 'piano', 'trompeta']


import { ref } from 'vue';
import Nota from './modelo/Midi/nota';

const numeros: number[] = Array.from({ length: 53 }, (_, i) => i);
const notas: number[] = [1, 2, 4, 8, 16, 32];
const musicaref = ref([] as Nota[][])
const drageandoref = ref(false);

let prim_notas = [] as Nota[];
prim_notas.push(new Nota(22, 1));

musicaref.value = [prim_notas];

function clase(numero: number) {
  if (numero < 10 || numero > 34) {
    return "noseve";
  }

  if (numero % 2 == 0) {
    return "espacio";
  } else 
  {
    if (numero > 20 && numero < 24) {
    return "noseve";
  }

    return "linea";
  }
}

function duracionnota(acordes: Nota[], numero: number) {
  for (let i = 0; i < acordes.length; i++) {
    if (acordes[i].nota == numero) {
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
    musicaref.value.push([new Nota(numero, drageando_duracion.value)]);
  }
  else {
   
    let acorde = musicaref.value[acordeid];
    const notaExistente = acorde.find(nota => nota.nota === numero);
    if (notaExistente) {
      notaExistente.duracion = drageando_duracion.value;
    } else {
      acorde.push(new Nota(numero, drageando_duracion.value));
    } 
  }
  pordrop_acorde.value = -1;
  pordrop_nronota.value = -1;
}
const drageando_duracion = ref(0);
function dragstart(nota: number) {
  drageandoref.value = true;
  drageando_duracion.value = nota;
  console.log("Dragstart", nota);
}

function dragend() {
  drageandoref.value = false;
  drageando_duracion.value = 0;

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
      
      midiplayer?.tocarNota(nota);
    }

    function soltar_nota(nota: string) {
     
     midiplayer?.soltarNota(nota);
   }

    function nombre_nota(numero: number) 
    {

      const toan = numero % 7;
      let modif = "";
      let escala = Math.floor(numero / 7);
      console.log("nombre_nota", numero, toan, escala);
      switch (toan) {
        case 1: return "C" + modif + escala;
        case 2: return "D" + modif + escala;
        case 3: return "E" + modif + escala;
        case 4: return "F" + modif + escala;
        case 5: return "G" + modif + escala;
        case 6: return "A" + modif + escala;
        case 0: return "B" + modif + escala;

      }
    }

    function tocar() 
    {
      /*
      for (acor in musicaref.value) {
        for (nota in acor) {
          midiplayer?.tocarNota(nota.nota);
        }
      }
    */
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
          const notanom = nombre_nota(nota.nota);
          console.log("Tocar", notanom, duracion, delay); 
          midiplayer?.play(notanom, duracion, delay);
        }
        delay += menor_del_acorde;
      }
      //midiplayer?.play("C4", 1, 0);
    }


</script>

<template>
    <div class="contMusica">

      <div class="cabecera">
        <div style="display: flex;"> 
          <div style="display: flex;">
            <div class="notaadd titnotas">Notas: </div> 
            <div class="notaadd" v-for="nota in notas" :key="nota" draggable="true"
            @dragstart="dragstart(nota)" @dragend="dragend()"> {{ nota }} </div>
          </div> 
          <div v-if="drageandoref"> 
            <div>Va a agregar</div>
            <div>{{  drageando_duracion }} - {{ pordrop_acorde }} - {{ pordrop_nronota }}</div>
          </div>

          <div>
            

            <button v-for="(nombre, id) in nombres_instrumentos" :key="id" @click="iniciar_midi(id)" > {{ nombre }}</button>
            
      <button @click="tocar()"  v-if="ref_instrumentocargado">TOCAR</button>


          </div>
        </div>


      </div>


      <div style="display: flex; width: 100%;" :class="{ 'drageando': drageandoref }">
            <div v-for="(acordes, acordeid) in musicaref" :key="acordeid">
              <div class="parte_pentagrama">
                <div v-for="numero in numeros" :key="numero" class="linea_pentagrama" :class="[clase(numero), { 'lineadrageando': pordrop_nronota == numero }]"  >
                    <div class="nota">
                      
                      <div v-if="!drageandoref">
                        <template v-if="duracionnota(acordes, numero) != -1">
                          <span>{{ duracionnota(acordes, numero) }}</span>
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

                <div v-for="numero in numeros" :key="numero" :class="[clase(numero), { 'lineadrageando': pordrop_nronota == numero }]">
                  <div class="nota">
                    <span @dragover="onDragOver($event, -1, numero)" 
                                  @drop="drop(-1, numero)"
                                  class="linea_pentagrama"
                                  :class="{'xDrag': pordrop_acorde == -1 && pordrop_nronota == numero }">N</span></div>
                  </div>
            </div>




    </div>
    <Pianocontrol @toco="tocar_nota" @solto="soltar_nota" v-if="ref_instrumentocargado"></Pianocontrol>

</div>
</template>

<style scoped>

.noseve {
  display: none;
}

.linea {
  border-bottom: 1px solid black;
  height: 6px;
}

.espacio {
  height: 6px;
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
</style>
