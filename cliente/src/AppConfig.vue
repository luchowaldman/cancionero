<script setup lang="ts">
import { ref, markRaw, onMounted, watch } from 'vue';
import Menu from './components/menu.vue';
import { Letra } from './modelo/letra';
import { Configuracion, Sesion }  from './modelo/configuracion';
import { Cliente }  from './modelo/client_socketio';
// Definir la canción y el contexto

const viendo = ref("perfil")


let config_load: string | null = localStorage.getItem("configuracion")
if (!config_load)
  config_load = ""

//let configuracionObj: Configuracion | null = JSON.parse(config_load)
let configuracionObj: Configuracion | null = null
if (!configuracionObj) {
  configuracionObj = new Configuracion()
  configuracionObj.sesion = new Sesion()
  configuracionObj.sesion.nombre = "default"
  configuracionObj.nombre = "no cargado"
  localStorage.setItem("configuracion", JSON.stringify(configuracionObj))
}


let cliente = new Cliente("http://localhost:8080/")
cliente.connect()

function replicaHandler(datos: string[]) {
  console.log("replicaHandler", datos)
}

cliente.setreplicaHandler(replicaHandler);


function play_acorde() {
  console.log("envia para replicar play_acorde")
  cliente.replicar(["4"])

}
    // Llamar a la función iniciarCompasEnComponentes cuando sea necesario 
    onMounted(() => { 
        console.log("APP CONFIGURACION MONTADA")
    });
    function click_opcion(viendostr: string) {
      viendo.value = viendostr
      
    }

    function guardar_configuracion() {
      
        localStorage.setItem("configuracion", JSON.stringify(configuracionObj))
    }

</script>

<template>
    <div>
        
        <Menu titulo="Configuracion"></Menu>
        <div class="row">
          <div class="col-3">
  <div class="d-flex flex-column flex-shrink-0 p-3 text-bg-dark" style="width: 280px;">
    <ul class="nav nav-pills flex-column mb-auto">
    
      
      <li @click="click_opcion('perfil')">
        <a href="#" class="nav-link text-white"  :class="{ 'active': viendo==='perfil' }" >
          
           Usuario 
        </a>
      </li>
      
      <li @click="click_opcion('sesion')">
        <a href="#" class="nav-link text-white" :class="{ 'active': viendo==='sesion' }" >
          
          Sesion
        </a>
      </li>
    </ul>

    <hr>
    <ul class="nav nav-pills flex-column mb-auto">
      
      <li @click="click_opcion('vistas')">
        <a href="#" class="nav-link text-white"
        :class="{ 'active': viendo==='vistas' }" >
          
          Vistas
        </a>
      </li>
      <li @click="click_opcion('conexiones')">
        <a href="#" class="nav-link text-white"
        :class="{ 'active': viendo==='conexiones' }" >
          
          Conexiones
        </a>
      </li>
      <li @click="click_opcion('datos')">
        <a href="#" class="nav-link text-white"
          :class="{ 'active': viendo==='datos' }" >
          Datos
        </a>
      </li>
      
      
    </ul>
    <hr>
    
    <ul class="nav nav-pills flex-column mb-auto">
      
      <li @click="click_opcion('acercade')">
        <a href="#" class="nav-link text-white"
        :class="{ 'active': viendo==='acercade' }" >
          
          Acerca de ...
        </a>
      </li>
    </ul>
  </div></div>


  <div class="col-9">
            
      <div v-if="viendo=='perfil'">
        Usuario : Aca vendria el input
        <!-- 
        <input v-model="configuracion.nombre">
      -->
      
      </div>
      
      <div v-if="viendo=='sesion'">
        Sesion
        <button @click="play_acorde()">MANDAR PLAY</button>
      </div>
      
      <div v-if="viendo=='vistas'">
        Vistas
      </div>
      <button @click="guardar_configuracion()">Guardar</button>
  </div>

        </div>




    
</div>


</template>

<style scoped></style>
