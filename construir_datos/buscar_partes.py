
def PartesDistintas(secuencia):
    return len(set(secuencia))

def contiente(acordes, parte):
    if len(acordes) < len(parte):
        return False
    
    for i in range(len(parte)):
        if acordes[i] != parte[i]:
            return False

    return True

def tryVN(n, acordes_inp):
    acordes = acordes_inp
    partes = []
    secuencia = []
    cont_tam = 0
    while len(acordes) > 0:
        encontro = False
        for p in partes:
            if contiente(acordes, p):
                acordes = acordes[len(p):]
                secuencia.append(partes.index(p))
                encontro = True
                break
        if encontro:
            continue


        # Esto es cuando tiene que agregar una nueva parte
        tam_parte = n[cont_tam]
        cont_tam = (cont_tam + 1) % len(n)
        parte1 = acordes[:tam_parte]        
        if parte1 not in partes:
            partes.append(parte1)
        acordes = acordes[len(parte1):]
        secuencia.append(partes.index(parte1))

    #print (f'partes: {partes}')
    #print (f'secuencia: {secuencia}')  
    return partes, secuencia
    
def ProbarPartes(formas, acordes):
    for forma in formas:
        partes, secuencia = tryVN(forma, acordes)
        dis = PartesDistintas(secuencia)
        #print (f'forma: {forma}, partes: {partes}, secuencia: {secuencia}, dis: {dis}')
        if len(forma) == dis:
            print (f'forma encontrada: {forma} partes: {partes}, secuencia: {secuencia}')
            descartar = False
            for i in range(len(formas) - 1):
                if formas[i] == partes[i].len():
                    descartar = True
                    break
            
            if descartar:
                print (f'forma descartada')
            else:
                return partes, secuencia
    return [acordes], [0]

def buscar_partes(acordes):

    formas = []
    #formas.append([4, 6])

    formas.append([4])
    formas.append([8]) # Flaca
    formas.append([5])
    formas.append([6])
    formas.append([7])
    formas.append([8])
    formas.append([9])
    
    formas.append([4, 4]) # Flaca
    formas.append([8, 8]) # Flaca
    formas.append([5, 5])
    formas.append([6, 6])
    formas.append([7, 7])
    formas.append([8, 8])
    formas.append([9, 9])
    
    formas.append([4, 6]) # Esta saliendo el sol
    formas.append([4, 4, 7]) # Fuego
    formas.append([3, 1, 1, 3]) # Casi sin pensar
    formas.append([3, 3, 4, 5, 4]) # Fuiste lo mejor
    formas.append([1, 4, 4, 4, 4]) # la parte de adelante
    formas.append([2, 4, 4]) # Cuando no estas
    aco, secu = ProbarPartes(formas, acordes)
    if (len(secu)> 1):
        return aco, secu
    
    return [acordes], [0]
    