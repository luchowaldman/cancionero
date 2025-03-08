import os
import requests
import json
from bs4 import BeautifulSoup
from acordes import Acordes, Parte
from buscar_partes import buscar_partes


# Define the directory where the pages will be saved
SAVE_DIRECTORY = 'cifraclub_pages'
DIRECTORIO_DATOS = '../cliente/public/data/'

def obtener_archivos_json(directorio):
    archivos = []
    try:
        for archivo in os.listdir(directorio):
            if archivo.endswith('.json'):
                archivos.append(archivo.replace('.json', '')) 
        return archivos
    except Exception as e:
        print(f"Error al leer el directorio: {e}")
        return []




def get_tema(banda, tema):
    try:
        with open(f'{DIRECTORIO_DATOS}{banda}_{tema}.json', 'r') as f:
            data = json.load(f)
            return data
    except Exception as e:
        throw(e)
        return None
    
def guardar_tema(banda, tema, data):
    try:
        with open(f'{DIRECTORIO_DATOS}{banda}_{tema}.json', 'w') as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Error al guardar tema de banda {banda}, tema {tema}: {e}")

estatadisticas = {}

def gettemaJSON(banda, tema):
    data = get_tema(banda, tema)
    if data:
            #print("data", data)
            acordes_data = data['acordes']
            partes = acordes_data['partes']
            partes_obj = []
            for parte in  partes:
                #print("parte", parte['nombre'], parte['acordes'])
                parte = Parte(parte['nombre'], parte['acordes'])
                partes_obj.append(parte)
            return Acordes(partes_obj, acordes_data['orden_partes'])


archivos = obtener_archivos_json(DIRECTORIO_DATOS)
total = 0
totalvalidos = 0
errores = 0
solounaparte = 0
dos = 0
masdedos = 0

for archivo in archivos:
    total = total + 1
    if '_' in archivo:
        banda = archivo.split('_')[0]
        tema = archivo.split('_')[1]
        try:
            temaJSON = gettemaJSON(banda, tema)
            if (temaJSON.orden_partes == [0]):
                solounaparte = solounaparte + 1
            elif (len(temaJSON.partes) == 2):
                dos = dos + 1
            else:
                masdedos = masdedos + 1
            totalvalidos = totalvalidos + 1
        except Exception as e:
            errores = errores + 1
            #print(f"Error al procesar banda {banda}, tema {tema}: {e}")

print(f"Total: {total}, totalvalidos: {totalvalidos}, errores: {errores}")
print(f"Solounaparte: {solounaparte}, dos: {dos}, masdedos: {masdedos}")