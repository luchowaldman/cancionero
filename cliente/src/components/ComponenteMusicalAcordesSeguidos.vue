<script setup lang="ts">
import { ref } from 'vue'
import { Cancion } from '../modelo/cancion';
import { watch } from 'vue';
import { VistaControl } from '../modelo/vista_control';

const props = defineProps<{ compas: number, cancion: Cancion, vista: VistaControl  }>()

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
      
      <div v-for="(parte, index) in cancion.acordes.orden_partes" :key="index" >
        <div>{{ cancion.acordes.partes[parte].nombre  }}</div>
        <div style="display: flex; flex-wrap: wrap;">
        <div  v-for="(aco, index_aco) in cancion.acordes.partes[parte].acordes" :key="index_aco"
         class="acorde"
         :style="{ 'max-height': vista.alto + 'px', 'width': (vista.tamanio_referencia * 3) + 'px', 'font-size' : vista.tamanio_referencia + 'px' }"
         :class="{ compas_actual: mostrando_parte === index && mostrando_compas_parte === index_aco }">
         {{ aco }}
        </div>
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
  margin: 1px;
  padding: 5px;
  border: 1px solid;
  border-radius: 5px;
}
.acorde  {
  font-size: large;
  margin: 1px;
  padding: 5px;
  border: 1px solid;
  border-radius: 5px;
  color: #a9a8f6;
  margin-right: 10px;
  
}
.ordenparte {
  border: 1px solid #888;
  width: 25%;
}

.compas_actual {
  background-color: red;
  color: white;
}


</style>
