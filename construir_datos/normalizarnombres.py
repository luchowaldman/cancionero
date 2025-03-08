import unidecode

def normalizar_nombre(nombre):
    # Convertir nombre a minúsculas
    nombre = nombre.lower()
    
    # Reemplazar espacios por '-'
    nombre = nombre.replace(' ', '-')
    nombre = nombre.replace(',', '')
    nombre = nombre.replace('?', '')
    nombre = nombre.replace('¿', '')
    nombre = nombre.replace('!', '')
    nombre = nombre.replace('¡', '')
    nombre = nombre.replace('.', '')
    
    # Eliminar acentos
    nombre = unidecode.unidecode(nombre)
    
    return nombre
