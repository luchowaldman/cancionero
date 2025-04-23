<script setup lang="ts">
import { item_lista } from '../modelo/item_lista';
import { Cancion } from '../modelo/cancion';
import { Acordes, Parte } from '../modelo/acordes';
import { EditarHelper } from '../components/comp_editar/editarHelper';
import EditAcordes from '../components/comp_editar/editAcordes.vue';
import Cabecera from '../components/comp_editar/cabecera.vue';

import { ref  } from 'vue';
import { Letra } from '../modelo/letra';
import { preProcessFile } from 'typescript';
import { Almacenado } from '../modelo/Almacenado';
import { AdminListasLocalStorage } from '../modelo/AdminListasStorage';

const props =defineProps<{ cancion: Cancion, item: item_lista }>()
const emit = defineEmits(['acciono']);


function guardar_cancioneditada() { 
    
    const almacen = new Almacenado();
    const generadorlistasLS = new AdminListasLocalStorage(almacen);
    const texto_cancion = (document.querySelector('.divEditable') as HTMLElement).innerHTML;
    props.cancion.letras.renglones =  [ texto_cancion.replace('&nbsp;', ' ').replace('<div>', '/n').replace('</div>', '').replace(/<br>/g, '/n').split('|') ] ;
    props.item.origen = "local";
    props.item.cancion = props.cancion.cancion;
    props.item.banda = props.cancion.banda;
    props.item.calidad = props.cancion.calidad;
    props.item.escala = props.cancion.escala;
    props.item.bpm = props.cancion.bpm;
    props.item.compas_cantidad = props.cancion.compas_cantidad;
    props.item.compas_unidad = props.cancion.compas_unidad;
    props.item.acordes = props.cancion.acordes.GetTodosLosAcordes().filter((acorde, index, self) => self.indexOf(acorde) === index).slice(0, 5).join(', ');
    generadorlistasLS.GuardarCancion(props.item, props.cancion);
}


function nueva_cancion() {
    props.item.banda = props.cancion.banda = "anonima";
    props.item.cancion = props.cancion.cancion = "Nueva";
    props.cancion.escala = "C";
    props.cancion.bpm = 120;
    props.cancion.compas_cantidad = 4;
    props.cancion.compas_unidad = 4;
    props.cancion.calidad = 0;
    props.cancion.acordes = new Acordes([], []);
    props.cancion.acordes.partes = [new Parte("Intro", [])];
    props.cancion.letras = new Letra([]);
    props.cancion.acordes.orden_partes = [0];
    updateContent();
    updateCancion();
    //= new Cancion("Nueva", "anonima", new Acordes([], []), );
}


  
const contentAcordes = ref("")
function updateContent() {
    const texto_cancion = (document.querySelector('.divEditable') as HTMLElement).innerHTML;
    const partes = texto_cancion.split('<div>');
    const nt = partes.map(parte => parte.replace('</div>', '')).join('<br>');
    const fondo = EditarHelper.ArmarFondoEditarAcordes(nt, props.cancion);
    contentAcordes.value = fondo;
}

function DescargarJSON() {
    const texto_cancion = (document.querySelector('.divEditable') as HTMLElement).innerHTML;
    const mi_letra =  [ texto_cancion.split('|').map(parte => parte.replace('</div>', '').replace(/<br>/g, '/n'))] ;
    const cancionJSON = JSON.stringify({
      cancion: props.cancion.cancion,
      banda: props.cancion.banda,
      acordes: {
        partes: props.cancion.acordes.partes.map(parte => ({
          nombre: parte.nombre,
          acordes: parte.acordes
        })),
        orden_partes: props.cancion.acordes.orden_partes
      },
      escala: props.cancion.escala,
      letras: mi_letra,
      bpm: props.cancion.bpm,
      calidad: props.cancion.calidad,
      compas_cantidad: props.cancion.compas_cantidad,
      compas_unidad: props.cancion.compas_unidad,
    });


    const blob = new Blob([cancionJSON], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    const nombreArchivo = `${props.cancion.banda.replace(/\s+/g, '-')}_${props.cancion.cancion.replace(/\s+/g, '-')}.json`.toLocaleLowerCase();
    a.download = nombreArchivo;
    a.click();
    URL.revokeObjectURL(url);
  }

function updateCancion() {
    
    const partes = props.cancion.letras.renglones.reduce((acc, val) => acc.concat(val), []).join('|').replace(/\/n/g, '<br>').split('<div>');
    const nt = partes.map(parte => parte.replace('</div>', '')).join('<br>');
    const fondo = EditarHelper.ArmarFondoEditarAcordes(nt, props.cancion);
    contentAcordes.value = fondo;
}


</script>
<template>
    
    <div class="contenedor-editar">
        <Cabecera  @descargar="DescargarJSON" @guardar="guardar_cancioneditada" @nuevo="nueva_cancion"  :cancion="cancion" :item="item"></Cabecera>
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
    width: 100%;
  border-radius: 5px;
  margin: 0px;
  padding: 0px;
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
