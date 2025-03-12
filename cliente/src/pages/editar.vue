<script setup lang="ts">
import ComponenteMusicalEditar from '../components/ComponenteMusicalEditar.vue';
import Cabecera from '../components/comp_editar/cabecera.vue';
import ParteEditar from '../components/comp_editar/parteeditar.vue';
import { item_lista } from '../modelo/item_lista';
import { Cancion } from '../modelo/cancion';
import { Musica } from '../modelo/musica';
import { Parte } from '../modelo/acordes';
import { ref, nextTick  } from 'vue';

const props =defineProps<{ cancion: Cancion, item: item_lista }>()
const emit = defineEmits(['acciono']);
const musica = new Musica();

function cerro_editar() {
    localStorage.setItem("editando", "no");
}


function guardar_cancioneditada() { 
    
    
}

function agregar_a_secuencia() 
{
  props.cancion.acordes.orden_partes.push(0);
}

function actualizarOrdenPartes(index: number) {
    
    props.cancion.acordes.orden_partes = props.cancion.acordes.orden_partes.filter(parte => parte !== -1);
   
  }


  function agregar_parte() {
  const nueva_parte = new Parte("Nueva Parte", []);
  props.cancion.acordes.partes.push(nueva_parte);
  
}
  
const contentAcordes = ref("")
function updateContent(event: Event) {
    
    const texto_cancion = (event.target as HTMLElement).innerHTML;
    ActualizarFondo(texto_cancion);
}

function texto_x_acorde(texto: string, acorde: string) {

    let tore = acorde;
    const tamaño_acorde = 9.5;
    if (acorde == undefined)
        tore = '';

    let tamaño = (texto.length + 1) * tamaño_acorde
    if (tore.length * tamaño_acorde > tamaño) {
        tamaño = tore.length * tamaño_acorde;
    }
    console.log(texto, acorde, tore.length, tamaño);



    return '<span style="display: inline-block; width: ' + tamaño.toString() +'px; ">' + tore + '</span>';
    if (acorde == undefined)
        tore = '';
    while (tore.length < texto.length + 1) {
        tore += ' ';
    }
    return tore;
}

function ActualizarFondo(texto_cancion: string) {    
    let contentAcordesString = '';
    const acordes = props.cancion.acordes.GetTodosLosAcordes()
    let cont = 0;

    const partes = texto_cancion.split('|');
    partes.forEach(parte => {

        if (parte.includes('<br>')) {
            const partes_split = parte.split('<br>');
            contentAcordesString += texto_x_acorde(partes_split[0], acordes[cont]);
            contentAcordesString += '<br>';
            contentAcordesString += texto_x_acorde(partes_split[1], '');
        } else {
            contentAcordesString += texto_x_acorde(parte, acordes[cont]); 
        }
        cont++;
    });
    contentAcordes.value = contentAcordesString;

}
/*
let texto = "";
props.cancion.letras.renglones.forEach(renglon => {
    texto += renglon.map(renglon => renglon.replace('\\n','<br>')).join('|') + '|';
});
///\/
ActualizarFondo(texto);
*/
</script>
<template>
    
    <div class="contenedor-editar">
        <Cabecera @cerrar="cerro_editar" @guardar="guardar_cancioneditada"  :cancion="cancion" :item="item"></Cabecera>
        
        
        
        <div class="row">
    <div class="col-8" style="position: relative;">
        <!-- Div editable -->
        <div class="divEditable" contenteditable="true" @input="updateContent"  v-html="props.cancion.letras.renglones.flat().join('|').replace(/\/n/g, '<br>')">
            
        </div>
        <div class="divAcordes" v-html="contentAcordes">
        </div>

    </div>
    <div class="col-4" >
        
    <h2 style="text-decoration: underline; margin-bottom: 2px;"> Secuencia </h2>
    <div style="display: flex; flex-wrap: wrap;">
          <div v-for="index in cancion.acordes.orden_partes" :key="index" class="ordendiv">
            
            <select v-model="cancion.acordes.orden_partes[index]" @change="actualizarOrdenPartes(index)" class="selectParteEnOrden">
            <option v-for="(parte, parteIndex) in cancion.acordes.partes" :key="parteIndex" :value="parteIndex">
                {{ parte.nombre }}
            </option>
            <option :value="-1">Eliminar</option>
          </select>

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
          
          
            <span  >{{ acorde }}</span>
            
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
            top: 20px;
            line-height: 2.5;
            font-size: 20px;
            width: 100%;
        }
        .divAcordes {
            position: absolute;
            top: 0px;
            font-size: 20px;
            line-height: 2.5;
            z-index: 1;
            pointer-events: none; /* Para que los eventos de mouse pasen a través de este div */
            color: red;
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

.divListas {
    border: 1px solid ;
    padding: 15px;
    margin: 10px;
    border-radius: 8px;
}
</style>
