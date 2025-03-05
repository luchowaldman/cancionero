<script setup lang="ts">
</script>
<template>
  <div>piano pa compilar</div>
</template>
<!-- PianoControl.vue 
<script setup lang="ts">
import { Nota } from '../modelo/nota';
import { ref } from 'vue';

const props = defineProps<{
  escala: string;
  acorde: string;
  notas_seleccionadas: Notas[];
}>();


import { watch } from 'vue';

watch(() => props.escala, (newVal, oldVal) => {
  console.log(`Escala changed from ${oldVal} to ${newVal}`);
  // Add your logic here to handle changes in escala
});

watch(() => props.acorde, (newVal, oldVal) => {
  console.log(`Acorde changed from ${oldVal} to ${newVal}`);
  // Add your logic here to handle changes in acorde
});


const emit = defineEmits(['toco', 'solto']);
const ref_Notas = ref([] as string[])
const escalas = [2, 3, 4, 5, 6]
const notas = ["C", "D", "E", "F", "G", "A", "B"]
function tiene_sostendio(nota: string) {
    return ["C", "D", "F", "G", "A"].includes(nota[0])
}

function nota_sostenido(nota: string) {
    return nota[0] + "#" + nota[1]
}


let allnotas: string[] = []

escalas.forEach(element => {
    notas.forEach((nota) => {
        allnotas.push(nota + element)
    });
    
});


ref_Notas.value = allnotas;

function toco_nota(nota: string) {
    
    emit('toco', nota)
}

function solto_nota(nota: string) {
    
    emit('solto', nota)
}


</script>

<template>
  <div>
  <ul class="piano">


    <li v-for="(nota, nota_id) in ref_Notas" :key="nota_id" class="key">
      <span class="white-key" @mousedown="toco_nota(nota)" @mouseup="solto_nota(nota)" >
        <span class="nota_seleccionada" v-if="props.notas_seleccionadas!= undefined && props.notas_seleccionadas.some(n => n.nota === nota)">X</span>
      </span>
      <span v-if="tiene_sostendio(nota)" @mousedown="toco_nota(nota_sostenido(nota))" @mouseup="solto_nota(nota_sostenido(nota))"
        class="black-key" > 
        <span class="nota_seleccionada" v-if="props.notas_seleccionadas!= undefined && props.notas_seleccionadas.some(n => n.nota === nota + '#')">X</span>
      </span>
      <br>
    </li> 



</ul>
</div>
</template>

<style scoped>

.nota_seleccionada {
  border: 3px solid red;
}

.piano {
  background: -webkit-linear-gradient(-65deg, #000000, #222222, #000000, #666666, #222222 75%);
  background: -moz-linear-gradient(-65deg, #000000, #222222, #000000, #666666, #222222 75%);
  background: -o-linear-gradient(-65deg, #000000, #222222, #000000, #666666, #222222 75%);
  background: linear-gradient(-65deg, #000000, #222222, #000000, #666666, #222222 75%);
  border-top: 2px solid #111;
  box-shadow: inset 0 -1px 1px rgba(255, 255, 255, 0.5), inset 0 -4px 5px #000000;
  padding: 0 1% 3%;
  text-align: center;
}
.key {
  display: inline-block;
  position: relative;
  margin: 0 2px;
  width: 2.5%;
  max-width: 85px;
}
.key:active .black-key,
.key.active .black-key {
  top: -5px;
}
.key .white-key {
  background: -webkit-linear-gradient(-30deg, #f8f8f8, #ffffff);
  background: -moz-linear-gradient(-30deg, #f8f8f8, #ffffff);
  background: -o-linear-gradient(-30deg, #f8f8f8, #ffffff);
  background: linear-gradient(-30deg, #f8f8f8, #ffffff);
  box-shadow: inset 0 1px 0px #ffffff, inset 0 -1px 0px #ffffff, inset 1px 0px 0px #ffffff, inset -1px 0px 0px #ffffff, 0 4px 3px rgba(0, 0, 0, 0.7), inset 0 -1px 0px #ffffff, inset 1px 0px 0px #ffffff, inset -1px -1px 15px rgba(0, 0, 0, 0.5), -3px 4px 6px rgba(0, 0, 0, 0.5);
  display: block;
  height: 200px;
}
.key .white-key:active,
.key .white-key.active {
  box-shadow: inset 0 1px 0px #ffffff, inset 0 -1px 0px #ffffff, inset 1px 0px 0px #ffffff, inset -1px 0px 0px #ffffff, 0 4px 3px rgba(0, 0, 0, 0.7), inset 0 -1px 0px #ffffff, inset 1px 0px 0px #ffffff, inset -1px -1px 15px #000000, -3px 4px 6px rgba(0, 0, 0, 0.5);
  position: relative;
  top: -5px;
  height: 200px;
}
.key .black-key {
  content: "";
  color: #ffffff;
  box-shadow: inset 0px -1px 2px rgba(255, 255, 255, 0.4), 0 2px 3px rgba(0, 0, 0, 0.4);
  background: -webkit-linear-gradient(-20deg, #222222, #000000, #222222);
  background: -moz-linear-gradient(-20deg, #222222, #000000, #222222);
  background: -o-linear-gradient(-20deg, #222222, #000000, #222222);
  background: linear-gradient(-20deg, #222222, #000000, #222222);
  border-width: 1px 3px 8px;
  border-style: solid;
  border-color: #666 #222 #111 #555;
  height: 160px;
  position: absolute;
  top: 0px;
  right: -40%;
  width: 70%;
  z-index: 10;
}
.key .black-key:active,
.key .black-key.active {
  border-bottom-width: 3px;
  top: 0;
}
@media (max-width: 767px) {
  .key {
    width: 8%;
  }
  .key:nth-child(1),
  .key:nth-child(2),
  .key:nth-child(3) {
    display: none;
  }
}
@media (max-width: 480px) {
  .key {
    width: 12%;
  }
  .key:nth-child(11),
  .key:nth-child(12),
  .key:nth-child(13),
  .key:nth-child(14) {
    display: none;
  }
}


</style>








-->