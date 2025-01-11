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
