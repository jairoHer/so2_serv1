# Con esto creo la imagen de mi aplicación
#FROM python:2.7
FROM python:3.6

EXPOSE 5001 5000

COPY . /app

WORKDIR /app


RUN pip install -r requirements.txt

RUN mkdir -p /elements/info
#COPY app.py /app
CMD python backend.py
