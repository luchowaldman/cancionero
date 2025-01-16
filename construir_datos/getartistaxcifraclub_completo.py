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

def procesar_html_artista(band_name):
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

def descargarbandacompleta(banda):
    #getartista_page(banda)
    procesar_html_artista(banda)
    download_cifraclub_artista(banda)



#descargarbandacompleta("gustavo cerati")
#descargarbandacompleta("indio solari")
#descargarbandacompleta("luis alberto spinetta")
#descargarbandacompleta("moris") <-- NO ANDUVO PORQUE NO TIENE TODAS LAS CANCIONES
#descargarbandacompleta("bob dylan")
#descargarbandacompleta("viejas locas")

