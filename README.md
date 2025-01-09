# Cancionero


Este trabajo propone una solución para orquestas profesionales y para una guitarreada en rededor de una fogata: los usuarios pueden crear y unirse a sesiones en la que se van a ir “reproduciendo” listas de canciones. En su dispositivo el guitarrista ve los acordes y las canciones de las letra; así como cada músico de la orquesta puede ver la partitura de su instrumento. La vista cambia en cada compás y modifica el acorde o el renglón de la letra resaltados.


# Requerimientos técnicos

La aplicación va a ser multiplataforma y progresiva, de modo que se pueda usar offline (intentar que se puedan conectar entre distintos dispositivos sin servidor)

# Cliente

Vue 3 + TypeScript + Vite

This template should help get you started developing with Vue 3 and TypeScript in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

Learn more about the recommended Project Setup and IDE Support in the [Vue Docs TypeScript Guide](https://vuejs.org/guide/typescript/overview.html#project-setup).

# Base de datos 

Sera distribuida en JSON, muy probablemente Casandra

# Construccion de datos

Vamos a obtener letras, acordes y partituras desde internet, mezclando datos o creandolas usando python.
