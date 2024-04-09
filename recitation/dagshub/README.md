# Recitation Outline for DagsHub

Dagshub is a collaborative data science platform that provides hosted services for machine learning projects. To get started for this recitation follow these steps:

1. Visit (DagsHub website)[https://dagshub.com/]
2. Create an account
3. Create a blank new repository

We will be using docker instead of python virtual environments (which are suggested in the DagsHub docs). In the `recitation/dagshub` directory of the class repo is a Docker file that extends the Jupyterlab container we have been using with required libraries for DagsHub. From the directory build the container with:

`docker build -t my-jlab .`

The run the container with

`docker run -p 8888:8888 -v "${PWD}":/home/jovyan/work my-jlab`

Once the container is running open the `DAGsHub_Stack_Exchange_Example.ipynb` notebook from within Jupyterlab. This is a complete example of an exploratory data analysis and benchmark model build using standard python libraries. 

Quickly review the notebook so that you are familiar with this first step as all projects have a similar flow. From here you are ready to start experimentation and versioning data. This will move us from a pure notebook environment to more of a CLI workflow.

1. Open a terminal in jupyterlab
2. Clone your DagsHub project into the working directory (which should still be the `recitation/dagshub/` directory)
3. Initialize DVC with `dvc init` 
4. Connect your dvc remote with instructions from DagsHub

Now that everything is set up and you have a git and dvc workflow you can now version code and data (datasets and models). Let's work through the tutorial by copying one of our scripts the `main.py` file from the root directory. This script does four important things:

1. Loads the data
2. Processes the data
3. Trains a classification model
4. Evaluates the model and records relevant metrics

To demonstrate how dvc works the tutorial covers three changes/updates to the `main.py` file resulting in updates to data that is also versioned. These can be found in the `recitation/dagshub/scripts` directory. When we push the data it is not tracked using dvc on DagsHub along with our code.

[Take a look at the full documentation tutorial here.](https://dagshub.com/docs/experiment_tutorial/)

