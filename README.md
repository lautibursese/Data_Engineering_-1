# <h1 align=center>**`Data Engineering`**</h1>

<p align="center">
<img src="https://files.realpython.com/media/What-is-Data-Engineering_Watermarked.607e761a3c0e.jpg"  height=300>
</p>

Welcome to this project! On this occasion, a job will be done in the role of a ***Data Engineer***.  

<hr>  

## **Introduction**

The idea of ​​this project is to internalize the knowledge required for the development and execution of an API.

`Application Programming Interface` is an interface that allows two applications to communicate with each other, independent of the underlying infrastructure. They are very versatile and fundamental tools for the creation of, for example, pipelines, since they allow you to move and provide simple access to the data that you want to make available through the different endpoints, or API exit points.

Today we have **FastAPI**, a modern and high-performance web framework for building APIs with Python.
<p align=center>
<img src = 'https://i.ibb.co/9t3dD7D/blog-zenvia-imagens-3.png' height=250><p>

## **Job offer**

The project consists of ingesting data from various sources, then applying the transformations that are considered relevant, and then making the clean data available for consultation through an API. This API will be built in a dockerized virtual environment.


The data will be provided in files of different extensions, such as *csv* or *json*. There will be a correction of data types, null and duplicate values, among other tasks. Later, they will have to relate the datasets so they can access their information through API queries.


The queries to be made are:

+ Maximum duration according to type of film (film/series), by platform and by year:
    The request should be: get_max_duration(year, platform, [min or season])

+ Number of movies and series (separated) by platform
    The request should be: get_count_platform(platform)  
  
+ Number of times a genre and platform is repeated with greater frequency.
    The request should be: get_listedin('gender')  

+ Actor who repeats himself the most according to platform and year.
  The request should be: get_actor(platform, year)

## **Project steps**

1. Data ingestion and normalization

2. Relate the data set and create the table needed to perform queries. Here it is recommended to verify what data you will need based on the queries to be made and concatenate the 4 tables

3. Create the API in a Docker environment

4. Make requested inquiries

5. Make a demonstration video

<p align=center>
<img src = 'https://i.postimg.cc/2SwvnTcw/Sin-t-tulo.png' height = 400></p>

## **Demo video**

A video will be made presenting the work and executing the mentioned tasks, it will **not exceed 5 minutes**. It will include a brief personal presentation, the project, code execution and mentioned tasks.

## **Concepts of interest**

- **`Docker`** is a complete solution for the production, distribution and use of containers.  
&nbsp;- **`Container`** is a software layer abstraction that allows *packaging* code, with libraries and dependencies in a partially isolated environment.  
&nbsp;- **`Image`** is a Docker executable that has everything needed to run applications, including a configuration file, environment and runtime variables, and libraries.  
&nbsp;- **`Dockerfile`** text file with instructions for building an image. Image creation automation can be considered.  

## **Resources and links**

Docker image with Uvicorn/Guinicorn for high performance web applications:

+ https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/ 

+ https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

FAST API Documentation:

+ https://fastapi.tiangolo.com/tutorial/