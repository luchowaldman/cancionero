import os
import json
from bs4 import BeautifulSoup

SAVE_DIRECTORY = 'cifraclub_pages/'
DIRECTORIO_DATOS = '../cliente/public/data/'





def tryN(n, parte):
    acordes = parte.get('acordes')
    print((len(acordes) + 1) % 4)



    orden_partes = [0]    
    parte_ret = { 'nombre': 'parte1', 'acordes': acordes }
    return parte_ret, orden_partes

    
     
# Función para calcular las partes de la canción
def calcular_partes(acordes, letras):
    
    parte = { 'nombre': 'parte1', 'acordes': acordes }
    orden_partes = [0]

    parte, orden_partes = tryN(1, parte)


    return {
        'partes': [parte],
        'orden_partes': orden_partes
    }


# Función para analizar un archivo HTML y guardarlo en JSON
def analizar_html_y_guardar_en_json(band_name, song_name ):
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
                lineas_dict[count] = line
                lineas_tieneacordes[count] = tiene_acordes
                count += 1

    i = 0
    while i < len(lineas_dict):
        tiene_acordes = lineas_tieneacordes[i]
        if not (tiene_acordes):
            acordes.append('')
            letras.append([lineas_dict[i]])
            i += 1
        else:
            if (i == len(lineas) - 1) or (lineas_tieneacordes[i + 1]):
                addacordes = [b.get_text() for b in BeautifulSoup(lineas_dict[i], 'html.parser').find_all('b')]
                acordes.extend(addacordes)
                addtexto = ['' for _ in addacordes]
                letras.append(addtexto)
                i += 1
            else:
                addacordes = [b.get_text() for b in BeautifulSoup(lineas_dict[i], 'html.parser').find_all('b')]
                acordes.extend(addacordes)

                positions = []
                last_pos = 0
                for b in BeautifulSoup(lineas_dict[i], 'html.parser').find_all('b'):
                    pos = lineas_dict[i].find(b.get_text(), last_pos)
                    positions.append(pos)
                    last_pos = pos + len(b.get_text())
                
                addtexto = []
                last_pos = 0
                for pos in positions:
                    addtexto.append(lineas[i + 1][last_pos:pos])
                    last_pos = pos
                addtexto.append(lineas[i + 1][last_pos:])
                letras.append(addtexto)
                i += 2
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
# analizar_html_y_guardar_en_json("intoxicados", "fuiste lo mejor")
# analizar_html_y_guardar_en_json("intoxicados", "fuego")

analizar_html_y_guardar_en_json('intoxicados', 'esta saliendo el sol')
analizar_html_y_guardar_en_json('intoxicados', 'se fue al cielo')
analizar_html_y_guardar_en_json('intoxicados', 'casi sin pensar')
analizar_html_y_guardar_en_json('intoxicados', 'pila pila')
analizar_html_y_guardar_en_json('intoxicados', 'volver a casa')