<script setup lang="ts">
import ComponenteMusicalEditar from '../components/ComponenteMusicalEditar.vue';
import Cabecera from '../components/comp_editar/cabecera.vue';
import ParteEditar from '../components/comp_editar/parteeditar.vue';
import { item_lista } from '../modelo/item_lista';
import { Cancion } from '../modelo/cancion';

defineProps<{ cancion: Cancion, item: item_lista }>()
const emit = defineEmits(['acciono']);


function cerro_editar() {
    localStorage.setItem("editando", "no");
}


function guardar_cancioneditada() { 
    
    
}

</script>
<template>
    <div class="contenedor-editar">
        <Cabecera @cerrar="cerro_editar" @guardar="guardar_cancioneditada"  :cancion="cancion" :item="item"></Cabecera>
        {{  cancion.acordes.orden_partes }}
        <ParteEditar v-for="(i, x) in cancion.acordes.orden_partes" :key="x"  :cancion="cancion" :parte="i" :parte_indice="x" :item="item"></ParteEditar>
        
        
        <div class="row">
    <div class="col-8" >
        CANCION
    </div>
    <div class="col-4" >
        HERRAMIENTAS
    </div>
</div>

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
