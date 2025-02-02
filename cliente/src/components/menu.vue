<script setup lang="ts">

import { Cancion } from '../modelo/cancion';
import ControladorTiempo from './ControladorTiempo.vue';
import ControladorSesion from './ControladorSesion.vue';
import { EstadoSesion } from '../modelo/estadosesion';




const emit = defineEmits(['acciono']);

function acciono(valor: string, compas: number = 0) {
    //console.log("Acciono--->", valor, compas);
    emit('acciono', valor, compas);
    
}
const props = defineProps<{ viendo_vista: string, compas: number, cancion: Cancion
  ,  nro_cancion: number, total_canciones: number, sesion: EstadoSesion }>()



if (props.viendo_vista == undefined) 
  console.log("Viendo vista no definida")
</script>

<template>
  <div class="navbarFogon">
    
    
    <div class="pagina_seleccionable" :class="{active: viendo_vista == 'tocar'}" >
        <p class="nombre-pagina" @click="acciono('tocar')"   :class="{active: viendo_vista == 'tocar'}" aria-current="page">
          
          <i class="bi bi-fire ilogo">

            
          </i>
          

        </p>	
      </div>
        <div class="ctrl_menu"  style="width: 40%;">
          <ControladorTiempo :nro_cancion="nro_cancion" :total_canciones="total_canciones"  :compas=compas :cancion="cancion"
          @play="acciono('play')" @pause="acciono('pause')" @stop="acciono('stop')" @next="acciono('next')" @previous="acciono('previous')"
            @update-compas="(valor) => acciono('update-compas', valor)">
        </ControladorTiempo> 
      </div>
      <div class="ctrl_menu">
        
        <ControladorSesion :compas=compas :cancion="cancion"  :sesion="sesion"
        @conectar="acciono('conectar')"> :ref="refSesion" >
        </ControladorSesion>
      </div>
       
      <div class="pagina_seleccionable aladerecha" @click="acciono('listas')"  :class="{active: viendo_vista == 'listas'}" >
        <p class="nombre-pagina"aria-current="page">
          <i class="bi bi-list"></i>
        </p>	
      </div>    
      


      <div class="pagina_seleccionable aladerecha" @click="acciono('editar')"  :class="{active: viendo_vista == 'editar'}" >
        <p class="nombre-pagina"aria-current="page">
            <i class="bi bi-pencil"></i>
        </p>	
      </div> 
      <div class="pagina_seleccionable aladerecha" @click="acciono('buscar')"  :class="{active: viendo_vista == 'buscar'}" >
        <p class="nombre-pagina"aria-current="page">
            <i class="bi bi-globe"></i>
        </p>	
      </div>    
      
          
          <div class="pagina_seleccionable aladerecha" @click="acciono('config')" :class="{active: viendo_vista == 'config'}" >
            <p class="nombre-pagina" aria-current="page">
              
              <i class="bi bi-gear-fill"></i>

            </p>
          </div>
    
    </div>
</template>

<style scoped>
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

}

.nombre-pagina {
  font-size: 60px;
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

</style>
