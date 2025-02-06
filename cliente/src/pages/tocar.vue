<script setup lang="ts">

import { Cancion } from '../modelo/cancion';
import { VistaControl } from '../modelo/vista_control';
import { onMounted, ref } from 'vue';


defineProps<{ compas: number, cancion: Cancion }>()


const vist: VistaControl[] = [
];
const ref_vista = ref(vist);
const ref_cont = ref(0);

function cambiar_vista(vista: number) {
  localStorage.setItem('viendo_vista', vista.toString());
  let toCH: VistaControl[] = [];
  const ancho = window.innerWidth;
  const alto = window.innerHeight;
  
  if (ancho > 1500) {
    const alto_controles = alto - 250;
  const paraPC = [
    [
      new VistaControl(alto / 40, 12, 7, "letra_acordes", "col-9", alto_controles),
      new VistaControl(alto / 20, 12, 7, "acordes", "col-3 d-md-block", alto_controles)
    ],
    [
      new VistaControl(ancho / 50, 12, 7, "letra", "col-12", alto_controles),
    ],
    [
      new VistaControl(ancho / 50, 12, 7, "acordes_seguidos", "col-9", alto_controles),
      new VistaControl(ancho / 30, 12, 7, "acordes", "col-3 d-md-block", alto_controles)
    ],
    [
      new VistaControl(ancho / 50, 12, 7, "detalle", "col-9", alto_controles)
    ],
    [
      new VistaControl(ancho / 50, 12, 7, "detalle", "col-9", alto_controles)
    ],
    [
      new VistaControl(ancho / 50, 12, 7, "tocar", "col-9", alto_controles),
      new VistaControl(ancho / 30, 12, 7, "acordes", "col-3 d-md-block", alto_controles)
    ]
  ];
  toCH = paraPC[vista];

} else {
  
  const alto_controles = alto - 360;
  const paraPC = [
    [
      new VistaControl(alto / 40, 12, 7, "letra_acordes", "col-10  d-md-block", alto_controles),
      new VistaControl(alto / 35, 12, 7, "acordes", "col-2 d-md-block", alto_controles)
    ],
    [
      new VistaControl(ancho / 20, 12, 7, "letra", "col-12", alto_controles),
    ],
    [
      new VistaControl(ancho / 50, 12, 7, "acordes_seguidos", "col-9", alto_controles),
      new VistaControl(ancho / 30, 12, 7, "acordes", "col-3 d-md-block", alto_controles)
    ],
    [
      new VistaControl(ancho / 50, 12, 7, "detalle", "col-9", alto_controles)
    ],
    [
      new VistaControl(ancho / 50, 12, 7, "detalle", "col-9", alto_controles)
    ],
    [
      new VistaControl(ancho / 50, 12, 7, "tocar", "col-9", alto_controles),
      new VistaControl(ancho / 30, 12, 7, "acordes", "col-3 d-md-block", alto_controles)
    ]
  ];
  toCH = paraPC[vista];

}
  ref_vista.value = toCH;
  ref_cont.value = ref_cont.value + 1;
}

const viendo_vista = parseInt(localStorage.getItem('viendo_vista') || '0');
cambiar_vista(viendo_vista);

// ENTORNO
const width = ref(window.innerWidth); 
const height = ref(window.innerHeight);
const updateDimensions = () => { width.value = window.innerWidth; height.value = window.innerHeight; };

onMounted(() => {
  
  console.log("TOCAR MONTADA")
  
  window.addEventListener('resize', updateDimensions);
})

</script>

<template>
  
  <div :style="{ width: width > 1500 ? '100%' : '120%' }">
    <div style="display: flex ;float: right;;">


      <div class="dropdown" >
    <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
      <i class="bi bi-eye"></i>
    </button>
    <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
      <li v-on:click="cambiar_vista(0)"><a class="dropdown-item" href="#">Todos</a></li>
      <li v-on:click="cambiar_vista(1)"><a class="dropdown-item" href="#">Cantante</a></li>
      <li v-on:click="cambiar_vista(2)"><a class="dropdown-item" href="#">Guitarrista</a></li>
      <li v-on:click="cambiar_vista(3)"><a class="dropdown-item" href="#">Pianista</a></li>
      <li v-on:click="cambiar_vista(4)"><a class="dropdown-item" href="#">Solo detalles</a></li>
      <li v-on:click="cambiar_vista(5)"><a class="dropdown-item" href="#">Tocar</a></li>
    </ul>
  </div>

    </div>
  <div class="row" :style="{height: height * 0.9 + 'px'}">
      <div v-for="(Componente, index) in ref_vista" :key="index" 
      :class="Componente.clase">
        <component :is="Componente.getMarkRaw()" :compas="compas" :key="index" :ref="Componente.componente" :vista="Componente" :cancion="cancion" val="ref_cont"></component>
      </div>
  </div>


  <p>Anchura: {{ width }} px - Altura: {{ height }} px</p>
  

 </div>

</template>

<style scoped>
.pantalla {
    margin-top: 10px;
    margin-left: 10px;
    margin-right: 10px;
    margin-bottom: 10px;
    padding: 10px;
    border: 1px solid black;
    border-radius: 10px;
    height: 100%;
    width: 100%;
}
</style>
