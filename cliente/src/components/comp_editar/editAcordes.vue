<script setup lang="ts">
import { ref, watch } from 'vue';
import { Cancion } from '../../modelo/cancion';
import { Musica } from '../../modelo/musica';
import { item_lista } from '../../modelo/item_lista';
import { Parte } from '../../modelo/acordes';
import { editarAcordesHelper  } from '../comp_editar/editarAcordesHelper';

let musica = new Musica();
const props = defineProps<{ cancion: Cancion  }>()
const refMixeando = ref(false);
const refSpliteando = ref(false);

const refBorrandoParteSecuencia = ref(false);
  const refAgregandoParteSecuencia = ref(false);
  const refAgregandoParte = ref(false);

const acordes_editando = ref("");

const refEditantoOrdenParte = ref(-1);
const emit = defineEmits(['actualizo_cancion']);

function click_editarparte(index: number) {
  acordes_editando.value = props.cancion.acordes.partes[props.cancion.acordes.orden_partes[index]].acordes.join('|').trim();
    refEditantoOrdenParte.value = index;
}

function click_okeditarparte(index: number) {
  const toana = acordes_editando.value.toUpperCase()
    .replace(/M/g, 'm')
    .replace(/SUS/g, 'sus')
    .replace(/MAJ/g, 'maj')

    props.cancion.acordes.partes[props.cancion.acordes.orden_partes[index]].acordes = toana.split('|');
    refEditantoOrdenParte.value = -1;
    emit('actualizo_cancion');
}

function actualizarOrdenPartes(index: number) {
    console.log(index);
    props.cancion.acordes.orden_partes = props.cancion.acordes.orden_partes.filter(parte => parte !== -1);
    emit('actualizo_cancion');
   
  }

  function click_acorde(parte: number, acorde: number) {
    if (refMixeando.value) {
      editarAcordesHelper.mix_acorde(props.cancion, parte, acorde);
      emit('actualizo_cancion');
      refMixeando.value = false;
    }
    if (refSpliteando.value) {
      editarAcordesHelper.splitear_parte(props.cancion, parte, acorde);        
      emit('actualizo_cancion');
      refSpliteando.value = false;
    }
  }

const refEditando = ref(false);
function click_editaracordes() {
    refEditando.value = !refEditando.value;
    if (refEditando.value) {
        refMixeando.value = false;
        refSpliteando.value = false;
        refBorrandoParteSecuencia.value = false;
        refAgregandoParteSecuencia.value = false;
        refAgregandoParte.value = false;
    }
  }

  function click_mixacorde() {
    refMixeando.value = !refMixeando.value;
    if (refMixeando.value) {
        refEditando.value = false;
        refSpliteando.value = false;
        refBorrandoParteSecuencia.value = false;
        refAgregandoParteSecuencia.value = false;
        refAgregandoParte.value = false;

    }    
  }

  function representa_acorde(parte: number, acorde: number) {
    let cont = 0;
    let sum = 0;
    while ( (cont < parte) && (props.cancion.acordes.orden_partes.length > cont) )
    {
      sum = sum + props.cancion.acordes.partes[props.cancion.acordes.orden_partes[cont]].acordes.length;
      cont++;
    }
    return sum + acorde;
  }
  
  let actualizo = false;
  function sobre_acorde(parte: number, acorde: number) {
    if (!actualizo) {
      emit('actualizo_cancion');
      actualizo = true;
    }


    const spanAcorde = document.getElementById('span_acorde-' + representa_acorde(parte, acorde).toString());
    if (spanAcorde) {
        //spanAcorde.style.backgroundColor = 'red';
        spanAcorde.classList.add('acorde_resaltado')
    }
  }


  function dejasobre_acorde(parte: number, acorde: number) {
    
    const spanAcorde = document.getElementById('span_acorde-' + representa_acorde(parte, acorde).toString());
    if (spanAcorde) {
        spanAcorde.style.backgroundColor = '';
        spanAcorde.classList.remove('acorde_resaltado')
    }

  }

  function click_splitacorde() {
    refSpliteando.value = !refSpliteando.value;
    if (refSpliteando.value) {
      
        refMixeando.value = false;
        refBorrandoParteSecuencia.value = false;
        refAgregandoParteSecuencia.value = false;
        refAgregandoParte.value = false;
        
    }
    
  }

  const drag_parte = ref(-1);
  function dragstart_ordenparte(index: number) {
    drag_parte.value = index;
    
  }

  function dragover_ordenparte(ev: DragEvent, index: number) {
    ev.preventDefault();
  }

  function drop_ordenparte(index: number) {
    if (drag_parte.value !== -1) {
      const temp = props.cancion.acordes.orden_partes[index];
      props.cancion.acordes.orden_partes[index] = props.cancion.acordes.orden_partes[drag_parte.value];
      props.cancion.acordes.orden_partes[drag_parte.value] = temp;
      emit('actualizo_cancion');
    }
  }

  
  function click_borrarpartesecuencia() {
    refBorrandoParteSecuencia.value = !refBorrandoParteSecuencia.value;
    if (refBorrandoParteSecuencia.value) {
        refAgregandoParteSecuencia.value = false;
        refAgregandoParte.value = false;
        refMixeando.value = false;
        refSpliteando.value = false

    }
}



  function click_agregarparte() {
    refAgregandoParte.value = !refAgregandoParte.value;
    if (refAgregandoParte.value) {
        refAgregandoParteSecuencia.value = false;
        refMixeando.value = false;
        refSpliteando.value = false;
        refBorrandoParteSecuencia.value = false;

    }
  }
  
  function click_agregarpartesecuencia() {
    refAgregandoParteSecuencia.value = !refAgregandoParteSecuencia.value;
    if (refAgregandoParteSecuencia.value) {
        refAgregandoParte.value = false;
        refMixeando.value = false;
        refSpliteando.value = false;
        refBorrandoParteSecuencia.value = false;
    }
  }
  function click_borrarparte(index: number) {
    props.cancion.acordes.orden_partes.splice(index, 1);
    emit('actualizo_cancion');
  }

  function click_enagregarparte(index: number) {
    if (refAgregandoParteSecuencia.value) {
      props.cancion.acordes.partes.push(new Parte('Nueva parte', ["."]));
      props.cancion.acordes.orden_partes.splice(index + 1, 0, props.cancion.acordes.partes.length - 1);
      emit('actualizo_cancion');
    }
    if (refAgregandoParte.value) {
        let n = [];

        for (let i = 0; i < props.cancion.acordes.orden_partes.length; i++) {
            n.push(props.cancion.acordes.orden_partes[i]);
            if (i == index) {
              n.push(props.cancion.acordes.orden_partes[i]);
            }
        }
        props.cancion.acordes.orden_partes = n;
        emit('actualizo_cancion');
    }
  }

</script>


<template>
<div class="componenteMusical">
<div style="display: flex; flex-wrap: wrap;">
    <div class="btnEditAcorde" :class="{ 'btnSeleccionado': refEditando }" @click="click_editaracordes">
      <span class="bi bi-pencil"></span>
      </div>
    <div class="btnEditAcorde" :class="{ 'btnSeleccionado': refMixeando }" @click="click_mixacorde">Mix</div>
    <div class="btnEditAcorde" :class="{ 'btnSeleccionado': refSpliteando }" @click="click_splitacorde">/</div>
    <div class="btnEditAcorde" :class="{ 'btnSeleccionado': refBorrandoParteSecuencia }" @click="click_borrarpartesecuencia">
      <span class="bi bi-trash"></span>
    </div>
    <div class="btnEditAcorde" :class="{ 'btnSeleccionado': refAgregandoParteSecuencia }" @click="click_agregarpartesecuencia">
      <span class="bi bi-plus"></span>
    </div>
    <div class="btnEditAcorde" :class="{ 'btnSeleccionado': refAgregandoParte }" @click="click_agregarparte">+ Parte</div>
</div>
    <div >
      <div >
        <div class="contAcordes" v-for="(parte, index) in cancion.acordes.orden_partes" :key="index">
            <div style="display: flex;">
                
              <div class="clsIdParte"
              draggable="true"
              @dragstart="dragstart_ordenparte(index)"
              @dragover="dragover_ordenparte($event, index)"
              @drop="drop_ordenparte(index)"
              >
               <span >{{  index + 1 }}</span>
         
       </div>
              <div class="btnEditAcorde"
               v-if="index!=refEditantoOrdenParte && refEditando"
              @click="click_editarparte(index)" ><span class="bi bi-pencil"></span></div>                
              <div class="btnEditAcorde" @click="click_okeditarparte(index)"              
               v-if="index==refEditantoOrdenParte">
                <span >Ok</span>         
        </div>
        
        <input type="text" v-model="cancion.acordes.partes[parte].nombre"
        :style="{ width :(1 + cancion.acordes.partes[parte].nombre.length).toString() + 'ch'}"
        v-if="index==refEditantoOrdenParte" />
        <select v-model="cancion.acordes.orden_partes[index]"  v-if="index!=refEditantoOrdenParte" @change="actualizarOrdenPartes(index)" class="selectParteEnOrden">
                  
                  <option v-for="(parte, parteIndex) in cancion.acordes.partes" :key="parteIndex" :value="parteIndex">
                  {{ parte.nombre }}
                </option>
                
            
          </select>
          
        </div>
                <div style="display: flex; flex-wrap: wrap;"  v-if="index!=refEditantoOrdenParte && cancion.acordes.partes[parte]">
                    <div class="acorde_edicion" 
                    :class="{ 'acorde_mixiando': refMixeando , 'acorde_split': refSpliteando }"
                    @click="click_acorde(index, index_acorde)"
                    @pointerover="sobre_acorde(index, index_acorde)"  @pointerleave="dejasobre_acorde(index, index_acorde)"  
                    v-for="(acorde, index_acorde) in cancion.acordes.partes[parte].acordes"
                     :key="index_acorde">{{ acorde }}</div>
                </div>       
                <input type="text" :style="{ width :(3 + acordes_editando.length).toString() + 'ch'}"
                v-model="acordes_editando" v-if="index==refEditantoOrdenParte"  />


                <div class="btnEditAcorde"
               v-if="refBorrandoParteSecuencia"
              @click="click_borrarparte(index)" ><span class="bi bi-trash"></span></div>     

              <div class="btnEditAcorde"
               v-if="refAgregandoParte || refAgregandoParteSecuencia"
              @click="click_enagregarparte(index)" ><span class="bi bi-plus"></span></div>     

        </div>
        </div>
        

    </div>
    
</div>
    


  
</template>



<style scoped>
.contAcordes {
    display: flex;
    flex-wrap: wrap;
    
}

.btnSeleccionado {
    background-color: #a9a8f6;
    color: white !important;
}
.acorde_edicion {
  font-size: x-large;
  border: 1px solid #a9a8f6;
  padding: 10px;
  border-left: none;
}
.acorde_split:hover {
  border: 2px solid #a9a8f6;
  margin-left: 30px;
}


.acorde_mixiando:hover {
  border: 2px solid #a9a8f6;
  color: red;
  border-right: none;
}
.btnEditAcorde {
    border: 1px solid;
    color: #a9a8f6;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 12px;
    padding: 10px 24px;
}

</style>
