<!--
<script setup lang="ts">
import { ref } from "vue"
import Nota from '../modelo/Midi/nota';
import { Musica } from '../modelo/musica';

const props = defineProps<{ clave: string, notas: Nota[][] }>()



const buscar = ref("𝅘𝅥𝅯");
const nota_en_top0 = ref("G5");
if (props.clave == "F") {
  nota_en_top0.value = "B3";
}
const musica = new Musica();
const nota_sol = new Nota("G4", 0);
const nota_fa = new Nota("B2", 0);
function estilo_nota(nota: Nota) 
{
  let top = musica.getDistanciaNotas(nota_en_top0.value, nota.nota, "C") * 6;
  return { 'position': 'absolute',
    'top': top + 'px'

   };
}



function getnota(nota: Nota) { 
  const duracion = nota.duracion;
  if (duracion == 1) {
    return "o";
  }
  if (duracion == 2) {
    return "𝅗";
  }
  if (duracion == 4) {
    return "𝅘𝅥";
  }
  if (duracion == 8) {
    return "𝅘𝅥𝅯";
  }
  if (duracion == 16) {
    return "𝅘𝅥𝅱";
  }

  if (duracion == -1) {
    return "𝄾";
  }
  if (duracion == -2) {
    return "𝄿";
  }
  if (duracion == -4) {
    return "𝄎";
  }
  if (duracion == -8) {
    return "𝄴";
  }  
  return " ";
}



</script>

<template>
  <div style="position: relative;">
<div style="font-family: 'Noto Music'; font-size: 50px; display: flex;">
  
  
  <div v-for="(nota, notaindex) in notas" :key="notaindex">
    
        <div v-for="(key, keyindex) in nota" :style="estilo_nota(key)" :key="keyindex">
          {{  getnota(key) }}
        </div>
        <div style="position: relative;"><img src="/img/pentagrama.png" /></div>
  </div>
  
  
  



  </div>




</div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
-->