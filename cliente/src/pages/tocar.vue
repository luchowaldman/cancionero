<script setup lang="ts">

import { on } from 'events';
import { Cancion } from '../modelo/cancion';
import { VistaControl } from '../modelo/vista_control';
import { markRaw, onMounted, onUpdated, ref } from 'vue';


const props = defineProps<{ compas: number, cancion: Cancion }>()


const vist: VistaControl[] = [
];
const ref_vista = ref(vist);
const ref_cont = ref(0);

function cambiar_vista(vista: number) {
  let toCH: VistaControl[] = [];
  switch (vista) {
    case 0:
      toCH = [
        new VistaControl(window.innerHeight / 50, 12, 7, "letra_acordes", "col-9", (window.innerHeight / 1.7)),
        new VistaControl(30, 12, 7, "acordes", "col-3 d-md-block", 1400)
        ];
      break;
    case 1:
    toCH = [
        new VistaControl(window.innerHeight / 50, 12, 7, "detalle", "col-9", (window.innerHeight / 1.7)),
        //new VistaControl(window.innerHeight / 50, 12, 7, "detalle", "col-9", (window.innerHeight / 1.7)),
          new VistaControl(30, 12, 7, "acordes", "col-3 d-md-block", 1400)
        ];
      break;
      case 2:
    toCH = [
        new VistaControl(window.innerHeight / 50, 12, 7, "detalle", "col-9", (window.innerHeight / 1.7))
        ];
      break;
      case 3:
    toCH = [
    new VistaControl(window.innerHeight / 50, 12, 7, "detalle", "col-9", (window.innerHeight / 1.7))
        ];
      break;

  }
  ref_vista.value = toCH;
  ref_cont.value = ref_cont.value + 1;
}
cambiar_vista(0);

// ENTORNO
const width = ref(window.innerWidth); 
const height = ref(window.innerHeight);
const updateDimensions = () => { width.value = window.innerWidth; height.value = window.innerHeight; };

onMounted(() => {
  
  console.log("TOCAR MONTADA")
  
  window.addEventListener('resize', updateDimensions);
})

</script>

<template>
  
  <div class="pantalla">
    <div class="cabecera_tocar" style="display: flex ;float: right;;">


      <div class="dropdown" >
    <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
      <i class="bi bi-eye"></i>
    </button>
    <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
      <li v-on:click="cambiar_vista(0)"><a class="dropdown-item" href="#">Mix 1</a></li>
      <li v-on:click="cambiar_vista(1)"><a class="dropdown-item" href="#">Cantante</a></li>
      <li v-on:click="cambiar_vista(2)"><a class="dropdown-item" href="#">Guitarrista</a></li>
      <li v-on:click="cambiar_vista(3)"><a class="dropdown-item" href="#">Solo detalles</a></li>
    </ul>
  </div>

    </div>
<div class="row">
    <div v-for="(Componente, index) in ref_vista" :key="index" 
    :class="Componente.clase">
      <component :is="Componente.getMarkRaw()" :compas="compas" :key="index" :ref="Componente.componente" :vista="Componente" :cancion="cancion" val="ref_cont"></component>
    </div>
</div>


<p>Anchura: {{ width }} px - Altura: {{ height }} px</p>
  

 </div>

</template>

<style scoped>
.pantalla {
    margin-top: 10px;
    margin-left: 10px;
    margin-right: 10px;
    margin-bottom: 10px;
    padding: 10px;
    border: 1px solid black;
    border-radius: 10px;
    height: 100%;
    
}
</style>
