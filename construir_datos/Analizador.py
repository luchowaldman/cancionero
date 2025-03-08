from acordes import Acordes 


class Analizador:
    def __init__(self, acordes: list[Acordes], textos, acordes_generado, textos_generado):
        self.acordes = acordes
        self.textos = textos
        self.acordes_generado = acordes_generado
        self.textos_generado = textos_generado
        self._maximo_texto = -1

    @property
    def maximo_texto(self):
        if self._maximo_texto != -1:
            return self._maximo_texto
        else:
            raise ValueError("El valor de maximo_texto no ha sido establecido.")
    def BorrarNoTexto(self):
        ok_letras = []
        ok_letras_generadas = []
        for (i_parte, parte) in enumerate(self.textos):
            agregar = True
            self._maximo_texto = max(self._maximo_texto, self.textos_generado[i_parte])
            if parte == ['']:
                agregar = False
            if len(parte) == 1:
                if parte[0] == '[Puente]':
                    agregar = False
            if agregar:
                ok_letras.append(parte)
                ok_letras_generadas.append(self.textos_generado[i_parte])
        self.textos = ok_letras
        self.textos_generado = ok_letras_generadas

    def borrar_generado(self, index):
        self.acordes_generado.pop(index)
        self.textos_generado.pop(index)
    
    def get_renglon_acordes(self):
        acorderet = []
        for acorde in self.acordes_generado:
            acorderet.append(acorde["linea"])
        return set(acorderet)
    
    def obtener_partes_renglon(self, desde, hasta, desde_gen, hasta_gen, con_texto):
        acordes_encontrados = []
        cont = 0
        indice = 0
        while (cont <= hasta_gen) and (indice < len(self.acordes)):
            cont =  self.acordes_generado[indice]['linea']
            if (cont >= desde_gen):
                acordes_encontrados.append(self.acordes[indice])
            indice = indice + 1

        
        if (con_texto):
            print ("Musica, ", desde, hasta, desde_gen, hasta_gen, acordes_encontrados)
        else:
            print ("Letra, ", desde, hasta, desde_gen, hasta_gen, acordes_encontrados)

        
    
    def obtener_partes(self):
        partes = []
        partes_id = []
        #print("self.textos", self.textos_generado)
        item = 0
        acordesId = []
        for acorde in self.acordes_generado:
            acordesId.append(acorde["linea"])
        acordesId = set(acordesId)
        #print("acordesId", acordesId)

        iniciando = True
        ultimo_texto_agregado = 0
        for (texto) in self.textos:
            if iniciando:
                partes.append([self.textos_generado[item], 0])
                partes_id.append([item, 0])
                ultimo_texto_agregado = self.textos_generado[item]
                iniciando = False
            
            texto_agregado_item = self.textos_generado[item]    
            if texto_agregado_item > ultimo_texto_agregado + 2:
                partes.append([self.textos_generado[item], 0])
                partes_id.append([item, 0])
            else:
                partes[len(partes) - 1][1] = self.textos_generado[item]
                partes_id[len(partes_id) - 1][1] = item
            ultimo_texto_agregado = texto_agregado_item
            item = item + 1


            #print("i", self.textos_generado[i])
        partes[len(partes) - 1][1] = item - 1
        return partes, partes_id


    @property
    def obtener_acordes_generado(self):
        return self.acordes_generado

    @property
    def obtener_textos_generado(self):
        return self.textos_generado
    
    @property
    def obtener_acordes(self):
        return self.acordes
    
    @property
    def obtener_textos(self):
        return self.textos
    
