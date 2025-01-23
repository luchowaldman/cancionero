import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

export default defineConfig({
  plugins: [vue()],
  build: {
    rollupOptions: {
      input: {
        index: resolve(__dirname, 'index.html'),
        music: resolve(__dirname, 'music.html')
      }
    }
  },
  server: {
    host: '0.0.0.0', // Permite que el servidor escuche en todas las interfaces
    port: 5173 // Asegúrate de que el puerto coincida
  }
})
