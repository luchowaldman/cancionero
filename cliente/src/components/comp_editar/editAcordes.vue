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
const emit = defineEmits(['actualizo_cancion']);

function actualizarOrdenPartes(index: number) {
    console.log(index);
    props.cancion.acordes.orden_partes = props.cancion.acordes.orden_partes.filter(parte => parte !== -1);
   
  }

  function click_acorde(parte: number, acorde: number) {
    if (refMixeando.value) {
      editarAcordesHelper.mix_acorde(props.cancion, parte, acorde);
      emit('actualizo_cancion');
    }
    if (refSpliteando.value) {
      editarAcordesHelper.splitear_parte(props.cancion, parte, acorde);        
      emit('actualizo_cancion');
    }
  }



  function click_mixacorde() {
    refMixeando.value = !refMixeando.value;
    if (refMixeando.value) {
        refSpliteando.value = false;
    }    
  }

  function representa_acorde(parte: number, acorde: number) {
    let cont = 0;
    let sum = 0;
    while (cont < parte) {
      sum = sum + props.cancion.acordes.partes[props.cancion.acordes.orden_partes[cont]].acordes.length;
      cont++;
    }
    return sum + acorde;
  }
  
  function sobre_acorde(parte: number, acorde: number) {
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
    }
    
  }
</script>


<template>
<div class="componenteMusical">
<div style="display: flex;">
    <div class="btnEditAcorde" :class="{ 'btnSeleccionado': refMixeando }" @click="click_mixacorde">Mix Acorde </div>
    <div class="btnEditAcorde" :class="{ 'btnSeleccionado': refSpliteando }" @click="click_splitacorde"  >Split Parte</div>
</div>
    <div >
        <div class="contAcordes" v-for="(parte, index) in cancion.acordes.orden_partes" :key="index">
            <div>
                

                <select v-model="cancion.acordes.orden_partes[index]" @change="actualizarOrdenPartes(index)" class="selectParteEnOrden">
            <option v-for="(parte, parteIndex) in cancion.acordes.partes" :key="parteIndex" :value="parteIndex">
                {{ parte.nombre }}
            </option>
            <option :value="-1">Eliminar</option>
          </select>
                <div style="display: flex; flex-wrap: wrap;">
                    <div class="acorde_edicion" 
                    :class="{ 'acorde_mixiando': refMixeando , 'acorde_split': refSpliteando }"
                    @click="click_acorde(index, index_acorde)"

                    @pointerover="sobre_acorde(index, index_acorde)"  @pointerleave="dejasobre_acorde(index, index_acorde)"  
                    v-for="(acorde, index_acorde) in cancion.acordes.partes[parte].acordes"
                     :key="index_acorde">{{ acorde }}</div>
                </div>       
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
