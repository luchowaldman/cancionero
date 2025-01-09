import requests

client_id = '2911edddc0e840e6b97fe81361c4087c'
client_secret = '09e3a3b2ee714ba5a0813fc79b4bbc20'

# URL para obtener el token de acceso
url = 'https://accounts.spotify.com/api/token'

# Datos para la solicitud
payload = {
    'grant_type': 'client_credentials'
}

# Realiza la solicitud para obtener el token
response = requests.post(url, auth=(client_id, client_secret), data=payload)
data = response.json()

# Token de acceso
access_token = data['access_token']
print(f'Token de acceso: {access_token}')
