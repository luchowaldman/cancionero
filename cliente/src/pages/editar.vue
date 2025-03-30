<script setup lang="ts">
import { item_lista } from '../modelo/item_lista';
import { Cancion } from '../modelo/cancion';
import { Parte } from '../modelo/acordes';
import { EditarHelper } from '../components/comp_editar/editarHelper';
import EditAcordes from '../components/comp_editar/editAcordes.vue';
import Cabecera from '../components/comp_editar/cabecera.vue';

import { ref  } from 'vue';

const props =defineProps<{ cancion: Cancion, item: item_lista }>()
const emit = defineEmits(['acciono']);

function cerro_editar() {
    localStorage.setItem("editando", "no");
}


function guardar_cancioneditada() { 
    
    
}

function agregar_a_secuencia() 
{
  props.cancion.acordes.orden_partes.push(0);
}



  function agregar_parte() {
  const nueva_parte = new Parte("Nueva Parte", []);
  props.cancion.acordes.partes.push(nueva_parte);
  
}
  
const contentAcordes = ref("")
function updateContent() {
    
    const texto_cancion = (document.querySelector('.divEditable') as HTMLElement).innerHTML;
    const partes = texto_cancion.split('<div>');
    const nt = partes.map(parte => parte.replace('</div>', '')).join('<br>');
    const fondo = EditarHelper.ArmarFondoEditarAcordes(nt, props.cancion);
    contentAcordes.value = fondo;
}

function updateCancion() {
    
    const partes = props.cancion.letras.renglones.reduce((acc, val) => acc.concat(val), []).join('|').replace(/\/n/g, '<br>').split('<div>');

    const nt = partes.map(parte => parte.replace('</div>', '')).join('<br>');
    const fondo = EditarHelper.ArmarFondoEditarAcordes(nt, props.cancion);
    contentAcordes.value = fondo;
}

function resaltar_acorde(id: number) {
    const spans = document.querySelectorAll('span');
    spans.forEach(span => {
        span.classList.remove('acorde_resaltado');
    });
    const span = document.getElementById('span_acorde-' + id.toString());
    console.log(span);
    if (span != null) {
        span.classList.add('acorde_resaltado');
    }
}   

</script>
<template>
    
    <div class="contenedor-editar">
        <Cabecera @cerrar="cerro_editar" @guardar="guardar_cancioneditada"  :cancion="cancion" :item="item"></Cabecera>
        
        
        
        <div class="row">
    <div class="col-8" style="position: relative;">
        <!-- Div editable -->
        <div class="divEditable" contenteditable="true" @input="updateContent"  v-html="props.cancion.letras.renglones.flat().join('|').replace(/\/n/g, '<br>')">
            
        </div>
        <div class="divAcordes" style="display: flex; flex-wrap: wrap" v-html="contentAcordes">
        </div>

    </div>
    <div class="col-4" >
        <EditAcordes :cancion="cancion" @actualizo_cancion="updateCancion" ></EditAcordes>
    <h2 style="text-decoration: underline; margin-bottom: 2px;"> Secuencia </h2>
    <div styactualizarOrdenPartesle="display: flex; flex-wrap: wrap;">
          <div v-for="index in cancion.acordes.orden_partes" :key="index" class="ordendiv">
            

          </div>
          <div style="border: 1px solid; padding: 2px;" @click="agregar_a_secuencia"> + </div>
            
          </div>


          
        <div> 
          
          <span  style="text-decoration: underline; font-size: xxx-large; margin-bottom: 2px;">Partes</span>
    <button @click="agregar_parte">+</button>

        </div>

    <div v-for="(parte, index_parte) in cancion.acordes.partes" :key="index_parte">
        <div  style="display: flex; flex-wrap: wrap;">
            <span>{{parte.nombre}}</span>
        </div>
        <div style="display: flex; flex-wrap: wrap;">
          <div v-for="(acorde, index) in parte.acordes" :key="index" class="acorde">
          
          
            <span @click="resaltar_acorde(3)"  >{{ acorde }}</span>
            
        </div>
        </div>
    </div> 

    </div>


</div>


    </div>

</template>

<style scoped>

.divEditable {
    min-height: 100px;
    position: absolute;
    top: 25px;
    line-height: 2.5;
    font-size: 20px;
    width: 100%;
    padding: 20px;
}
.divAcordes {
    padding: 20px;
    min-height: 100px;
    position: absolute;
    top: 0px;
    line-height: 2.5;
    font-size: 20px;
    z-index: 1;
    pointer-events: none; /* Para que los eventos de mouse pasen a través de este div */
}

.contenedor-editar {
  border-radius: 5px;
  margin: 10px;
  padding: 6px;
}
.cancion {
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
}

.acorde_resaltado {
    background-color: yellow;
    border: 1px solid;
}


</style>
