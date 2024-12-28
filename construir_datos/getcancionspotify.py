import requests
import json
import os

# Directorio donde se guardará el archivo index.json 
DIRECTORIO_DATOS = '../cliente/public/data/'

# Tu token de acceso
token = 'BQDaZAgdUftOK3oST4XeYH-Ar56A_60-INUM7sMrI-PpCSlKngAhZEouVjyTW2926pCI4aFm-o6YSCEPKO4ogpw-dOzotSf362I1IXm6NieGj5pn-y4'

# Datos para la solicitud
headers = {
    'Authorization': f'Bearer {token}'
}

# Crear el archivo index.json
def crear_archivo_index():
    if not os.path.exists(DIRECTORIO_DATOS):
        os.makedirs(DIRECTORIO_DATOS)
    
    ruta_archivo = os.path.join(DIRECTORIO_DATOS, 'index.json')
    if not os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'w', encoding='utf-8') as file:
            json.dump([], file, ensure_ascii=False, indent=4)

# Obtener el ID de la banda
def obtener_id_banda(nombre_banda):
    url = 'https://api.spotify.com/v1/search'
    params = {
        'q': nombre_banda,
        'type': 'artist',
        'limit': 1
    }
    response = requests.get(url, headers=headers, params=params)
    
    data = response.json()
    if data['artists']['items']:
        return data['artists']['items'][0]['id']
    else:
        return None

# Obtener los discos de la banda
def obtener_discos_banda(id_banda):
    url = f'https://api.spotify.com/v1/artists/{id_banda}/albums'
    params = {
        'include_groups': 'album',
        'limit': 50
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    discos = [{'nombre_disco': album['name'], 'id_disco': album['id']} for album in data['items']] 
    print ("Discos obtenidos: ", discos)
    return discos

# Obtener las pistas de un disco
def obtener_tracks_disco(id_disco): 
    url = f'https://api.spotify.com/v1/albums/{id_disco}/tracks' 
    params = { 'limit': 50 } 
    response = requests.get(url, headers=headers, params=params) 
    data = response.json() 
    tracks = [{'nombre_pista': track['name'], 'id_pista': track['id']} for track in data['items']] 
    print ("Tracks obtenidos: ", tracks)
    return tracks

# Obtener las características de audio de una pista
def obtener_caracteristicas_track(id_track):
    # audio-analysis
    url = f'https://api.spotify.com/v1/audio-analysis/{id_track}'
    response = requests.get(url, headers=headers)
    data = response.json()
    
    # Verificar que todos los campos estén presentes en los datos
    escala = data.get('key', 'N/A')
    bpm = data.get('tempo', 'N/A')
    modo = 'Mayor' if data.get('mode') == 1 else 'Menor'
    energia = data.get('energy', 'N/A')
    danzabilidad = data.get('danceability', 'N/A')
    acustica = data.get('acousticness', 'N/A')
    instrumentalidad = data.get('instrumentalness', 'N/A')
    valencia = data.get('valence', 'N/A')
    popularidad = data.get('popularity', 'N/A')
    
    return {
        'escala': escala,
        'bpm': bpm,
        'modo': modo,
        'energia': energia,
        'danzabilidad': danzabilidad,
        'acustica': acustica,
        'instrumentalidad': instrumentalidad,
        'valencia': valencia,
        'popularidad': popularidad
    }


# Insertar o actualizar una canción específica en index.json
def insertar_actualizar_cancion(nombre_cancion):
    url = 'https://api.spotify.com/v1/search'
    params = {
        'q': nombre_cancion,
        'type': 'track',
        'limit': 1
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    if data['tracks']['items']:
        track = data['tracks']['items'][0]
        nombre_realcancion = track['name']
        id_cancion = track['id']
        nombre_banda = track['artists'][0]['name']
        id_banda = track['artists'][0]['id']
        caracteristicas = obtener_caracteristicas_track(id_cancion)
        info_cancion = {
            'nombre_cancion': track['name'],
            'nombre_banda': nombre_banda,
            'id_cancion': id_cancion,
            'id_banda': id_banda,
            'estado': 0,
            'bpm': caracteristicas['bpm'],
            'escala': caracteristicas['escala'],
            'modo': caracteristicas['modo'],
            'energia': caracteristicas['energia'],
            'danzabilidad': caracteristicas['danzabilidad'],
            'acustica': caracteristicas['acustica'],
            'instrumentalidad': caracteristicas['instrumentalidad'],
            'valencia': caracteristicas['valencia'],
            'popularidad': caracteristicas['popularidad']
        }

        ruta_archivo = os.path.join(DIRECTORIO_DATOS, 'index.json')
        with open(ruta_archivo, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            cancion_existente = None
            for cancion in data:
                print ("NOMBRE BANDA", nombre_banda, "NOMBRE CANCION",track['name'])
                if cancion['nombre_banda'] == nombre_banda and cancion['nombre_cancion'] == nombre_realcancion:
                    cancion_existente = cancion
                    break
            
            if cancion_existente:
                # Actualizar los datos de la canción existente
                cancion_existente.update(info_cancion)
                print(f'Canción "{nombre_cancion}" actualizada en el índice.')
            else:
                # Insertar nueva canción
                data.append(info_cancion)
                print(f'Canción "{nombre_cancion}" agregada al índice.')

            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)
    else:
        print(f'No se encontró la canción: {nombre_cancion}')




# Crear el archivo index.json
crear_archivo_index()

# Ejemplo de uso: Insertar canciones de Intoxicados en index.json
# insertar_canciones_en_index('Intoxicados')
# insertar_actualizar_cancion('Fuiste lo Mejor')
insertar_actualizar_cancion('Imagine')


