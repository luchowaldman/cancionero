import os
import requests
import copy
import json
from bs4 import BeautifulSoup
from acordes import Acordes, Parte
from buscar_partes import ProbarPartes, buscar_partes, tryVN
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
        print(f"Error al obtener ESTE JSON {directorio}, tema {archivo}: {e}")
        return None
    

    
def guardar_tema(banda, tema, data):
    try:
        with open(f'{DIRECTORIO_DATOS}{banda}_{tema}.json', 'w') as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Error al guardar tema de banda {banda}, tema {tema}: {e}")


def renglon_valido(renglon):
    if renglon['tipo'] == 'l':
        texto = renglon['letra'].strip()
        
        excluidos = ['','[Puente]','[Estribillo]','[Solo Final]','[Primera Parte]', 'Intro:','Bajo:','RIFF']
        if texto in excluidos:
            return  False
        
        contiene = ['|Intro', 'Tempo :', '|']
        for cont in contiene:
            if cont in texto:
                return False
    return True

def armar_vector(vector):
    if (len(vector) == 0):
        for i in range(3, 9):
            vector.append([i])
    else:
        toret = []
        for patrones in vector:
            for i in range(1, 9):
                copia = patrones.copy()
                copia.append(i)
                toret.append(copia)
        return toret
    return vector

def probar(prof, acordes):
    formas = []
    toret = prof

    while toret > 0:
        toret = toret - 1
        formas = armar_vector(formas)
    aco, secu = ProbarPartes(formas, acordes)
    dividio = len(secu) > 1
    if (dividio):
        return aco, secu, True
    return aco, secu, False
    




def analizarxletra(banda, tema):
    #print(f"analizarxletra {banda}, {tema}")
    renglones = get_JSON(DIRECTORIO_DATOS_GENERADA, f'{banda}_{tema}')
    if (renglones == None):
        return { 'generado': 0}
    val_reng = []
    if (renglones):
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
            renglon['conl'] = False
            for acor in renglon['acordes']:
                acordes.append(acor['acorde'])
            if i+1 < len(renglones):
                if renglones[i+1]['tipo']=='l':
                    renglon['conl'] = True
                    renglon['letra'] = renglones[i+1]
                    renglones[i+1]['_m'] = 'SI'
            musicas.append(renglon)
        if renglon['tipo'] == 'l':            
            if '_m' not in renglon:
                print("LETRA SIN MUSICA", renglon)
                
                renglon['_m'] = 'NO'
                con_letra_sin_musica = True


            #print (renglon['_m'])
        i = i + 1

    acordes_nuevos = []
    for renglon in renglones:
        if (renglon['tipo'] == 'm' and renglon['conl']):
            for acor in renglon['acordes']:
                acordes_nuevos.append(acor['acorde'])


    son_distintos = (acordes_nuevos != acordes)

    
    resu = len(acordes) == 0
    prof = 1
    max_prof = 5
    while not resu and prof <= max_prof:
        if (prof > 5):            
            print("proxima empieza prueba ",prof,"> 5")
        if son_distintos:
            aco, secu, resu = probar(prof, acordes_nuevos)
        if not resu:
            aco, secu, resu = probar(prof, acordes)
        prof = prof + 1
    prof = prof - 1
        

    if resu:
       #print("encontrada prof", prof, tema)
       a = 4
    else:
        print("no encontrada", tema, len(acordes))

        
    if con_letra_sin_musica:
        print("con letra sin musica", tema)
        return { 'generado': 0 }
    


    #print("Se puede generar completa" , tema)
    return { 'generado': 1 }
