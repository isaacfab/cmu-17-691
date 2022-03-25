# Lecture 4 - Do you even ML bro?

# Focus: Foundations

Philosophical/Programmatical consideration. What are you doing, and why?

# ML Project Workflow

- Data Engineering
    - DataOps: Automation, Data pipelines
- Data Science
    
    ![image](https://user-images.githubusercontent.com/85018020/160034401-8f448791-5d04-42e7-b14a-36f681179fa0.png)
    
    - MLOps: Places for automation, testing, evaluation
    - **Focus for today**: Baseline Model. How to set up the system to test the feasibility of the approach?
- Software Engineering
    - DevOps: Movement towards containerized applications. Combining Development with Operations with high levels of automation.
    

![image](https://user-images.githubusercontent.com/85018020/160034425-7eeacc61-b037-4a81-8570-caf661a6428f.png)

- Ask Questions
- Collect and Label Data
- Build Model
- Deploy and Monitor

(Data Flywheel)

# Metrics

What does your model do? 

How to test the quality of your model?

Measuring the value of your ML product

## Feasibility Assessment

- Is this even possible? Is ML the right solution?
- Thorough problem definition + user discovery
    - Interviews, Surveys, Is the data available?
- Analyze available literature and State Of The Art
    - What is possible?
    - Is the problem too challenging?
        - eg., ground autonomy. The vehicle can move from on-road to off-road dynamically (on the fly). It May sound trivial but extremely difficult in practice.
    - Readily available solutions [PapersWithCode](https://paperswithcode.com)
        - What is the closest to best-performing model right now?
        - Feasibility analysis using these resources
- Build a smaller model using a 100-1000 example labeled dataset
    - Gives an idea of how challenging scaling up will be.
- Build an MVP
- Again, Are you sure you need ML  ?

## Picking Metrics

- Data Modeling vs Algorithmic Modeling
    - Understanding quality when you give up explainability will be hard.
- Accuracy vs FP vs FN
    - Depends on domain
    - Some errors may be more acceptable than others
    - Accuracy alone is often not good enough
    - Everybody focuses on only accuracy but does not translate to real-world very well.
- Sensitivity to outliers.
    - Are edge cases handled well?
- Cost Function
    
    ![image](https://user-images.githubusercontent.com/85018020/160034474-4b59628b-54d8-47e1-9fb2-e8cf296a5dd8.png)
    
    - Does your optimization function make sense?
    - Squared Error is very sensitive to outliers. Different approaches to optimization will lead to different results.
    - DL models do not come with explainability. Adjust cost function to include uncertain components. It can be used as a tool to judge the quality of your prediction (adds some explainability).
- Confusion Matrix
    
    ![image](https://user-images.githubusercontent.com/85018020/160034499-6a36753e-acb8-4f8c-b229-1e6562166041.png)
    
- Accuracy, Precision, Recall: Which is the right one? Or do you pick a combo? There is a trade-off.
    - Combining Metrics
        - Simple Average
        - Weighted Average (F1 Score)
        - Thresholds (becoming more common now, eg in regulated applications) eg. Medical Devices
            - Considerations
                - Industry Requirement; how difficult is it to meet them?
                - How important is the metric for creating value? Does the metric decide value?
                - How does the baseline model perform?
- Baseline Model
    - First Pass
    - The lowest amount of effort
    - Relatively simple
        - How simple can you make your first pass?
        - Start with the most basic cost function to get to proof of concept.
        - Don’t go too sophisticated too quick.
    
    ![image](https://user-images.githubusercontent.com/85018020/160034514-a9c41afe-62bf-4a33-86b2-35cba7495a92.png)
    
- Baseline Ideas
    - Low cost lower bound
        - Threshold, above which the challenge is to improve the performance to be relatively valuable.
        - eg, 80% baseline. Reasonable to get to 85-90%. Depends on the use case.
    - Placeholder
        - The goal is to give you all the mechanics.
        - What features come in/out need not be a concern. Architecture can be decided later.
- Baseline Sources
    - Industry Standards
    - Published Results - Can be misleading. May not be practical for your own use case. Performance considerations.
    - Heuristics or Rule-based (little old lady in tennis shoes)
        - Old lady at a store
        - Lady knows everything about the store
        - Lady is a great predictor
        - What heuristics does the lady use?
        - Somebody has a “rule of thumb”. FInd that rule of thumb, and convert it into a programmatical solution.
    - Human performance
        - Eg, cancer detection. Radiologists are pretty good at it. Very difficult to beat. How do you determine how good these individuals are? How good does your model need to be?
    - Simple ML Model
        - D-Tree, Random Forest
    - AutoML
        - Deep learning, search through different architectures
        - A good ML Engg can almost always beat AutoML

# In-Class Exercise

- What are the benefits and drawbacks of using a heuristic as a baseline?
    - (+) Gives you an easy to generate and understanding starting point that your ML solution must beat
    - (-) A good heuristic can sometimes be too complex. A simple ML model might be a better choice at this point.
- What is an important takeaway about baseline models according to Google’s ML Product Rules 1-4?
    - Start small and simple. Focus on system design and a robust infrastructure first before pursuing baseline models
    - A good amount of thought needs to be given to understanding the problem
    - Choosing simple features can help get a good baseline ML model. Model explainability and interpretation is important at this stage.
- Choose one of the AutoML products from your reading. How much do they align with the AutoML paper? What portion of the ML Workflow is covered?
    - The paper outlines all the steps that an ideal AutoML solution would follow. It offers various techniques that such a solution could take. For example, the data
    the cleaning process can be approached as either a boosting problem or a hyperparameter search problem.
    - Google’s VertexAI pushes data cleaning more towards the user than the paper suggests. It expects relatively clean data
    - Vertex AI also adds some wrappers and tools on top as “extra features” Eg, TensorBoard allows you to visualize metrics, analyze model weights, biases, etc.
    - Other features added include edge computing, CI/CD integration, SageMaker Studio for development, and others.
- What are the benefits and drawbacks of using AutoML as a baseline?
    - Easy to obtain, no expertise needed
    - You give up on interpretability for a better baseline.

# AutoML

- Potentially can automate must of the architecture
- Great option for non-ML Engineers
- Does have known issues
    - Black boxes
    - Unknown quality of model
    - Edge cases, does it generalize well?
    - Not much control over quality
    - Often times this is okay and can be overcome with lots of good data

![image](https://user-images.githubusercontent.com/85018020/160034531-6bb63185-9535-42d0-bfa6-84155a6e8bba.png)

- Automate either all of it or a piece of it with AutoML.
- You don’t have to use all of the AutoML features.
    - Pick and choose what is valuable to you for your use case.

# Readings

## **Best Practices for ML Engineering**

[https://developers.google.com/machine-learning/guides/rules-of-ml](https://developers.google.com/machine-learning/guides/rules-of-ml) 

- Outlines several rules for building ML products
    
    ![image](https://user-images.githubusercontent.com/85018020/160034558-e49a1e22-b2f0-40cc-a5f8-bff1018ad211.png)
    
- Can be used as a skeleton for making sure your ML project is headed in the right direction. All the way from problem recognition to maintaining and measuring the performance of your model.
