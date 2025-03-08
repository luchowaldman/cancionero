import os
import requests

# Define the directory where the pages will be saved
SAVE_DIRECTORY = 'cifraclub_pages'

def download_cifraclub_page(band_name, song_name):
    # Format the URL
    band_name = band_name.replace(' ', '-')
    song_name = song_name.replace(' ', '-')
    url = f'https://www.cifraclub.com/{band_name}/{song_name}/'
    
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


download_cifraclub_page('andres calamaro', 'cuando no estas')
download_cifraclub_page('andres calamaro', 'te quiero igual')
download_cifraclub_page('andres calamaro', 'crimenes perfectos')
download_cifraclub_page('andres calamaro', 'paloma')
download_cifraclub_page('andres calamaro', 'cartas sin marcar')
download_cifraclub_page('andres calamaro', 'donde manda marinero')
download_cifraclub_page('andres calamaro', 'pasemos a otro tema')
download_cifraclub_page('andres calamaro', 'mi gin tonic')
download_cifraclub_page('andres calamaro', 'loco')
download_cifraclub_page('andres calamaro', 'soy tuyo')
download_cifraclub_page('andres calamaro', 'el salmon')
download_cifraclub_page('andres calamaro', 'alta suciedad')
download_cifraclub_page('andres calamaro', 'media veronica')
download_cifraclub_page('andres calamaro', 'diez años despues')
download_cifraclub_page('andres calamaro', 'bohemio')





