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


function Iniciar_Compas(nro_compas: number) 
{ 
  console.log(`Iniciando compás ${nro_compas} en ComponenteMusicalAcordes`); 
}

</script>

<template>

  <div class="row">
  
    <h2>Orden</h2>
    <div class="row ">
          <div v-for="(parte, index) in cancion.acordes.orden_partes" :key="index" class="col-2 acorde">
            <span :class="{ compas_actual: mostrando_parte === index }" >{{ cancion.acordes.partes[parte].nombre }}</span>
          </div>
          
    </div>
    <h1>&nbsp;</h1>

    <h2>Partes</h2>
    <div v-for="(parte, index_parte) in cancion.acordes.partes" :key="parte.nombre" class="row" >
      
        <h3>{{ parte.nombre }}</h3>
        <div class="parte">
          <div v-for="(acorde, index) in parte.acordes" class="acorde" :key="acorde">
            <span  :class="{ compas_actual: ((  mostrando_compas_parte === index ) &&
                                             ( index_parte  === cancion.acordes.orden_partes[mostrando_parte]  ))
             }">{{ acorde }}</span>
          </div>
        </div>
    </div>
  
</div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}

</style>
