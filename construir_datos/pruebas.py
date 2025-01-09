import os
import json
from bs4 import BeautifulSoup

# Función para analizar un archivo HTML y guardarlo en JSON
def analizar_html_y_guardar_en_json(nombre_archivo_html, nombre_archivo_json):
    # Leer el contenido del archivo HTML
    with open(nombre_archivo_html, 'r', encoding='utf-8') as file:
        contenido_html = file.read()
    
    # Analizar el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(contenido_html, 'lxml')
    
    # Crear un diccionario para almacenar el análisis
    analisis = {}
    
    # Obtener el tono de la canción
    cifra_tom = soup.find('span', id='cifra_tom')
    if cifra_tom and cifra_tom.find('a'):
        tono = cifra_tom.find('a').get_text()
    else:
        tono = 'No se encontró el tono'
    
    analisis['tono'] = tono
    
    # Ejemplo de análisis: obtener el título del documento
    titulo = soup.title.string if soup.title else 'No se encontró título'
    analisis['titulo'] = titulo
    
    # Ejemplo de análisis: obtener todos los párrafos
    parrafos = [p.get_text() for p in soup.find_all('p')]
    analisis['parrafos'] = parrafos
    
    # Ejemplo de análisis: obtener todos los enlaces
    enlaces = [{'texto': a.get_text(), 'href': a['href']} for a in soup.find_all('a', href=True)]
    analisis['enlaces'] = enlaces

    # Obtener los acordes y la letra desde el tag <pre>
    pre_tag = soup.find('pre')
    if pre_tag:
        acordes = []
        letras = []
        for line in pre_tag.get_text().split('\n'):
            acorde_linea = []
            letra_linea = []
            last_index = 0
            for tag in pre_tag.find_all('b'):
                acorde = tag.get_text()
                acordes.append(acorde)
                acorde_linea.append(acorde)
                acorde_start = line.find(acorde, last_index)
                if acorde_start != -1:
                    letra_linea.append(line[last_index:acorde_start].strip())
                    last_index = acorde_start + len(acorde)
            letra_linea.append(line[last_index:].strip())
            letras.append(letra_linea)
        analisis['acordes'] = acordes
        analisis['letras'] = letras
    else:
        analisis['acordes'] = 'No se encontraron acordes'
        analisis['letras'] = 'No se encontraron letras'
    
    # Crear el directorio si no existe
    directorio = os.path.dirname(nombre_archivo_json)
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    
    # Guardar el análisis en un archivo JSON
    with open(nombre_archivo_json, 'w', encoding='utf-8') as file:
        json.dump(analisis, file, ensure_ascii=False, indent=4)

# Ejemplo de uso
nombre_archivo_html = 'ejemplo.html'
nombre_archivo_json = './datos/analisis_ejemplo.json'
analizar_html_y_guardar_en_json(nombre_archivo_html, nombre_archivo_json)
