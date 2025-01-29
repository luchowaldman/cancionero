<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue';
import { Cancion } from '../modelo/cancion';
import { Musica } from '../modelo/musica';
import { AnalisisArmonico } from '../modelo/analisis_armonico';
import Acordedit from './acordedit.vue';

let musica = new Musica();
const props = defineProps<{ compas: number, cancion: Cancion, editando_cancion: boolean }>()

const emit = defineEmits(['cerrar']);


function cerrar_edicion() {
  emit('cerrar');
}


const editando_renglon = ref(-1);
const editando_parte = ref(-1);

function editarPalabra(renglonIndex: number, palabraIndex: number) {
  console.log("editarPalabra", renglonIndex, palabraIndex, props.cancion.letras.renglones[renglonIndex][palabraIndex]);
  editando_renglon.value = renglonIndex;
  editando_parte.value = palabraIndex;
}

function guardarPalabra(renglonIndex: number, palabraIndex: number) {
  console.log("guardarPalabra", renglonIndex, palabraIndex, props.cancion.letras.renglones[renglonIndex][palabraIndex]);
  editando_renglon.value = -1;
  editando_parte.value = -1;

}

function borrar(renglonIndex: number, palabraIndex: number) {
  console.log("borrar", renglonIndex, palabraIndex, props.cancion.letras.renglones[renglonIndex][palabraIndex]);
  props.cancion.letras.renglones[renglonIndex].splice(palabraIndex, 1);
}

  function guardar_cancion() {
    const cancionJSON = JSON.stringify({
      cancion: props.cancion.cancion,
      banda: props.cancion.banda,
      acordes: {
        partes: props.cancion.acordes.partes.map(parte => ({
          nombre: parte.nombre,
          acordes: parte.acordes
        })),
        orden_partes: props.cancion.acordes.orden_partes
      },
      letras: props.cancion.letras.renglones,
      tempo: props.cancion.tempo
    });


    const blob = new Blob([cancionJSON], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    const nombreArchivo = `${props.cancion.banda.replace(/\s+/g, '-')}_${props.cancion.cancion.replace(/\s+/g, '-')}.json`.toLocaleLowerCase();
    a.download = nombreArchivo;
    a.click();
    URL.revokeObjectURL(url);
  }


</script>
<template>
<div v-if="editando_cancion">

  <div class="navbarEdit" >
    <div class="marca">
      Editando
    </div>
    
    
    
    <div class="botoneraleft">
      <button @click="guardar_cancion()" >Guardar</button>
      <button @click="cerrar_edicion()">Cerrar</button>
  </div>
  </div>
    


  <div class="row">
    <div class="col-8">
      <div>
        <div v-for="(renglon, renglonIndex) in cancion.letras.renglones" :key="renglonIndex" style="display: flex;">
          <div v-for="(palabra, palabraIndex) in renglon" :key="palabraIndex" class="palabraedit">
            <div @click="editarPalabra(renglonIndex, palabraIndex)" v-if="renglonIndex != editando_renglon || palabraIndex != editando_parte" >
              <p v-if="palabra!=''"> {{ palabra }}</p>
              <p v-if="palabra==''">
                <i class="bi bi-music-note"></i>
              </p>
            </div>
            <div v-if="renglonIndex == editando_renglon && palabraIndex == editando_parte">
              <input  v-model="cancion.letras.renglones[renglonIndex][palabraIndex]" @blur="guardarPalabra(renglonIndex, palabraIndex)" />
              <button>
                <i class="bi bi-trash" @click="borrar(renglonIndex, palabraIndex)"></i>
              </button>
          </div> 
          </div>
        </div>
      </div>

    </div>
    <div class="col-4">
Acordes
      
</div>
      
</div>
</div>

</template>



<style scoped>
.read-the-docs {
  color: #888;
}


.noesta_enscala {
  color: red;
}

.palabraedit {
  margin: 2px;
  height: 20px;
}


.botoneraleft {
  margin-left: auto
}

.navbarEdit {
  display: flex;
  border: 1px solid;
}


.break {
    flex-basis: 100%;
  }
.parte {
  display: flex;
}
.acorde {
  border: 1px solid #888;
  width: 25%;
}
.ordenparte {
  border: 1px solid #888;
  width: 25%;
}

.compas_actual {
  background-color: #00FF00;
  color: white;
}



</style>
