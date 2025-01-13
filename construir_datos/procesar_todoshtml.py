import os
import requests
import json
from bs4 import BeautifulSoup

# Define the directory where the pages will be saved
SAVE_DIRECTORY = 'cifraclub_pages'
DIRECTORIO_DATOS_GENERADA = 'data_generada/'
# nombre_archivo_json  = os.path.join(DIRECTORIO_DATOS, f'{band_name}_{song_name}.json')
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

def existe_preprocesado(band_name, song_name ):
    # Crear un diccionario para almacenar el análisis
    band_name = band_name.replace(' ', '-')
    song_name = song_name.replace(' ', '-')
    nombre_archivo_generado_json  = os.path.join(DIRECTORIO_DATOS_GENERADA, f'{band_name}_{song_name}.json')
    return os.path.isfile(nombre_archivo_generado_json)
# Función para analizar un archivo HTML y guardarlo en JSON
def construir_prearchivo(band_name, song_name ):
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



arch = obtener_archivos(SAVE_DIRECTORY)
desde, hasta = 45, 1500
cont = 0
for archivo in arch:
    print (archivo, desde, hasta, cont)
    if (desde > cont):
        cont = cont  + 1
        continue
    if (cont > hasta):
        break
        

    spl = archivo.split('_')
    
    if (len(spl)==2):
        try:       
            if (not existe_preprocesado(spl[0],spl[1])):
                print ("Procesar", spl[0],spl[1])
                construir_prearchivo(spl[0],spl[1])
        except:
            print("Error procesando")
    else:
        print (cont, archivo)
    cont = cont  + 1


    