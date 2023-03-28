# Class Notes: Baselines: Do you even ML Bro?
## Lecture Notes:
### Lesson Objectives:
- Build a human-defined baseline
- Understand AutoML and some of its commercial implementations

### Main Focus: Foundation

- Performance
- Evaluation
- Generate model baseline

### ML Project Workflow Overview

#### 3 Basic components of ML product:

- Data Engineering
- Data Science
- Software Engineering

<img width="800" alt="image-20230327233156999" src="https://user-images.githubusercontent.com/100179117/228269122-f32a3ce4-bf09-45b7-9478-d21f7631bcbd.png">

#### Expanding into ML project workflow:

- Data pipeline: data acquisition & data preparation
- Machine learning pipeline: ML model training & serving
- Software code pipeline: integrating ML model into the product

![image](https://user-images.githubusercontent.com/100179117/228273924-cdca8b7a-2c07-4ac1-88d0-ca8b972ef4ef.png)
Reference: https://ml-ops.org/content/end-to-end-ml-workflow

#### Basic ML project workflow:

1. Start with the problem: root in user-defined consideration
2. Curate data and labeling
3. Model development
4. Deploy and monitor

<img width="384" alt="image-20230327234033980" src="https://user-images.githubusercontent.com/100179117/228273845-86172217-bcf6-4b62-a6ba-fad78ccd1ff4.png">

The virtual cycle only works when we evaluate the quality of the value we are producing. Thus, we need metrics that are directly tied to the value we are producing for expected outcomes.

### Metrics

Metrics for Large Language Model: 

- Initially trained on cost function -> Unsatisfactory outcome
- Tune model on reinforcement learning with human feedback (RLHF) -> Magic work!

#### Before Building a Model: Feasibility Assessment

- Do you even need to do machine learning at all?
- Have you gone through problem definition and user discovery?
  - Are you comfortable that you are working on something that is going to provide value?
- Have you looked at available literature and current state-of-the-art?
  - Have you looked at what people are currently doing to solve the problem?
  - Is that something within reach?
- Try to build a small labeled dataset
- Build a Minimum Viable Product (MVP)
  - Are users excited about the product?
- Again, do you even need to do machine learning at all?

#### Picking Metrics

##### Accuracy vs. False positive vs. False negatives:

- Depends on a different context
- e.g., Lots false negatives in self-driving car situation (Miss pedestrians or things on the road) would cause accidents
- Addiction to accuracy in ML community: Often used as a competition metric, but we should not overweight its role

##### Sensitivity to outliers:

- Edge cases in computer vision are still challenging

##### Right cost function:

<img width="500" alt="image-20230328000340320" src="https://user-images.githubusercontent.com/100179117/228269438-ad77930c-15ea-42a4-ab7c-bd5b3464a0de.png">

Need to consider:

- How is the model providing value?
- Where is it acceptable to make errors, and where is it not acceptable?

##### Confusion Matrix

Indication about the cost of things being wrong

<img width="626" alt="image-20230328001030069" src="https://user-images.githubusercontent.com/100179117/228269485-9f7eb7e4-9063-44b5-a64b-eb1a26f8a1f2.png">
Reference: https://fullstackdeeplearning.com/spring2021/lecture-5/


Medical industry:

- FDA guidelines for precision and recall low-line threshold around medical devices: 70% precision, 50% recall
- Model has to be frozen: Once deployed, not be able to constantly update

##### Combine Metrics

- Average: Less common but easy and intuitive  
  - Simple Average
  - Weighed Average
- Thresholds
  - Base industry requirements
  - How important are the metrics to create value?
  - How do baseline models perform?
  - Common in regulation: FDA guidelines

### Baseline Model

 ~~Define problem -> Collect small datasets -> .~~ Build your first model
 
 Baseline Models help us set expectations for how well our model will perform.

#### Baseline Idea: How complicated?

- Simplest possible model to test out initial data pipeline
- Provide lower bound of cost on expected performance
  - Take others' work and tweak it to improve the concept
  - Alpaca: Similar performance with GPT with a $200 infrastructure cost
- 'Place holder' from which to build MLOps and product architecture

#### Baseline Sources:

- Industry standard
  - Healthcare
- Published results
  - Sometimes can be misleading or hard to replicate
- Heuristics or Rules-based 
  - Logical framework to solve the problem without training machine learning model
  - People who have been solving the problem for a long time may have the rule of thumb that they used to make predictions
  - Great place to start the baseline model
- Human Performance
- Simple ML model
  - Avoid deep learning unless you are in deep learning use case
  - Tree methods
- AutoML
  - If in the deep learning use case, use AutoML solution to start

### AutoML

- Mechanism where one can generate model architectures without a lot of extra work
- Not good as handcrafted model but a great place to start for a baseline
- Great option for those who are not great ML engineers
- Known issues:
  - Lead to bias

#### AutoML Components:

<img width="583" alt="image-20230328003904930" src="https://user-images.githubusercontent.com/100179117/228269530-45ef6f69-ab18-40a5-9bd4-9c1fe37e2af2.png">
References: https://www.sciencedirect.com/science/article/pii/S0950705120307516

### In-class exercise:

- [Required Tutorial](https://calmcode.io/human-learn/introduction.html)
- Problem: What is the likelihood that you are going to survive the Titanic
- Good heuristic: Female
- Improved heuristic: Age smaller than 16 or Female
