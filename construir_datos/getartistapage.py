import os
import requests

# Define the directory where the pages will be saved
SAVE_DIRECTORY = 'cifraclub_pages'

def getartista_page(band_name):
    # Format the URL
    band_name = band_name.replace(' ', '-')
    url = f'https://www.cifraclub.com/{band_name}'
    
    # Make the request to get the page content
    response = requests.get(url)
    
    if response.status_code == 200:
        # Ensure the save directory exists
        if not os.path.exists(SAVE_DIRECTORY):
            os.makedirs(SAVE_DIRECTORY)
        
        # Define the file path
        file_path = os.path.join(SAVE_DIRECTORY, f'{band_name}.html')

        # Save the content to a file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)
        
        print(f'Page saved successfully: {file_path}')
    else:
        print(f'Failed to download page: {url} (Status code: {response.status_code})')


getartista_page("bob-marley")
exit()
getartista_page("led-zeppelin")
getartista_page("michael-jackson")
getartista_page("gilda")
getartista_page("supertramp")
getartista_page("rodrigo")
getartista_page("damas-gratis")
getartista_page("aerosmith")
getartista_page("los-palmeras")
getartista_page("calle-13")
getartista_page("silvio-rodriguez")
getartista_page("pablo-milanes")
getartista_page("fabiana-cantilo")
getartista_page("ac-dc")
getartista_page("the-smiths")
getartista_page("leo-garcia")
getartista_page
# Example usage
# download_cifraclub_page('intoxicados', 'fuiste lo mejor')
# download_cifraclub_page('intoxicados', 'fuego')Nah
#download_cifraclub_page('intoxicados', 'esta saliendo el sol')
#download_cifraclub_page('intoxicados', 'se fue al cielo')
#download_cifraclub_page('intoxicados', 'casi sin pensar')
#download_cifraclub_page('intoxicados', 'pila pila')
#download_cifraclub_page('intoxicados', 'volver a casa')
#download_cifraclub_page('andres calamaro', 'flaca')
#download_cifraclub_page('andres calamaro', 'la parte de adelante')

#getartista_page("zambayonny")
exit()

getartista_page("arjona-ricardo")
getartista_page("alejandro-sanz")
getartista_page("luis-fonsi")
getartista_page("luis-miguel")
getartista_page("calle-13")
getartista_page("mana")
getartista_page("manal")
getartista_page("sui-generis")



exit()
getartista_page("parra-violeta")
getartista_page("alfredo-zitarrosa")
getartista_page("elvis-presley")
getartista_page("michael-jackson")
getartista_page("aretha-franklin")
getartista_page("frank-sinatra")
getartista_page("bruce-springsteen")
getartista_page("stevie-wonder") 
getartista_page("taylor-swift")
getartista_page("lady-gaga")
getartista_page("jay-z")
getartista_page("kanye-west")

getartista_page("sandro")
getartista_page("palito-ortega")
getartista_page("jimenez-jose-alfredo")
getartista_page("george-harrison")
getartista_page("violeta-parra")
getartista_page("chico-buarque")
getartista_page("caetano-veloso")
getartista_page("leo-masliah")

getartista_page("jorge-drexler")
getartista_page("alfred-zitarrosa")
getartista_page("ruben-rada")
getartista_page("natalia-oreiro")
getartista_page("leon-gieco")
getartista_page("victor-jara")
getartista_page("gilberto-gil")
getartista_page("roberto-carlos")
getartista_page("milton-nascimento")


getartista_page("victor-jara")
getartista_page("gilberto-gil")
getartista_page("roberto-carlos")
getartista_page("milton-nascimento")

getartista_page("madonna")
getartista_page("beyonce") 
getartista_page("prince")
getartista_page("beyonce")



exit()
getartista_page("conociendo-rusia")
getartista_page("la-mosca")
getartista_page("la-mona-gimenez")
getartista_page("almafuerte")
getartista_page("os-paralamas-do-sucesso")

getartista_page("los piojos")
getartista_page("bersuit-vergarabat")
getartista_page("conoziendo-rusia")
getartista_page("el-bordo")
getartista_page("la-25")
getartista_page("la-vela-puerca")
getartista_page("las-pastillas-del-abuelo")
getartista_page("los-autenticos-decadentes")
getartista_page("los-caballeros-de-la-quema")
getartista_page("los-fabulosos-cadillacs")
getartista_page("los-piojos")
getartista_page("manu-chao")
getartista_page("no-te-va-gustar")
getartista_page("la-renga")
getartista_page("zaz")
getartista_page("la-mississippi")
getartista_page("jose-larralde")
getartista_page("la-mosca-tse-tse")
getartista_page("la-mona-jimenez")
getartista_page("carlos gardel")
getartista_page("roberto-goyeneche")
getartista_page("almendra")
getartista_page("jim-morrison")
getartista_page("john-lennon")
getartista_page("paul-mccartney")
getartista_page("jose-larralde")
getartista_page("jorge-cafrune")
getartista_page("mercedes-sosa")
getartista_page("los-chalchaleros")
getartista_page("los-nocheros")
getartista_page("los-tekis")
getartista_page("los-almafuerte")
exit()

getartista_page("bob dylan")
getartista_page("viejas locas")
getartista_page("gustavo cerati")
getartista_page('charly garcia')
getartista_page('the rolling stones')
getartista_page('fito paez')
getartista_page('shakira')
getartista_page('joaquin sabina')
getartista_page('joan-manuel-serrat')
getartista_page('los-redonditos-de-ricota')
getartista_page('soda stereo')


getartista_page('the beatles')
getartista_page('intoxicados')
getartista_page('andres calamaro')
