<script setup lang="ts">
import { MidiPlayer} from './modelo/midiplayer';
import { Musica} from './modelo/musica';
import Pianocontrol from './components/pianocontrol.vue';
import Pentagrama from './components/pentagrama.vue';


import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import 'bootstrap-icons/font/bootstrap-icons.css';

const ref_instrumentocargado = ref(false)
const ref_viendoacorde = ref(0);
let midiplayer: MidiPlayer | null = null;
let archivos_instrumentos = ['acordion', 'bateria', 'guitarra', 'guitarraelectrica', 'harmonica', 'piano', 'trompeta']
let nombres_instrumentos = ['acordion', 'bateria', 'guitarra', 'guitarra electrica', 'harmonica', 'piano', 'trompeta']


import { ref } from 'vue';
import { Cancion } from './modelo/cancion';
import { Acordes, Parte } from './modelo/acordes';
import { Letra } from './modelo/letra';
import Nota from './modelo/Midi/nota';
import { NotasCancion, NotasParteCancion }    from './modelo/notasdecancion';
import { GetCanciones } from './modelo/GetCanciones';
import { parse } from 'path';



function tocar_notas(compases: NotasParteCancion[]) {
  
  const bpm = editando_cancion.value.bpm;
      const duracion_blanca = (60 / bpm) * editando_cancion.value.compas_unidad;
      let delay = 0;

  for (let notas_index = 0; notas_index < compases.length; notas_index++) 
      {
        
        let menor_del_acorde = 11111;
        for (let i = 0; i < compases[notas_index].length; i++) 
        {
          const notas = compases[notas_index][i];
          for (let j = 0; j < notas.length; j++) {
            
            const nota = notas[j];
            const duracion = duracion_blanca / nota.duracion;
            console.log(duracion);
            if (duracion < menor_del_acorde) 
            {
              menor_del_acorde = duracion;
            }
            
          midiplayer?.play(nota.nota, duracion, delay);
          }
           
        delay += menor_del_acorde;
        console.log("delay", delay);
        }
      }


}
function tocar(parteid: number) 
    {
      tocar_notas(editando_cancion.value.notas_cancion[0].partes[parteid].notas);
      tocar_notas(editando_cancion.value.notas_cancion[1].partes[parteid].notas);
    }


const editando_cancion = ref(new Cancion("no song name", "no band name", new Acordes([new Parte("p1", ["C"])], [0]), new Letra([[""]]), 120, 4, 4, 4, "C"));
const letra = ref([] as string[])
const musica = new Musica();

const editando_parte_id = ref(-1)
const editando_acorde_id = ref(-1)

function click_editar_acorde(parte_id: number, acorde_id: number) {
  editando_parte_id.value = parte_id
  editando_acorde_id.value = acorde_id
}

function cargar_edit() {
  let item = JSON.parse(localStorage.getItem("editando_cancion") || "{}");
  GetCanciones.obtenerCancion(item).then((cancion_get: Cancion) => {
      editando_cancion.value = cancion_get;

      // ARMO LA LETRA
      let flt_renglones: string[] = []
      for (let i = 0; i < cancion_get.letras.renglones.length; i++) {
        flt_renglones.push(cancion_get.letras.renglones[i].join(''))
      }
      letra.value = flt_renglones 


      agregar_instrumento("piano_mi");
      agregar_instrumento("piano_md");
    });
}

function agregar_instrumento(instrumento: string) {

  let notascan: NotasParteCancion[] = [];
  for (let i = 0; i < editando_cancion.value.acordes.partes.length; i++) 
  {

    let compases_en_parte = [];
    for (let j = 0; j < editando_cancion.value.acordes.partes[i].acordes.length; j++) 
    {
      let notas_compas: Nota[] = [];
      for (let k = 0; k < editando_cancion.value.acordes.partes[i].acordes[j].length; k++) 
      {
        notas_compas.push(new Nota("C4", 1));
      }
      compases_en_parte.push([notas_compas]);

    }

    let notas = new NotasParteCancion(editando_cancion.value.acordes.partes[i].nombre, compases_en_parte);
    notascan.push(notas);
  }


  let clave = "G";
  if (instrumento == "piano_md") {
    clave = "F";
  }
  let notas =  new NotasCancion(instrumento, notascan, clave);
  editando_cancion.value.notas_cancion.push(notas);
  
}

cargar_edit();
const modi_escala = ref(0);
function click_agregarpatron(patron: string, instruid: number) 
{

  const modificador: number = parseInt(modi_escala.value);
  const editando_acorde = editando_cancion.value.acordes.partes[editando_parte_id.value].acordes[editando_acorde_id.value];
  const clave: string = editando_cancion.value.notas_cancion[instruid].clave;
  console.log("clave: " , clave);
  let desde_clave: string = "4";
  if (clave == "F") {
    desde_clave = "2";
  }

if (patron == "negras") 
{
  const notas_acorde4 = musica.getNotasdeacorde(editando_acorde, (parseInt(desde_clave) + modificador).toString());
  editando_cancion.value.notas_cancion[instruid].partes[editando_parte_id.value].notas[editando_acorde_id.value] =    
  [[new Nota(notas_acorde4[0], 4)],[ new Nota(notas_acorde4[0], 4)],[ new Nota(notas_acorde4[0], 4)],[ new Nota(notas_acorde4[0], 4)]];
}

if (patron == "escalera1") 
{
  const notas_acorde4 = musica.getNotasdeacorde(editando_acorde, (parseInt(desde_clave) + modificador).toString());
  
  editando_cancion.value.notas_cancion[instruid].partes[editando_parte_id.value].notas[editando_acorde_id.value] =    
  [[new Nota(notas_acorde4[0], 4)],[ new Nota(notas_acorde4[1], 4)],[ new Nota(notas_acorde4[2], 4)],[ new Nota(notas_acorde4[0], 4)]];
}


if (patron == "blancas") 
  {
    const notas_acorde4 = musica.getNotasdeacorde(editando_acorde, (parseInt(desde_clave) + modificador).toString());
    editando_cancion.value.notas_cancion[instruid].partes[editando_parte_id.value].notas[editando_acorde_id.value] =    
    [[new Nota(notas_acorde4[0], 2)],[ new Nota(notas_acorde4[0], 2)]];
  }


  if (patron == "redonda") 
  {
    const notas_acorde4 = musica.getNotasdeacorde(editando_acorde, (parseInt(desde_clave) + modificador).toString());
    editando_cancion.value.notas_cancion[instruid].partes[editando_parte_id.value].notas[editando_acorde_id.value] =    
    [[new Nota(notas_acorde4[0], 1)]];
  }


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

   
</script>

<template>
<div>
<div> 
  
  <div>
            

            <button v-for="(nombre, id) in nombres_instrumentos" :key="id" @click="iniciar_midi(id)" > {{ nombre }}</button>
          </div>


</div>

<div display="flex">

    <div style="width: 70%;">
      <div v-for="(parte, parteid) in editando_cancion.acordes.partes" :key="parteid">
        <div>
          <h3>{{ parte.nombre }}</h3><button @click="tocar(parteid)"  v-if="ref_instrumentocargado">TOCAR </button>
        </div>
        
        <div class="notaparte">
          
            <div v-for="(nota, acordeid) in parte.acordes" :key="acordeid" @click="click_editar_acorde(parteid, acordeid)" style="display: flex;">
              <div>
              <div>{{ nota }}</div>
              <div v-for="(instru, instruid) in editando_cancion.notas_cancion" :key="instruid" style="display: flex;">
                
                <div v-if="parteid == editando_parte_id && acordeid == editando_acorde_id">
              <div>Editando
                Octava: <input type="number"  v-model="modi_escala" style="width: 7ch;" />

              </div>
              <div class="patron">
                <div class="pa_patron" @click="click_agregarpatron('negras', instruid)">Negras</div>
                <div  class="pa_patron" @click="click_agregarpatron('blancas', instruid)">Blancas</div>
                <div  class="pa_patron" @click="click_agregarpatron('redonda', instruid)">Redondas</div>
                <div  class="pa_patron" @click="click_agregarpatron('escalera1', instruid)">Escalera 1</div>
                
                
              </div>
                </div>
                <Pentagrama :clave="instru.clave" :notas="instru.partes[parteid].notas[acordeid]"></Pentagrama>
              </div>
            </div>
            
            </div>
        </div>
      
      </div>
  </div>
  <div> 
    Edutabdi
  </div>
</div>






</div>
</template>

<style scoped>
.notaparte {
  display: flex;
}
.patron {
  display: flex;
  flex-wrap: wrap;
  max-width: 300px;
}
.pa_patron {
  flex: 1 1 100px; /* Adjust the width of each item */
  margin: 2px;
  text-align: center;
  border: 1px solid #ccc;
  padding: 5px;
  cursor: pointer;
}

.btnModos {
  cursor: pointer;
  padding: 5px;
  margin: 5px;
  border: 1px solid;
  
}
</style>

