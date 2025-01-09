class Parte:
    def __init__(self, nombre: str, acordes: list):
        self.nombre = nombre
        self.acordes = acordes

class Acordes:
    def __init__(self, partes: list, orden_partes: list):
        self.partes = partes
        self.orden_partes = orden_partes

    def toJson(self):
        return {
            'partes': [parte.__dict__ for parte in self.partes],
            'orden_partes': self.orden_partes
        }