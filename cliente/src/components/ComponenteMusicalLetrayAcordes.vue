<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue';
import { Cancion } from '../modelo/cancion';
import { Contexto } from '../modelo/contexto';
import { VistaControl } from '../modelo/vista_control';
import { Musica } from '../modelo/musica';
const props = defineProps<{ compas: number, cancion: Cancion, vista: VistaControl }>()
const scrollTop = ref(0); // Ref to store the horizontal scroll position

const letraDiv = ref<HTMLElement | null>(null); // Ref to the div

const mostrando_parte = ref(-1)
const mostrando_compas_parte = ref(-1)
const currentCompas = ref(0);
const letras = ref([] as string[][]);
const musica = new Musica();

watch(() => props.cancion, (cancion: Cancion) => {
  actualizarLetras(cancion);
});

function actualizarLetras(cancion: Cancion) {
  let contador_renglon_texto = 0;
  let contador_renglon_parte_texto = 0;
  let nueva_letra = [] as string[][];
  for (var i = 0; i < cancion.acordes.orden_partes.length; i++) {
    let nuevo_renglon = [] as string[];
    
    for (var j = 0; j < cancion.acordes.partes[cancion.acordes.orden_partes[i]].acordes.length; j++) 
    {

      nuevo_renglon.push(cancion.letras.renglones[contador_renglon_texto][contador_renglon_parte_texto]);
      contador_renglon_parte_texto++;
      if (contador_renglon_parte_texto >= cancion.letras.renglones[contador_renglon_texto].length) {
        contador_renglon_texto++;
        contador_renglon_parte_texto = 0;
      }
    } 
    nueva_letra.push(nuevo_renglon);
  }
  letras.value = nueva_letra;
}

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

  const ve = (musica.get_renglontexto_de_compas(props.cancion ,newCompas) * 53) - 150;
  const nueva_pos = Math.max(ve, 0);
  mover_scroll(nueva_pos)
      
  console.log('Compas actual', currentCompas.value);
});


function mover_scroll(posX: number) 
{
  
  letraDiv.value?.scrollTo({ top: posX, behavior: 'smooth' });
}


function Actualizar() {
  if (letras.value.length === 0) {
    console.log('actualizar letras');
 //   actualizarLetras(props.cancion);
  }
  return false;

}
// Función para manejar el evento de scroll
const handleScroll = () => {
  
  if (letraDiv.value) {
    console.log('Scrolling', letraDiv.value.scrollTop);
    scrollTop.value = letraDiv.value.scrollTop; // Actualiza la posición del scroll
  }
};
// Añadir el evento de scroll cuando se monta el componente
onMounted(() => {
  if (letraDiv.value) {
    letraDiv.value.addEventListener('scroll', handleScroll);
  }
});

// Eliminar el evento de scroll cuando se desmonta el componente
onUnmounted(() => {
  if (letraDiv.value) {
    letraDiv.value.removeEventListener('scroll', handleScroll);
  }
});

defineExpose({  Actualizar });

</script>
<template>
  <div class="componenteMusical">
    
    <div ref="letraDiv"   class="overflow-auto" :style="{ 'max-height': vista.alto + 'px' }"> 
    <div style="display: flex; flex-wrap: wrap;"  :style="{ 'font-size' : vista.tamanio_referencia + 'px'}">
      <template v-for="(parte, index) in cancion.acordes.orden_partes" :key="index" class="parte">
        
        <template  v-for="(aco, index_aco) in cancion.acordes.partes[parte].acordes" :key="index_aco">
                <div v-if="!letras[index][index_aco].includes('/n')" :class="{ en_compas: mostrando_parte === index && mostrando_compas_parte === index_aco }">
                  <div><div  class="acordediv"> {{ aco }}</div></div>
                  <div class="divletra" >{{ letras[index][index_aco] }}&nbsp;</div>
                </div>
                <div v-if="letras[index][index_aco].includes('/n')" :class="{ en_compas: mostrando_parte === index && mostrando_compas_parte === index_aco }">
                  <div><div  class="acordediv"> {{ aco }}</div></div>
                  <div class="divletra">{{ letras[index][index_aco].split('/n')[0] }}</div>
                </div>
                <div class="break" v-if="letras[index][index_aco].includes('/n')"></div>
                <div v-if="letras[index][index_aco].includes('/n')" :class="{ en_compas: mostrando_parte === index && mostrando_compas_parte === index_aco }">
                  <div><div  class="noacorde">  &nbsp; </div></div>
                  <div class="divletra">{{ letras[index][index_aco].split('/n')[1] }}</div>
                </div>
                
        </template>
      </template>
    </div>
  </div>
</div>
</template>



<style scoped>
.componenteMusical {
  border: 1px solid;
  border-radius: 5px;
  color: white;
  padding: 6px;
}
.read-the-docs {
  color: #888;
}

.break {
    flex-basis: 100%;
  }
.parte {
  display: flex;
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


.noacorde {
  margin: 1px;
  padding: 6px;
  font-size: large;
  
}

.ordenparte {
  border: 1px solid #888;
  width: 25%;
}

.en_compas .acordediv {
  background-color: #00FF00;
  color: white;
}

.en_compas .acordediv {
  background-color: red;
  color: white;
}
.en_compas .divletra  {
  color: red;
}
</style>
