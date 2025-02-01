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


function click_editarpartetexto(index: number) {
  editando_partecombo.value = index;
  editando_texto.value = false;
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

const ref_escala = ref([] as string[]);
const ref_noescala = ref([] as string[]);
//ref_escala.value = musica.GetAcordesdeescala(props.cancion.escala)

function forsarcompases_escala() {
  ref_escala.value = musica.GetAcordesdeescala(props.cancion.escala);
  let nuev_noescala: string[] = [];
  props.cancion.acordes.partes.forEach((parte) => {
    parte.acordes.forEach((acorde) => {
      if (!ref_escala.value.includes(acorde)) {
        nuev_noescala.push(acorde);
      }
    });
  });
  ref_noescala.value = nuev_noescala;

  
}
function estilo_acorde(acorde: string) 
{
  if (ref_escala.value.length == 0 && props.cancion.escala != "") {
    ref_escala.value = musica.GetAcordesdeescala(props.cancion.escala);

    let nuev_noescala: string[] = [];
  props.cancion.acordes.partes.forEach((parte) => {
    parte.acordes.forEach((acorde) => {
      if (!ref_escala.value.includes(acorde)) {
        if (!nuev_noescala.includes(acorde))
        { 
        nuev_noescala.push(acorde);
      }
    }
    });
  });
  ref_noescala.value = nuev_noescala;
  }

  if (!acorde.includes(' ')) {
  const find_acord = acorde.replace(/7|5/g, '');
  const index = ref_escala.value.indexOf(find_acord);
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



const editando_texto = ref(false);
const editando_parteordendid = ref(-1);
const texto_editado = ref("");

const acordes_iniciales = ref (-1 as number);
const acordes_actuales = ref (-1 as number);
const accion_completar = ref ("" as string);


function click_editartexto(parteorden: number) {
  editando_parteordendid.value = parteorden;
  editando_texto.value = true;
  let newEdit = "";
  textos_parte(parteorden).forEach((texto) => {
    newEdit  += texto.replace('/n','\n') + "|";
  });
  if (newEdit.endsWith("|")) {
    newEdit = newEdit.slice(0, -1);
  }
  texto_editado.value = newEdit;
  acordes_iniciales.value = texto_editado.value.split('|').length;
  console.log("Textos", texto_editado.value.split('|'))
}


function guardar_texto_editado() {
  const texto_nuevo = [];
  let contado_renglon = 0;
  let contador_renglon_pal = 0;

  for (var i = 0; i < props.cancion.acordes.orden_partes.length; i++) {
    if (i == editando_parteordendid.value) {
      const texto = texto_editado.value.split('|');
      for (var j = 0; j < texto.length; j++) {
        texto_nuevo.push(texto[j].replace('\n', '/n') );
      }
    }
    else {
      for (var j = 0; j < textos_parte(i).length; j++) {
        texto_nuevo.push(textos_parte(i)[j]);
      }
    }
  }

  props.cancion.letras.renglones = [texto_nuevo];
  editando_texto.value = false;

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
      <input type="text" v-model="cancion.escala" @change="forsarcompases_escala" /> /
      

    </div>
    
    <div></div>
    
    <div class="botoneraleft">
      <button @click="descargar()" >Descargar</button>
      <button @click="emit('cerrar')">Cerrar</button>
  </div>
  </div>
    


  <div class="row">
    <div class="col-8" >
      
    <div class="recuadro overflow-auto" :style="{ 'max-height': 800 + 'px' }">
      <div  style="display: flex; flex-wrap: wrap;"  :style="{ 'font-size' : 30 + 'px'}">

      <template v-for="(parte, index) in cancion.acordes.orden_partes">
      <!--- TEXT AREAAA -->
      <!--- TEXT AREAAA -->
      <!--- TEXT AREAAA -->
      <!--- TEXT AREAAA -->
      <!--- TEXT AREAAA -->
      <!--- TEXT AREAAA -->
      <div v-if="editando_texto && editando_partecombo == index" style="width: 100%;"> 
        <div style="display: flex;">
            <div class="parte_secuencia"> {{   cancion.acordes.partes[cancion.acordes.orden_partes[index]].nombre }} </div>
            <div>
              
              Acordes : <div v-for="(acorde) in cancion.acordes.partes[cancion.acordes.orden_partes[index]].acordes" class="acordediv" :key="acorde" :style="estilo_acorde(acorde)">
            <span  >{{ acorde }}</span>
          </div>
          
            </div>

            <div v-if="acordes_iniciales < texto_editado.split('|').length">Agregas compaces</div>
          <div v-if="acordes_iniciales > texto_editado.split('|').length">
            
            Quitas compaces
          </div>
          

          <button @click="guardar_texto_editado(index)">Guardar</button>
          <button @click="editando_texto = false">Cancelar</button>
        </div>
          <textarea v-model="texto_editado" :rows="texto_editado.split('\n').length" style="width: 100%;">

          </textarea>
         
        </div>
        <template v-for="(texto, textoid) in textos_parte(index)" v-if="((parte != -1) && (!editando_texto || ( editando_parteordendid != index) ))">

      
        <div >
          
          <div style="display: flex;">

            <div 
              class="acorde"
              :style="{ 'max-height': 70 + 'px', 'width': (44) + 'px'  }">
              {{  cancion.acordes.partes[parte].acordes[textoid] }}
          </div>
          
          <div v-if="textoid==0  && editando_partecombo != index" @click="click_editarpartetexto(index)" class="parte_secuencia" > {{  cancion.acordes.partes[parte].nombre }}</div>
          <select v-model="cancion.acordes.orden_partes[index]" @change="actualizarOrdenPartes(index)" class="selectParteEnOrden"
           v-if="textoid==0 && editando_partecombo == index" >
            <option v-for="(parte, parteIndex) in cancion.acordes.partes" :key="parteIndex" :value="parteIndex">
                {{ parte.nombre }}
            </option>
            <option :value="-1">Eliminar</option>
          </select>
          <button v-if="textoid == 0 && editando_partecombo == index" @click="click_editartexto(index)">
            <i class="bi bi-pencil"></i>
          </button>
        </div>
          <div class="divletra">
            <b v-if="texto.trim() === ''"><i class="bi bi-music-note"></i></b>
            {{ texto.split('/n')[0] }}
          </div>
        </div>
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
  
    


    
    <h2  style="text-decoration: underline; margin-bottom: 2px;">Acordes</h2>
    
    <div class="partediv">
          <div v-for="(acorde, index) in ref_escala" class="acordediv" :key="acorde" :style="estilo_acorde(acorde)">
            <span  >{{ acorde }}</span>
          </div>
          <div class="acordediv"  :style="estilo_acorde('')">
            &nbsp;
          </div>
          <div v-for="(acorde, index) in ref_noescala" class="acordediv" :key="acorde" :style="estilo_acorde(acorde)">
            <span  >{{ acorde }}</span>
          </div>
          
        </div>
        
    <h2  style="text-decoration: underline; margin-bottom: 2px;">Partes</h2>
    <div v-for="(parte, index_parte) in cancion.acordes.partes" :key="parte.nombre" class="row" >
      <div style="display: flex;">
        <div class="parte_secuencia" >{{ parte.nombre }}</div>
        <div>Editar</div>
        </div>
        <div class="partediv">
          <div v-for="(acorde, index) in parte.acordes" class="acordediv" :key="acorde" :style="estilo_acorde(acorde)">
            <span  >{{ acorde }}</span>
          </div>
        </div>
    </div>
    <h2 style="text-decoration: underline; margin-bottom: 2px;"> Secuencia </h2>
    <div style="display: flex; flex-wrap: wrap;">
          <div v-for="(parte, index) in cancion.acordes.orden_partes" :key="index" class="ordendiv">
            
            <select v-model="cancion.acordes.orden_partes[index]" @change="actualizarOrdenPartes(index)" class="selectParteEnOrden">
            <option v-for="(parte, parteIndex) in cancion.acordes.partes" :key="parteIndex" :value="parteIndex">
                {{ parte.nombre }}
            </option>
            <option :value="-1">Eliminar</option>
          </select>

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

.parte_secuencia {
  font-size: large;
  margin: 1px;
  padding: 5px;
  border: 1px solid;
  border-radius: 5px;
  color: #30a0d3;
  margin-right: 10px;
  
}
.ordenparte {
  border: 1px solid #888;
  width: 25%;
}

textarea, input, select {
  color: #a9a8f6;
  background-color: black;
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
