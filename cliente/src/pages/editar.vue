<script setup lang="ts">
import { ref } from 'vue';
import { GetCanciones } from '../modelo/GetCanciones';
import ComponenteMusicalEditar from '../components/ComponenteMusicalEditar.vue';
import Cabecera from '../components/comp_editar/cabecera.vue';
import { item_lista } from '../modelo/item_lista';
import { AdminListasURL } from '../modelo/AdminListasURL';
import { Almacenado } from '../modelo/Almacenado';
import { AdminListasLocalStorage } from '../modelo/AdminListasStorage';
import { AdminListasTocables } from '../modelo/AdminIndiceListas';
import { Acordes, Parte } from '../modelo/acordes';
import { Letra } from '../modelo/letra';
import { Cancion } from '../modelo/cancion';

defineProps<{ cancion: Cancion, item: item_lista }>()
const emit = defineEmits(['acciono']);
const almacen = new Almacenado();


function cerro_editar() {
    localStorage.setItem("editando", "no");
}


function guardar_cancioneditada() { 
    
    
}

</script>
<template>
    <div class="contenedor-editar">
        <Cabecera @cerrar="cerro_editar" @guardar="guardar_cancioneditada"  :cancion="cancion" :item="item"></Cabecera>
        <ComponenteMusicalEditar @cerrar="cerro_editar" @guardar="guardar_cancioneditada" :item_indice="item" :editando_cancion="true" :compas="-1" :cancion="cancion"  ref="editref">

        </ComponenteMusicalEditar>
    </div>

</template>

<style scoped>



.contenedor-editar {
  border: 1px solid;
  border-radius: 5px;
  margin: 10px;
  padding: 6px;
  height: 100%;
}

.cancion {
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
}

.divListas {
    border: 1px solid ;
    padding: 15px;
    margin: 10px;
    border-radius: 8px;
}
</style>
