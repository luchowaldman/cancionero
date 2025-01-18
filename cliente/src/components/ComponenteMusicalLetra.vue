<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue';
import { Cancion } from '../modelo/cancion';
import { Contexto } from '../modelo/contexto';

const props = defineProps<{ compas: number, cancion: Cancion, contexto: Contexto }>()

const mostrando_renglon = ref(-1);
const mostrando_palabra = ref(-1);
const letraDiv = ref<HTMLElement | null>(null); // Ref to the div
const scrollTop = ref(0); // Ref to store the horizontal scroll position

watch(() => props.compas, (newCompas: number) => {
  
  let totalCompases = 0;
  for (let i = 0; i < props.cancion.letra.renglones.length; i++) {
    let compases_x_parte = 0;
    if (props.cancion.letra.renglones[i])
      compases_x_parte = props.cancion.letra.renglones[i].length;

    if (newCompas < totalCompases + compases_x_parte) {
      mostrando_renglon.value = i;
      mostrando_palabra.value = newCompas - totalCompases;

      const conti_prev = 3;
      const mostrar_renglonen = Math.max((mostrando_renglon.value * 18) - (18 * conti_prev), 0);
      

      mover_scroll(mostrar_renglonen);
      break;
    }
    totalCompases += compases_x_parte;
  }

  if (newCompas >= totalCompases) {
    mostrando_renglon.value = -1;
    mostrando_palabra.value = -1;
  }
});

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

function mover_scroll(posX: Number) 
{
  let prevPosX = posX as number;
  letraDiv.value?.scrollTo({ top: prevPosX, behavior: 'smooth' });
}
</script>

<template>
<div class="row">
  <div>
    <div id="letra" ref="letraDiv" class="overflow-auto" style="max-height: 500px;">
      <span v-for="(palabra, index_palabra) in props.cancion.letra.renglones.flat()" 
          :key="index_palabra" 
          :class="{ compas_actual: props.compas === index_palabra }"
          v-html="palabra.replace(/\/n/g, '<br>')"></span>
    </div>
  </div>
  
</div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
