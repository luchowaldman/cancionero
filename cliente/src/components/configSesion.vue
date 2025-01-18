<script setup lang="ts">
import { ref, onMounted, onUnmounted, watchEffect } from 'vue';
import { Cliente } from '../modelo/client_socketio';
import { Configuracion } from '../modelo/configuracion';

const props = defineProps<{ cliente: Cliente, config_guardada: Configuracion  }>()
const replicas_recibidas = ref<string[][]>([])
function conectarse() {
  props.config_guardada.sesion.usuario_sesion = props.config_guardada.nombre + Math.random()
  props.config_guardada.sesion.estado = "...conectando.."
  props.cliente.connect()
}

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
            </div>
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
