<script setup lang="ts">

import { Cancion } from '../modelo/cancion';
import { VistaControl } from '../modelo/vista_control';
import { onMounted, Ref, ref } from 'vue';
import ComponenteMusicalLetrayAcordes from '../components/comp_tocar/ComponenteMusicalLetrayAcordes.vue';
import ComponenteMusicalLetra from '../components/comp_tocar/ComponenteMusicalLetra.vue';
import ComponenteMusicalAcordes from '../components/comp_tocar/ComponenteMusicalAcordes.vue';
import ComponenteMusicalAcordesSeguidos from '../components/comp_tocar/ComponenteMusicalAcordesSeguidos.vue';
import ComponenteMusicalPartitura from '../components/ComponenteMusicalPartitura.vue';

const props = defineProps<{ compas: number, cancion: Cancion, width: number, height: number }>()

class vista_tocar {
  viendo: string = "karaoke";
  secuencia: boolean = true;
  partes: boolean = true;
  largo_principal: number = 70;
}
const vista: Ref<vista_tocar> = ref(new vista_tocar());
vista.value.viendo = localStorage.getItem("viendo_vista_tocando") || "karaoke";
vista.value.secuencia = localStorage.getItem("secuencia") == "true" ? true : false;
vista.value.partes = localStorage.getItem("partes") == "true" ? true : false;
adecu_ancho();
function cambiar_vista(nvista: string) {
  vista.value.viendo = nvista;
  localStorage.setItem("viendo_vista_tocando", nvista);
  adecu_ancho();
  
}
function adecu_ancho() {
  if (vista.value.secuencia || vista.value.partes) {
    vista.value.largo_principal = 70;
  } else {
    vista.value.largo_principal = 100;
  }
}
function click_secuencia() {
  vista.value.secuencia = !vista.value.secuencia;
  localStorage.setItem("secuencia", vista.value.secuencia ? "true" : "false");
  adecu_ancho();

}

function click_partes() {
  vista.value.partes = !vista.value.partes;
  localStorage.setItem("partes", vista.value.partes ? "true" : "false");
  adecu_ancho();
}

function GetStylePantallaPlay() {
  return {
    width: props.width + "px",
    height: props.height + "px"

  }
}

const vistaLetraYAcordes = ref(new VistaControl(20, 12, 7, "acordes_seguidos", "col-9", props.height - 180));
const vistaKaraoke = ref(new VistaControl(20, 12, 7, "acordes_seguidos", "col-9", props.height - 180));
const vistaAcordes = ref(new VistaControl(30, 12, 7, "acordes_seguidos", "col-9", props.height - 240));



</script>

<template>
  <div class="pantallaPlay" :style="GetStylePantallaPlay()">
    <div :style="{ width: vista.largo_principal + '%' }">

      <ComponenteMusicalLetrayAcordes v-if="vista.viendo == 'acordes'" :cancion="cancion"  :compas="compas" :vista="vistaLetraYAcordes"></ComponenteMusicalLetrayAcordes>
      <ComponenteMusicalLetra  v-if="vista.viendo == 'karaoke'" :cancion="cancion"  :compas="compas" :vista="vistaKaraoke"></ComponenteMusicalLetra>
      <ComponenteMusicalAcordesSeguidos  v-if="vista.viendo == 'soloacordes'" :cancion="cancion"  :compas="compas" :vista="vistaKaraoke"></ComponenteMusicalAcordesSeguidos>
      <ComponenteMusicalPartitura  v-if="vista.viendo == 'partitura'" :cancion="cancion"  :compas="compas" :vista="vistaKaraoke"></ComponenteMusicalPartitura>
      
    </div>
    <div :style="{ width: (100 - vista.largo_principal) + '%' }">

      <ComponenteMusicalAcordes :cancion="cancion" :compas="compas" :vista="vistaAcordes"
      :secuencia="vista.secuencia" :partes="vista.partes" :width="props.width" :height="props.height"
      ></ComponenteMusicalAcordes>

    </div>
    <div class="dropdown" >
    <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
      <i class="bi bi-eye"></i>
    </button>
    <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
      <li v-on:click="cambiar_vista('karaoke')"><a class="dropdown-item" href="#">Karaoke</a></li>
      <li v-on:click="cambiar_vista('acordes')"><a class="dropdown-item" href="#">Acordes</a></li>
      <li v-on:click="cambiar_vista('soloacordes')"><a class="dropdown-item" href="#">Solo Acordes</a></li>
      <li v-on:click="cambiar_vista('partitura')"><a class="dropdown-item" href="#">Partitura</a></li>
      <li><hr class="dropdown-divider"></li>

      <li v-on:click="click_secuencia()"><a class="dropdown-item" href="#">
        <i class="bi bi-check-circle" v-if="vista.secuencia"></i> Secuencia</a></li>
      <li v-on:click="click_partes()"><a class="dropdown-item" href="#">
        <i class="bi bi-check-circle" v-if="vista.partes"></i> 
        Partes</a></li>

    </ul>
  </div>
    
    
 </div>

</template>

<style scoped>
.pantallaPlay {
  border: 1px solid ;
  display: flex;
}
</style>
