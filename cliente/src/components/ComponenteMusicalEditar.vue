<script setup lang="ts">
import { ref, watch } from 'vue';
import { Cancion } from '../modelo/cancion';
import { Musica } from '../modelo/musica';
import { item_lista } from '../modelo/item_lista';
import { text } from 'stream/consumers';

let musica = new Musica();
const props = defineProps<{ compas: number, cancion: Cancion, item_indice: item_lista, editando_cancion: boolean }>()
const emit = defineEmits(['cerrar', 'guardar']);
const letras_porparte = ref([] as string[][]);
const editando_partecombo = ref(-1);
watch(() => props.cancion, () => {
}, { deep: true });

function actualizar_letrar() {
  
  props.cancion.letras.renglones = [ ["Un"]]; 

  
}

function click_editarpartetexto(index: number) {
  editando_partecombo.value = index;
}

function textos_parte(index: number) {
  if (index == -1) {
    return ["", "", "", "/n"];
  } 
  
  let cont_acordesanteriores = 0;
  let i = 0;
  while (i < index) {
    cont_acordesanteriores += props.cancion.acordes.partes[props.cancion.acordes.orden_partes[i]].acordes.length;
    i++;
  }

  let cont = 0;
  i = 0;
  let toRet: string[] = [];
  if (props.cancion.acordes.partes[props.cancion.acordes.orden_partes[index]] == undefined) {
    return ["", "", "", "/n"];
  }
  while 
  (
    (toRet.length < props.cancion.acordes.partes[props.cancion.acordes.orden_partes[index]].acordes.length) &&
    (i < props.cancion.letras.renglones.length))  {

        for (let j = 0; j < props.cancion.letras.renglones[i].length; j++) {
          if (cont >= cont_acordesanteriores) {
            toRet.push(props.cancion.letras.renglones[i][j]);
            if (toRet.length >= props.cancion.acordes.partes[props.cancion.acordes.orden_partes[index]].acordes.length) {
              return toRet;
            }
          }
          
          cont++;
        }
        i++;
  }

  return toRet;

}


function actualizarOrdenPartes(index: number) {
    console.log(index, props.cancion.acordes.orden_partes[index])
    if (props.cancion.acordes.orden_partes[index] === -1) {
      console.log("Eliminar", index);
      props.cancion.acordes.orden_partes.splice(index, 1);
    }
    editando_partecombo.value = -1;
  }

</script>
<template>
<div v-if="editando_cancion" class="recuadro">

  <div class="navbarEdit" >
    <div class="marca">
      Editando: {{  cancion.banda }} - {{ cancion.cancion }} --Tempo: <input type="number" v-model="cancion.tempo" /> Origen: {{ item_indice.origen }} 
      <button @click="emit('guardar')">
        <i class="bi bi-save"></i> Guardar
      </button>
      -- Tipo compas  
      <input type="number" v-model="cancion.compas_cantidad" /> /
      <input type="number" v-model="cancion.compas_unidad" />

      -- Escala  
      <input type="text" v-model="cancion.escala" /> /
      

    </div>
    
    <div></div>
    
    <div class="botoneraleft">
      <button @click="guardar_cancion()" >Descargar</button>
      <button @click="emit('cerrar')">Cerrar</button>
  </div>
  </div>
    


  <div class="row">
    <div class="col-8" >
      
    <div class="recuadro overflow-auto" :style="{ 'max-height': 800 + 'px' }">
      <div  style="display: flex; flex-wrap: wrap;"  :style="{ 'font-size' : 30 + 'px'}">

      <template v-for="(parte, index) in cancion.acordes.orden_partes">
      
        <template v-for="(texto, textoid) in textos_parte(index)" v-if="parte != -1">

      
        <div >
          
          <div style="display: flex;">

            <div
              class="acorde"
              :style="{ 'max-height': 70 + 'px', 'width': (44) + 'px'  }">
              {{  cancion.acordes.partes[parte].acordes[textoid] }}
          </div>
          
          <div v-if="textoid==0  && editando_partecombo != index" @click="click_editarpartetexto(index)" >-- {{  cancion.acordes.partes[parte].nombre }}</div>
          <select v-model="cancion.acordes.orden_partes[index]" @change="actualizarOrdenPartes(index)" class="form-select"
           v-if="textoid==0 && editando_partecombo == index" >
            <option v-for="(parte, parteIndex) in cancion.acordes.partes" :key="parteIndex" :value="parteIndex">
                {{ parte.nombre }}
            </option>
            <option :value="-1">Eliminar</option>
          </select>
        </div>
          <div class="divletra">
            <b v-if="texto.trim() === ''"><i class="bi bi-music-note"></i></b>
            {{ texto.split('/n')[0] }}
          </div>
        </div>

        
        <!--
          <select v-model="cancion.acordes.orden_partes[index]" @change="actualizarOrdenPartes(index)" class="form-select"
           v-if="textoid==0">
            <option v-for="(parte, parteIndex) in cancion.acordes.partes" :key="parteIndex" :value="parteIndex">
                {{ parte.nombre }}
            </option>
            <option :value="-1">Eliminar</option>
          </select>
-->
          



        
        

        
        <div class="break" v-if="texto.includes('/n')"></div>
        <div v-if="texto.includes('/n')" >
            <div>
              <div  class="noacorde">  &nbsp; </div>
              <div class="divletra">{{ texto.split('/n')[1] }}</div>
            </div>
        </div>




      </template></template>

          


      </div>
    </div>
    
  <div>
   Total Acordes: {{ musica.total_compases(cancion) }}
  Total letra: {{ cancion.letras.renglones.flat().length }} 

</div>


  




    </div>
    <div class="col-4">

      
  <div class="row">
  QUITADO ACORDES
</div>
</div>
      
</div>

</div>
      
</template>



<style scoped>
.read-the-docs {
  color: #888;
}


.recuadro {
  border: 1px solid;
  border-radius: 5px;
  padding: 6px;
}

.pTexto {
  color: white;
  font-size: larger;
}

.resaltada {
  background-color: hsl(211, 47%, 51%);
}

.noesta_enscala {
  color: red;
}

.palabraedit {
  margin: 2px;
  height: 20px;
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


.parte {
  display: flex;
  margin: 1px;
  padding: 5px;
  border: 1px solid;
  border-radius: 5px;
}
.acorde  {
  font-size: large;
  margin: 1px;
  padding: 5px;
  border: 1px solid;
  border-radius: 5px;
  color: #a9a8f6;
  margin-right: 10px;
  
}
.ordenparte {
  border: 1px solid #888;
  width: 25%;
}

.compas_actual {
  background-color: red;
  color: white;
}


.palabraeditando {
  border: 1px solid;
  margin: 0px;
}

</style>
