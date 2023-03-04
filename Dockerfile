FROM python:3.10.10
COPY . /usr/src/app
COPY Datasets_clean/platforms.csv /usr/src/app/data/
COPY requirements.txt /usr/src/app

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "main:app", "--reload"]


# docker build -t fastapi .                                               -- it creates the image 332.4s
# docker images                                                           -- visualizes the images created 
# docker run -it -p 8000:8000 -v %cd%:/usr/src/app fastapi                -- create the container
# docker run -it -p 8000:8000 -v "C:\Users\Predator\Desktop\Lauti\Programación\GitHub\1. Data Engineering\#1:/usr/src/app" fastapi                -- create the container