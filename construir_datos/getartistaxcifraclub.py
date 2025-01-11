import os
import requests
import json

# Define the directory where the pages will be saved
SAVE_DIRECTORY = 'cifraclub_pages'
DIRECTORIO_DATOS = '../cliente/public/data/'

def download_cifraclub_page(band_name, song_name):
    # Format the URL
    band_name = band_name.replace(' ', '-')
    song_name = song_name.replace(' ', '-').replace('?', '')
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
    
    band_name = band_name.replace(' ', '-')
    nombre_archivo_json  = os.path.join(DIRECTORIO_DATOS, f'{band_name}.json')
    # Load the JSON file
    with open(nombre_archivo_json, 'r', encoding='utf-8') as file:
        canciones = json.load(file)
    
    # Iterate over the list of songs and download each page
    for song_name in canciones:
        print (f'Descargar... {song_name}')
        download_cifraclub_page(band_name, song_name)




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
exit()


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


exit()
download_cifraclub_artista("indio solari")
download_cifraclub_artista("luis alberto spinetta")
download_cifraclub_artista("moris")
download_cifraclub_artista("bob dylan")
download_cifraclub_artista('charly garcia')
download_cifraclub_artista('the rolling stones')
download_cifraclub_artista('fito paez')
download_cifraclub_artista('shakira')
download_cifraclub_artista('joaquin sabina')
download_cifraclub_artista('joan-manuel-serrat')
download_cifraclub_artista('los-redonditos-de-ricota')
download_cifraclub_artista('soda stereo')

exit()
download_cifraclub_artista('intoxicados')
download_cifraclub_artista('the beatles')
download_cifraclub_artista('andres calamaro')