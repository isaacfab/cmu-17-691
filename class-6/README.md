# Lecture 6 - Deployment and Monitoring

## Reading Summary

### Article 1: [**MLOps Stack Canvas by INNOQ**](https://ml-ops.org/content/mlops-stack-canvas)

**Background:** The number of current MLOps platforms and frameworks is exploding and it is challenging for the companies to keep the development pace. Faced with emerging and fast-evolving technologies, companies are experiencing difficulties integrating their technology stack.

**MLOps Stack Canvas:** A series of steps that we perform during the machine learning development life cycle.

![MLOps Stack Canvas](https://ml-ops.org/img/mlops-stack.jpg)

**Scope:** Ensure that ML model solutions have a (business) impact. Planning the cost of infrastructure components and orchestration of the ML system. Designing the ML system to fulfill reproducibility, reliability, and efficiency.

**Components:**

- *Value Proposition*: For (target customer) who (need or opportunity), our (product/service name) is (product category) that (benefit).

- *Data Sources and Data Versioning*: Estimate the cost of data acquisition, storage, and processing.

- *Data Analysis and Experiment Management*: Run experiments to evaluate the feasibility of the project.

- *Feature Store and Workflows*: Seperate the features engineering from the development process.

- *CI/CT pipelines*: Consider the configurations of the process.

- *Model Registry and Model Versioning*: Establish model and data versioning control.

- *Model Deployment*: Deploy the ML model to fit in the target environment.

- *Prediction Serving*: Determine several aspects of the serving, e.g., distributed model.

- *Monitoring*: Model quality must be constantly monitored.

- *Metadata Store*: Each execution of the experimens, data, and model pipeline is recorded.

**Takeaway:** Manage to consider the settings and methodologies used of each step in the MLOps Stack Canvas. Better designing and better management can lead to a more efficient ML product.

### Article 2: [**Model Deployment Stanford Lecture Notes by Chip Huyen**](https://docs.google.com/document/d/1hNuW6bqWYZjlwpit_8W1cu7kllb-jTfy3Liof1GJWug/edit)

**Batch Prediction vs. Online Prediction**

- Online prediction: predictions are generated and returned as soon as requests for these predictions arrived, also known as synchronous prediction:

- Batch prediction: predictions are generated periodically or whenever triggered. Also known as asynchronous prediction

**From Batch Prediction To Online Prediction**

- More natural way to serve predictions is probably online.

- But the model might take too long to generate predictions.

- A solution would be to compute predictions in advance and store them in your database, and fetch them when requests arrive.

- Problem with batch prediction :less responsive to users’ change preferences.

- Another problem with batch prediction: you need to know what requests to generate predictions for in advance

- Recently companies move from batch prediction to online prediction.

- Two components are required to overcome latency problem:
  
  - Realtime pipeline
  - Fast inference model

**Unifying Batch Pipeline And Streaming Pipeline**

Having two different streaming pipelines to process your data is a common cause for bugs in ML production, when one pipeline aren’t correctly replicated in the other

**Three main approaches to reduce inference latency:**

1. Make inference faster
2. Make model smaller
3. Make the hardware run faster

**ML on the Cloud and on the Edge**

- Considers “where your model’s computation will happen”
- On the cloud: computation done on cloud
- On the edge: computation done on the consumer devices

**Why Edge over Cloud?**

- Cloud services such as AWS or GCP are easy but cost may be high.

- Using consumer devices eliminates network latency.

- Edge better handles sensitive data from users

- Therefore companies are in a race to develop edge devices.

**Compiling and Optimizing Models for Edge Devices**

- Not all frameworks such as Tensorflow or Pytorch are supported by all hardwares, and providing support of edge computing is hard.
- An alternative is ‘middle man’ to bridge frameworks and platforms. They are called “Intermediate representation (IR)”
- IRs lie at the core of how compilers work, also called “lowering”. Lowers high level code into low level hardware native code.

**4 Level of IR:** High Level Its, Tuned IRs, Low level Its, Machine Code

**Model Optimization**

Two ways to optimize ML Models:

1. Locally: optimize an operator or set of operators of your model.
   a. *Vectorization* use hardware primitives to operate on multiple elements contiguous in memory
   
   b. *Parallelization* divide it into different, independent work chunks, and do the operation on each chunk individually
   
   c. *Loop tilling* change the data accessing order in a loop to leverage hardware’s memory layout and cache
   d. *Operator Fusion* fuse multiple operators into one to avoid redundant memory access

2. Globally: optimize the entire computation graph end to end.

**Using ML to optimize ML models**

Traditionally vendors hire optimization engineer. But nowadays such optimization can be achieved by ML. e.g. cuDNN autotune or autoTVM

**ML in Browsers**

Webassembly (WASM) allows users to run executable programs in browsers. Useful for on-the-edge computing. However, WASB run slower than native applications.

### Ariticle 3: **[Intro Docs for Evidently.ai tool](https://docs.evidentlyai.com/)**

Evidently is an open-source Python library for data scientists and ML engineers. It helps evaluate, test and monitor the performance of ML models from validation to production.

Evidently has a modular approach with 3 interfaces on top of the shared `Analyzer` functionality.

1. Interactive visual reports: Evidently generates interactive HTML reports from `pandas.DataFrame` or `csv` files. like Data Drift and Quality, Categorical and Numerical Target Drift, Classification Performance and Regression Performance.

2. Data and model profiling: Evidently also generates JSON `Profiles`, which can be used to integrate the data or model evaluation step into the ML pipeline.

3. Real-time ML monitoring: Evidently also has `Monitors` that collect data and model metrics from a deployed ML service, which can be used to build live monitoring dashboards.

## Lecture Notes

### Model Deployment

#### 1. Database

- Running ahead of time

- Preprocessing, user don’t even know

e.g. search engine use caches, recommendation system use look up table. drawback: not real time, needed to be updated in batches

#### 2. Server (server side mode linferrencing)

- Pre-process model interface and cache reults

- Minimal performance impacts to user

- Idea for a manageable set of predictions (recommender systems)

- Is not dynamic

- Easy to be integrated, but could impact performance if model inference use too much resource. 
  
  Alternative: package model as external service API, it can self update without need of knowing the software.

#### 3. Model as a Service (MaaS)

- Model is packaged and deployed as an external service (API)

- Easier to manage infrasture and scale (Docker)

- Can add complexity to product archetecture (Scaling)

- Many managed options available

**Tech stack**: Flask, FaskAPI, Docker, Kubernetes

**Example**: Take advantage of standardization components: Open Neural network Exchange (ONNX), easy to deploy

#### 4. Deploying at the Edge

- Model is on the device

- Low latency and no connectivity required

- Limited to hardware specs

- Updating models can be challenging

- Many services are optimized

- Customeized edge models are available

**Example**: Tensorflow light, core ML with Apple, Nvidia AI embedded systems, Jetson Nano Developer Kit for Live Object Detection. Trade off between efficiency and accuracy. When model is smaller, some fidelity is lost.

### Class Discussions

#### Stack

- Track model, performance need to be monitored, insuring integrity of product, work as the way intended to

- Strategy for product

- Consider trade offs

- Impact of development on system 

- Model versioning with quality check 

- What metrics to use

- Format matters

- Continuous training

- Model decay

#### Online

- Immediate result

- Online can be slower

- Guarantee privacy, more data control

- Can handle more diverse input

#### Batch

- More efficient, reduce latency by retrieve cached result

- Batch Optimized for Through put

- Optimized batch size

- Trade off between low latency and cache

- Need to understand inputs

#### Evidently.ai

- Monitoring Data Drift - keep track of it

- Dashboard visualization

- Quality of data

- Model inference time

- Model performance comparison

### Model Monitoring

#### **Why monitor after deployment?**

- Always monitor, otherwise model quality will decay.

- Primary issue is that model performance after deployment does not meet expetations

- Dirft is the common term for this phenomenon is 
  
  - Data Drift - Issue in production data pipeleine
  
  - Model/Concept Drivt - Fundamental change in system the model was trained in
  
  - Domanin Shift - Misalignemnt from training and production

#### Drift types

Typically refers to the features, input to the models (what actually goes in your model)

###### By Types

- Data Drift: issue in data pipeline

- Model/Concept drift, fundamental change in system of the model 

- Domain Shift, MOST COMMON in real life. Very hard to collect data that are unbiased.

###### By Time:

- Instantaneous:  Instant difference between training and deployment

- Gradual: Gradually change over time and gap between training and deployment increases

- Temporary: Sudden change caused inaccuracy but go back online later, e.g. COVID-19.

- Periodic

#### What to Monitor

The harder to measure, more information will get.

- Model metrics - accuracy, percision, recall

- Business metrics - customer churn, ROI, etc.

- Distributions of Model inputs and inference: 
  
  - A/B Tests
  
  - Visual inspection
  
  - K-S test, difference between model and empirical CDF

- System Performance

###### Looking for Feature Distribution Shifts

- Classical statistical hypothesis test

- Collect 2 samples and compare then (reference / traning data)

###### Tools

- Model should be logging metrics

- Part of the app should be dedicated to collection and analytics

- Store metrics in a database table : e.g. Evident AI, Neptune AI

### Summary

- Many Options for Deployment 

- Choose one best for your product.

- Keep track of it