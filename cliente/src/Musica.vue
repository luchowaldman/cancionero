<script setup lang="ts">
import Partituracontrol from './components/partituracontrol.vue';

import { MusicXML } from '@stringsync/musicxml';


const xml = `<?xml version="1.0" encoding="UTF-8"?>
<score-partwise version="4.0">
  <part-list>
    <score-part id="P1">
      <part-name></part-name>
    </score-part>
  </part-list>
  <part id="P1">
    <measure number="1"/>
  </part>
</score-partwise>`;

// parse
const musicXml = MusicXML.parse(xml);
console.log(musicXml.serialize() === xml); // true
console.log(musicXml.serialize());

</script>

<template>
    <div>

<Partituracontrol signature="1/4"></Partituracontrol>
</div>
</template>

<style scoped>

</style>
