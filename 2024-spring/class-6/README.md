# Class Notes
Type your notes into this file and then submit them as a pull request within 1 week of the class.

# Lecture Title: Deployment and Monitoring
Scribe Members: Chi-Hsiang(Johnson) Lo, Jason Li
## Agenda:
House Cleaning
MLOps Stack Review
Model Deployment
Model Monitoring

The lecture focuses on the practical aspects of machine learning, particularly within the scope of MLOps, which is crucial for deploying and monitoring machine learning models effectively. The agenda covers a variety of topics including house cleaning, MLOps stack review, model deployment, and model monitoring.

## MLOps Stack Review: 
The lecture discusses the expansive nature of the ML project workflow, detailing various sub-components of an ML product. This includes data engineering, data versioning, exploration, warehouse/lake infrastructure, pipelines, software engineering, model versioning/management, cloud development environments, CI/CD, testing, and deployment orchestration tools. The tools mentioned range from data versioning tools like DVC to cloud services like AWS, Azure, GCP, and frameworks for modeling like TensorFlow, PyTorch, and Scikit-learn.

## Model Deployment: 
The deployment section addresses the structure of applications for deploying machine learning models, distinguishing between edge and remote/cloud deployments. It discusses batch prediction and Model as a Service (MaaS) deployment strategies, detailing the advantages and challenges of deploying models within the application framework or as external services. Furthermore, it touches upon deploying at the edge, emphasizing low latency, hardware limitations, and the challenges of updating models.

## Model Monitoring:
Monitoring post-deployment is crucial due to potential performance degradations, known as "drift." The lecture categorizes drift into data drift, model/concept drift, and domain shift, highlighting the importance of monitoring for data quality. It also explains different types of drifts, including instantaneous, gradual, periodic, and temporary drifts, and suggests what to monitor, from model metrics like accuracy, precision, and recall to business metrics and system performance.

# Tools and Techniques:
For managing and monitoring deployed models, the lecture suggests using tools like evidently.ai and neptune.ai, emphasizing the need for logging metrics and analyzing data to detect and address drift.

In summary, this lecture provides a comprehensive overview of the considerations, tools, and strategies involved in deploying and monitoring machine learning models, highlighting the importance of selecting the right deployment option based on product requirements and actively monitoring model performance to address any issues of drift promptly.
