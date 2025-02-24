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

import { ref } from 'vue';
import { Cancion } from './modelo/cancion';
import { Acordes, Parte } from './modelo/acordes';
import { Letra } from './modelo/letra';
import Nota from './modelo/Midi/nota';
import { NotasCancion, NotasParteCancion }    from './modelo/notasdecancion';
import { GetCanciones } from './modelo/GetCanciones';
import { parse } from 'path';
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
function click_agregarpatron(patron: string, instruid: number) 
{

  const editando_acorde = editando_cancion.value.acordes.partes[editando_parte_id.value].acordes[editando_acorde_id.value];
  const clave: string = editando_cancion.value.notas_cancion[instruid].clave;
  console.log("clave: " , clave);
  let desde_clave: string = "4";
  if (clave == "F") {
    desde_clave = "2";
  }
  if (patron == "cuatros") 
  {
    const notas_acorde4 = musica.getNotasdeacorde(editando_acorde, desde_clave);
    editando_cancion.value.notas_cancion[instruid].partes[editando_parte_id.value].notas[editando_acorde_id.value] =    
    [[new Nota(notas_acorde4[0], 4)],[ new Nota(notas_acorde4[0], 4)],[ new Nota(notas_acorde4[0], 4)],[ new Nota(notas_acorde4[0], 4)]];
  }
  if (patron == "cuatros5") 
  {
    const notas_acorde4 = musica.getNotasdeacorde(editando_acorde, (parseInt(desde_clave) + 1).toString());
    editando_cancion.value.notas_cancion[instruid].partes[editando_parte_id.value].notas[editando_acorde_id.value] =    
    [[new Nota(notas_acorde4[0], 4)],[ new Nota(notas_acorde4[0], 4)],[ new Nota(notas_acorde4[0], 4)],[ new Nota(notas_acorde4[0], 4)]];
  }

if (patron == "cuatros6") 
{
  const notas_acorde4 = musica.getNotasdeacorde(editando_acorde, (parseInt(desde_clave) + 2).toString());
  editando_cancion.value.notas_cancion[instruid].partes[editando_parte_id.value].notas[editando_acorde_id.value] =    
  [[new Nota(notas_acorde4[0], 4)],[ new Nota(notas_acorde4[0], 4)],[ new Nota(notas_acorde4[0], 4)],[ new Nota(notas_acorde4[0], 4)]];
}

if (patron == "cuatros3") 
{
  const notas_acorde4 = musica.getNotasdeacorde(editando_acorde, (parseInt(desde_clave) - 1).toString());
  editando_cancion.value.notas_cancion[instruid].partes[editando_parte_id.value].notas[editando_acorde_id.value] =    
  [[new Nota(notas_acorde4[0], 4)],[ new Nota(notas_acorde4[0], 4)],[ new Nota(notas_acorde4[0], 4)],[ new Nota(notas_acorde4[0], 4)]];
}

}

</script>

<template>
<div>


<div display="flex">

    <div style="width: 70%;">
      <div v-for="(parte, parteid) in editando_cancion.acordes.partes" :key="parteid">
        <div>
          <h3>{{ parte.nombre }}</h3>
        </div>
        
        <div class="notaparte">
          
            <div v-for="(nota, acordeid) in parte.acordes" :key="acordeid" @click="click_editar_acorde(parteid, acordeid)" style="display: flex;">
              <div>
              <div>{{ nota }}</div>
              <div v-for="(instru, instruid) in editando_cancion.notas_cancion" :key="instruid" style="display: flex;">
                <Pentagrama :clave="instru.clave" :notas="instru.partes[parteid].notas[acordeid]"></Pentagrama>
                <div v-if="parteid == editando_parte_id && acordeid == editando_acorde_id">
              <div>Editando</div>
              <div @click="click_agregarpatron('cuatros3', instruid)">cuatros-1</div>
              <div @click="click_agregarpatron('cuatros', instruid)">cuatros</div>
              <div @click="click_agregarpatron('cuatros5', instruid)">cuatros+1</div>
              <div @click="click_agregarpatron('cuatros6', instruid)">cuatros+2</div>
            </div>
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

</style>
