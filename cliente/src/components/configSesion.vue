<script setup lang="ts">
import { ref, onMounted, onUnmounted, watchEffect } from 'vue';
import { Cliente } from '../modelo/client_socketio';
import { Configuracion } from '../modelo/configuracion';
import { dir } from 'console';

const props = defineProps<{ cliente: Cliente, config_guardada: Configuracion  }>()
const replicas_recibidas = ref<string[][]>([])
const director = ref("");
const bandas = ref("");
const temas = ref("");


function conectarse() {
  props.config_guardada.sesion.usuario_sesion = props.config_guardada.nombre + Math.random()
  props.config_guardada.sesion.estado = "...conectando.."
  props.cliente.connect()
}

function onDirector(directorrec: string) {
  director.value = directorrec;
  console.log("Un nuevo director")
}

props.cliente.setdirectorHandler(onDirector)

function replicaHandler(datos: string[]) {
  console.log("replicaHandler", datos)
  replicas_recibidas.value.push(datos)
}
props.cliente.setreplicaHandler(replicaHandler);

props.cliente.setconectadoHandler((estado: string)=> {
  console.log("conectado", estado)
  if (estado=="") {
      props.config_guardada.sesion.estado = "conectado"
      props.cliente.unirme_sesion(props.config_guardada.sesion.nombre, props.config_guardada.sesion.usuario_sesion)
  }
    
  if (estado=="desconecado") {
        props.config_guardada.sesion.estado = "desconectado"
  }
    if (estado=="error") {
     props.config_guardada.sesion.estado = "error"
  }
})

function play_acorde() {
  console.log("envia para replicar play_acorde")
  props.cliente.replicar(props.config_guardada.sesion.nombre, props.config_guardada.nombre, ["play_acorde"])

}


function mandar_lista() {
  props.cliente.set_lista(bandas.value.split(','), temas.value.split(','))
}


function onListaRecibida(listaBandas: string[], listaTemas: string[]) {
  bandas.value = listaBandas.join(',');
  temas.value = listaTemas.join(',');
  console.log("Lista recibida", listaBandas, listaTemas);
}

props.cliente.setlistaHandler(onListaRecibida);

function get_director() {
  
  props.cliente.get_director()
}

const nro_cancion = ref(0);
const nro_compas = ref(0);

function mandar_nro_cancion() {
  console.log("envia para replicar nro_cancion");
  props.cliente.set_cancion(nro_cancion.value);
}

function mandar_nro_compas() {
  console.log("envia para replicar nro_compas");
  props.cliente.set_compas(nro_compas.value);
}

function mandar_init_compas() {
  console.log("envia init_compas nro_compas");
  props.cliente.setinit_compas(nro_compas.value);
}


function onNroCancionRecibido(nro: number) {
  nro_cancion.value = nro;
  console.log("Nro Cancion recibido", nro);
}

function onNroCompasRecibido(nro: number) {
  nro_compas.value = nro;
  console.log("Nro Compas recibido", nro);
}

function onStartCompasRecibido(nro: number) {
  nro_compas.value = nro;
  console.log("Star recibido", nro);
}

props.cliente.setstartCompasHandler(onStartCompasRecibido);
props.cliente.setcancionHandler(onNroCancionRecibido);
props.cliente.setcompasHandler(onNroCompasRecibido);

</script>
<template>
  
        <div>
          <div  class="row">
            <div class="col-6">
              <div class="form-group col-6">
                <label>Nombre sesion</label>
                <input v-model="config_guardada.sesion.nombre">
                <label>Estado: {{ config_guardada.sesion.estado }}</label>
              </div>
            </div>
            <div class="col-6">
              <div class="form-group col-6">
                <label>Iniciar al conectarse</label>
                <input v-model="config_guardada.sesion.iniciar_alcomienzo" type="checkbox">
              </div>
            </div>
          </div>

          <div class="row">
            <div class="col-12">
              <div v-if="config_guardada.sesion.estado != 'conectado'">
              <button @click="conectarse()">Conectarse</button>
            </div>
            <div v-if="config_guardada.sesion.estado === 'conectado'">
              <button @click="play_acorde()">MANDAR PLAY</button>      
              <button @click="get_director()">GET DIRECTOR</button>      
              Director: {{  director  }}
            </div>
          </div>
          </div>
          

          <div class="row" v-if="config_guardada.sesion.estado === 'conectado'">
            <div class="col-3">
              <input type="text" v-model="bandas">
              <input type="text" v-model="temas">
              <button @click="mandar_lista()">Mandar Lista</button>
            
          </div>

          <div class="col-3">
            <input type="text" v-model="nro_cancion">
            <button @click="mandar_nro_cancion()">Mandar Nro Cancion</button>
          </div>
          <div class="col-3">
            <input type="text" v-model="nro_compas">
            <button @click="mandar_nro_compas()">Mandar Nro Compas</button>
            <button @click="mandar_init_compas()">Mandar Init Compas</button>
            
          </div>

          </div>


          <div class="row">
            <div class="col-6"> {{  replicas_recibidas }}</div>
          </div>
          

        </div>

        
        

        
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
