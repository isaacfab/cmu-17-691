# Class notes

Update this file with notes for the class. Include summay of readings, in-class activities, and the lecture.

## Reading Summary

### Ariticle 3: **[Intro Docs for Evidently.ai tool](https://docs.evidentlyai.com/)**

Evidently is an open-source Python library for data scientists and ML engineers. It helps evaluate, test and monitor the performance of ML models from validation to production.

Evidently has a modular approach with 3 interfaces on top of the shared `Analyzer` functionality.

1. Interactive visual reports: Evidently generates interactive HTML reports from `pandas.DataFrame` or `csv` files. like Data Drift and Quality, Categorical and Numerical Target Drift, Classification Performance and Regression Performance.

2. Data and model profiling: Evidently also generates JSON `Profiles`, which can be used to integrate the data or model evaluation step into the ML pipeline.

3. Real-time ML monitoring: Evidently also has `Monitors` that collect data and model metrics from a deployed ML service, which can be used to build live monitoring dashboards.

## Lecture - Deployment and Monitoring



### Model Deployment

##### Application Structure

###### 1. Batch Prediction

- Pre-process model interface and cache reults

- Minimal performance impacts to user

- Idea for a manageable set of predictions (recommender systems)

- Is not dynamic

###### 2. Model as a Service (MaaS)

- Model is packaged and deployed as an external service (API)

- Easier to manage infrasture and scale (Docker)

- Can add complexity to product archetecture (Scaling)

- Many managed options available

**Tech stack**: Flask, FaskAPI, Docker, Kubernetes

**Example**: ONNX

###### 3. Deploying at the Edge

- Model is on the device

- Low latency and no connectivity required

- Limited to hardware specs

- Updating models can be challenging

- Many services are optimized

- Customeized edge models are available

**Example**: Tensorflow light, core ML with Apple, Nvidia AI embedded systems

### Model Monitoring

###### Importance

- Primary issue is that model performance after deployment does not meet expetations

- Dirft is the common term for this phenomenon is 
  
  - Data Drift - Issue in production data pipeleine
  
  - Model/Concept Drivt - Fundamental change in system the model was trained in
  
  - Domanin Shift - Misalignemnt from training and production

###### Drift types

- Instantaneous

- Gradual

- Periodic

- Temporary

###### What to Monitor

The harder to measure, more information will get.

- Model metrics - accuracy, percision, recall

- Business metrics - customer churn, ROI, etc.

- Distributions of Model inputs and inference

- System Performance

###### Looking for Feature Distribution Shifts

- Classical statistical hypothesis test

- Collect 2 samples and compare then (reference / traning data)

###### Tools

- Evidently.ai / Neptune.ai