<script setup lang="ts">
import { AnalisisArmonico } from '../modelo/analisis_armonico';

defineProps<{ analisis: AnalisisArmonico  }>()
</script>
<template>
  <div :class="{ noesta_enscala: analisis.esta_enscala === false } ">
    <p v-if="analisis">{{ analisis.muestra }}</p>
    <p v-if="analisis.muestra === ''">&nbsp;</p>
    <p v-if="!analisis">&nbsp;</p>
  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}

.noesta_enscala {
  color: red;
}
</style>
