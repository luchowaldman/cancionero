<script setup lang="ts">
import { ref } from 'vue'
import { Cancion } from '../modelo/cancion';
import { Contexto } from '../modelo/contexto';
import { watch } from 'vue';

const props = defineProps<{ compas: number, cancion: Cancion, contexto: Contexto }>()

const mostrando_parte = ref(-1)
const mostrando_compas_parte = ref(-1)
const currentCompas = ref(0);



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


</script>

<template>
    <div>
      <div v-for="(parte, index) in cancion.acordes.orden_partes" :key="index" class="parte">
        <div  v-for="(aco, index_aco) in cancion.acordes.partes[parte].acordes" :key="index_aco"
         class="acorde"
         :class="{ compas_actual: mostrando_parte === index && mostrando_compas_parte === index_aco }">
         {{ aco }}
        </div>
      </div>
    </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
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
