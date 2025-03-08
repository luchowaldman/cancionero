import os
import requests
import json
from bs4 import BeautifulSoup

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

arch = obtener_archivos(SAVE_DIRECTORY)
for archivo in arch:
    print (archivo)