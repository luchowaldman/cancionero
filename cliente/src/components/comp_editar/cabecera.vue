<script setup lang="ts">
import { item_lista } from '../../modelo/item_lista';
import { Cancion } from '../../modelo/cancion';



const props = defineProps<{ cancion: Cancion, item: item_lista }>()
const emit = defineEmits(['cerrar', 'guardar', 'nueva', 'descargar']);


</script>

<template>
    

    

<div class="menuEditar" >
    <div class="marca">
      
      
        <span class="lblCabecera">BPM:</span> <input type="range" style="background-color: #a9a8f6; color: white;"  v-model="cancion.bpm" min="30" max="240" /> {{ cancion.bpm }} - 
     
        <span  style="color: white  !important;"  v-if="cancion.bpm < 40">No cargada o menos que lenta</span>
        <span  style="background-color: #a9a8f6; color: white;"  v-if="cancion.bpm >= 40 && cancion.bpm <= 60">Largo</span>
<span v-if="cancion.bpm > 60 && cancion.bpm <= 66">Largo a Adagio</span>
<span v-if="cancion.bpm > 66 && cancion.bpm <= 76">Adagio</span>
<span v-if="cancion.bpm > 76 && cancion.bpm <= 108">Andante</span>
<span v-if="cancion.bpm > 108 && cancion.bpm <= 120">Moderato</span>
<span v-if="cancion.bpm > 120 && cancion.bpm <= 168">Allegro</span>
<span v-if="cancion.bpm > 168 && cancion.bpm <= 176">Vivace</span>
<span v-if="cancion.bpm > 176 && cancion.bpm <= 200">Presto</span>
<span v-if="cancion.bpm > 200">Prestissimo</span>

<span class="lblCabecera">Compas:</span> 
         <input type="text" v-model="cancion.compas_cantidad" maxlength="1" :style="{ width: '3ch' }" /> / 
        <input type="text" v-model="cancion.compas_unidad" maxlength="1" :style="{ width: '3ch' }" /> - Escala  
        <input type="text" v-model="cancion.escala" maxlength="4" :style="{ width: '6ch' }" />
        Calidad: <input type="range" v-model="cancion.calidad" min="0" max="10" />

        <div style="display: inline; float: right;">
            
            <div div class="btnsMenu" style="display: flex; flex-wrap: wrap;">|
   
              <div class="divBtnMenu" @click="emit('nuevo')">
        <i class="bi bi-file-earmark-plus"></i> Nuevo
      
      </div>
      <div class="divBtnMenu" @click="emit('guardar')">
        <i class="bi bi-file-earmark-plus"></i>Guardar
      
      </div>
      
      <div class="divBtnMenu" @click="emit('descargar')">
        
              <i class="bi bi-download"></i>Descargar
      </div>

      

    </div>
          </div>
        </div>
          
          
        
        
        </div>
          

</template>

<style scoped>
.lblCabecera {
  margin: 13px 0px 0px 15px;
  font-size: 20px;
}
.menuEditar {
  border: 5px solid #a9a8f6;
  height: 80px;
  padding: 4px;
}
.read-the-docs {
  color: #888;
}


.divBtnMenu {
  border: 1px solid;
  margin: 5px 10px 5px 10px;
  border-radius: 20px;
  padding: 10px;
  color: #a9a8f6;
}

</style>

