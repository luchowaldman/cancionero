import os
import requests
import json
from bs4 import BeautifulSoup
from acordes import Acordes, Parte
from buscar_partes import ProbarPartes, buscar_partes
from Analizador  import Analizador


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
        print(f"Error al obtener JSON {directorio}, tema {archivo}: {e}")
        return None
    

    
def guardar_tema(banda, tema, data):
    try:
        with open(f'{DIRECTORIO_DATOS}{banda}_{tema}.json', 'w') as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Error al guardar tema de banda {banda}, tema {tema}: {e}")


def renglon_valido(renglon):
    if renglon['tipo'] == 'l':
        excluidos = ['','[Puente]','[Estribillo]','[Solo Final]','[Primera Parte]']
        if renglon['letra'] in excluidos:
            return  False
    return True



def analizarxletra(banda, tema):
    print(f"analizarxletra {banda}, {tema}")
    renglones = get_JSON(DIRECTORIO_DATOS_GENERADA, f'{banda}_{tema}')
    val_reng = []
    for renglon in renglones:
        if (renglon_valido(renglon)):
            val_reng.append(renglon)
    renglones = val_reng

    partes = []
    i = 0
    nuevo = True
    parte = { 'tipo':'0', 'letra': [], 'musica': []}

    musicas = []
    acordes = []
    con_letra_sin_musica = False
    while i < len(renglones):
        renglon = renglones[i]
        if renglon['tipo'] == 'm':
            for acor in renglon['acordes']:
                acordes.append(acor['acorde'])
            if renglones[i+1]['tipo']=='l':
                renglon['conl'] = True
                renglon['letra'] = renglones[i+1]
                renglones[i+1]['_m'] = 'SI'
            musicas.append(renglon)
        if renglon['tipo'] == 'l':            
            if '_m' not in renglon:
                print("LETRA SIN MUSICA", renglon)
                renglon['_m'] = 'NO'
                print(renglones[i+1])
                con_letra_sin_musica = True


            #print (renglon['_m'])
        i = i + 1

    #for mus in musicas:
    #    print(mus)   
    
    formas = []
    formas.append([4])
    formas.append([8])
    for i in range(4, 8):
        formas.append([4, i])
    for i in range(4, 8):
        formas.append([4, 4, i])
    
    
    aco, secu = ProbarPartes(formas, acordes)
    if len(secu) == 1:
        print("No encontre el patron")
        return { 'generado': 0 }

    if con_letra_sin_musica:
        print("con letra sin musica")
        return { 'generado': 0 }


    print("Se puede generar completa")
    return { 'generado': 1 }


        
resultados = []
resultados.append(analizarxletra('intoxicados', 'fuego'))
resultados.append(analizarxletra('andres-calamaro', 'flaca'))
resultados.append(analizarxletra("intoxicados", "fuiste-lo-mejor"))
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
