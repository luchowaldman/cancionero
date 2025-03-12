<script setup lang="ts">
import { item_lista } from '../../modelo/item_lista';
import { Cancion } from '../../modelo/cancion';
import { ref } from 'vue';



const props = defineProps<{ cancion: Cancion, item: item_lista, parte_indice: number, parte: number }>();
const editando_acorde_id = ref(-1);
const editando_acorde_renglonbajo = ref(false);

function click_letra(acorde_id:number, renglonbajo:boolean) {
  editando_acorde_id.value = acorde_id;
  editando_acorde_renglonbajo.value = renglonbajo;
  console.log(editando_acorde_id.value);
  console.log(editando_acorde_renglonbajo.value);
} 

function base_texto() {
  let cont = 0;
  for (let i = 0; i < props.parte_indice; i++) {
    cont += props.cancion.acordes.partes[props.cancion.acordes.orden_partes[i]].acordes.length;
  }
  return cont;
}
</script>

<template>
<div style="display: flex;  flex-wrap: wrap;" v-if="parte < cancion.acordes.orden_partes.length">
  <template v-for="(acorde, acorde_id) in cancion.acordes.partes[parte].acordes" :key="acorde_id">
    
    <template v-if="cancion.letras.renglones.flat()[base_texto() + acorde_id].includes('/n')">
      
      <div>
        <div>{{ acorde }}|</div>
        <div @click="click_letra(acorde_id, false)">
          <input type="text" v-model="cancion.letras.renglones.flat()[base_texto() + acorde_id].split('/n')[0]" v-if="acorde_id == editando_acorde_id"/>
          {{  cancion.letras.renglones.flat()[base_texto() + acorde_id].split('/n')[0] }}

        </div>
      </div>
      <div class="break"></div>
      <div @click="click_letra(acorde_id, false)">
        <div>&nbsp;</div>
        <div>{{  cancion.letras.renglones.flat()[base_texto() + acorde_id].split('/n')[1] }}|</div>
      </div>

    </template>
    <template v-else>
      
      
      <div>
        <div>{{ acorde }}|</div>
        <div>
        <input type="text" v-model="cancion.letras.renglones.flat()[base_texto() + acorde_id]" v-if="acorde_id == editando_acorde_id"/>
      </div>
        <div @click="click_letra(acorde_id, false)">{{  cancion.letras.renglones.flat()[base_texto() + acorde_id] }}|</div>
      </div>

    </template>

  </template>
  
  


  
  
</div>
          

</template>

<style scoped>


.break {
    flex-basis: 100%;
  }
</style>

