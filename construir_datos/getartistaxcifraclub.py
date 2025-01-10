import os
import requests
import json

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



download_cifraclub_artista("indio solari")
download_cifraclub_artista("luis alberto spinetta")
download_cifraclub_artista("moris")
download_cifraclub_artista("bob dylan")

exit()

download_cifraclub_artista('charly garcia')
download_cifraclub_artista('the rolling stones')
download_cifraclub_artista('fito paez')
download_cifraclub_artista('shakira')
download_cifraclub_artista('joaquin sabina')
download_cifraclub_artista('joan-manuel-serrat')
download_cifraclub_artista('los-redonditos-de-ricota')
download_cifraclub_artista('soda stereo')

exit()
download_cifraclub_artista('intoxicados')
download_cifraclub_artista('the beatles')
download_cifraclub_artista('andres calamaro')