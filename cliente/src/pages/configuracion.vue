<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { ModeloConfiguracion }  from '../modelo/modeloconfiguracion';

import { Cliente }  from '../modelo/client_socketio';
import ConfigSesion from '../components/configSesion.vue';
import CompoMidiPlayer from '../components/compoMidiPlayer.vue';
import { EstadoSesion } from '../modelo/estadosesion';

// Definir la canción y el contexto

const viendo = ref("sesion")


let config_load: string | null = localStorage.getItem("configuracion")
if (!config_load)
  config_load = ""

let configuracionObj: ModeloConfiguracion | null = JSON.parse(config_load)
//let configuracionObj: Configuracion | null = null
if (!configuracionObj) {
  configuracionObj = new ModeloConfiguracion()
  configuracionObj.sesion = new EstadoSesion()
  configuracionObj.sesion.nombre = "default"
  configuracionObj.nombre = "default"
  localStorage.setItem("configuracion", JSON.stringify(configuracionObj))
}


let cliente = new Cliente("http://192.168.0.202:8080/")
const config_guardada = ref(configuracionObj)


    // Llamar a la función iniciarCompasEnComponentes cuando sea necesario 
    onMounted(() => { 
        console.log("APP CONFIGURACION MONTADA")
    });
    function click_opcion(viendostr: string) {
      viendo.value = viendostr
      
    }

    function guardar_configuracion() {
      console.log("guardar_configuracion")      
        localStorage.setItem("configuracion", JSON.stringify(config_guardada.value))
    }






</script>

<template>
    <div>
        
        
        <div class="row">
          <div class="col-3">
  
  
  <div class="" style="width: 280px;">
    <ul class="nav nav-pills flex-column mb-auto">
    
      
      <li @click="click_opcion('perfil')">
        <a href="#" class="nav-link text-white"  :class="{ 'activo': viendo==='perfil' }" >
          
           Perfil 
        </a>
      </li>
      
      <li @click="click_opcion('sesion')">
        <a href="#" class="nav-link text-white" :class="{ 'activo': viendo==='sesion' }" >
          
          Sesion
        </a>
      </li>
    </ul>

    <hr>
    <ul class="nav nav-pills flex-column mb-auto">
      
      <li @click="click_opcion('vistas')">
        <a href="#" class="nav-link text-white"
        :class="{ 'activo': viendo==='vistas' }" >
          
          Vistas
        </a>
      </li>
      <li @click="click_opcion('conexiones')">
        <a href="#" class="nav-link text-white"
        :class="{ 'activo': viendo==='conexiones' }" >
          
          Conexiones
        </a>
      </li>
      <li @click="click_opcion('datos')">
        <a href="#" class="nav-link text-white"
          :class="{ 'activo': viendo==='datos' }" >
          Datos
        </a>
      </li>
      <li @click="click_opcion('midis')">
        <a href="#" class="nav-link text-white"
          :class="{ 'activo': viendo==='midis' }" >
          MIDIS
        </a>
      </li>
      
      
      
    </ul>
    <hr>
    
    <ul class="nav nav-pills flex-column mb-auto">
      
      <li @click="click_opcion('acercade')">
        <a href="#" class="nav-link text-white"
        :class="{ 'activo': viendo==='acercade' }" >
          
          Acerca de ...
        </a>
      </li>
    </ul>
  </div></div>


  <div class="col-9 innerConfig">
            
      <div v-if="viendo=='perfil'" class="container">
        <div class="row">
          <div class="col-6">
            <div class="form-group col-6">
              <label>Nombre</label>
              <input v-model="config_guardada.nombre">
            </div>
          </div>

        </div>
        
      </div>
      
      <div v-if="viendo=='sesion'">
        <ConfigSesion :cliente="cliente" :config_guardada="config_guardada"></ConfigSesion>
      
      
        </div>
        

        
      
      <div v-if="viendo=='vistas'">
        Vistas
      </div>

      
      <div v-if="viendo=='midis'">
        <CompoMidiPlayer ></CompoMidiPlayer>
      </div>
      <div v-if="viendo=='acercade'">
        <div>
        Desarrollado por Luis Waldman para y gracias a:
      </div>
      <A href="https://fi.uba.ar/"><img src="https://fi.uba.ar/images/logo-fiuba.png"></A>
        
  <p></p>+
  <p>github: <a href="https://github.com/luchowaldman/cancionero">cancionero</a></p>
  <p>comercial: <a href="https://www.instagram.com/eme.redes/">Eme.redes</a></p>
  <p>donaciones al alias: la.plata.de.luis</p>

      </div>
      <div>
      <button id="btnGuardar" @click="guardar_configuracion()">Guardar</button></div>
    </div>

    

        </div>




    
</div>


</template>

<style scoped>
  .innerConfig {
    padding: 20px;
  }

  #btnGuardar {
    font-size: 30px;
  }

  .botoneraConfig {padding: 20px;
  }
  .activo {
    color: white;
    background-color: blueviolet;
  }

</style>
