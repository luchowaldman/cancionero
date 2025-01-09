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

function modificar_nombre(index_parte: number) 
{
  const nuevoNombre = prompt("Ingrese el nuevo nombre de la parte:", props.cancion.acordes.partes[index_parte].nombre);
  if (nuevoNombre !== null && nuevoNombre.trim() !== "") {
    props.cancion.acordes.partes[index_parte].nombre = nuevoNombre.trim();
  }
  console.log("Editando nombre de parte", index_parte)
}


function agregar_compas(index_parte: number) 
{
  const nuevoNombre = prompt("Ingrese los acordes de la parte:");
  if (nuevoNombre !== null && nuevoNombre.trim() !== "") {
    props.cancion.acordes.partes[index_parte].acordes.push(nuevoNombre.trim());
  }
  console.log("Editando nombre de parte", index_parte)
}


function modificar_compas(index_parte: number, index: number) 
{
  const nuevoNombre = prompt("Ingrese los acordes de la parte:", props.cancion.acordes.partes[index_parte].acordes[index]);
  if (nuevoNombre !== null &&  nuevoNombre.trim() == "")
  {    
    props.cancion.acordes.partes[index_parte].acordes.splice(index, 1);

  }
  else if (nuevoNombre !== null && nuevoNombre.trim() !== "") {
    props.cancion.acordes.partes[index_parte].acordes[index] = nuevoNombre.trim();
  }
  console.log("Editando nombre de parte", index_parte)
}




</script>

<template>

  <div class="componente_acordes">
  
    <div v-for="(parte, index_parte) in cancion.acordes.partes" :key="parte.nombre" >
        <div>
          <span>{{ parte.nombre }}</span><button @click="modificar_nombre(index_parte)">Editar</button>
        </div>
        <div class="parte">
          
          <div v-for="(acorde, index) in parte.acordes" class="acorde" :key="acorde">
            <span  :class="{ compas_actual: ((  mostrando_compas_parte === index ) &&
                                             ( index_parte  === cancion.acordes.orden_partes[mostrando_parte]  ))
             }" @click="modificar_compas(index_parte, index)">{{ acorde }}</span>
          </div>

          <button @click="agregar_compas(index_parte)">Agregar</button>
        </div>
    </div>
  <h3>Partes</h3>
        <div class="parte">
          <div v-for="(parte, index) in cancion.acordes.orden_partes" :key="index" class="ordenparte">
            <span :class="{ compas_actual: mostrando_parte === index }" >{{ cancion.acordes.partes[parte].nombre }}</span>
          </div>
          
        </div>
</div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}

</style>
