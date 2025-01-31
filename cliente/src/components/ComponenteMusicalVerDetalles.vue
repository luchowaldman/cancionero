<script setup lang="ts">
import { ref, watch } from 'vue';
import { Cancion } from '../modelo/cancion';
import { VistaControl } from '../modelo/vista_control';
import { Musica } from '../modelo/musica';
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


</script>
<template>
  <div>
   Total Acordes: {{ musica.total_compases(cancion) }}
  Total letra: {{ cancion.letras.renglones.flat().length }} 
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
