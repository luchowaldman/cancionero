from analisisletra  import analizarxletra
import os
import json

# Define the directory where the pages will be saved
SAVE_DIRECTORY = 'cifraclub_pages'
DIRECTORIO_DATOS = '../cliente/public/data/'
DIRECTORIO_DATOS_GENERADA = 'data_generada/'




def get_JSON(directorio, archivo):
    try:
        with open(f'{directorio}{archivo}.json', 'r') as f:
            data = json.load(f)
            return data
    except Exception as e:
        #print(f"Error al obtener JSON {directorio}, tema {archivo}: {e}")
        return None
    

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


        
resultados = []

arch = obtener_archivos_json(DIRECTORIO_DATOS_GENERADA)
for ar in arch:
    sp = ar.split('_')
    if (len(sp) == 2):
        try:
            if (sp[0] == 'the-beatles'):
                resultados.append(analizarxletra(sp[0], sp[1]))
        except Exception as e:
            #print(f"Error al archivo {ar}: {e}")
            resultados.append({ 'generado': 0 })
generados = 0
for gen in resultados:
    generados = generados + gen['generado']

print("total", len(resultados), "generado", generados)

#analizarxletra('andres calamaro', 'la parte de adelante')
#analizarxletra('intoxicados', 'esta saliendo el sol')
#analizarxletra('intoxicados', 'se fue al cielo')
#analizarxletra('intoxicados', 'casi sin pensar')
#analizarxletra('intoxicados', 'pila pila')
#analizarxletra('intoxicados', 'volver a casa')
#analizarxletra('andres calamaro', 'la parte de adelante')
#analizarxletra('andres calamaro', 'cuando no estas')

exit()
