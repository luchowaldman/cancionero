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
        
        excluidos = ['','[Puente]','[Estribillo]','[sin musica]','[repite todo]','(sin musica)','(repite todo)','[Solo Final]','[Primera Parte]', 'Intro:','Bajo:','RIFF']
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
    
def subtexto(texto, desde, hasta):
        if desde < 0:
            desde = 0
        if hasta > len(texto):
            hasta = len(texto)
        if desde >= hasta:
            return ""
        return texto[desde:hasta]

def letra_separar(verso, acordes):
    intro = ""
    partes = []
    desde = 0
    for aco in acordes:
        sb = subtexto(verso, desde, aco['pos'])
        partes.append(sb)
        desde = aco['pos']
    partes.append(subtexto(verso, desde, len(verso)))
    intro = partes[0]
    partes.pop(0)
    return intro, partes

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
                #print("LETRA SIN MUSICA", renglon)
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
            acordes_de_partes, secu, resu = probar(prof, acordes_nuevos)
        if not resu:
            acordes_de_partes, secu, resu = probar(prof, acordes)
        prof = prof + 1
    prof = prof - 1
        


#    if con_letra_sin_musica:
#        print("con letra sin musica", tema)
#        return { 'generado': 0 }
   

    if resu:
       #print("encontrada prof", prof, aco, secu)
       # ARMO EL ARCHIVO
       letra = []
       secu_fin = []
       termino_secu = True
       indice_secu = -1
       procesando_secu = -1
       #print(acordes_de_partes, secu)
       acordes_agregados = []
       id_renglon = -1

       acordes_originales_renglones = []

    letras_fin = []
    for renglon in renglones:
        id_renglon = id_renglon + 1
        secuenciasagregadas = []
        acordesrenglon = []
        acordes_agregados = []
            #print (renglon)
        if (renglon['tipo'] == 'm'):
                for acor in renglon['acordes']:
                    if termino_secu:
                        termino_secu = False
                        procesando_secu = procesando_secu + 1
                    indice_secu = indice_secu + 1
                    if procesando_secu  >= len(secu):
                        #print("Termino el vector", termino_secu, indice_secu)
                        a = 3
                    else:
                        #print("secuencia", secu[procesando_secu])
                        #print("acordes busca:", procesando_secu, acordes_de_partes[secu[procesando_secu]])
                        acordes_agregados.append(acor['acorde'])
                        termino_secu = len(acordes_de_partes[secu[procesando_secu]])  == len(acordes_agregados)
                        
                        if (renglon['conl']):
                            acordesrenglon.append(acor)
                
                        if termino_secu:
                                secu_fin.append(secu[procesando_secu])
                                secuenciasagregadas.append(secu[procesando_secu])
                                indice_secu = -1
                                acordes_agregados.clear()
                    #print (procesando_secu, indice_secu,termino_secu )

                letra = ""
                if (renglon['conl']):
                    #print("<-- CPM RENGLON -->", acordesrenglon)
                    letra = renglon['letra']['letra']
                    acordes_originales_renglones.append([secuenciasagregadas, acordesrenglon])
                ini_letra, reng_letra = letra_separar(letra, acordesrenglon)
                if (ini_letra.strip != '')  and (len(letras_fin) > 0):
                    try:
                        texto_paragregar = letras_fin[-1][-1]
                        letras_fin[-1][-1] = texto_paragregar  + '/n' + ini_letra
                    except Exception as e:
                        sory_man = 1

                letras_fin.append(reng_letra)
                if len(letras_fin) == 0:
                    print("INICIOOO", ini_letra)
                    letras_fin[0][0] = ini_letra + letras_fin[0][0]
                

        else:
                if renglon['_m'] == 'SI':
                    a = 3

                else:
                    texto_desde = id_renglon                    
                    ind_texto = texto_desde + 1
                    #print(texto_desde, ind_texto)
                    renglones_sinmusica = []
                    renglones_sinmusica.append(renglones[texto_desde])
                    while  (ind_texto < len(renglones)):
                        if (renglones[ind_texto]['tipo'] == 'l'):
                            #print("Agrego renglon sin musica")
                            renglones_sinmusica.append(renglones[ind_texto])
                            renglones[ind_texto]['_m'] = 'SI'
                        else:
                            break
                        ind_texto = ind_texto + 1

                    indice_reng  = 0
                    
                    secuencia_aca, acordes_enrenglon = acordes_originales_renglones[indice_reng]
                    for i in range(texto_desde, ind_texto):
                        for secu_aca in secuencia_aca:
                            secu_fin.append(secu_aca)
                        indice_reng = (indice_reng + 1) % len(acordes_originales_renglones)
                        #print("Ponemos musica para", renglones[i]['letra'], secu_aca, acordes_enrenglon)
                        ini_letra, reng_letra = letra_separar(renglones[i]['letra'], acordes_enrenglon)
                        if (ini_letra.strip != '')  and (len(letras_fin) > 0):
                            texto_paragregar = letras_fin[-1][-1]
                            letras_fin[-1][-1] = texto_paragregar  + '/n' + ini_letra
                        letras_fin.append(reng_letra)
                        


    print("Cancion Completa", acordes_de_partes, secu_fin, letras_fin)

    partes_obj = []
    
    i = 0
    for parte in  acordes_de_partes:
        i = i + 1
        parte = Parte(f"parte{i}", parte)
        partes_obj.append(parte)
    acordes = Acordes(partes_obj, secu_fin)
    data = {
        'tono': 'X',
        'tempo': 60,        
        'compas_cantidad': 4,
        'compas_unidad': 4,
        'acordes': acordes.toJson(),
        'orden_partes': secu_fin,
        'letras': letras_fin,
    }
    guardar_tema(banda, tema, data)

    #print("Se puede generar completa" , tema)
    return { 'generado': 1 }
