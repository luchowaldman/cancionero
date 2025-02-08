<script setup lang="ts">


import { ref } from 'vue';
import Nota from './modelo/Midi/nota';

const numeros: number[] = Array.from({ length: 53 }, (_, i) => i);
const notas: number[] = [1, 2, 4, 8, 16, 32];
const musicaref = ref([] as Nota[][])

let prim_notas = [] as Nota[];
prim_notas.push(new Nota(22, 1));
musicaref.value = [prim_notas, prim_notas, prim_notas]

function clase(numero: number) {
  if (numero < 10 || numero > 34) {
    return "noseve";
  }

  if (numero % 2 == 0) {
    return "espacio";
  } else 
  {
    if (numero > 20 && numero < 24) {
    return "noseve";
  }

    return "linea";
  }
}

function duracionnota(acordes: Nota[], numero: number) {
  for (let i = 0; i < acordes.length; i++) {
    if (acordes[i].nota == numero) {
      return acordes[i].duracion
    }
  }
  return -1;
}

</script>

<template>
    <div>

      <div class="cabecera">
        <div style="display: flex;"> 
          Notas: <div v-for="nota in notas" :key="nota"> {{ nota }} </div>
        </div>
      </div>






      <div style="display: flex; width: 100%;">
            <div v-for="(acordes, acordeid) in musicaref" :key="acordeid">
              <div  style="width: 30px;">
                <div v-for="numero in numeros" :key="numero" :class="clase(numero)" >
                    <div class="nota">
                      <span v-if="duracionnota(acordes, numero) != -1">{{ duracionnota(acordes, numero) }}</span>
                    </div>
                  </div>
              </div>



            </div>

      <!-- Pa Agregar-->
      <div>

        <div v-for="numero in numeros" :key="numero" :class="clase(numero)">
        <div class="nota">
        &nbsp;
        </div>
        </div>
      </div></div>


</div>
</template>

<style scoped>

.espacio {
  height: 20px;
  margin: 0px;
  padding: 0px;
}

.linea {
  height: 1px;
  background-color: black;
  margin: 0px;

}

.noseve {
  height: 1px;
}

.linea .nota {
  color: red;
  position: relative;
  top: -13px;
}

</style>
