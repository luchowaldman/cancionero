import os
import requests
import json

from normalizarnombres import normalizar_nombre

# Define the directory where the pages will be saved
SAVE_DIRECTORY = 'cifraclub_pages'
DIRECTORIO_DATOS = '../cliente/public/data/'

def download_cifraclub_page(band_name, song_name):
    # Format the URL
    band_name = normalizar_nombre(band_name)
    song_name = normalizar_nombre(song_name)
    file_path = os.path.join(SAVE_DIRECTORY, f'{band_name}_{song_name}.html')
    if os.path.exists(file_path):
        return
        
    url = f'https://www.cifraclub.com/{band_name}/{song_name}/'.lower()
    
    # Make the request to get the page content
    response = requests.get(url)
    
    if response.status_code == 200:
        # Ensure the save directory exists
        if not os.path.exists(SAVE_DIRECTORY):
            os.makedirs(SAVE_DIRECTORY)
        
        # Define the file path
        file_path = os.path.join(SAVE_DIRECTORY, f'{band_name}_{song_name}.html')
        
        # Save the content to a file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)
        
        print(f'Page saved successfully: {file_path}')
    else:
        print(f'Failed to download page: {url} (Status code: {response.status_code})')

def download_cifraclub_artista(band_name):
    
    band_name = normalizar_nombre(band_name)

    nombre_archivo_json  = os.path.join(DIRECTORIO_DATOS, f'{band_name}.json')
    
    # Load the JSON file
    with open(nombre_archivo_json, 'r', encoding='utf-8') as file:
        canciones = json.load(file)
    
    # Iterate over the list of songs and download each page
    for song_name in canciones:
        #print (f'Descargar... {song_name}')
        download_cifraclub_page(band_name, song_name)


download_cifraclub_artista("mala-fama")
download_cifraclub_artista("bizarrap")
download_cifraclub_artista("phil-collins")
download_cifraclub_artista("yes")
download_cifraclub_artista("ramones")
download_cifraclub_artista("muse")
download_cifraclub_artista("radiohead")
download_cifraclub_artista("u2")
download_cifraclub_artista("genesis")
download_cifraclub_artista("coldplay")
download_cifraclub_artista("divididos")
download_cifraclub_artista("traveling-wilburys")
download_cifraclub_artista("david-bowie")
download_cifraclub_artista("elton-john")
exit()



download_cifraclub_artista("bizarrap")
download_cifraclub_artista("dillom")
download_cifraclub_artista("nathy-peluso")
download_cifraclub_artista("los-caballeros-de-la-quema")
download_cifraclub_artista("ivan-noble")
download_cifraclub_artista("bee-gees")
download_cifraclub_artista("l-gante")
download_cifraclub_artista("bob-marley")
download_cifraclub_artista("queen")
download_cifraclub_artista("the-police")
download_cifraclub_artista("the-clash")
download_cifraclub_artista("the-cranberries")
download_cifraclub_artista("the-doors")
download_cifraclub_artista("los-autenticos-decadentes")
download_cifraclub_artista("rem")
download_cifraclub_artista("los-pericos")
download_cifraclub_artista("los-piojos")
download_cifraclub_artista("vilma-palma-e-vampiros")
download_cifraclub_artista("bersuit-vergarabat")
exit()

download_cifraclub_artista("led-zeppelin")
download_cifraclub_artista("michael-jackson")
download_cifraclub_artista("gilda")
download_cifraclub_artista("supertramp")
download_cifraclub_artista("rodrigo")
download_cifraclub_artista("damas-gratis")
download_cifraclub_artista("aerosmith")
download_cifraclub_artista("los-palmeras")
download_cifraclub_artista("calle-13")
download_cifraclub_artista("silvio-rodriguez")
download_cifraclub_artista("pablo-milanes")
download_cifraclub_artista("fabiana-cantilo")
download_cifraclub_artista("ac-dc")
download_cifraclub_artista("the-smiths")
download_cifraclub_artista("leo-garcia")
exit()
download_cifraclub_artista('zambayonny')
exit()
download_cifraclub_artista('la renga')
download_cifraclub_artista("bob dylan")
download_cifraclub_artista('charly garcia')
download_cifraclub_artista('the rolling stones')
download_cifraclub_artista('fito paez')
download_cifraclub_artista('shakira')
download_cifraclub_artista('joaquin sabina')
download_cifraclub_artista('joan-manuel-serrat')
download_cifraclub_artista('los-redonditos-de-ricota')
download_cifraclub_artista('soda stereo')

download_cifraclub_artista('intoxicados')
download_cifraclub_artista('the beatles')
download_cifraclub_artista('andres calamaro')
exit()
download_cifraclub_artista("sui-generis")
download_cifraclub_artista("luis-miguel")
download_cifraclub_artista("calle-13")
download_cifraclub_artista("mana")
download_cifraclub_artista("manal")
download_cifraclub_artista("sui-generis")
download_cifraclub_artista("arjona ricardo")
download_cifraclub_artista("alejandro-sanz")
download_cifraclub_artista("luis-fonsi")
download_cifraclub_artista("ruben-rada")
download_cifraclub_artista("natalia-oreiro")
download_cifraclub_artista("leon-gieco")
download_cifraclub_artista("victor-jara")
download_cifraclub_artista("gilberto-gil")
download_cifraclub_artista("roberto-carlos")
download_cifraclub_artista("milton-nascimento")


download_cifraclub_artista("victor-jara")
download_cifraclub_artista("gilberto-gil")
download_cifraclub_artista("roberto-carlos")
download_cifraclub_artista("milton-nascimento")

download_cifraclub_artista("madonna")
download_cifraclub_artista("beyonce") 
download_cifraclub_artista("prince")
download_cifraclub_artista("beyonce")


download_cifraclub_artista("chico-buarque")
download_cifraclub_artista("caetano-veloso")
download_cifraclub_artista("leo-masliah")

download_cifraclub_artista("jorge-drexler")
download_cifraclub_artista("parra-violeta")
download_cifraclub_artista("alfredo-zitarrosa")
download_cifraclub_artista("elvis-presley")
download_cifraclub_artista("michael-jackson")
download_cifraclub_artista("aretha-franklin")
download_cifraclub_artista("frank-sinatra")
download_cifraclub_artista("bruce-springsteen")
download_cifraclub_artista("stevie-wonder") 
download_cifraclub_artista("taylor-swift")
download_cifraclub_artista("lady-gaga")
download_cifraclub_artista("jay-z")
download_cifraclub_artista("kanye-west")

download_cifraclub_artista("sandro")
download_cifraclub_artista("palito-ortega")
download_cifraclub_artista("jimenez-jose-alfredo")
download_cifraclub_artista("george-harrison")

download_cifraclub_artista("conociendo-rusia")
download_cifraclub_artista("carlos gardel")
download_cifraclub_artista("roberto-goyeneche")
download_cifraclub_artista("la-mosca")
download_cifraclub_artista("almendra")
download_cifraclub_artista("jim-morrison")
download_cifraclub_artista("john-lennon")
download_cifraclub_artista("paul-mccartney")
download_cifraclub_artista("jose-larralde")
download_cifraclub_artista("jorge-cafrune")
download_cifraclub_artista("mercedes-sosa")
download_cifraclub_artista("los-chalchaleros")
download_cifraclub_artista("los-nocheros")
download_cifraclub_artista("los-tekis")
download_cifraclub_artista("la-mona-gimenez")
download_cifraclub_artista("almafuerte")
download_cifraclub_artista("os-paralamas-do-sucesso")


download_cifraclub_artista("indio solari")
download_cifraclub_artista("luis alberto spinetta")
