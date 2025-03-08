import os
import json
from procesar_archivo import construiracordes_dehtml

# Define the directory where the pages will be saved
SAVE_DIRECTORY = 'cifraclub_pages'
DIRECTORIO_DATOS = '../cliente/public/data/'
# nombre_archivo_json  = os.path.join(DIRECTORIO_DATOS, f'{band_name}_{song_name}.json')
def obtener_archivos(directorio):
    archivos = []
    try:
        for archivo in os.listdir(directorio):
            if archivo.endswith('.html'):
                archivos.append(archivo.replace('.html', '')) 
        return archivos
    except Exception as e:
        print(f"Error al leer el directorio: {e}")
        return []

print ("ni")
archivos = obtener_archivos(SAVE_DIRECTORY)
print ("archivos", archivos)
for archivo in archivos:
    if '_' in archivo:
            banda = archivo.split('_')[0]
            tema = archivo.split('_')[1]
            print(f'Procesando banda: {banda}, tema: {tema}')
            try:
                construiracordes_dehtml(banda, tema)
            except Exception as e:
                print(f"Error al procesar banda {banda}, tema {tema}: {e}")
