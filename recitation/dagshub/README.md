# Recitation Outline for DagsHub

Dagshub is a collaborative data science platform that provides hosted services for machine learning projects. To get started for this recitation follow these steps:

1. Visit (DagsHub website)[https://dagshub.com/]
2. Create and account
3. Create a blank new repository

We will be using docker instead of python virtual environments (which are suggested in the DagsHub docs). In this directory of the class repo is a Docker file that extends the jupyterlab container we have been using with required libraries for DagsHub. From the directory.

`docker build -t my-jlab .`

The run the container with

`docker run -p 8888:8888 -v "${PWD}":/home/jovyan/work my-jlab`