import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

export default defineConfig({
  plugins: [vue()],
  build: {
    rollupOptions: {
      input: {
        index: resolve(__dirname, 'index.html'),
        editar: resolve(__dirname, 'editar.html'),
        listas: resolve(__dirname, 'listas.html'),
        configurar: resolve(__dirname, 'configurar.html'),
        ritmo: resolve(__dirname, 'ritmo.html')
      }
    }
  },
  server: {
    host: '0.0.0.0', // Permite que el servidor escuche en todas las interfaces
    port: 5173 // Asegúrate de que el puerto coincida
  }
})
