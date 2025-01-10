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
        print(f"Error al obtener tema de banda {banda}, tema {tema}: {e}")
        return None
    
def guardar_tema(banda, tema, data):
    try:
        with open(f'{DIRECTORIO_DATOS}{banda}_{tema}.json', 'w') as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Error al guardar tema de banda {banda}, tema {tema}: {e}")


def reordenar_acordes(banda, tema):
    try:
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
            acordes = Acordes(partes_obj, acordes_data['orden_partes'])
            if (acordes.orden_partes != [0]):
                print(f"Reordenando{tema} , {banda}", acordes.partes[0].acordes)
                todos_acordes = []
                for parte in acordes.orden_partes:
                    todos_acordes += acordes.partes[parte].acordes
                print( todos_acordes)


                acordes = Acordes([Parte("p1-rg", [todos_acordes])], [0])
                                  

            if (acordes.orden_partes == [0]):
                print(f"Inicial{tema} , {banda}", acordes.partes[0].acordes)

                partes, secuencia = buscar_partes(acordes.partes[0].acordes)
                partes_obj = []
                for (i, parte) in enumerate(partes):
                    partes_obj.append(Parte(f'Parte {i + 1}', parte))
                acordes = Acordes(partes_obj, secuencia)

            data['acordes'] = acordes.toJson()


            #partes = [Parte(parte['nombre'], parte['acordes']) for parte in acordes_data['partes']]
            #acordes = Acordes(partes, acordes_data['orden_partes'])
            #print(acordes_data['partes'])
            
            
            guardar_tema(banda, tema, data)
        
            
        
    except Exception as e:
        print(f"Error al reordenar acordes de banda {banda}, tema {tema}: {e}")

def hacer_archivo():
    archivos = obtener_archivos_json(DIRECTORIO_DATOS)
    for archivo in archivos:
        if '_' in archivo:
            banda = archivo.split('_')[0]
            tema = archivo.split('_')[1]
            print(f'Ordenando banda: {banda}, tema: {tema}')
            try:
                reordenar_acordes(banda, tema)
            except Exception as e:
                print(f"Error al procesar banda {banda}, tema {tema}: {e}")

#reordenar_acordes('andres-calamaro', 'ansia-en-plaza-francia')
reordenar_acordes('andres-calamaro', 'Aguas-peligrosas')
