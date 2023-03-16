# Recitation Outline for Docker

> A container is a standard unit of software that packages up code and all its dependencies, so the application runs quickly and reliably from one computing environment to another. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings. [Source](https://www.docker.com/resources/what-container/)

Containers are great tools for packaging up applications that have Machine Learning Components. This recitation does a quick overview of the basic mechanics for how that works.

1. Docker overview
	1. containers use resources more flexibility than more ridged virtual machines
	2. containers are the basis for a 'micro-services' software architecture
	3. They are standard, lightweight, portable, and reproducible (declarative)
	4. You can install the [docker engine (docker runtime)](https://docs.docker.com/engine/install/) in any computing environment.
2. We can use other people’s containers for ML use cases
	1. [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/) are pre-built containers hosted on Docker Hub that have complete ML development environments with Jupyterlab and related dependencies
		1. you can run the example using: `docker run -it --rm -p 10000:8888 -v "${PWD}":/home/jovyan/work jupyter/datascience-notebook:2023-02-28`
		2. -p maps ports between the host and the container
		3. -v mounts a persistent volume (otherwise anything saved is lost as containers are ephemeral)
	2. [Docker Hub](https://hub.docker.com/) is an open source container registry where you can host or use pre-built docker containers
	3. Docker containers can be used to turn a machine learning model into a 'micro-service'
3. Build an example that turns a scikit-learn model into a containerized API
	1. build and save the model `ml-container.ipynb` has the code for this
	2. create a rest api using flask `app/app.py` is the simple code to create this using the saved model
	3. build a docker container using the docker file
		1. container builds are layered and can be extended
		2. this example extends a python docker image called python:3.8-slim that has python 3.8 installed
		3. we just install the packages we need at runtime using requirements.txt 
		4. then run the command that starts the flask app when the container is started
		5. the actual build is done with the command `docker build -t api .` the -t flag tags or names the image the '.' is the current directory where the command is run
	4. run the newly built container with `docker run -p 8080:8080 api`
	5. test the api with a POST request: `curl -X POST 127.0.0.1:8080/predict -H 'Content-Type: application/json' -d '[{\"f1\":0.80576177,\"f2\":1.37593746,\"f3\":-0.09609774,\"f4\":-0.46983664,\"f5\":-0.46399264,\"f6\":-0.41596074}]'`
# Recitation Outline for Docker

> A container is a standard unit of software that packages up code and all its dependencies, so the application runs quickly and reliably from one computing environment to another. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings. [Source](https://www.docker.com/resources/what-container/)

Containers are great tools for packaging up applications that have Machine Learning Components. This recitation does a quick overview of the basic mechanics for how that works.

1. Docker overview
	1. containers use resources more flexibility than more ridged virtual machines
	2. containers are the basis for a 'micro-services' software architecture
	3. They are standard, lightweight, portable, and reproducible (declarative)
	4. You can install the [docker engine (docker runtime)](https://docs.docker.com/engine/install/) in any computing environment.
2. We can use other people’s containers for ML use cases
	1. [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/) are pre-built containers hosted on Docker Hub that have complete ML development environments with Jupyterlab and related dependencies
		1. you can run the example using: `docker run -it --rm -p 10000:8888 -v "${PWD}":/home/jovyan/work jupyter/datascience-notebook:2023-02-28`
		2. -p maps ports between the host and the container
		3. -v mounts a persistent volume (otherwise anything saved is lost as containers are ephemeral)
	2. [Docker Hub](https://hub.docker.com/) is an open source container registry where you can host or use pre-built docker containers
	3. Docker containers can be used to turn a machine learning model into a 'micro-service'
3. Build an example that turns a scikit-learn model into a containerized API
	1. build and save the model `ml-container.ipynb` has the code for this
	2. create a rest api using flask `app/app.py` is the simple code to create this using the saved model
	3. build a docker container using the docker file
		1. container builds are layered and can be extended
		2. this example extends a python docker image called python:3.8-slim that has python 3.8 installed
		3. we just install the packages we need at runtime using requirements.txt 
		4. then run the command that starts the flask app when the container is started
		5. the actual build is done with the command `docker build -t api .` the -t flag tags or names the image the '.' is the current directory where the command is run
	4. run the newly built container with `docker run -p 8080:8080 api`
	5. test the api with a POST request: `curl -X POST 127.0.0.1:8080/predict -H 'Content-Type: application/json' -d '[{\"f1\":0.80576177,\"f2\":1.37593746,\"f3\":-0.09609774,\"f4\":-0.46983664,\"f5\":-0.46399264,\"f6\":-0.41596074}]'`
