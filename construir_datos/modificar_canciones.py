import os
import requests
import json
from bs4 import BeautifulSoup
from acordes import Acordes, Parte
from buscar_partes import buscar_partes


# Define the directory where the pages will be saved
SAVE_DIRECTORY = 'cifraclub_pages'
DIRECTORIO_DATOS = '../cliente/public/data/canciones/'

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
        raise Exception
    
def guardar_tema(banda, tema, data):
    try:
        with open(f'{DIRECTORIO_DATOS}{banda}_{tema}.json', 'w') as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Error al guardar tema de banda {banda}, tema {tema}: {e}")

    tema_nuevo = {}
    try:
        tema_nuevo = {}
        tema_nuevo = { 'banda': banda, 'cancion': tema }
        data = get_tema(banda, tema)
        acordesJSON = getAcordes(data)
        
        tema_nuevo['escala'] = acordesJSON.partes[0].acordes[0] if acordesJSON and acordesJSON.partes and acordesJSON.partes[0].acordes else ''
        
        
        compases = 0
        for parte in acordesJSON.orden_partes:
            compases += len(acordesJSON.partes[parte].acordes)
        acordes = []
        for parte in acordesJSON.partes:
            acordes += parte.acordes
        acordes = set(acordes)

        tema_nuevo['compases'] = compases
        tema_nuevo['len_secuencia'] = len(acordesJSON.orden_partes)
        tema_nuevo['acordes'] = '.'.join(list(acordes)[:6] + (['+'] if len(acordes) > 6 else []))
        tema_nuevo['len_partes'] = [len(parte.acordes) for parte in acordesJSON.partes]



        tema_nuevo['compas_unidad'] = data.get('compas_unidad', 4) if data else 4
        tema_nuevo['compas_cantidad'] = data.get('compas_cantidad', 4) if data else 4
        tema_nuevo['bpm'] = data.get('bpm', 60) if data else 60
        tema_nuevo['calidad'] = data.get('calidad', 1) if data else 1
    except Exception as e:
        tema_nuevo = { 'banda': banda, 'cancion': tema, 'error': str(e), 'calidad': 0,  'estado': 'error' }
        #print(f"Error al procesar banda para el indice {banda}, tema {tema}: {e}")
    return tema_nuevo


def procesar_todos_los_archivos():
    archivos = obtener_archivos_json(DIRECTORIO_DATOS)
    indice = []
    errores = 0


    for archivo in archivos:
        if '_' in archivo:
            
            banda = archivo.split('_')[0]
            tema = archivo.split('_')[1]
            #if (banda != 'intoxicados'):
            try:
                #   continue
                print(f'Procesando tema de banda: {banda}, tema: {tema}')
                temadatos = get_tema(banda, tema)
                if 'bpm' not in temadatos:
                    temadatos['bpm'] = 12  # Default value if bpm is not present
                if temadatos['bpm'] == 12:
                    temadatos['bpm'] = 80
                    guardar_tema(banda, tema, temadatos)
            except Exception as e:
                print(f"Error al procesar tema de banda {banda}, tema {tema}: {e}")
                errores += 1
                continue



procesar_todos_los_archivos()
exit()
indice = []
indice.append(obtenerItemIndice('elvis-presley', 'fool-fool-fool'))
with open(f'{DIRECTORIO_DATOS}indice.json', 'w') as f:
            json.dump(indice, f)