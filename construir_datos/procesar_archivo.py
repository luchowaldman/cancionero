import os
import json
from bs4 import BeautifulSoup


from acordes import Acordes, Parte
from buscar_partes import buscar_partes


SAVE_DIRECTORY = 'cifraclub_pages/'
DIRECTORIO_DATOS = '../cliente/public/data/'

# Función para calcular las partes de la canción

def calcular_partes(acordes, letras):
    
    partes, secuencia = buscar_partes(acordes)
    partes_obj = []
    for (i, parte) in enumerate(partes):
        partes_obj.append(Parte(f'Parte {i + 1}', parte))
    acorde = Acordes(partes_obj, secuencia)
    return acorde.toJson()


# Función para analizar un archivo HTML y guardarlo en JSON
def construiracordes_dehtml(band_name, song_name ):
    # Crear un diccionario para almacenar el análisis
    analisis = {}
    analisis['banda'] = band_name
    analisis['cancion'] = song_name
    band_name = band_name.replace(' ', '-')
    song_name = song_name.replace(' ', '-')
    
    nombre_archivo_html = os.path.join(SAVE_DIRECTORY, f'{band_name}_{song_name}.html')
    nombre_archivo_json  = os.path.join(DIRECTORIO_DATOS, f'{band_name}_{song_name}.json')
    # Leer el contenido del archivo HTML
    with open(nombre_archivo_html, 'r', encoding='utf-8') as file:
        contenido_html = file.read()
    
    # Analizar el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(contenido_html, 'lxml')
    
    
    # Obtener el tono de la canción
    cifra_tom = soup.find('span', id='cifra_tom')
    if cifra_tom and cifra_tom.find('a'):
        tono = cifra_tom.find('a').get_text()
    else:
        tono = 'No se encontró el tono'
    
    analisis['tono'] = tono

    # Crear un diccionario vacío
    lineas_dict = {}
    lineas_tieneacordes = {}
    
    # Obtener los acordes y la letra desde el tag <pre>
    pre_tag = soup.find('pre')
    if pre_tag:
        # Eliminar todos los tags de la clase 'tablatura' y 'cnt'
        for tag in pre_tag.find_all(class_=['tablatura', 'cnt']):
            tag.decompose()
        acordes = []
        letras = []
        lineas = pre_tag.decode_contents().split('\n')
    count = 0



    for i, line in enumerate(lineas):
            if line.strip():  # Verificar si la línea no es un string en blanco
                tiene_acordes = bool(BeautifulSoup(line, 'html.parser').find('b'))
                #print(f'{i}: {tiene_acordes}- {line}')
                if tiene_acordes:
                    addacordes = [b.get_text() for b in BeautifulSoup(line, 'html.parser').find_all('b')]
                    acordes.extend(addacordes)
                else:
                    letras.append([line])


    #print(f'calculo partes: {band_name} - {song_name}')
    analisis['acordes'] = calcular_partes(acordes, letras)
    analisis['letras'] = letras



        
    # Crear el directorio si no existe
    directorio = os.path.dirname(nombre_archivo_json)
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    
    # Guardar el análisis en un archivo JSON
    with open(nombre_archivo_json, 'w', encoding='utf-8') as file:
        json.dump(analisis, file, ensure_ascii=False, indent=4)

# Ejemplo de uso



construiracordes_dehtml('andres calamaro', 'la parte de adelante')
#exit()
construiracordes_dehtml("intoxicados", "fuiste lo mejor")
construiracordes_dehtml("intoxicados", "fuego")
construiracordes_dehtml('intoxicados', 'esta saliendo el sol')
construiracordes_dehtml('intoxicados', 'se fue al cielo')
construiracordes_dehtml('intoxicados', 'casi sin pensar')
construiracordes_dehtml('intoxicados', 'pila pila')
construiracordes_dehtml('intoxicados', 'volver a casa')

construiracordes_dehtml('andres calamaro', 'flaca')
construiracordes_dehtml('andres calamaro', 'la parte de adelante')
construiracordes_dehtml('andres calamaro', 'cuando no estas')
construiracordes_dehtml('andres calamaro', 'te quiero igual')
construiracordes_dehtml('andres calamaro', 'crimenes perfectos')
construiracordes_dehtml('andres calamaro', 'paloma')
construiracordes_dehtml('andres calamaro', 'cartas sin marcar')
construiracordes_dehtml('andres calamaro', 'donde manda marinero')
construiracordes_dehtml('andres calamaro', 'pasemos a otro tema')
construiracordes_dehtml('andres calamaro', 'mi gin tonic')
construiracordes_dehtml('andres calamaro', 'loco')
construiracordes_dehtml('andres calamaro', 'soy tuyo')
construiracordes_dehtml('andres calamaro', 'el salmon')
construiracordes_dehtml('andres calamaro', 'alta suciedad')
construiracordes_dehtml('andres calamaro', 'media veronica')
construiracordes_dehtml('andres calamaro', 'bohemio')
