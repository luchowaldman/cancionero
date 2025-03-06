# Construir la imagen
docker build -t server-cancionero .

# Etiquetar la imagen
docker tag server-cancionero gcr.io/fogoncancionero/server-cancionero:v1.0

# Autenticarte en GCR
gcloud auth configure-docker

# Subir la imagen a GCR
docker push gcr.io/fogoncancionero/server-cancionero:v1.0


# desde el google cloud shell
# subir el programa
gcloud app deploy app.yaml --image-url gcr.io/fogoncancionero/server-cancionero:v1.0
