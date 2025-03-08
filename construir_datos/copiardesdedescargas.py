import os
import re
import glob


DIRECTORIO_DATOS = '../cliente/public/data/canciones/'
DIRECTORIO_DESCARGAS = 'C:\\Users\\luisw\\Downloads\\'
archivos_json = glob.glob(os.path.join(DIRECTORIO_DESCARGAS, '*.json'))
ultimo = {}

for archivo in archivos_json:
    nombre_archivo = os.path.basename(archivo)
    base_nombre_archivo = re.sub(r'\(\d+\)', '', nombre_archivo).replace('.json', '').strip()
    
    match = re.search(r'\((\d+)\)', nombre_archivo)
    numero = int(match.group(1)) if match else 0
    
    if base_nombre_archivo not in ultimo or ultimo[base_nombre_archivo] < numero:
        ultimo[base_nombre_archivo] = numero

for base_nombre_archivo, numero in ultimo.items():
    archivo_original = f"{base_nombre_archivo} ({numero}).json" if numero > 0 else f"{base_nombre_archivo}.json"
    archivo_original_destino = f"{base_nombre_archivo}.json" if numero > 0 else f"{base_nombre_archivo}.json"
    archivo_origen = os.path.join(DIRECTORIO_DESCARGAS, archivo_original)
    archivo_destino = os.path.join(DIRECTORIO_DATOS, archivo_original_destino)
    print(archivo_origen, archivo_destino)
    os.replace(archivo_origen, archivo_destino)
    #os.rename(archivo_origen, archivo_destino)

print(ultimo)