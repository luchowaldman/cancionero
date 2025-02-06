import json
import os
from bs4 import BeautifulSoup
import requests

# Define the directory where the pages will be saved
SAVE_DIRECTORY = 'cifraclub_pages'

def obtener_bpm(band_name, song_name):
    # Format the URL
    band_name = band_name.replace(' ', '-')
    url = f'https://songbpm.com/@{band_name}/{song_name}'
    
    # Make the request to get the page content
    response = requests.get(url)
    
    if response.status_code == 200:




        soup = BeautifulSoup(response.text, 'lxml')   
        bpm_span = soup.find('span', class_='pl-1 text-sm')
        if bpm_span:
            bpm_text = bpm_span.previous_sibling.strip()
            print(f'The BPM for {song_name} by {band_name} is: {bpm_text}')
            return bpm_text
        else:
            return 1



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
            temas.append(spl[1])
    return temas
    

def modificar_bpm(banda, cancion, bpm):
    DIRECTORIO_DATOS = '../cliente/public/data/canciones/'
    filename = f'{banda}_{cancion}.json'
    with open(os.path.join(DIRECTORIO_DATOS, filename), 'r', encoding='utf-8') as file:
        data = json.load(file)
        data['bpm'] = bpm
    with open(os.path.join(DIRECTORIO_DATOS, filename), 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
            

def obtener_y_modificar(banda, cancion):
    bpm = obtener_bpm(banda, cancion)
    print(bpm)
    if bpm:
        modificar_bpm(banda, cancion, float(bpm))
    else:
        print(f'No BPM found for {cancion} by {banda}')


#obtener_y_modificar("los-caballeros-de-la-quema", "avanti-morocha-35b62c92-d7d1-4baa-bff2-f70d3265ce5b")



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




getpagina("los-caballeros-de-la-quema")
bpms_disponibles = get_bpm_banda("los-caballeros-de-la-quema")
#print(bpms_disponibles)
temas = get_temas("los-caballeros-de-la-quema")
for tema in temas:
    archivo = get_archivo(bpms_disponibles, tema)
    if archivo is not None:
        obtener_y_modificar(archivo)