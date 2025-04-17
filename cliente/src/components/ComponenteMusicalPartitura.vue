<script setup lang="ts">

import Pentagrama from '../components/pentagrama.vue';
import { Ref, ref, watch } from 'vue';
import { Cancion } from '../modelo/cancion';
import { VistaControl } from '../modelo/vista_control';
import { Musica } from '../modelo/musica';
import { CompacesPartitura } from '../modelo/PartituraInstrumento';
const props = defineProps<{ compas: number, cancion: Cancion, vista: VistaControl  }>()


const mostrando_parte = ref(-1)
const mostrando_compas_parte = ref(-1)
const currentCompas = ref(0);
const musica = new Musica();



watch(() => props.compas, (newCompas) => {
  let totalCompases = 0;
  for (let i = 0; i < props.cancion.acordes.orden_partes.length; i++) 
  {
    let compases_x_parte = props.cancion.acordes.partes[props.cancion.acordes.orden_partes[i]].acordes.length; 
    if (newCompas < totalCompases + compases_x_parte) {
      mostrando_parte.value = i;
      mostrando_compas_parte.value = newCompas - totalCompases;
      break;
    }
    totalCompases += compases_x_parte;
  }
  currentCompas.value = newCompas;
});

const primer_pentagrama: Ref<CompacesPartitura[][]> = ref([]);
const segundo_pentagrama: Ref<CompacesPartitura[][]> = ref([]);

function calcular_vista() 
{

  const N = 4; // Número de compases por grupo

  primer_pentagrama.value = [];
  const compases = props.cancion.partitura_instrumentos[0].compaces;

  for (let i = 0; i < compases.length; i += N) {
    primer_pentagrama.value.push(compases.slice(i, i + N));
  }

}
calcular_vista();
</script>
<template>
  <div>
    Partitura
    <div class="renglon_compas" v-for="(grupo, index) in primer_pentagrama" :key="index">
      <div class="compas" v-for="(compas, compasIndex) in grupo" :key="compasIndex">
      
      <Pentagrama :clave="'G'" :notas="compas.notas"></Pentagrama>
      </div>
    </div>
    
    
</div>
</template>



<style scoped>

.read-the-docs {
  color: #888;
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
