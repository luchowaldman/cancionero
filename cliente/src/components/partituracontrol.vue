<template>
  <div id="output"></div>
</template>

<script lang="ts">
import { defineComponent, onMounted } from "vue";
//import { Renderer, Stave, StaveNote, Voice, Formatter, Vex } from "vexflow";
import { StaveNote, Voice, Vex } from "vexflow";

export default defineComponent({
  name: "Pentagram",
  props: {
    signature: {
      type: String,
      required: true
    }
  },
  dibujar_partitura() {

  },
  setup() {
    onMounted(() => {


      //const div = document.getElementById("output");
      const vf = new Vex.Flow.Factory({ renderer: { elementId: 'output', width: 1500, height: 1200 } });
      //const score = vf.EasyScore();
      const system = vf.System();

          
      // Notas para Clave de Sol
      // w redonda, h blanca, q negra, 8 corchea, 16 semicorchea
      const trebleNotes = [
        new StaveNote({ clef: "treble", keys: ["c/4"], duration: "h" }),
        //new StaveNote({ clef: "treble", keys: ["d/4"], duration: "q" }),
        new StaveNote({ clef: "treble", keys: ["e/4"], duration: "q" }),
        new StaveNote({ clef: "treble", keys: ["f/4"], duration: "q" })
      ];

      // Crear las voces
      const trebleVoice = new Voice({ num_beats: 4,  beat_value: 4 }).addTickables(trebleNotes);
    // Crear el primer compás
    system.addStave({
      voices: [
        trebleVoice,
      ],
    }).addClef('treble').addTimeSignature('4/4');

    // Crear el segundo compás
    const trebleNotes2 = [
      new StaveNote({ clef: "treble", keys: ["g/4"], duration: "h" }),
      new StaveNote({ clef: "treble", keys: ["a/4"], duration: "q" }),
      new StaveNote({ clef: "treble", keys: ["b/4"], duration: "q" })
    ];
    const trebleVoice2 = new Voice({ num_beats: 4, beat_value: 4 }).addTickables(trebleNotes2);

    system.addStave({
      voices: [
        trebleVoice2,
      ],
    });

    // Formatear y dibujar
    vf.draw();



















    });
  }
});
</script>

<style scoped>
#output {
  border: 1px solid black;
  margin: 20px;
}
</style>
