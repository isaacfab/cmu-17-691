# Ethics and Governance

![](https://ml-ops.org/img/ml-engineering.jpg)

After deciding what is to be built and deploying it into production, there are external concerns. For these concerns, we pay special attention to testing, integration, and deployment. 

## Example Sub-Components of an ML Product for Governance
- Data Versioning (i.e. DVC)
- Data Labeling (i.e. Label Studio)
- Model Versioning/Mgt (i.e. CML, MLflow)
- MVP Demo (i.e. HF Spaces, Streamlit, Gradio)
- CI/CD and testing (i.e. Gitlab, Github, Bitbucket)
- Model Monitoring (i.e. seldon, evidently.ai, weights & biases)

## Why AI/ML Ethics Matter
- Projects can be shutdown due to the lack of standards and bad PR
- Biases can create negative reputation
- Can result in allegations and lawsuits
- Examples: 
    - Alphabet Smart city Project shutdown
    - Apple Card alogirthm found showing gender bias
    - Amazon's AI recruiting tool showing bias against women
- Training on biased data will result in a biased model
- [List of failed ML projects](https://github.com/kennethleungty/Failed-ML)
- We need to get in front of these issues and design around them as to not make the same mistakes as the above projects


[Practical Guide to Building Ethical AI](https://hbr.org/2020/10/a-practical-guide-to-building-ethical-ai)

## AI Ethics Stack (By CMU)
- Consider an ethical framework for your product
- Ethical considerations needs to be made at the outset of any project
![](https://images.squarespace-cdn.com/content/v1/51d98be2e4b05a25fc200cbc/f66e9e6e-d741-4225-bbc5-fda9555fa23c/tay1.png)

[See More](https://ai.cs.cmu.edu/about)

## Primary Sources of AI/ML Ethical Considerations

1. Data Security and Privacy
    - Does your system have the tendency to leak sensitive information?
    - Are you abiding by regional compliance laws
    - [Amazon has the largest GDPR fines ~ $877 million](https://www.tessian.com/blog/biggest-gdpr-fines-2020/)
2. Adverserial AI/Counter-AI
    - Using AI to overtly conduct nefarious activity
    - [Unregulated Deepfakes](https://fortune.com/2021/03/05/tom-cruise-deepfake-creator-technology-should-be-regulated/)
3. Unpredictable AI Behavior
    - It does things you don't expect
    - [Microsoft's racist chatbot](https://www.bbc.com/news/technology-35902104)
4. Harmful/Biased Autonomy
    - Does the system have a direct impact on another person directly without human involvement?
    - [Facial recognition falls short in preventing crime](https://www.nytimes.com/2020/01/12/technology/facial-recognition-police.html)

## In Class Exercise

### Required Readings

1. [Ethics and AI: 3 Conversations Companies Need to Be Having by Ried Blackman et a.](https://hbr.org/2022/03/ethics-and-ai-3-conversations-companies-need-to-be-having)
2. [A Practical Guide to Building Ethical AI by Reid Blackman](https://hbr.org/2020/10/a-practical-guide-to-building-ethical-ai)
3. [What is AI Model Governance? by Harrish Doddi](https://www.forbes.com/sites/forbestechcouncil/2021/08/02/what-is-ai-model-governance/?sh=37d74bca15cd)

### Questions

1. Pick one of the 3 conversations and give some insight:
    - Define your organization's ethical standard for AI
        - define legal and regulatory compliance
        - organize an ethical risk evaluation process
        - identify specific ethical risks to the relevant industry
        - if data is biased than models will be biased
    - Identify the gaps between where you are now and what your standards call for
    - Understand the complex sources of the problems and operationalize solutions
        - connect sources of problems to solutions (sources of bias to risk mitigation strategies)
2. What are some practical considerations for building ethical AI?
    - ensure data diversity
    - involve stakeholders in the development process
    - be transparent about the decision making process
    - focus on data privacy and control
    - utilize metrics to evaluate program effectiveness
    - incorporate human oversight and accountability
    - effective communication with customers
    - incentivize ethical AI
    - identify standards and goals
    - utilize modeling techniques such as LIME
    - make dashboards and metrics accessible
    - create risk mitigation plans
    - invest in tools and incentivize their use
    - Use a data governance board
    - Attempt data augmentation for underrepresented groups
3. What are important considerations for ML Model governance?
    - governance solutions should be able to track metrics
    - avoid model and team silos 
    - implement standardized practices
    - how ml products perform in the real world differ significantly from test/development environments
    - be careful about model/data security
    - model/data versioning
    - post deployment monitoring
    - tailor frameworks to their industry
    - monitor impacts
    - how inputs are weighed and what objective function is used

## Governance
- Not just self-imposed, can come from regulatory authorities
- Governance must be part of the data flywheel model lifecycle
![](https://cdn-images-1.medium.com/max/800/1*GY_sWM8SfZdp023IPJ1LXQ.png)

## Data and AI/ML Strategy

- Organizations are responsible for publishing a data and AI/ML Strategy
- A good strategy will include:
    - Short term focus
    - Long term flexibility
    - Clear understanding of priorities
    - Clear way to evaluate value
    - Specific tools to track progress

## Model Governance Tools

1. [DVC for data versioning for machine learning projects](https://dvc.org/)
2. [DataHub - open source data catalog](https://datahubproject.io/)

## Conclusion
- Ethical implications should be considered at all stages of development
- Governance is vital to see ethical improvements

