<script setup lang="ts">
import { ref, watch } from 'vue';
import { Cancion } from '../modelo/cancion';
import { Musica } from '../modelo/musica';
import { item_lista } from '../modelo/item_lista';
import { text } from 'stream/consumers';
import { Parte } from '../modelo/acordes';
import { escape } from 'querystring';

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
    return '#a9a8f6';
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
        if (!nuev_noescala.includes(acorde))
        {
        nuev_noescala.push(acorde);
        }
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

// EDICION POR ACORDES
const refiereedit_parteid = ref(0);
const mostrando_separadores = ref(false);
const editando_parte = ref(false);
const combinando_parte = ref(false);

function separar_parte(parteid: number) {
  mostrando_separadores.value = true;
  refiereedit_parteid.value = parteid
}

function editar_parte(parteid: number) {
  editando_parte.value = true;
  refiereedit_parteid.value = parteid
}
// DRAG AND DROP ACORDES
const arrastrando_acordes = ref(false);
const acorde_arrastrado = ref("");
function inicio_arrastrar(acorde: string) {
  arrastrando_acordes.value = true;
  acorde_arrastrado.value = acorde;
}


function onDragOver(event: DragEvent) {
      event.preventDefault();
      
}

function dropeo_intervalo(id: number) {
  console.log("Intervalo", acorde_arrastrado.value, id);
  if (id === -1) {
    props.cancion.acordes.partes[refiereedit_parteid.value].acordes.unshift(acorde_arrastrado.value);
  } else {
    props.cancion.acordes.partes[refiereedit_parteid.value].acordes.splice(id + 1, 0, acorde_arrastrado.value);
  }
  arrastrando_acordes.value = false;
}

function dropeo_nota(id: number) {
  console.log("Nota", acorde_arrastrado.value, id);
  arrastrando_acordes.value = false;
  props.cancion.acordes.partes[refiereedit_parteid.value].acordes[id] = acorde_arrastrado.value;
}



/// PARTES

function combinar_parte(parteid: number) {

  
    let nueva_parte_id = props.cancion.acordes.partes.length;
    let nuevaSecuencia = [];

    let buscando_secuencia = false;
    
    
    for (var i = 0; i < props.cancion.acordes.orden_partes.length; i++) 
    {
      
      if (props.cancion.acordes.orden_partes[i] == parteid) 
      {
        if (buscando_secuencia) {
            nuevaSecuencia[nuevaSecuencia.length - 1] = nueva_parte_id;
        }
        else {
          nuevaSecuencia.push(props.cancion.acordes.orden_partes[i]);
        }
      }
      else 
      {
        
        nuevaSecuencia.push(props.cancion.acordes.orden_partes[i]);
      }
      buscando_secuencia = props.cancion.acordes.orden_partes[i] == refiereedit_parteid.value;

    }
    

    const acor1 = props.cancion.acordes.partes[refiereedit_parteid.value].acordes;
    const acor2 = props.cancion.acordes.partes[parteid].acordes;
    const nombre = props.cancion.acordes.partes[refiereedit_parteid.value].nombre + " + " + props.cancion.acordes.partes[parteid].nombre; 
    let nueva_parte = new Parte(nombre, acor1.concat(acor2));
    props.cancion.acordes.partes.push(nueva_parte);

    props.cancion.acordes.orden_partes = nuevaSecuencia;

    
  mostrando_separadores.value = false;
  refiereedit_parteid.value = -1
}

function borrar_parte(parteid: number) {
  
  let nuevaSecuencia = [];
  for (var i = 0; i < props.cancion.acordes.orden_partes.length; i++) {
    if (props.cancion.acordes.orden_partes[i] != parteid) 
    {
      if (props.cancion.acordes.orden_partes[i] > parteid) {
        nuevaSecuencia.push(props.cancion.acordes.orden_partes[i] - 1);
      }
      else {
        nuevaSecuencia.push(props.cancion.acordes.orden_partes[i]);
      }
    }
  }
  props.cancion.acordes.orden_partes = nuevaSecuencia;
  forsarcompases_escala();
  props.cancion.acordes.partes.splice(parteid, 1);


}
function cancelar_parte(parteid: number) {
  combinando_parte.value = false;
  editando_parte.value = false;
  mostrando_separadores.value = false;
  refiereedit_parteid.value = -1
}
function click_barra(acordeid: number) {
  if (editando_parte.value) {
    click_combinaracorde(acordeid);
  } else if (mostrando_separadores.value) {
    click_separar(acordeid);
  }
}



function click_borraracordeparte(acordeid: number) {
  if (editando_parte.value) {
    props.cancion.acordes.partes[refiereedit_parteid.value].acordes.splice(acordeid, 1);
  }
  
  forsarcompases_escala();
}





function texto_combino_editado(parte: number, acordeid: number) {
  const texto_nuevo = [];
  let contado_renglon = 0;
  let contador_renglon_pal = 0;

  for (var i = 0; i < props.cancion.acordes.orden_partes.length; i++) 
  {
    if (props.cancion.acordes.orden_partes[i] == parte) 
    {
      let contado_palabra = 0;
      for (var j = 0; j < textos_parte(i).length; j++) 
      {
        if (contado_palabra == acordeid) 
        {
          texto_nuevo.push(textos_parte(i)[j] + ' ' + textos_parte(i)[j + 1]);
          j++;
        }
        else 
        {
          texto_nuevo.push(textos_parte(i)[j]);
        }

      }
    }
    else 
    {
      // COPIA IGUAL
      for (var j = 0; j < textos_parte(i).length; j++) {
        texto_nuevo.push(textos_parte(i)[j]);
      }
    }
  }

  props.cancion.letras.renglones = [texto_nuevo];
  editando_texto.value = false;
}

function click_combinaracorde(acordeid: number) {
  
    
  if (acordeid < props.cancion.acordes.partes[refiereedit_parteid.value].acordes.length) 
  {
    texto_combino_editado(refiereedit_parteid.value, acordeid);
    const siguienteAcorde = props.cancion.acordes.partes[refiereedit_parteid.value].acordes[acordeid + 1];
    props.cancion.acordes.partes[refiereedit_parteid.value].acordes[acordeid] += ' ' + siguienteAcorde;
    props.cancion.acordes.partes[refiereedit_parteid.value].acordes.splice(acordeid + 1, 1);
  }
  forsarcompases_escala();
  
}
function click_separar(acordeid: number) {
    
    let nueva_parte_id = props.cancion.acordes.partes.length;
    let nuevaSecuencia = [];
    let viejos_acordes = [];
    let nuevos_acordes = [];
    const acor = props.cancion.acordes.partes[refiereedit_parteid.value].acordes;
    for (var i = 0; i < acor.length; i++){
      if (i <= acordeid) {
        viejos_acordes.push(acor[i])
      }
      else {
        nuevos_acordes.push(acor[i])
      }
    }

    if (nuevos_acordes.length > 0) {
      props.cancion.acordes.partes[refiereedit_parteid.value].acordes = viejos_acordes;
      let nueva_parte = new Parte(props.cancion.acordes.partes[refiereedit_parteid.value].nombre + "BIS", nuevos_acordes);
      console.log("Nueva parte", nueva_parte);
      props.cancion.acordes.partes.push(nueva_parte);
    }

    for (var i = 0; i < props.cancion.acordes.orden_partes.length; i++) 
    {
      if (props.cancion.acordes.orden_partes[i] == refiereedit_parteid.value) {
        nuevaSecuencia.push(refiereedit_parteid.value);
        nuevaSecuencia.push(nueva_parte_id);
      }
      else {
        nuevaSecuencia.push(props.cancion.acordes.orden_partes[i]);
      }
    }
    
    props.cancion.acordes.orden_partes = nuevaSecuencia;

    
  mostrando_separadores.value = false;
  refiereedit_parteid.value = -1
}


function DescargarJSON() {
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
      letras: props.cancion.letras.renglones,
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
</script>


<template>
<div v-if="editando_cancion" class="recuadro">

  <div class="navbarEdit" >
    <div class="marca">
      <input type="text" v-model="cancion.banda" /> - <input type="text" v-model="cancion.cancion" /> --BPM: <input type="number" v-model="cancion.bpm" /> Origen: <input type="text" v-model="item_indice.origen" />
      <button @click="emit('guardar')">
        <i class="bi bi-save"></i> Guardar
      </button>
      Compas: <input type="number" v-model="cancion.compas_cantidad" /> / <input type="number" v-model="cancion.compas_unidad" /> - Escala  
      <input type="text" v-model="cancion.escala" @change="forsarcompases_escala" />
      Calidad: <input type="text" v-model="cancion.calidad" />

    </div>
    
    <div></div>
    
    <div class="botoneraleft">
      <button @click="DescargarJSON()" >Descargar</button>
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
          <button @click="editando_texto = false">Listo</button>
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
  
    


    <!-- PARTES  -->
    <!-- PARTES  -->
    <!-- PARTES  -->
    <!-- PARTES  -->
    <!-- PARTES  -->
    <!-- PARTES  -->
    <h2  style="text-decoration: underline; margin-bottom: 2px;">Acordes</h2>
    
    <div class="partediv">
          <div v-for="(acorde, index) in ref_escala" :draggable="editando_parte" 
            @dragstart="inicio_arrastrar(acorde)" 
            @dragend="arrastrando_acordes = false"
            :class="{acorde_paraarrastrar: editando_parte }" class="acordediv" :key="acorde" :style="estilo_acorde(acorde)">
            <span  >{{ acorde }}</span>
          </div>
          <div class="acordediv" :draggable="editando_parte"  
          @dragstart="inicio_arrastrar('')" 
              :style="estilo_acorde('')"   :class="{acorde_paraarrastrar: editando_parte }" >
            &nbsp;
          </div>
          <div v-for="(acorde, index) in ref_noescala" 
            @dragstart="inicio_arrastrar(acorde)" 
            :draggable="editando_parte" :class="{acorde_paraarrastrar: editando_parte }"  class="acordediv" :key="acorde" :style="estilo_acorde(acorde)">
            <span  >{{ acorde }}</span>
          </div>
          
        </div>
        
    <h2  style="text-decoration: underline; margin-bottom: 2px;">Partes</h2>
    <div v-for="(parte, index_parte) in cancion.acordes.partes" :key="parte.nombre" class="row" >
      <h2  v-if="!editando_parte || (refiereedit_parteid != index_parte)" >{{ parte.nombre }}</h2>
      <input v-model="parte.nombre" v-if="editando_parte && (refiereedit_parteid == index_parte)" />
        
      <div style="display: flex;">
        <div class="ctrlEditSecuencia" @click="editar_parte(index_parte)">Editar</div>
        <div  class="ctrlEditSecuencia" @click="separar_parte(index_parte)">Separar</div>
        <div class="ctrlEditSecuencia" v-if="(editando_parte) && (refiereedit_parteid != index_parte)"  @click="combinar_parte(index_parte)">Combinar</div>
        <div class="ctrlEditSecuencia"  @click="borrar_parte(index_parte)">Borrar</div>
        <div  class="ctrlEditSecuencia" v-if="(mostrando_separadores || editando_parte || combinando_parte) && (refiereedit_parteid == index_parte)" @click="cancelar_parte(index_parte)">Listo</div>
        </div>

        <div class="partediv">
          
          <div class="acordediv acordediv_parte" 

           v-if="( arrastrando_acordes) && refiereedit_parteid == index_parte" 
           @click="click_barra(-1)"
           :class="{divacoarrastrando_acordes: arrastrando_acordes }"
           @drop="dropeo_intervalo(-1)"
      @dragover="onDragOver($event)"
           >
            <span  > | </span>
          </div>
          <template v-for="(acorde, index) in parte.acordes" :key="index" >
          
          
            <div style="display: inline-block; border: 1px solid red; padding: 4px; "
            v-if="(editando_parte) && refiereedit_parteid == index_parte"
            @click="click_borraracordeparte(index)"  >x</div>
          
          
          
            <div class="acordediv acordediv_parte" :style="estilo_acorde(acorde)"
                        @drop="dropeo_nota(index_parte)"
                  @dragover="onDragOver($event)"
            >
            <span  >{{ acorde }}</span>
          </div>
          
          <div class="acordediv acordediv_parte" :style="estilo_acorde(acorde)"
           v-if="((mostrando_separadores) || (editando_parte)) && refiereedit_parteid == index_parte" 
            @drop="dropeo_intervalo(index)"
            @dragover="onDragOver($event)"
            @click="click_barra(index)">
            <span  > | </span>
          </div>

        </template>

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

.ctrlEditSecuencia {
  border: 1px solid;
  padding: 4px;
  margin: 3px;

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
  font-size: xx-large;
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

.acordediv_parte {
  font-size: xx-large !important;
}

.acorde_paraarrastrar {
  
}

.divacoarrastrando_acordes {
  border: 2px solid;
}
</style>
