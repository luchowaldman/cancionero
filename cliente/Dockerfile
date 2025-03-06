# Utiliza una imagen de Nginx para servir la aplicación
FROM nginx:stable-alpine as production-stage

# Copia los archivos compilados a la carpeta de Nginx
COPY /dist /usr/share/nginx/html

# Copia la configuración de Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expone el puerto 80
EXPOSE 80

# Define el punto de entrada
CMD ["nginx", "-g", "daemon off;"]
