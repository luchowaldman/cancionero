<script setup lang="ts">
import { item_lista } from '../modelo/item_lista';
import { Cancion } from '../modelo/cancion';



const props = defineProps<{ cancion: Cancion, item: item_lista }>()
const emit = defineEmits(['cerrar', 'guardar', 'nuevo']);


function DescargarJSON() {
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
      escala: props.cancion.escala,
      letras: props.cancion.letras.renglones,
      bpm: props.cancion.bpm,
      calidad: props.cancion.calidad,
      compas_cantidad: props.cancion.compas_cantidad,
      compas_unidad: props.cancion.compas_unidad,
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
    

    

<div class="menuEditar" >
    <div class="marca">
      
      
        BPM: <input type="range" style="background-color: #a9a8f6; color: white;"  v-model="cancion.bpm" min="30" max="240" /> {{ cancion.bpm }} - 
     
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

      
        Compas: <input type="text" v-model="cancion.compas_cantidad" maxlength="1" :style="{ width: '3ch' }" /> / 
        <input type="text" v-model="cancion.compas_unidad" maxlength="1" :style="{ width: '3ch' }" /> - Escala  
        <input type="text" v-model="cancion.escala" @change="forsarcompases_escala" maxlength="4" :style="{ width: '6ch' }" />
        Calidad: <input type="range" v-model="cancion.calidad" min="0" max="10" />

        <div style="display: inline; float: right;">
            <button @click="emit('guardar')">
        <i class="bi bi-save"></i> 
            </button>
            <button @click="emit('nuevo')">
              <i class="bi bi-file-earmark-plus"></i>
            </button>
            <button @click="DescargarJSON()">
              <i class="bi bi-download"></i>
            </button>
            
          </div>
        </div>
          
          
        
        
        </div>
          

</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>

