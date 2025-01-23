<script setup lang="ts">
import { ref, onMounted, onUnmounted, watchEffect } from 'vue';
import { AnalisisArmonico } from '../modelo/analisis_armonico';
import { MidiPlayer} from '../modelo/midiplayer';

const ref_instrumentocargado = ref(false)
const ref_Notas = ref([] as string[])
const escalas = [3, 4]
const notas = ["C", "D", "E", "F", "G", "A", "B"]
function tiene_sostendio(nota: string) {
    return ["C", "D", "F", "G", "A"].includes(nota[0])
}

function nota_sostenido(nota: string) {
    return nota[0] + "#" + nota[1]
}


let allnotas = []

escalas.forEach(element => {
    notas.forEach((nota, index) => {
        allnotas.push(nota + element)
    });
    
});


ref_Notas.value = allnotas;




let midiplayer: MidiPlayer = null;
let archivos_instrumentos = ['acordion', 'bateria', 'guitarra', 'guitarraelectrica', 'harmonica', 'piano', 'trompeta']
let nombres_instrumentos = ['acordion', 'bateria', 'guitarra', 'guitarra electrica', 'harmonica', 'piano', 'trompeta']
function iniciar_midi(id_instrumeto) {
  console.log("iniciar_midi") 

fetch('data/notas_midi/' + archivos_instrumentos[id_instrumeto]  +'.json')
  .then(response => response.json())
  .then(samples => {
    midiplayer = new MidiPlayer(samples);
    midiplayer.initialize();

    ref_instrumentocargado.value = true;
    // Puedes establecer el handler aquí si lo necesitas:
    midiplayer.setConectadoHandler((resultado: string) => {
      console.log(resultado);
    });

    // Ejemplo para tocar una nota:
    
  })
  .catch(error => {
    console.error("Error loading samples:", error);
  });
    }

    function tocar_midi(nota) {
      console.log("tocar_midi")
      midiplayer.play(nota);
    }

</script>
<template>
    <div>
      <div class="row">
        <div class="col-4">
          <button v-for="(nombre, id) in nombres_instrumentos" :key="id" @click="iniciar_midi(id)" > {{ nombre }}</button>
          
        </div>

      </div>
      
        <ul class="piano"  v-if="ref_instrumentocargado">


          <div>

            <li v-for="(nota, nota_id) in ref_Notas" :key="nota_id" class="key">
    <span class="white-key" @click="tocar_midi(nota)" >{{ nota }} </span>
    <span v-if="tiene_sostendio(nota)" @click="tocar_midi(nota_sostenido(nota))" class="black-key" >{{ nota_sostenido(nota) }} # </span>
    <br>
    
  </li>
          </div>

          
</ul>
</div>
</template>

<style scoped>



.piano {
  background: -webkit-linear-gradient(-65deg, #000000, #222222, #000000, #666666, #222222 75%);
  background: -moz-linear-gradient(-65deg, #000000, #222222, #000000, #666666, #222222 75%);
  background: -o-linear-gradient(-65deg, #000000, #222222, #000000, #666666, #222222 75%);
  background: linear-gradient(-65deg, #000000, #222222, #000000, #666666, #222222 75%);
  border-top: 2px solid #111;
  box-shadow: inset 0 -1px 1px rgba(255, 255, 255, 0.5), inset 0 -4px 5px #000000;
  padding: 0 1% 3%;
  text-align: center;
}
.key {
  display: inline-block;
  position: relative;
  margin: 0 2px;
  width: 6%;
  max-width: 85px;
}
.key:active .black-key,
.key.active .black-key {
  top: -5px;
}
.key .white-key {
  background: -webkit-linear-gradient(-30deg, #f8f8f8, #ffffff);
  background: -moz-linear-gradient(-30deg, #f8f8f8, #ffffff);
  background: -o-linear-gradient(-30deg, #f8f8f8, #ffffff);
  background: linear-gradient(-30deg, #f8f8f8, #ffffff);
  box-shadow: inset 0 1px 0px #ffffff, inset 0 -1px 0px #ffffff, inset 1px 0px 0px #ffffff, inset -1px 0px 0px #ffffff, 0 4px 3px rgba(0, 0, 0, 0.7), inset 0 -1px 0px #ffffff, inset 1px 0px 0px #ffffff, inset -1px -1px 15px rgba(0, 0, 0, 0.5), -3px 4px 6px rgba(0, 0, 0, 0.5);
  display: block;
  height: 300px;
}
.key .white-key:active,
.key .white-key.active {
  box-shadow: inset 0 1px 0px #ffffff, inset 0 -1px 0px #ffffff, inset 1px 0px 0px #ffffff, inset -1px 0px 0px #ffffff, 0 4px 3px rgba(0, 0, 0, 0.7), inset 0 -1px 0px #ffffff, inset 1px 0px 0px #ffffff, inset -1px -1px 15px #000000, -3px 4px 6px rgba(0, 0, 0, 0.5);
  position: relative;
  top: -5px;
  height: 295px;
}
.key .black-key {
  content: "";
  color: #ffffff;
  box-shadow: inset 0px -1px 2px rgba(255, 255, 255, 0.4), 0 2px 3px rgba(0, 0, 0, 0.4);
  background: -webkit-linear-gradient(-20deg, #222222, #000000, #222222);
  background: -moz-linear-gradient(-20deg, #222222, #000000, #222222);
  background: -o-linear-gradient(-20deg, #222222, #000000, #222222);
  background: linear-gradient(-20deg, #222222, #000000, #222222);
  border-width: 1px 3px 8px;
  border-style: solid;
  border-color: #666 #222 #111 #555;
  height: 160px;
  position: absolute;
  top: 0px;
  right: -40%;
  width: 70%;
  z-index: 10;
}
.key .black-key:active,
.key .black-key.active {
  border-bottom-width: 3px;
  top: 0;
}
@media (max-width: 767px) {
  .key {
    width: 8%;
  }
  .key:nth-child(1),
  .key:nth-child(2),
  .key:nth-child(3) {
    display: none;
  }
}
@media (max-width: 480px) {
  .key {
    width: 12%;
  }
  .key:nth-child(11),
  .key:nth-child(12),
  .key:nth-child(13),
  .key:nth-child(14) {
    display: none;
  }
}




.nota_negra {
    background-color: black;
    color: white;
    position: relative;
    left: -20px;
    margin-right: -20px;
}
.pianomio {
    display: flex;
    
}

.tecla {
    width: 50px;
    height: 200px;
    border: 1px solid black;
    
    
}

.nota_negra {
    background-color: black;
    color: white;
    width: 40px;
    height: 120px;
    margin-left: -20px;
}


</style>
