# Class notes
Update this file with notes for the class. Include summay of readings, in-class activities, and the lecture.

# In Class Discussion
- Why is model interpretability important?
    - Machine learning models can only be debugged and audited (e.g. detecting bias) when they can be interpreted. 
    -  Interpretability can increase social acceptance for a machine learning model. (This point is debatable though. As discussed in the class, social acceptance might be more related to the importance of decision made by the model)
    - Interpretability is important when the model has significant financial or social impact. 
    - Interpretability is important when the problem domain is not well studied. Interpretability makes it possible to extract this additional knowledge captured by the model.
    - Interpretability also resonates with the human characteristic of curiosity to learn and know what something is doing.


- What are the trade-offs using ‘model-agnostic methods’ vs. an interpretable model?
    - Model-agnostic Methods
        - (+) Flexible: can be applied to a number of black box models
        - (+) Easy to compare: good for comparing interpretability across a number of black box models.
        - (-) Lack of interpretability: by nature, black box models lacks interpretability. 
        - (-) Limited application: MA are limited to specific model classes(regression weights) and applied after the model has been trained on feature i/p-o/p pairs. 
    - Interpretable Model
        - (+) Superior interpretability: being able to understand the underlying model structure
        - (-) Hard to compare: interpretability can be hard to compare across a number of interpretable models.
        - (-) Lower performance: interpretable models generally show lower performance than black box models.


- What is the difference between global and local methods?
    - Global:
        - Looks at how your model behaves across the space of possible inputs.
        - Focused on explaining the distribution of the total set of events. 
        - Describes how features affect the prediction on average.
        - Could be very difficult to achieve in practice.
    
    - Local:
        - Looks at one prediction and explain individual prediction. 

- What are some similarities and difference in testing models vs code?
    - Similarity: 
        - Both need to make sure the function can work as expected without any errors. 
        - Both need load testing / stress testing
    - Difference: 
        - ML systems could run with no obvious errors or exceptions even when the system is not correct. We need to catch errors quickly. 
        - Tracking experimentation for model testings is necessary.
        - ML models requires large integration-type tests while unit test code uses small atomic tests on method/functions.
        - Testing code focus on details of each functions, whereas testing models does not.
        - Testing granularity for model testing: Behavioral testing can only happen when testing models and the boundary of right or wrong for testing models is not binary.

# Reading Notes

- Interpretability
	- Importance
		- Advance the science
		- Ensure safety for real-world tasks
		- Debug biased models
		- Increase social acceptance
		- Audit mistakes
	- When is interpretability not important?
		- Low stakes tasks
		- Well-researched/understood problems
		- When transparency would allow people to game the system
	- Methods:
		- Model-specific tools examine the internal mechanisms of a model to explain how it works.
		- Model-agnostic tools treat the model as a black box, analyzing how the inputs relate to the outputs.
	- Types of interpretation:
		- Local: explaining a single prediction
		- Global: explaining broad trends in model behavior
	- Explanation methods properties:
		- Expressive power: What is the "language" of the explanation ?
		- Translucency: Does it analyze the inner workings of the model?
		- Portability: Does it translate to multiple models?
		- Algorithmic complexity: How fast can we generate the explanation?
	- Individual explanation properties:
		- Accuracy: How well does it generalize to unseen data?
		- Fidelity: How well does it describe the actual predictions of the model?
		- Consistency: How much does the explanation change for models that produce similar results?
		- Stability: How much does the explanation change for similar instances on a fixed model?
		- Comprehensibility: Can humans understand the explanations?
		- Certainty: Can the explanation determine how sure the model is about different predictions?
		- Degree of Importance: What features and model attributes contribute the most to the predictions?
		- Novelty: Is the instance radically different from the training data?
		- Representativeness: How much of the model's behavior does the explanation cover?
	- Explanations must account for human psychology. It isn't practical to enumerate every detail that affects the models behavior.

- Testing ML Systems
	- Major types of code tests:
		- Unit
		- Integration
		- System
		- Acceptance
		- Regression
	- Testing framework:
		- Arrange: choose the inputs for the tests
		- Act: run the component on those inputs
		- Assert: check that the output matches expectations
	- Test-driven development: write the tests as you work on the component, not once it is completed
	- Some useful tools:
		- pytest
		- great_expectations
