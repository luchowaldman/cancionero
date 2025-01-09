import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

export default defineConfig({
  plugins: [vue()],
  build: {
    rollupOptions: {
      input: {
        index: resolve(__dirname, 'index.html'),
        edit: resolve(__dirname, 'edit.html'),
        listas: resolve(__dirname, 'listas.html'),
      }
    }
  }
})
