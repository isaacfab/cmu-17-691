
# Required Readings
## [First article: MLOps Stack Canvas by INNOQ](https://ml-ops.org/content/mlops-stack-canvas)
### Overview: 
The MLOps Stack Canvas is a visual representation of the key components and processes involved in building and deploying machine learning (ML) models in production, with a focus on scalability, reliability, and maintainability.
### CRISP-ML(Q) process model & MLOps Stack Canvas 
![MLOps Stack Canvas](https://ml-ops.org/img/mlops-stack.jpg)
### Data & Code Management
- *Data Sources & Data Versioning*: estimate the cost of data preparation, analyze model performance and predictions in each version.
- *Data Analysis and Experiment Management*: translate business objectives to ML tasks
- *Feature Store and Workflows*: manage, reproduce, discover and reuse features in ML projects
- *Foundations (Reflecting DevOps)*: follow the DevOps principles
### Model Management
- *Value Proposition*: how customer benefit from the service
- *CI/CT/CD ML Pipeline Orchestration*: automate the data and model training pipeline workflows to operationalize the model
- *Model Registry and Model Versioning*: establish the foundation for reproducibility in ML
- *Model Deployment*: make a model available on the target environment for receiving prediction requests
- *Prediction Serving*: 5 patterns - Model-as-Service, Model-as-Dependency, Precompute, Model-on-Demand, and Hybrid-Serving
- *ML Model, Data, and System Monitoring*: constantly monitor the model to ensure the model quality
### Metadata Management
- *Metadata Store*: record information about each execution of the experiments, data and model pipeline to provide data and artifacts lineage, reproducibility, and debug errors.

## [Second article: Model Deployment Stanford Lecture Notes by Chip Huyen](https://docs.google.com/document/d/1hNuW6bqWYZjlwpit_8W1cu7kllb-jTfy3Liof1GJWug/edit)
### Batch Prediction vs. Online Prediction
- Online Prediction (synchronous prediction with low latency): predictions are generated and returned as soon as requests for these predictions arrive
- Batch Prediction (asynchronous prediction with high throughput): predictions are generated periodically or whenever triggered
- Batch prediction makes models less responsive to users’ change preferences, and requires requests in advance which will cause mild inconvenience. Companies recently invested significantly in the switch from batch prediction to online prediction, with components like real-time pipeline and fast-inference model to overcome the latency challenge. 
- Building infra to unify the batch pipeline and streaming pipeline help prevent bugs in ML production.
### ML on the Cloud and on the Edge
- Pros & Cons of Cloud:
  - Make it easy to bring ML models into production
  - High costs of cloud service
- Pros & Cons of Edge:
  - Help with controlling costs
  - Allow models to work with no Internet connections
  - Less affected by network latency
  - Handle sensitive user data
  - Might be easier for attackers to steal user data
  - High requirements in computing power and memory space
- Compiling Models for Edge Devices - Intermediate Representation (IR)
  - A series of high- and low-level IR are generated before generating the code native to a hardware backend so that it can run on that hardware backend
- Optimizing Models for Edge Devices
  - Locally optimize the ML models
    - Vectorization
    - Parallelization
    - Loop Tiling
    - Operator Fusion
  - Globally optimize the computation graph
    - E.g. the computation graph of a convolution neural network can be fused vertically or horizontally to reduce memory access and speed up the model
  - Using ML to optimize ML models
    - Adopt ML methods instead of heuristics
    - Use ML to narrow down search space
    - Can cache and reuse the optimization search considering the time-consuming process

## [Third article: Intro Docs for Evidently.ai tool](https://docs.evidentlyai.com/)
### Overview: 
Evidently is an open-source Python library for data scientists and ML engineers.
It helps evaluate, test, and monitor the performance of ML models from validation to production.
Evidently helps evaluate and test data and ML model quality throughout the model lifecycle.
### Evidently has three components: *Reports*, *Tests*, and *Monitors* (in development).
 - Test suites: Tests perform structured data and ML model quality checks. You typically compare two datasets: reference and current. You can set test parameters manually or let Evidently learn the expectations from the reference. Tests verify a condition and return an explicit pass or fail result.
 - Reports: interactive dashboards. Reports calculate various metrics and provide rich interactive visualizations. You can create a custom Report from individual metrics or run one of the Presets that cover a specific aspect of the model or data performance. For example, Data Quality or Classification Performance. Reports are best for exploratory analysis, debugging, and documentation.
 - Monitors: real-time ML monitoring. Evidently also has Monitors that collect data and model metrics from a deployed ML service. In this scenario, Evidently is deployed as a monitoring service. You can use configuration to define the monitoring logic. Evidently calculates the metrics over the streaming data and emits them in Prometheus format. There are pre-built Grafana dashboards to visualize them.
### Core concepts in Evidently
  - A *Metric* is a core component of Evidently. You can combine multiple Metrics in a Report. Reports are best for visual analysis and debugging of your models and data.
  - A *Test* is a metric with a condition. Each test returns a pass or fail result. You can combine multiple Tests in a Test Suite. Test Suites are best for automated model checks as part of an ML pipeline.
  - For both Tests and Metrics, Evidently has *Presets*. These are pre-built combinations of metrics or checks that fit a specific use case.
  - A *Report* is a combination of different Metrics that evaluate data or ML model quality.
  - A *Metric Preset* is a pre-built Report that combines Metrics for a particular use case. You can think of it as a template. For example, there is a Preset to check for Data Drift (DataDriftPreset), Data Quality (DataQualityPreset), or Regression Performance (RegressionPreset).
  - You can list multiple Tests and execute them together in a *Test Suite*.
  - A *Test Preset* is a pre-built Test Suite that combines checks for a particular use case. You can think of it as a template to start with. For example, there is a Preset to check for Data Quality (DataQualityTestPreset), Data Stability (DataStabilityTestPreset), or Regression model performance (RegressionTestPreset).
### Test Suites or Reports?
  - *Reports* are best for debugging, exploratory and ad hoc analytics. They focus on interactive visualizations and do not require setting any expectations upfront. You can use them, for example, when you just put a model in production and want to closely monitor the performance. It is best to use Reports on smaller datasets or sample your data first.
  - *Test Suites* are best for automation. Use them when you can set up expectations upfront (or derive them from the reference dataset). Tests force you to think through what you expect from your data and models, and you can run them at scale, only reacting to the failure alerts. You can use Test Suites on larger datasets since they do not include heavy visuals.


# During class
## Application Structure
- Data stored in a database
- Server
- Web App / Mobile App / IoT Device
## Model Deployment - Where do we put the model
- Batch Prediction - put the model in the database
  - E.g. Zillow calculates all estimates at one time and deploy the model as a table in the database
  - Create exhaustive and static predictions for fast user requests and interactions
  - Allow regularly update the predictions regardless the running time since it is separated from user experience
- Server-side ML Inferencing - put the model on the server
  - package up the model as a component that allows clients to call the application as a service.
  - For small models, integrate models with the micro service architecture that enables resource control and segment. E.g. package model up as a docker container.
  - For large models, it has the risk of server failure. E.g. LLM Apps like ChatGPT
- Model as a Service (MaaS) - decouple model from app
  - Create an independent or standalone service that's managed as a totally separate piece of infrastructure
  - Develop APIs as contract for collaboration and connection
  - Enable one service to provide service for multiple apps 
  - Easy to scale but can be expensive (trade-off)
  - Tech & Tools: MLflow, Flask, FaskAPI, Docker, Kubernetes
  - Example: [ONNX](https://onnx.ai/) framework by Microsoft - transit built model to generic framework, package and deploy it as a service
- Deploying at the Edge - common for mobile app
  - Mobile devices equipped with processors that is capable to conduct inference
  - Limited to hardware specifications
  - Example: [TensorFlow](https://www.tensorflow.org/lite) / Pytorch for edge devices; [Core ML](https://developer.apple.com/documentation/coreml); Chips for IoT Apps: [Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/jetson-nano-developer-kit)
 
## Discussion
### First question: From the MLOps stack canvas article, discuss some key insights about deployment and monitoring.
- Deployment:
  -	We need to consider target customers and target environment.
  -	Format is important.
  -	Release policy – how and when we should deploy it.
  -	Continuous deployment
  -	Shadow deployment
- Monitoring:
  -	Which metrics to use for monitoring.
  -	How to detect data skew and model performance decay?
  -	Continuous monitoring and feedback can help teams identify and resolve issues quickly.
  -	Need to consider alerting strategies and decide what triggers model retraining.
  -	Model + data versioning.

### Second question: What are some trade-offs between online and batch prediction according to the readings?
|             | Batch Prediction | Online Prediction |
| ----------- | ----------- | ---------------- |
| Application | Recommendation System (Zestimate)|Translation|
| Advantage   | 1.	Batch is good if bounded (you know exactly what users will be requesting)<br> 2.	Better for high-through data| 1.	Batch is good if bounded (you know exactly what users will be requesting)<br> 2.	Better for high-through data|
| Drawback    |1.	Batch prediction is less responsive. <br>2.	Less latency<br> 3.	Need to have knowledge of requests<br> 4.	Batch may generate waste computation.| 1.	Higher cost<br> 2.	Less complex and less accurate|

### Third question: From the Evidently.ai what are key things to look for when monitoring model performance?
-	error testing
-	data drift
-	target drift
-	data quality
-	statistic testing
-	serving availability
-	eval metrics

## Model Monitoring
When model performance after deployment doesn't meet expecations. Monitoring for data quaility is important as well as drift.
- Drift
    - *Data Drift* - issue in production data pipeline
    - *Model/Concept Drift* – fundamental change in system the model was trained in
    - *Domain Shift* – Misalignment from training setting a deployment setting
- Type of Drifts by time
    - *Instantaneous* - Deployment performance is constanly lower than training process.
    - *Gradual* - Deployment performance gradually drop over time.
    - *Periodic* - Deployment performance periodically chanage. Sometimes it may be the same as training performance, others worse.
    - *Temporary* - Deployment performance may suddenly drop at some time, and then return to the normal situation.
- What to monitor?
    - *Model Metrics* - Accuracy, Predicsion, Recall. The hardest to measure, but get the most info.
    - *Business Metrics* - Customer Churn, ROI, etc. The second hardest to measure, and get the second most info.
    - *Distribution of Model inputs and Inference*. The second easiest to measure, and get the second least info.
    - *System Performance*. The easily to measure, and get the least info.
- Looking for Feature Distribution Shifts
    - Classical Statistical Hypothesis Test
    - Collect two samples and compare them(reference/training data and current/production data)
    - Other approaches
      - Visual inspection
      - Paired t-test
      - K-S test (difference in distributions)
      - Distance calculations (p norms)
- Tools
    - Should "logging" metrics
    - Part of app should be dedicated to the collection and analysis of data
    - Most common implementation is to store metrics in a database table
    - Evidently.ai / Neptune.ai could be helpful.
### Summary
- There are many options for model deployment
- Chose the best options based on your products requirements
- After deployment collect and save model metrics
- Monitor the metrics for drift
- Drift has many root causes

#  MLOps Testing and Explainability 
## Expanding into the ML Project Workflow
After everything is deployed, how to make sure the information we are getting back is what we want.

## Sample Sub
<img width="473" alt="image" src="https://user-images.githubusercontent.com/19539597/229902218-73bcfaa4-5a1b-447d-86d9-0c4af1a3c89a.png">


## Model Interpretability
Interpretable approach vs. Blackbox approach
<img width="454" alt="image" src="https://user-images.githubusercontent.com/19539597/229902942-a336c4a2-209d-485b-8ae8-773e5c588d21.png">

Need to answer three questions when evaluating two approaches
- Why not just trust the trust the model?
- What if you adversely impact someone with a model?
- Are there regulatory requirements?

### Interpretable Models
- They are models that are designed with explanatory values
- Types of interpretable features include
	- Linear: model coefficients are proportional to  
outputs
	- Monotone: model coefficients go in the same  
direction as the target outcome
	- Interactions: feature interactions can easily be  
included to

### Typical Interpretable Models
- General Linear Model (GLM)
	- Linear and Logistic Regression
- Decision Tree
- RuleFit - sparse linear model

### Black Box Models
- Ensemble
- Deep Neural Networks
- Everything that works well as is called ‘AI’

### Taxonomy
- Intrinsic or post hoc
	- intrinsic: Explainability is built-in
	- Post hoc: Explaining after the model is built
- Some results of the method
	- Feature summary statistic  
	- Feature summary viz  
	- Model internals (learned weights)  
	- Data point  
	- Intrinsically interpretable
- Model-specific or model-agnostic explainability
- Local or Global explainability

## In-Class Exercise
### Why is model interpretability important?
- Compliance
- Building trust
- Detect bias in models
- Debug and audit models
- Understand why certain decisions were made
- Human curiosity and learning
- Safety: Feels good 
- Interpretability may incentivize humans to game the system

### What are the trade-offs of using ‘model-agnostic methods’ vs. an interpretable model?
- Offering flexibilities
- Easier to compare models
- UI becomes independent of the underlying model
- Interpretable model may be too simple and hard to explain the data


### What is the difference between global and local methods?
- Global is average behavior
- Local explains individual predictions

### From the testing section of ‘Made With ML.’ What are some similarities and differences in testing models vs code?
- Similarity: 
	- Validating the inputs and outputs of a system
- Difference: 
	- Testing model is more than just detecting exceptions and may require manual inspections and interpretation
	- Iterative approach to testing
	- Directionality End-to-End
- Assertions may be too ambiguous


## Model Testing
### Why Test?
- Models should work as intended  
- You get what you test for not what you expect for  
- Common software best practice is to do TDD  
- A CI/CD process is characterized by rigorous automated testing  
Related to interpretability and  explainability

## Model Testing
### Why Test?
- Models should work as intended  
- You get what you test for not what you expect for  
- Common software best practice is to do TDD  
- A CI/CD process is characterized by rigorous automated testing  
Related to interpretability and  explainability


### Testing in ML
- Test data
	- The formats and quality
	- e.g. Is there drift?
- Models
	- Typical operations
	- Specific settings (behavioral Testing)
	- Edgecases, boundary behaviors
- Deployment
	- AB tests. User behavior
	- Canary tests
	- Shadow tests ( in parallel with the production system)

## Wrap Up
- Ask how much interpretation is needed?
- When do you need it? For what reasons? How to collect the information.
- Testing models can be an aid to interpretability and managing expectation




