<script setup lang="ts">
import { ref } from 'vue';
import { Cancion } from '../modelo/cancion';
import { Musica } from '../modelo/musica';
import { item_lista } from '../modelo/item_lista';

let musica = new Musica();
const props = defineProps<{ compas: number, cancion: Cancion, item_indice: item_lista, editando_cancion: boolean }>()
const texto_toadd = ref("");
const texto_toadd_calculo = ref([] as string[][]);
const emit = defineEmits(['cerrar', 'guardar']);
function click_calcular_textotoadd() {
  const nue_reng = texto_toadd.value.split("\n");
  texto_toadd_calculo.value = nue_reng.map((reng) => {
    return reng.split("|");
  });
}

function click_ponerletraparaedit() {
  click_calcular_textotoadd();
  props.cancion.letras.renglones = texto_toadd_calculo.value;
}

function click_cargarletraparaedit() {
  texto_toadd.value = props.cancion.letras.renglones.map((renglon) => {
    return renglon.join("|");
  }).join("\n");
}

function click_agregartextocalculado() {
  
texto_toadd_calculo.value.forEach((renglon) => {
  props.cancion.letras.renglones.push(renglon);
});
}


function cerrar_edicion() {
  emit('cerrar');
}


const editando_renglon = ref(-1);
const editando_parte = ref(-1);

function editarPalabra(renglonIndex: number, palabraIndex: number) {
  console.log("editarPalabra", renglonIndex, palabraIndex, props.cancion.letras.renglones[renglonIndex][palabraIndex]);
  editando_renglon.value = renglonIndex;
  editando_parte.value = palabraIndex;
}

function reset_editPalabra() {
  editando_renglon.value = -1;
  editando_parte.value = -1;

}

function guardarPalabra(renglonIndex: number, palabraIndex: number) {
  console.log("guardarPalabra", renglonIndex, palabraIndex, props.cancion.letras.renglones[renglonIndex][palabraIndex]);
  editando_renglon.value = -1;
  editando_parte.value = -1;

}

function borrar(renglonIndex: number, palabraIndex: number) {
  console.log("borrar", renglonIndex, palabraIndex, props.cancion.letras.renglones[renglonIndex][palabraIndex]);
  props.cancion.letras.renglones[renglonIndex].splice(palabraIndex, 1);
}

  function guardar_cancion() {
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
      letras: props.cancion.letras.renglones,
      tempo: props.cancion.tempo
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
  const mostrando_compas_parte = ref(0);
  const mostrando_parte = ref(0);
  const editando_compas = ref(-1);

  function agregarAcorde(index_parte: number) {
    props.cancion.acordes.partes[index_parte].acordes.push('');
  }

  function eliminarAcorde(index_parte: number, index_acorde: number) {
    props.cancion.acordes.partes[index_parte].acordes.splice(index_acorde, 1);
  }

  function agregarParte() {
    props.cancion.acordes.partes.push({ nombre: 'Nueva Parte', acordes: [] });
  }

  function eliminarParte(index_parte: number) {
    props.cancion.acordes.partes.splice(index_parte, 1);
  }

  function editarAcorde(index_parte: number, index_acorde: number) {
    editando_compas.value = index_acorde;
    editando_parte.value = index_parte;
  }

  function guardarAcorde() {
    editando_compas.value = -1;
    editando_parte.value = -1;
  }

  function actualizarOrdenPartes(index: number) {
    console.log(index, props.cancion.acordes.orden_partes[index])
    if (props.cancion.acordes.orden_partes[index] === -1) {
      console.log("Eliminar", index);
      props.cancion.acordes.orden_partes.splice(index, 1);

    }
  }

  function agregarOrdenParte() {
    props.cancion.acordes.orden_partes.push(0);
  }

  function agregarPalabra(renglonIndex: number, palabraIndex: number) {
    props.cancion.letras.renglones[renglonIndex].splice(palabraIndex + 1, 0, '');
  }

  function click_enter(renglonIndex: number, palabraIndex: number) {
    reset_editPalabra();

    const palabrasRestantes = props.cancion.letras.renglones[renglonIndex].splice(palabraIndex + 1);
    props.cancion.letras.renglones.splice(renglonIndex + 1, 0, palabrasRestantes);
  }

  function agregarRenglon(renglonIndex: number) {
    reset_editPalabra();
    props.cancion.letras.renglones.splice(renglonIndex + 1, 0, ['']);
  }

  function borrarRenglon(renglonIndex: number) {
    props.cancion.letras.renglones.splice(renglonIndex, 1);
  }

  const renglonCopiado = ref<string[] | null>(null);

  function copiarRenglon(renglonIndex: number) {
    renglonCopiado.value = [...props.cancion.letras.renglones[renglonIndex]];
  }

  function pegarRenglon(renglonIndex: number) {
    if (renglonCopiado.value) {
      props.cancion.letras.renglones[renglonIndex] = [...renglonCopiado.value];
      
    }
  }


  const renglonesResaltadas = ref<string[][]>([]);
  renglonesResaltadas.value = [];

  function ver_parte_deorden(index: number) {
    
    
    let nRenglones: string[][] = [[]];
    let contador_renglon_texto = 0;
    let contador_renglon_parte_texto = 0;
    try {
      for (var i = 0; i < props.cancion.acordes.orden_partes.length; i++) {
      for (var j = 0; j < props.cancion.acordes.partes[props.cancion.acordes.orden_partes[i]].acordes.length; j++) {
        if (index == i) {
        if (nRenglones[contador_renglon_texto] == undefined) {
          nRenglones[contador_renglon_texto] = [];
        }
        nRenglones[contador_renglon_texto][contador_renglon_parte_texto] = "r";
        }

        contador_renglon_parte_texto++;
        if (contador_renglon_parte_texto >= props.cancion.letras.renglones[contador_renglon_texto].length) {
        contador_renglon_texto++;
        contador_renglon_parte_texto = 0;
        }
      }
      }
    } catch (error) {
      console.error("Error processing the song parts:", error);
    }





    renglonesResaltadas.value = nRenglones;


    
  }
  

</script>
<template>
<div v-if="editando_cancion">

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
      <button @click="cerrar_edicion()">Cerrar</button>
  </div>
  </div>
    


  <div class="row">
    <div class="col-8" >
      
      <div >
      <div v-for="(renglon, renglonIndex) in cancion.letras.renglones" :key="renglonIndex" style="display: flex;">
        <div v-for="(palabra, palabraIndex) in renglon" :key="palabraIndex" 
        :class="{ 'resaltada': renglonesResaltadas[renglonIndex] != undefined && renglonesResaltadas[renglonIndex][palabraIndex] == 'r' }" class="palabraedit">
          
        <div @click="editarPalabra(renglonIndex, palabraIndex)" v-if="renglonIndex != editando_renglon || palabraIndex != editando_parte"  >
          <p v-if="palabra!=''">{{ palabra }}</p>
          
          <p v-if="palabra==''">
          <i class="bi bi-music-note"></i>
          </p>
        </div>
        <div v-if="renglonIndex == editando_renglon && palabraIndex == editando_parte">
          <input  v-model="cancion.letras.renglones[renglonIndex][palabraIndex]" @blur="guardarPalabra(renglonIndex, palabraIndex)" />
          <button @click="borrar(renglonIndex, palabraIndex)">
          <i class="bi bi-trash"></i>
          </button>
          <button @click="agregarPalabra(renglonIndex, palabraIndex)">
          <i class="bi bi-plus"></i>
          </button>
          <button @click="click_enter(renglonIndex, palabraIndex)">
            <i class="bi bi-arrow-return-left"></i>
          </button>
        </div> 
        </div>
        <div>
        <button @click="agregarRenglon(renglonIndex)">
          <i class="bi bi-plus"></i> <i class="bi bi-arrow-return-left"></i>
        </button>
        <button @click="borrarRenglon(renglonIndex)">
          <i class="bi bi-trash"></i> <i class="bi bi-arrow-return-left"></i>
        </button>
        <button @click="copiarRenglon(renglonIndex)">
          <i class="bi bi-clipboard"></i> 
        </button>
        <button @click="pegarRenglon(renglonIndex)">
          <i class="bi bi-clipboard-check"></i> 
        </button>
        </div>
      </div>
      </div>

      
  <div @click="reset_editPalabra">
   Total Acordes: {{ musica.total_compases(cancion) }}
  Total letra: {{ cancion.letras.renglones.flat().length }} 

</div>


      
<div @click="reset_editPalabra">
  
<div class="row">
  <div class="col-9">

    <button @click="click_calcular_textotoadd">Calcular</button>
    <button @click="click_agregartextocalculado">Agregar</button>
    <button @click="click_cargarletraparaedit">Cargar</button>
    <button @click="click_ponerletraparaedit">Ponen nueva letra</button>

  </div>
</div>
<div class="row">
  <div class="col-9">
  <textarea v-model="texto_toadd" style="width: 100%; height: 280px;"></textarea>
</div>
<div class="col-3">
   {{ texto_toadd_calculo }}
</div>
</div>
  

</div>




    </div>
    <div class="col-4">

      
  <div class="row">
  
  <h2>Partes</h2>
  <div v-for="(parte, index_parte) in cancion.acordes.partes" :key="parte.nombre" class="row">
    <input type="text" v-model="parte.nombre" />
    
    <div class="parte">
      <div v-for="(acorde, index) in parte.acordes" class="acorde" :key="acorde">
        <div v-if="editando_parte === index_parte && editando_compas === index">
          <input type="text" v-model="parte.acordes[index]" @blur="guardarAcorde()" />
          <button @click="eliminarAcorde(index_parte, index)" class="btn btn-danger btn-sm">
            <i class="bi bi-trash"></i>
          </button>
        </div>
        <div v-else :class="{ compas_actual: ((mostrando_compas_parte === index) && (index_parte === cancion.acordes.orden_partes[mostrando_parte])) }" @click="editarAcorde(index_parte, index)">
            <span>
            <span v-if="acorde">{{ acorde }}</span>
            <i v-else class="bi bi-music-note"></i>
            </span>
        </div>
      </div>
      <div>
      <button @click="agregarAcorde(index_parte)" class="btn btn-primary btn-sm">
        <i class="bi bi-plus"></i>
      </button>
    </div>
    </div>
    <div>
    <button @click="eliminarParte(index_parte)" class="btn btn-danger btn-sm">
      <i class="bi bi-trash"></i>
    </button>
  </div>
  </div>
  <div>
  <button @click="agregarParte" class="btn btn-primary btn-sm">
    <i class="bi bi-plus"></i>
  </button>
</div>
  <h1>&nbsp;</h1>
  <h2>Orden</h2>
<div style="display: flex; flex-wrap: wrap;">
  <div v-for="(index) in cancion.acordes.orden_partes" :key="index" class="col-2 acorde">
    <select v-model="cancion.acordes.orden_partes[index]" @change="actualizarOrdenPartes(index)" class="form-select">
      <option v-for="(parte, parteIndex) in cancion.acordes.partes" :key="parteIndex" :value="parteIndex">
        {{ parte.nombre }}
      </option>
      <option :value="-1">Eliminar</option>
    </select>
    <button @click="ver_parte_deorden(index)" class="btn btn-info btn-sm">
      <i class="bi bi-eye"></i>
    </button>
  </div>
  <button @click="agregarOrdenParte" class="btn btn-primary btn-sm">
    <i class="bi bi-plus"></i> Agregar Parte al Orden
  </button>
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

.palabraeditando {
  border: 1px solid;
  margin: 0px;
}

</style>
