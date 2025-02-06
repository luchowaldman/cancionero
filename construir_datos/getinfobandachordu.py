import json
import os
from bs4 import BeautifulSoup
import requests

# Define the directory where the pages will be saved
SAVE_DIRECTORY = 'cifraclub_pages'

def getpagina(band_name):
    # Format the URL
    band_name = band_name.replace(' ', '-')
    url = f'https://chordu.com/search?q={band_name.replace("-", "+")}'
    
    # Make the request to get the page contentpyth
    response = requests.get(url)
    
    if response.status_code == 200:
        # Ensure the save directory exists
        if not os.path.exists(SAVE_DIRECTORY):
            os.makedirs(SAVE_DIRECTORY)
        

        soup = BeautifulSoup(response.text, 'lxml')   
        songs = []
        for div in soup.find_all('div', class_='style_track__I_xun'):
            song_info = {
            'title': div.get_text(strip=True)[4:],
            'link': div.find('a')['href'] if div.find('a') else None
            }
            songs.append(song_info)
        # Save the data to a JSON file
        band_data = {band_name: songs}
        json_filename = os.path.join(SAVE_DIRECTORY, f'{band_name}.json')
        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(band_data, json_file, ensure_ascii=False, indent=4)

def get_bpm_banda(band_name):
                json_filename = os.path.join(SAVE_DIRECTORY, f'{band_name}.json')
                if os.path.exists(json_filename):
                    with open(json_filename, 'r', encoding='utf-8') as json_file:
                        band_data = json.load(json_file)
                        result = []
                        for song in band_data.get(band_name, []):
                            title = song.get('title')
                            link = song.get('link')
                            result.append({'title': title, 'link': link})
                        return result
                else:
                    print(f'No data found for band: {band_name}')
                    return []

def get_temas(banda):
    temas = []
    DIRECTORIO_DATOS = '../cliente/public/data/canciones/'
    for filename in os.listdir(DIRECTORIO_DATOS):
        if not filename.endswith('json'):
            continue
        spl = filename.split('_')
        if len(spl) != 2:
            continue
        if (banda == spl[0]):
            temas.append(spl[1].replace(".json", "").replace("-", " "))
    return temas

def prepararpalabra(palabra):
    replacements = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'uno': '1', 'dos': '2', 'tres': '3', 'nueve': '9',
        'Uno': '1', 'Dos': '2', 'Tres': '3', 'Nueve': '9',
        '(Pseudo Video)': '', 'Request Chords': ''
    }
    for accented_char, unaccented_char in replacements.items():
        palabra = palabra.replace(accented_char, unaccented_char)
    return palabra.replace(" ", "-")
def get_archivo(disponibles, tema):
    archivo = None
    min_len = float('inf')
    for disponible in disponibles:
        if prepararpalabra(tema.lower()) in prepararpalabra(disponible['title'].lower()):
            if len(disponible['title']) < min_len:
                if disponible['link'] is not None:
                    min_len = len(disponible['title'])
                    archivo = disponible['link']
    return archivo
    

def obtener_y_modificar(archivo):
    # Format the URL
    archivo = archivo.replace(' ', '-')
    url = f'https://www.cifraclub.com/{archivo}'
    
    # Make the request to get the page content
    response = requests.get(url)
    
    if response.status_code == 200:
        # Ensure the save directory exists
        print("Consigue la pagina de la cancion")
        if not os.path.exists(SAVE_DIRECTORY):
            os.makedirs(SAVE_DIRECTORY)
        
        # Define the file path
        file_path = os.path.join(SAVE_DIRECTORY, f'{archivo.replace('/','')}.html')


        print("Imprime en", file_path)
        # Save the content to a file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)
        
        print(f'Page saved successfully: {file_path}')
    else:
        print(f'Failed to download page: {url} (Status code: {response.status_code})')


#getpagina("los-caballeros-de-la-quema")
bpms_disponibles = get_bpm_banda("los-caballeros-de-la-quema")
#print(bpms_disponibles)
temas = get_temas("los-caballeros-de-la-quema")
for tema in temas:
    archivo = get_archivo(bpms_disponibles, tema)
    if archivo is not None:
        obtener_y_modificar(archivo)
    #print(f'Obtained BPM for {tema}')