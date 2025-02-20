<script setup lang="ts">

import { Cancion } from '../modelo/cancion';
import ControladorTiempo from './ControladorTiempo.vue';
import ControladorSesion from './ControladorSesion.vue';
import Metronomo from './metronomo.vue';
import { EstadoSesion } from '../modelo/estadosesion';
import { ref } from 'vue';




const emit = defineEmits(['acciono']);
const ctrlSesion = ref();
const ViendoDetalle = ref(false);

function acciono(valor: string, compas: number = 0) {
    //console.log("Acciono--->", valor, compas);
    emit('acciono', valor, compas);
    
}
const props = defineProps<{ viendo_vista: string, compas: number, cancion: Cancion
  ,  nro_cancion: number, total_canciones: number, sesion: EstadoSesion }>()


  function actualizar_vista() {
    ctrlSesion?.value.actualizar_vista();
  }

  defineExpose ({ actualizar_vista  });



</script>

<template>
  <div class="navbarFogon">
    
    
    <div class="pagina_seleccionable" :class="{active: viendo_vista == 'tocar'}" >
        <p class="clase_tocar" @click="acciono('tocar')"   :class="{active: viendo_vista == 'tocar'}" aria-current="page">
          
          <i class="bi bi-fire ilogo">

            
          </i>
          

        </p>	
      </div>
        <div class="ctrl_menu">
          <ControladorTiempo :nro_cancion="nro_cancion" :total_canciones="total_canciones"  :compas=compas :cancion="cancion"
          :viendo_vista="viendo_vista"
          @play="acciono('play')" @pause="acciono('pause')" @stop="acciono('stop')" @next="acciono('next')" @previous="acciono('previous')"
            @update-compas="(valor) => acciono('update-compas', valor)">
        </ControladorTiempo> 
      </div>

      
      <Metronomo v-if="viendo_vista=='tocar'" ref="metronomeRef" :cancion="cancion"></Metronomo>

       
      <div class="otras_paginas">
    
      <div class="otra_paginas" @click="acciono('listas')"  :class="{active: viendo_vista == 'conectar'}" >
        
          
        <ControladorSesion :sesion="sesion"
        @desconectar="acciono('desconectar')"
          
          @conectar="acciono('conectar')">
        </ControladorSesion>
      </div>

        <div class="otra_paginas" @click="acciono('listas')"  :class="{active: viendo_vista == 'listas'}" v-if="ViendoDetalle">
        
          <i class="bi bi-list"></i>
        
      </div>    
      


      <div class="otra_paginas" @click="acciono('editar')"  :class="{active: viendo_vista == 'editar'}" v-if="ViendoDetalle">
        
            <i class="bi bi-pencil"></i>
        
      </div> 
      <div class="otra_paginas" @click="acciono('buscar')"  :class="{active: viendo_vista == 'buscar'}" v-if="ViendoDetalle">
        
            <i class="bi bi-globe"></i>
        
      </div>    
      
          
          <div class="otra_paginas" @click="acciono('config')" :class="{active: viendo_vista == 'config'}" v-if="ViendoDetalle">
              <i class="bi bi-gear-fill"></i>
          </div>
          <div class="otra_paginas" @click="ViendoDetalle = !ViendoDetalle"  v-if="ViendoDetalle" >
              <i class="bi bi-dash"></i>
          </div>

          <div class="otra_paginas"  @click="ViendoDetalle = !ViendoDetalle"  v-if="!ViendoDetalle" >
              <i class="bi bi-plus"></i>
          </div>

        </div>

        
    </div>
</template>

<style scoped>

.otras_paginas {
  font-size: 30px ;
  display: flex;
  border: 1px solid;
  margin: 10px 10px 15px 10px;
  right: 0 auto;
  border-radius: 20px;
  color: #a9a8f6;
  height: 44%;
  margin-left: auto
}


.otra_paginas {
  margin-left: auto;
  border: 1px solid;
  margin: 5px 10px 5px 10px;
  border-radius: 20px;
  color: #a9a8f6;
}

.navbarFogon {
  display: flex;
  border: 1px solid;
  margin: 5px 10px 5px 10px;
  border-radius: 20px;
  color: #a9a8f6;
}

.ctrl_menu {
  margin: 4px;
  padding: 10px 0px 10px 10px;
  border-radius: 20px;
  border: 1px solid;

}

.pagina_seleccionable {
  display: flex;
  border: 1px solid transparent;
  margin: 10px 0px 10px 10px;
}

.pagina_seleccionable:hover {
  border-color: black;
}

.active {
  color: red;
}

.ilogo {
  margin: 14px;
  padding-right: 12px;
  font-size: 70px;
  border: 1px solid #a9a8f6 ;
  border-radius: 40px;

}

.aladerecha {
  margin-left: auto
}

.navbar {
  background-color: #FFF;
  padding: 10px;
}

.navbar-brand {
  color: #8B4513; /* Color marrón para un estilo de papel viejo */
  font-size: 42px; /* Aumentar tamaño de la marca */
  text-decoration: none;
}

.navbar-toggler {
  border: none;
  background-color: transparent;
}

.navbar-toggler-icon {
  display: inline-block;
  width: 30px;
  height: 30px;
  background-color: #8B4513;
}

.navbar-collapse {
  display: flex;
  flex-direction: column;
}

.nav-item {
  list-style: none;
}

.navbar-nav {
  display: flex;
  flex-direction: column;
}

.dropdown-menu {
  display: none;
  flex-direction: column;
  padding: 0;
  margin: 0;
}

.nav-item.dropdown:hover .dropdown-menu {
  display: flex;
}

.clase_tocar {
  font-size: 30px;
  padding: 10px;
}
.conectado {
  border-color: #f5da09;
}

</style>
