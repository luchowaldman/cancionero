<template>
  <div id="output"></div>
</template>

<script lang="ts">
import { defineComponent, onMounted } from "vue";
import { Renderer, Stave, StaveNote, Voice, Formatter } from "vexflow";

export default defineComponent({
  name: "Pentagram",
  setup() {
    onMounted(() => {
      const div = document.getElementById("output");
      const renderer = new Renderer(div, Renderer.Backends.SVG);
      renderer.resize(800, 400);
      const context = renderer.getContext();
      context.setFont("Arial", 10);

      // Clave de Sol
      const trebleStave = new Stave(10, 50, 700);
      trebleStave.addClef("treble").addTimeSignature("4/4");
      trebleStave.setContext(context).draw();

      // Notas para Clave de Sol
      const trebleNotes = [
        new StaveNote({ clef: "treble", keys: ["c/4"], duration: "q" }),
        new StaveNote({ clef: "treble", keys: ["d/4"], duration: "q" }),
        new StaveNote({ clef: "treble", keys: ["e/4"], duration: "q" }),
        new StaveNote({ clef: "treble", keys: ["f/4"], duration: "q" })
      ];

      // Clave de Fa
      const bassStave = new Stave(10, 150, 700);
      bassStave.addClef("bass").addTimeSignature("4/4");
      bassStave.setContext(context).draw();

      // Notas para Clave de Fa
      const bassNotes = [
        new StaveNote({ clef: "bass", keys: ["c/3"], duration: "q" }),
        new StaveNote({ clef: "bass", keys: ["d/3"], duration: "q" }),
        new StaveNote({ clef: "bass", keys: ["e/3"], duration: "q" }),
        new StaveNote({ clef: "bass", keys: ["f/3"], duration: "q" })
      ];

      // Crear las voces
      const trebleVoice = new Voice({ num_beats: 4,  beat_value: 4 }).addTickables(trebleNotes);
      const bassVoice = new Voice({ num_beats: 4,  beat_value: 4 }).addTickables(bassNotes);

      // Formatear y dibujar las voces
      new Formatter().joinVoices([trebleVoice]).format([trebleVoice], 600);
      new Formatter().joinVoices([bassVoice]).format([bassVoice], 600);

      trebleVoice.draw(context, trebleStave);
      bassVoice.draw(context, bassStave);
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
