<script setup lang="ts">
import { ref } from 'vue'
import { Cancion } from '../modelo/cancion';
import { watch } from 'vue';
import { Musica } from '../modelo/musica';
import { VistaControl } from '../modelo/vista_control';

const props = defineProps<{ compas: number, cancion: Cancion, vista: VistaControl  }>()

const mostrando_parte = ref(-1)
const mostrando_compas_parte = ref(-1)
const currentCompas = ref(0);


const secu_resu = ref([] as number[]);
const repe_resu = ref([] as number[]);

const mostrando_resumen_parte_index = ref(-1);
const mostrando_resumen_parte = ref(-1);


const musica = new Musica()
const compases_escala = ref(musica.GetAcordesdeescala(props.cancion.escala))



function color_x_index(index: number) {
  switch (index) {
    case 0:
      return '#a9a8f6';
    case 1:
      return '#497aff';
    case 2:
      return '#a9a8g6';
    case 3:
      return '#497aff';      
    case 4:
      return 'orange';
    case 5:
      return '#497aff';
    case 6:
      return 'orange';    
    default:
      return 'green';

  }
}

function estilo_acorde(acorde: string) 
{
  if (compases_escala.value.length == 0 && props.cancion.escala != "") {
    compases_escala.value = musica.GetAcordesdeescala(props.cancion.escala);
  }

  if (!acorde.includes(' ')) {
  const find_acord = acorde.replace(/7|5/g, '');
  const index = compases_escala.value.indexOf(find_acord);
  const color = color_x_index(index);
  return { 'border-color': color };
  
  }
  else 
  {
//    const acordes = acorde.split(' ');
//    const primerAcorde = acordes[0];
 //   const ultimoAcorde = acordes[acordes.length - 1];

  }
}


watch(() => props.cancion, (newCancion) => {
  compases_escala.value = musica.GetAcordesdeescala(newCancion.escala);
  let new_resu: number[] = [];
  let newpartes_resu: number[] = [];
  let metiendo  = -1;
  newCancion.acordes.orden_partes.forEach(element => {
     if (metiendo != element) {
       new_resu.push(element);
       newpartes_resu.push(1);
       metiendo = element;
     }
     else {
       newpartes_resu[newpartes_resu.length - 1] += 1;
     }
  });  
  secu_resu.value = new_resu;
  repe_resu.value = newpartes_resu;
});

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
  calcular_resumen_parte();

});

function calcular_resumen_parte() 
{
  
  if (repe_resu.value.length == 0) {
    return;
  }

  
  let cont = repe_resu.value[0];
  let i = 0;
  while (cont <= mostrando_parte.value) {
    
    i++;
    cont += repe_resu.value[i];
  }
  
  
  mostrando_resumen_parte_index.value = i;
  mostrando_resumen_parte.value = repe_resu.value[i] - (cont - mostrando_parte.value);
  



}


</script>

<template>
<div>
  <div class="row">

    <div v-if="repe_resu.length == 0">
    <h2 style="text-decoration: underline; margin-bottom: 2px;">Secuencia</h2>
    <div style="display: flex; flex-wrap: wrap;">
          <div v-for="(parte, index) in cancion.acordes.orden_partes" :key="index" class="ordendiv">
            <span :class="{ compas_actual: mostrando_parte === index }"
            :style="{ 'font-size' : (vista.tamanio_referencia / 2 ) + 'px'}"
            >{{ cancion.acordes.partes[parte].nombre }}</span>
          </div>
          
    </div>
    
  </div>
    
    
    <div v-if="repe_resu.length > 0">
    <h2 style="text-decoration: underline; margin-bottom: 2px;">Secuencia</h2>
    <div style="display: flex; flex-wrap: wrap;">
          <div v-for="(parte, index) in secu_resu" :key="index">
            <div  class="ordendiv">
            <span :class="{ compas_actual: mostrando_resumen_parte_index === index }"
            :style="{ 'font-size' : (vista.tamanio_referencia / 2 ) + 'px'}"
            >{{ cancion.acordes.partes[parte].nombre }}</span> 
          </div>
          <div class="repeticion" v-if="repe_resu[index] > 1">
              <span v-if="mostrando_resumen_parte_index != index">x {{ repe_resu[index] }}</span>
              <span v-if="mostrando_resumen_parte_index == index">{{ mostrando_resumen_parte + 1  }} / {{ repe_resu[index] }}</span>
          </div>
          </div>
          
    </div>
  </div>
  
    <h2  style="text-decoration: underline; margin-bottom: 2px;">Partes</h2>
    <div v-for="(parte, index_parte) in cancion.acordes.partes" :key="parte.nombre" class="row" >
      
        <div :style="{ 'font-size' : (vista.tamanio_referencia / 1.7 ) + 'px'}">{{ parte.nombre }}</div>
        <div class="partediv">
          <div v-for="(acorde, index) in parte.acordes" class="acordediv" :key="acorde" :style="estilo_acorde(acorde)">
            <span  
             :style="{ 'font-size' : vista.tamanio_referencia + 'px'}"
            :class="{ compas_actual: ((  mostrando_compas_parte === index ) &&
                                             ( index_parte  === cancion.acordes.orden_partes[mostrando_parte]  ))
             }
             
             ">{{ acorde }}</span>
          </div>
        </div>
    </div>
  
 </div>
</div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}

.ordendiv  {
  font-size: large;
  margin: 1px;
  padding: 5px;
  border: 1px solid;
  border-radius: 5px;
  display: inline-block;
  color: #a9a8f6;
  margin-right: 10px;
  
}

.partediv {
  display: flex;
  flex-wrap: wrap;
}

.compas_actual {
  background-color: red;
  color: white;
  }

.acordediv {
  font-size: large;
  margin: 1px;
  padding: 5px;
  border: 1px solid;
  border-radius: 5px;
  display: inline-block;
  color: #a9a8f6;

  margin-right: 10px;
  
}

.domi {
  color: #497aff;
}

/*
  Tonica
  color: #a9a8f6;
  Semi Dominante:
  color: blue;
  Dominante
  background-color: red;
*/
.repeticion {
  display: inline-block;
  margin: 4px;
}
</style>
