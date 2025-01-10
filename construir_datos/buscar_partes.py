
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
    
def buscar_partes(acordes):

    formas = []
    #formas.append([4, 6])
    
    formas.append([8]) # Flaca
    formas.append([4, 4]) # Flaca
    formas.append([8, 8]) # Flaca
    
    formas.append([4, 6]) # Esta saliendo el sol
    formas.append([4, 4, 1, 7]) # Fuego
    formas.append([3, 1, 1, 3]) # Casi sin pensar
    formas.append([3, 3, 4, 5, 4]) # Fuiste lo mejor
    
    for forma in formas:
        partes, secuencia = tryVN(forma, acordes)
        dis = PartesDistintas(secuencia)
        if len(forma) == dis:
            print (f'forma encontrada: {forma} partes: {partes}, secuencia: {secuencia}')
            return partes, secuencia
        
    return [acordes], [0]