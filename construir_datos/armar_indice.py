import os
import requests
import json
from bs4 import BeautifulSoup


# Define the directory where the pages will be saved
SAVE_DIRECTORY = 'cifraclub_pages'
DIRECTORIO_DATOS = '../cliente/public/data/'

def download_cifraclub_page(band_name, song_name):
    # Format the URL
    band_name = band_name.replace(' ', '-')
    song_name = song_name.replace(' ', '-').replace('?', '')
    url = f'https://www.cifraclub.com/{band_name}/{song_name}/'.lower()
    
    # Make the request to get the page content
    response = requests.get(url)
    
    if response.status_code == 200:
        # Ensure the save directory exists
        if not os.path.exists(SAVE_DIRECTORY):
            os.makedirs(SAVE_DIRECTORY)
        
        # Define the file path
        file_path = os.path.join(SAVE_DIRECTORY, f'{band_name}_{song_name}.html')
        
        # Save the content to a file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)
        
        print(f'Page saved successfully: {file_path}')
    else:
        print(f'Failed to download page: {url} (Status code: {response.status_code})')
def download_cifraclub_artista(band_name):
    
    band_name = band_name.replace(' ', '-')
    nombre_archivo_json  = os.path.join(DIRECTORIO_DATOS, f'{band_name}.json')
    # Load the JSON file
    with open(nombre_archivo_json, 'r', encoding='utf-8') as file:
        canciones = json.load(file)
    
    # Iterate over the list of songs and download each page
    for song_name in canciones:
        print (f'Descargar... {song_name}')
        download_cifraclub_page(band_name, song_name)
def getartista_page(band_name):
    # Format the URL
    band_name = band_name.replace(' ', '-')
    url = f'https://www.cifraclub.com/{band_name}/'
    
    # Make the request to get the page content
    response = requests.get(url)    
    if response.status_code == 200:
        # Ensure the save directory exists
        if not os.path.exists(SAVE_DIRECTORY):
            os.makedirs(SAVE_DIRECTORY)
        
        # Define the file path
        file_path = os.path.join(SAVE_DIRECTORY, f'{band_name}.html')
        
        # Save the content to a file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)
        
        print(f'Page saved successfully: {file_path}')
    else:
        print(f'Failed to download page: {url} (Status code: {response.status_code})')

    
    band_name = band_name.replace(' ', '-')
    nombre_archivo_json  = os.path.join(DIRECTORIO_DATOS, f'{band_name}.json')
    # Load the JSON file
    with open(nombre_archivo_json, 'r', encoding='utf-8') as file:
        canciones = json.load(file)
    
    # Iterate over the list of songs and download each page
    for song_name in canciones:
        print (f'Descargar... {song_name}')
        download_cifraclub_page(band_name, song_name)



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

# Ejemplo de uso:
directorio = '/ruta/al/directorio'
archivos = obtener_archivos(directorio)
print('Archivos:', archivos)

def descargarbandacompleta(banda):
    #getartista_page(banda)
    procesar_html(banda)
    download_cifraclub_artista(banda)


def get_bandas():
    arch = obtener_archivos(SAVE_DIRECTORY)
    bandas = []
    for archivo in arch:
        if '_' in archivo:
            banda = archivo.split('_')[0]
            banda = banda.replace('-', ' ')
            bandas.append(banda)
    bandas = list(set(bandas))
    return bandas



for banda in get_bandas():
    print(f"Indexando {banda}")