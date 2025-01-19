<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue';
import { Cancion } from '../modelo/cancion';
import { Contexto } from '../modelo/contexto';
import { Musica } from '../modelo/musica';
import { AnalisisArmonico } from '../modelo/analisis_armonico';
import Acordedit from './acordedit.vue';
import { todo } from 'node:test';

let musica = new Musica();
const props = defineProps<{ compas: number, cancion: Cancion, contexto: Contexto }>()
const mostrando_renglon = ref(-1);
const mostrando_palabra = ref(-1);
const letraDiv = ref<HTMLElement | null>(null); // Ref to the div
const scrollTop = ref(0); // Ref to store the horizontal scroll position



// Watch for changes in the compas prop
const reng_letra = ref([] as String[][]);
const reng_Acordes = ref([] as String[]);
const acord_escala = ref([] as String[]);
const analisis_armonicos = ref([] as AnalisisArmonico[]);
const cancion_enescala = ref(false);
const nota_escala = ref("");


let tiene_enters = [] as boolean[];
let len_renglon = [] as number[];


let todos_los_acordes: string[] = [];

function ConstruyeCancion(cancion: Cancion) {
  
  const secu = cancion.acordes.orden_partes;
  todos_los_acordes = [];
  // Construimos reng_Acordes
  secu.forEach(secu_val => {
    todos_los_acordes.push(...cancion.acordes.partes[secu_val].acordes);
  });
  reng_Acordes.value = todos_los_acordes;
  // Construimos reng_letra (ejemplo, puedes ajustarlo según tus necesidades)
  const nuevosRengLetra = [] as String[][];


  len_renglon = [] as number[];
  
  let falta: string = "";
  for (let i = 0; i < cancion.letra.renglones.length; i++) {
    let tieneEnter = false;
    let toAdd: string[] = cancion.letra.renglones[i];  
    if (falta != "")
    {
      toAdd[0] = falta + toAdd[0];
      falta = "";
    }

    if (toAdd.length > 0 && toAdd[toAdd.length - 1].includes('/n')) {
      const split = toAdd[toAdd.length - 1].split('/n');
      falta = split[1];
      toAdd[toAdd.length - 1] = split[0];
      tieneEnter = true;
    }
    if (toAdd.length > 0)
    {
      tiene_enters.push(tieneEnter);
      len_renglon.push(toAdd.length);
      nuevosRengLetra.push(toAdd)
    }
    

  }
  reng_letra.value = nuevosRengLetra;
}
function BuscaMusica(escala: string, cancion: Cancion) {
      console.log("BuscaMusica", escala, cancion);
      let acordes_escala = musica.GetAcordesdeescala(escala);

      let analisis_armonicosnuev: AnalisisArmonico[] = []
      cancion_enescala.value = true;
      for (var acorde in todos_los_acordes) {
        let ana = musica.getAnalisis(todos_los_acordes[acorde], acordes_escala);
        if (!ana.esta_enscala)
        {
          cancion_enescala.value = false;
        }
        analisis_armonicosnuev.push(ana);
      }

      acord_escala.value = acordes_escala;
      analisis_armonicos.value = analisis_armonicosnuev
      
}

watch(() => props.cancion, (cancion: Cancion) => {
  ConstruyeCancion(cancion);
  const nota = cancion.acordes.partes[0].acordes[0];
  nota_escala.value = nota; 
  BuscaMusica(nota, cancion);
});


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

function getAcorde(reng_texto: number, parte_texto: number) {
  let cont_part = 0;
  for (var i = 0; i < reng_texto; i++) 
  {
    cont_part += len_renglon[i];
    if (i > 0)
    {
      if (tiene_enters[i - 1]) {
        cont_part -= 1;
      }
    }
  }
  if (reng_texto > 0)
    {
      if (tiene_enters[reng_texto - 1]) {
          
        if (parte_texto == 0)
        {
          return "";
        }
        cont_part -= 1;
      }
    }
  return reng_Acordes.value[cont_part + parte_texto];

}




function getAnalisisArmonico(reng_texto: number, parte_texto: number): AnalisisArmonico {
    try {
        // Aquí iría tu lógica de análisis
        let resultado = getAnalisisArmonicoTry(reng_texto, parte_texto);
        if (resultado == undefined)
        {
          return new AnalisisArmonico(false, -1, "", "");
        }
        return resultado;
    } catch (e) {
        // Retorna un nuevo objeto AnalisisArmonico en caso de excepción
        return new AnalisisArmonico(false, -1, "", "");
    }
}


function getAnalisisArmonicoTry(reng_texto: number, parte_texto: number): AnalisisArmonico {

  let cont_part = 0;
  for (var i = 0; i < reng_texto; i++) 
  {
    cont_part += len_renglon[i];
    if (i > 0)
    {
      if (tiene_enters[i - 1]) {
        cont_part -= 1;
      }
    }
  }

  if (reng_texto > 0)
    {
      if (tiene_enters[reng_texto - 1]) {
          
        if (parte_texto == 0)
        {
          return new AnalisisArmonico(-1, false, "", "", "");
        }
        cont_part -= 1;
      }
    }
  return analisis_armonicos.value[cont_part + parte_texto];

}


function compas_activo(reng_texto: number, parte_texto: number) {
  return reng_texto + parte_texto;
}
</script>
<template>
  <div class="row">
    <div class="col-8">

    <!-- CANCION COMPLETA LETRA Y ACORDES EDIT -->
      <div class="overflow-auto" ref="letraDiv" style="max-height: 500px;">
    <div v-for="(parte, letra_parte) in reng_letra" :key="letra_parte" class="col-12">
      <div style="display: flex; flex-wrap: wrap;">
        <div v-for="(p, id_p) in parte" :key="id_p" style="margin-right: 5px; display: flex; flex-direction: column; align-items: flex-start;"
          :class="{ compas_actual: props.compas === compas_activo(letra_parte, id_p) }">
          <!-- Texto por encima del span -->
          <Acordedit :analisis="getAnalisisArmonico(letra_parte, id_p)"></Acordedit>
          <!-- Texto del span -->
          <div>{{ p }}</div>
        </div>
      </div>
    </div>
  </div>


    </div>
    <div class="col-4">
      

      
<div class="row">
  <div class="col-3" :class="{ noesta_enscala: cancion_enescala === false } ">Escala {{ nota_escala }} </div>
  <div class="col-3">Acordes de Escala {{ acord_escala }}</div>

</div>
  <div class="row">
  
  <h2>Orden</h2>
  <div class="row ">
        <div v-for="(parte, index) in cancion.acordes.orden_partes" :key="index" class="col-2 acorde">
          <span >{{ cancion.acordes.partes[parte].nombre }}</span>
        </div>
        
  </div>
  <h1>&nbsp;</h1>

  <h2>Partes</h2>
  <div v-for="(parte, index_parte) in cancion.acordes.partes" :key="index_parte" class="row" >
    
      <h3>{{ parte.nombre }}</h3>
      <div class="parte">
        <div v-for="(acorde, index) in parte.acordes" class="acorde" :key="index">
          <span  >{{ acorde }}</span>
        </div>
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


.noesta_enscala {
  color: red;
}
</style>
