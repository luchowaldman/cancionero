import os
import json
from bs4 import BeautifulSoup


from acordes import Acordes, Parte
from buscar_partes import buscar_partes


SAVE_DIRECTORY = 'cifraclub_pages/'
DIRECTORIO_DATOS = '../cliente/public/data/'

# Función para calcular las partes de la canción

# Función para analizar un archivo HTML y guardarlo en JSON
def procesar_html(band_name):
    # Crear un diccionario para almacenar el análisis
    analisis = {}
    analisis['banda'] = band_name
    band_name = band_name.replace(' ', '-')
    
    nombre_archivo_html = os.path.join(SAVE_DIRECTORY, f'{band_name}.html')
    nombre_archivo_json  = os.path.join(DIRECTORIO_DATOS, f'{band_name}.json')
    # Leer el contenido del archivo HTML
    with open(nombre_archivo_html, 'r', encoding='utf-8') as file:
        contenido_html = file.read()
    
    # Analizar el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(contenido_html, 'lxml')
    
    
    # Obtener el tono de la canción
    todaslascanciones = soup.find('ul', id='js-a-songs')
    lis = todaslascanciones.find_all('li')
    canciones = []
    for (i, li) in enumerate(lis):
        a = li.find('a')
        if a:
            cancion = a.get_text()
            canciones.append(cancion)
            print (f'cancion: {cancion}')
            

    # Crear el directorio si no existe
    directorio = os.path.dirname(nombre_archivo_json)
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    
    # Guardar el análisis en un archivo JSON
    with open(nombre_archivo_json, 'w', encoding='utf-8') as file:
        json.dump(canciones, file, ensure_ascii=False, indent=4)

# Ejemplo de uso



procesar_html('charly garcia')
procesar_html('the rolling stones')
procesar_html('fito paez')
procesar_html('shakira')
procesar_html('joaquin sabina')
procesar_html('joan-manuel-serrat')
procesar_html('los-redonditos-de-ricota')
procesar_html('soda stereo')
exit()

procesar_html('the beatles')
procesar_html('andres calamaro')
procesar_html('intoxicados')
