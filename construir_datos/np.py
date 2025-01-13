import json

data = '''[
    {
        "tipo": "m",
        "linea": 10,
        "acordes": [
            {
                "acorde": "D",
                "pos": 0
            },
            {
                "acorde": "A",
                "pos": 20
            }
        ]
    },
    {
        "tipo": "l",
        "linea": 11,
        "letra": "Esta vez es en serio"
    },
    {
        "tipo": "m",
        "linea": 12,
        "acordes": [
            {
                "acorde": "G",
                "pos": 13
            }
        ]
    },
    {
        "tipo": "l",
        "linea": 13,
        "letra": "No estoy mintiendo"
    },
    {
        "tipo": "l",
        "linea": 14,
        "letra": "Esto está agrupado"
    },
    {
        "tipo": "m",
        "linea": 15,
        "acordes": [
            {
                "acorde": "A",
                "pos": 6
            }
        ]
    }
]'''

renglones = json.loads(data)

partes = []
i = 0
while i < len(renglones):
    elemento = renglones[i]

    if elemento["tipo"] == "m":
        if i + 1 < len(renglones) and renglones[i + 1]["tipo"] == "l":
            parte = {
                "tipo": "letra_y_musica",
                "elementos": [elemento, renglones[i + 1]]
            }
            i += 1  # Saltar la siguiente línea porque ya fue agregada
        else:
            parte = {
                "tipo": "solo_musica",
                "elementos": [elemento]
            }
    elif elemento["tipo"] == "l":
        letras = [elemento]
        while i + 1 < len(renglones) and renglones[i + 1]["tipo"] == "l":
            letras.append(renglones[i + 1])
            i += 1
        parte = {
            "tipo": "solo_letra",
            "elementos": letras
        }

    partes.append(parte)
    i += 1

print("Partes:", json.dumps(partes, indent=4))




import os
import json

from acordes import Acordes, Parte
from buscar_partes import buscar_partes


SAVE_DIRECTORY = 'cifraclub_pages/'
DIRECTORIO_DATOS = '../cliente/public/data/'
DIRECTORIO_DATOS_GENERADA = 'data_generada/'
# Función para calcular las partes de la canción
def nocalcular_partes(acordes, letras):
    
    partes, secuencia = [acordes], [0]
    partes_obj = []
    for (i, parte) in enumerate(partes):
        partes_obj.append(Parte(f'Parte {i + 1}', parte))
    acorde = Acordes(partes_obj, secuencia)
    return acorde.toJson()

    
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
    to_json = {}
    to_json['banda'] = band_name
    to_json['cancion'] = song_name
    to_json['tempo'] = 60
    to_json['compas_cantidad'] = 4
    to_json['compas_unidad'] = 4
    to_json['tono'] = ''

    to_gene = {}

    
    band_name = band_name.replace(' ', '-')
    song_name = song_name.replace(' ', '-')
    
    nombre_archivo_html = os.path.join(SAVE_DIRECTORY, f'{band_name}_{song_name}.html')
    nombre_archivo_json  = os.path.join(DIRECTORIO_DATOS, f'{band_name}_{song_name}.json')
    nombre_archivo_generado_json  = os.path.join(DIRECTORIO_DATOS_GENERADA, f'{band_name}_{song_name}.json')
    # Leer el contenido del archivo HTML
    print (f'leyendo archivo: {nombre_archivo_html}')
    with open(nombre_archivo_html, 'r', encoding='utf-8') as file:
        contenido_html = file.read()
    
    print(contenido_html)
    exit()
    
    
    # Obtener el tono de la canción
    cifra_tom = soup.find('span', id='cifra_tom')
    if cifra_tom and cifra_tom.find('a'):
        tono = cifra_tom.find('a').get_text()
    else:
        tono = 'No se encontró el tono'
    
    to_json['tono'] = tono

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
        acordes_gen = []
        letras = []
        letras_gen = []
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
    to_json['acordes'] = nocalcular_partes(acordes, letras)
    to_json['letras'] = letras



        
    # Crear el directorio si no existe
    directorio = os.path.dirname(nombre_archivo_json)
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    
    # Guardar el análisis en un archivo JSON
    with open(nombre_archivo_json, 'w', encoding='utf-8') as file:
        json.dump(to_json, file, ensure_ascii=False, indent=4)

# Ejemplo de uso

print('Construyendo acordes de canciones...')
construiracordes_dehtml('andres calamaro', 'la parte de adelante')
exit()

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
