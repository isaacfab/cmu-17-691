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




