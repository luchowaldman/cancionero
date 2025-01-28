<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue';
import { Cancion } from '../modelo/cancion';
import { Musica } from '../modelo/musica';
import { AnalisisArmonico } from '../modelo/analisis_armonico';
import Acordedit from './acordedit.vue';

let musica = new Musica();
const props = defineProps<{ compas: number, cancion: Cancion, editando_cancion: boolean }>()

const emit = defineEmits(['cerrar']);
const mostrando_renglon = ref(-1);
const mostrando_palabra = ref(-1);
const letraDiv = ref<HTMLElement | null>(null); // Ref to the div
const scrollTop = ref(0); // Ref to store the horizontal scroll position
const toc_cancion = ref(props.cancion)
const letras = ref([] as string[][]);


// Watch for changes in the compas prop
const reng_letra = ref([] as String[][]);
const reng_Acordes = ref([] as String[]);
const acord_escala = ref([] as String[]);
const analisis_armonicos = ref([] as AnalisisArmonico[]);
const cancion_enescala = ref(false);
const nota_escala = ref("");

const mostrando_parte = ref(-1)
const mostrando_compas_parte = ref(-1)

const currentCompas = ref(0);
let tiene_enters = [] as boolean[];
let len_renglon = [] as number[];


let todos_los_acordes: string[] = [];

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

watch(() => props.cancion, (micancion: Cancion) => {
  toc_cancion.value = micancion;
  reload_song();
  
  actualizarLetras(micancion);
});


function actualizarLetras(cancion: Cancion) {
  let contador_renglon_texto = 0;
  let contador_renglon_parte_texto = 0;
  let nueva_letra = [] as string[][];
  for (var i = 0; i < cancion.acordes.orden_partes.length; i++) {
    let nuevo_renglon = [] as string[];
    
    for (var j = 0; j < cancion.acordes.partes[cancion.acordes.orden_partes[i]].acordes.length; j++) 
    {

      nuevo_renglon.push(cancion.letra.renglones[contador_renglon_texto][contador_renglon_parte_texto]);
      
      contador_renglon_parte_texto++;
      if (contador_renglon_parte_texto >= cancion.letra.renglones[contador_renglon_texto].length) {
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

function reload_song() {
  try {

    const nota = toc_cancion.value.acordes.partes[0].acordes[0];
    nota_escala.value = nota; 
    BuscaMusica(nota, toc_cancion.value);
  } catch (error) {
    console.error("Error al procesar la canción:", error);
  }
}

function cerrar_edicion() {
  emit('cerrar');
}

defineExpose({  reload_song });
</script>
<template>
<div v-if="editando_cancion">

  <div class="navbarEdit" >
    <div class="marca">
      Editando
    </div>
    
    
    
    <div class="botoneraleft">
      <button @click="reload_song()">Guardar</button>
      <button @click="cerrar_edicion()">Cerrar</button>
  </div>
  </div>
    



  <div class="row">
    <div class="col-6">
    <div style="display: flex; flex-wrap: wrap;">
      <template v-for="(parte, index) in cancion.acordes.orden_partes" :key="index" class="parte">
        
        <template  v-for="(aco, index_aco) in cancion.acordes.partes[parte].acordes" :key="index_aco">
                <div v-if="!letras[index][index_aco].includes('/n')" :class="{ compas_actual: mostrando_parte === index && mostrando_compas_parte === index_aco }">
                  <div>{{ aco }}</div>
                  <div>{{ letras[index][index_aco] }}</div>
                </div>
                <div v-if="letras[index][index_aco].includes('/n')" :class="{ compas_actual: mostrando_parte === index && mostrando_compas_parte === index_aco }">
                  <div>{{ aco }}</div>
                  <div>{{ letras[index][index_aco].split('/n')[0] }}</div>
                </div>
                <div class="break" v-if="letras[index][index_aco].includes('/n')"></div>
                <div v-if="letras[index][index_aco].includes('/n')" :class="{ compas_actual: mostrando_parte === index && mostrando_compas_parte === index_aco }">
                  <div>&nbsp;</div>
                  <div>{{ letras[index][index_aco].split('/n')[1] }}</div>
                </div>
                
        </template>
      </template>
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

      
</div>

</template>



<style scoped>
.read-the-docs {
  color: #888;
}


.noesta_enscala {
  color: red;
}


.botoneraleft {
  margin-left: auto
}

.navbarEdit {
  display: flex;
  border: 1px solid;
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
