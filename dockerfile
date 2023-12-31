# Utiliza una imagen base con Python preinstalado
FROM python:latest

COPY . /usr/src/app/

# Establece el directorio de trabajo en /app
WORKDIR /usr/src/app/

COPY requirements.txt /usr/src/app/

# Instala las dependencias del programa Python
RUN pip install -r requirements.txt

# Ejecuta el programa Python
ENTRYPOINT python app.py
