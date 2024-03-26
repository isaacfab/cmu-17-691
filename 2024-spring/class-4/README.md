### ML Workflow
There are three "categories" of work in creating an ML product.
0. Problem definition
  - what are you actually hoping to do with this ML product? You need to know what the desired outcome is in order to get there.
1. Data engineering
  - acquire raw data
  - sanitize or process this data into some usable format
1. Data science
  - building and tuning the ML model
  - analytics
  - evaluation
1. Software engineering
  - turning that model into something that the average user can extract value from

### Metrics for ML
- Is ML even the right solution?
  - Get a thorough problem definition!
  - Is there some existing solution for that problem?
  - Can you make an MVP or promising mimimal solution for the problem?
  - Does ML actually help to solve the problem?
- Is your ML model good?
  - Define some metrics to determine what "good" performance is for your model.
  - The evaluation criteria for models, especially deployed models interacting with real users, may not be easy to define.
  - How impactful are false positives? False negatives? How does your model handle outliers or bad data?
  - When tuning your model, are you overfitting to the test set?
  - How are you defining a good model (what is your cost function)? Why are you using that cost function?
- Thresholds
  - At what threshold for any given metric do you consider it to be poor? At what point does a poor-quality model no longer produce value?
  - How do you intend to monitor metrics vs thresholds?
- Baselines
  - Compare model results to existing models or other solutions
    - industry standards
    - published results
    - human experts
    - Other simple models
    - AutoML models (see below)

### Top Tips for Developing ML Products
- One of the main uses of machine learning is to extract some set of rules from data and corresponding labels (training set). The assumption is that those rules apply to future data.
- You should take care to make sure your model is robust enough to handle missing data fields, and in cases where the machine learning model is not confident about being able to label (classify) some data, you should consider labeling it as such or setting some other fallback classification.
- ML products are not really useful without some baseline or metric to measure against. Get data from current systems before putting effort into adding ML capabilities, even if that data is just codifying human intuition.
- Start small and add complexity later. Simple models and products are easier to test and verify that the basics work before the system gets too advanced, preventing wasted time and effort.

### AutoML
- AutoML (automated machine learning) is a new technology for building deep learning (DL) models designed to lower the barrier to entry by handling some amount of data preparation, feature engineering, model generation, and model evaluation for the users, and using those results to improve the generated models.
- AutoML primarily focuses on optimizing Neural Architecture Search (NAS), or finding the best setup for a neural network based ML model for some DL problem that AutoML can test and evaluate.
- Automated machine learning also includes the concept of automatic data preparation, such as removing or marking outliers in data sets, and maximizing the value of features derived from those data sets.

### ML as a Product
- AutoML products include Google's Vertex AI, AWS AutoGluon, and AWS SageMaker - tools to help you build ML tools
- Amazon also sells Rekognition as a pre-trained computer vision (image classification) product
