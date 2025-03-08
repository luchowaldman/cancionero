import os
import json
from bs4 import BeautifulSoup


from acordes import Acordes, Parte
from buscar_partes import buscar_partes


SAVE_DIRECTORY = 'cifraclub_pages/'
DIRECTORIO_DATOS = '../cliente/public/data/'
DIRECTORIO_DATOS_GENERADA = 'data_generada/'
# Función para calcular las partes de la canción
def nocalcular_partes(acordes, letras):
    acorde = Acordes([Parte('p1', [acordes])], [0])
    return acorde.toJson()

    
def calcular_partes(acordes, letras):
    
    partes, secuencia = buscar_partes(acordes)
    partes_obj = []
    for (i, parte) in enumerate(partes):
        partes_obj.append(Parte(f'Parte {i + 1}', parte))
    acorde = Acordes(partes_obj, secuencia)
    return acorde.toJson()


# Función para analizar un archivo HTML y guardarlo en JSON
def construir_prearchivo(band_name, song_name ):
    # Crear un diccionario para almacenar el análisis
    data_gen = {}
    band_name = band_name.replace(' ', '-')
    song_name = song_name.replace(' ', '-')
    
    nombre_archivo_html = os.path.join(SAVE_DIRECTORY, f'{band_name}_{song_name}.html')
#    nombre_archivo_json  = os.path.join(DIRECTORIO_DATOS, f'{band_name}_{song_name}.json')
    nombre_archivo_generado_json  = os.path.join(DIRECTORIO_DATOS_GENERADA, f'{band_name}_{song_name}.json')
    # Leer el contenido del archivo HTML
    print (f'leyendo archivo: {nombre_archivo_html}')
    with open(nombre_archivo_html, 'r', encoding='utf-8') as file:
        contenido_html = file.read()
    
    # Analizar el contenido HTML con BeautifulSoup
    
    
    renglones = []
    
    # Obtener los acordes y la letra desde el tag <pre>
    soup = BeautifulSoup(contenido_html, 'lxml')
    pre_tag = soup.find('pre')
    if pre_tag:
        # Eliminar todos los tags de la clase 'tablatura' y 'cnt'
        for tag in pre_tag.find_all(class_=['tablatura', 'cnt']):
            tag.decompose()
        lineas = pre_tag.decode_contents().split('\n')
    max_renglon = 0
    for i, line in enumerate(lineas):
        #print(i, line)
        pos = 0
        acorde_inline = line.split('<b>')
        tiene_acordes = (len(acorde_inline) > 1)
        if (not tiene_acordes):
            pos = 0
            renglones.append({'tipo': 'l', 'linea':i, 'letra': line } )
            #print (i, line)
        else:
            acordes = []
            for acorde in acorde_inline:
                if acorde.__contains__('</b>'):
                    acorde_r = acorde.split('</b>')[0]
                    acordes.append({'acorde':acorde_r, 'pos': pos})
                pos += len(acorde)
            renglones.append({'tipo': 'm', 'linea':i, 'acordes': acordes })
            
        
    with open(nombre_archivo_generado_json, 'w', encoding='utf-8') as file:
        json.dump(renglones, file, ensure_ascii=False, indent=4)

    return 'ok'
# Ejemplo de uso



print('Construyendo acordes de canciones...')

construir_prearchivo('intoxicados', 'casi sin pensar')
construir_prearchivo("intoxicados", "fuego")
construir_prearchivo("intoxicados", "fuiste lo mejor")
construir_prearchivo('andres-calamaro', 'la parte de adelante')
construir_prearchivo('intoxicados', 'esta saliendo el sol')
construir_prearchivo('intoxicados', 'se fue al cielo')
construir_prearchivo('intoxicados', 'casi sin pensar')
construir_prearchivo('intoxicados', 'pila pila')
construir_prearchivo('intoxicados', 'volver a casa')

construir_prearchivo('andres calamaro', 'flaca')
construir_prearchivo('andres calamaro', 'la parte de adelante')
construir_prearchivo('andres calamaro', 'cuando no estas')
exit()
construir_prearchivo('andres calamaro', 'te quiero igual')
construir_prearchivo('andres calamaro', 'crimenes perfectos')
construir_prearchivo('andres calamaro', 'paloma')
construir_prearchivo('andres calamaro', 'cartas sin marcar')
construir_prearchivo('andres calamaro', 'donde manda marinero')
construir_prearchivo('andres calamaro', 'pasemos a otro tema')
construir_prearchivo('andres calamaro', 'mi gin tonic')
construir_prearchivo('andres calamaro', 'loco')
construir_prearchivo('andres calamaro', 'soy tuyo')
construir_prearchivo('andres calamaro', 'el salmon')
construir_prearchivo('andres calamaro', 'alta suciedad')
construir_prearchivo('andres calamaro', 'media veronica')
construir_prearchivo('andres calamaro', 'bohemio')
