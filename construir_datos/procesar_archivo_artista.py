import os
import json
from bs4 import BeautifulSoup


from acordes import Acordes, Parte
from buscar_partes import buscar_partes


SAVE_DIRECTORY = 'cifraclub_pages/'
DIRECTORIO_DATOS = '../cliente/public/data/'

# Función para calcular las partes de la canción

# Función para analizar un archivo HTML y guardarlo en JSON
def procesar_html_artista(band_name):
    # Crear un diccionario para almacenar el análisis
    analisis = {}
    analisis['banda'] = band_name
    band_name = band_name.replace(' ', '-')
    
    nombre_archivo_html = os.path.join(SAVE_DIRECTORY, f'{band_name}.html')
    nombre_archivo_json  = os.path.join(DIRECTORIO_DATOS, f'{band_name}.json')
    # Leer el contenido del archivo HTML
    with open(nombre_archivo_html, 'r', encoding='utf-8') as file:
        contenido_html = file.read()
    
    # Analizar el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(contenido_html, 'lxml')
    
    
    # Obtener el tono de la canción
    todaslascanciones = soup.find('ul', id='js-a-songs')
    lis = todaslascanciones.find_all('li')
    canciones = []
    for (i, li) in enumerate(lis):
        a = li.find('a')
        if a:
            cancion = a.get_text()
            canciones.append(cancion)
            print (f'cancion: {cancion}')
            

    # Crear el directorio si no existe
    directorio = os.path.dirname(nombre_archivo_json)
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    
    # Guardar el análisis en un archivo JSON
    with open(nombre_archivo_json, 'w', encoding='utf-8') as file:
        json.dump(canciones, file, ensure_ascii=False, indent=4)

# Ejemplo de uso


#procesar_html_artista("estelares")

#procesar_html_artista("los-rodriguez")

procesar_html_artista("the-who")
procesar_html_artista("abel-pintos")
procesar_html_artista("atahualpa-yupanqui")
procesar_html_artista("jorge-cafrune")
procesar_html_artista("horacio-guarany")
procesar_html_artista("julio-sosa")
procesar_html_artista("anibal-troilo")
procesar_html_artista("sumo")
procesar_html_artista("ariana-grande")
procesar_html_artista("alice-in-chains")
procesar_html_artista("attaque-77")
procesar_html_artista("alice-in-chains")
procesar_html_artista("alice-in-chains")
procesar_html_artista("depeche-mode")
procesar_html_artista("deep-purple")
procesar_html_artista("daft-punk")
procesar_html_artista("diego-torres-musicas")
procesar_html_artista("dire-straits")
procesar_html_artista("dread-mar-i")
procesar_html_artista("los-chalchaleros")
procesar_html_artista("sesto-camilo")
procesar_html_artista("disney")
procesar_html_artista("the-cure")
procesar_html_artista("canciones-populares")
procesar_html_artista("creedence-clearwater-revival")
procesar_html_artista("britney-spears")
procesar_html_artista("backstreet-boys")
procesar_html_artista("buena-vista-social-club")
procesar_html_artista("blur")
procesar_html_artista("bon-jovi")
procesar_html_artista("billy-joel")
procesar_html_artista("bad-bunny")
procesar_html_artista("bruno-mars")
procesar_html_artista("billie-eilish")
procesar_html_artista("el-mato-un-policia-motorizado")
procesar_html_artista("estelares")
exit()

procesar_html_artista("enanitos-verdes")
procesar_html_artista("mon-laferte")
procesar_html_artista("trio-los-panchos")
procesar_html_artista("airbag")
procesar_html_artista("nathy-peluso")
procesar_html_artista("nirvana")
procesar_html_artista("babasonicos")
exit()

procesar_html_artista("mala-fama")
procesar_html_artista("bizarrap")
procesar_html_artista("phil-collins")
procesar_html_artista("yes")
procesar_html_artista("ramones")
procesar_html_artista("muse")
procesar_html_artista("radiohead")
procesar_html_artista("u2")
procesar_html_artista("genesis")
procesar_html_artista("coldplay")
procesar_html_artista("divididos")
procesar_html_artista("traveling-wilburys")
procesar_html_artista("david-bowie")
procesar_html_artista("elton-john")



exit()
procesar_html_artista("dillom")
procesar_html_artista("nathy-peluso")
procesar_html_artista("los-caballeros-de-la-quema")
procesar_html_artista("ivan-noble")
procesar_html_artista("bee-gees")
procesar_html_artista("l-gante")
procesar_html_artista("bob-marley")
procesar_html_artista("queen")
procesar_html_artista("the-police")
procesar_html_artista("the-clash")
procesar_html_artista("the-cranberries")
procesar_html_artista("the-doors")
procesar_html_artista("los-autenticos-decadentes")
procesar_html_artista("rem")
procesar_html_artista("los-pericos")
procesar_html_artista("los-piojos")
procesar_html_artista("vilma-palma-e-vampiros")
procesar_html_artista("bersuit-vergarabat")

procesar_html_artista("led-zeppelin")
procesar_html_artista("michael-jackson")
procesar_html_artista("gilda")
procesar_html_artista("supertramp")
procesar_html_artista("rodrigo")
procesar_html_artista("damas-gratis")
procesar_html_artista("aerosmith")
procesar_html_artista("los-palmeras")
procesar_html_artista("calle-13")
procesar_html_artista("silvio-rodriguez")
procesar_html_artista("pablo-milanes")
procesar_html_artista("fabiana-cantilo")
procesar_html_artista("ac-dc")
procesar_html_artista("the-smiths")
procesar_html_artista("leo-garcia")
exit()

procesar_html_artista("zambayonny")
exit()
procesar_html_artista("alejandro-sanz")
procesar_html_artista("luis-fonsi")
procesar_html_artista("arjona-ricardo")
procesar_html_artista("luis-miguel")
procesar_html_artista("calle-13")
procesar_html_artista("mana")
procesar_html_artista("manal")
procesar_html_artista("sui-generis")
exit()

procesar_html_artista("parra-violeta")
procesar_html_artista("alfredo-zitarrosa")
procesar_html_artista("elvis-presley")
procesar_html_artista("michael-jackson")
procesar_html_artista("aretha-franklin")
procesar_html_artista("frank-sinatra")
procesar_html_artista("bruce-springsteen")
procesar_html_artista("stevie-wonder") 
procesar_html_artista("taylor-swift")
procesar_html_artista("lady-gaga")
procesar_html_artista("jay-z")
procesar_html_artista("kanye-west")

exit()
#procesar_html_artista("parra-violeta")
#procesar_html_artista("alfredo-zitarrosa")

#procesar_html_artista("elvis-presley")
#procesar_html_artista("michael-jackson")
#procesar_html_artista("aretha-franklin")
#procesar_html_artista("frank-sinatra")
#procesar_html_artista("madonna")
#procesar_html_artista("bruce-springsteen")
#procesar_html_artista("beyonce") 
#procesar_html_artista("stevie-wonder") 
#procesar_html_artista("prince")
#procesar_html_artista("lady-gaga")
#procesar_html_artista("beyonce")
#procesar_html_artista("jay-z")
#procesar_html_artista("kanye-west")
#procesar_html_artista("rihanna")
#procesar_html_artista("billy-joel")
#procesar_html_artista("john-legend")
#procesar_html_artista("elton-john")
#procesar_html_artista("bruno-mars")
#procesar_html_artista("katy-perry")

exit()

procesar_html_artista("ruben-rada")
procesar_html_artista("natalia-oreiro")
procesar_html_artista("leon-gieco")
procesar_html_artista("victor-jara")
procesar_html_artista("gilberto-gil")
procesar_html_artista("roberto-carlos")
procesar_html_artista("milton-nascimento")


procesar_html_artista("victor-jara")
procesar_html_artista("gilberto-gil")
procesar_html_artista("roberto-carlos")
procesar_html_artista("milton-nascimento")

procesar_html_artista("chico-buarque")
procesar_html_artista("caetano-veloso")
procesar_html_artista("leo-masliah")
procesar_html_artista("jorge-drexler")


procesar_html_artista("sandro")
procesar_html_artista("palito-ortega")
procesar_html_artista("jimenez-jose-alfredo")
procesar_html_artista("george-harrison")

procesar_html_artista("conociendo-rusia")
procesar_html_artista("carlos gardel")
procesar_html_artista("roberto-goyeneche")
procesar_html_artista("la-mosca")
procesar_html_artista("almendra")
procesar_html_artista("jim-morrison")
procesar_html_artista("john-lennon")
procesar_html_artista("paul-mccartney")
procesar_html_artista("jose-larralde")
procesar_html_artista("jorge-cafrune")
procesar_html_artista("mercedes-sosa")
procesar_html_artista("los-chalchaleros")
procesar_html_artista("los-nocheros")
procesar_html_artista("los-tekis")
procesar_html_artista("la-mona-gimenez")
procesar_html_artista("almafuerte")
procesar_html_artista("os-paralamas-do-sucesso")

exit()
procesar_html_artista("los piojos")
procesar_html_artista("bersuit-vergarabat")

procesar_html_artista("el-bordo")
procesar_html_artista("la-25")
procesar_html_artista("la-vela-puerca")
procesar_html_artista("las-pastillas-del-abuelo")
procesar_html_artista("los-autenticos-decadentes")
procesar_html_artista("los-caballeros-de-la-quema")
procesar_html_artista("los-fabulosos-cadillacs")
procesar_html_artista("los-piojos")
procesar_html_artista("manu-chao")
procesar_html_artista("no-te-va-gustar")
procesar_html_artista("la-renga")
procesar_html_artista("zaz")
procesar_html_artista("la-mississippi")
procesar_html_artista("jose-larralde")

procesar_html_artista('charly garcia')
procesar_html_artista('the rolling stones')
procesar_html_artista('fito paez')
procesar_html_artista('shakira')
procesar_html_artista('joaquin sabina')
procesar_html_artista('joan-manuel-serrat')
procesar_html_artista('los-redonditos-de-ricota')
procesar_html_artista('soda stereo')

procesar_html_artista('the beatles')
procesar_html_artista('andres calamaro')
procesar_html_artista('intoxicados')
