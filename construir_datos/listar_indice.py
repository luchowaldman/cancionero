import requests
import json
import os

DIRECTORIO_DATOS = '../cliente/public/data/'

# Nueva función para imprimir la banda y el nombre del tema
def imprimir_bandas_y_canciones():
    ruta_archivo = os.path.join(DIRECTORIO_DATOS, 'index.json')
    with open(ruta_archivo, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for cancion in data:
            print(f"Banda: {cancion['banda']}, Canción: {cancion['nombre']}")



# Ejemplo de uso: Imprimir banda y nombre de las canciones en index.json
imprimir_bandas_y_canciones()
