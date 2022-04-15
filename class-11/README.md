# Lecture 9 - Applying ML concepts to DA

## Focus: Value
- Calculate the value of a ML model in a project relative to the quality of the model BEFORE building the model

- Amount of analysis typically has a negative corelation with the number of decisions that you can do for that analysis. ML allows to decisions very fast through automation - i.e it allows to add scale

## Decision Modeling characteristics
![image](https://user-images.githubusercontent.com/14092419/163651925-cef0e404-021c-4e14-84b9-a1e9df977c69.png)

Consider the following example decision analysis tree:

![image](https://user-images.githubusercontent.com/14092419/163652094-d7e61c10-21ca-457d-aa0f-67360318163d.png)

- Compare branches based on their E-values (expected values)
- Assumption: Risk neutral - terminal values do not change based on stakeholder's preferences
- Convert uncertainty into a certain equivalent - the expected value of the uncertainty is a certain equivalent compared to a guaranteed value
- Here, guaranteed value = $1000, certain equivalent (E-value) = $1,500\*0.25 + $500\*0.75 = $750
- Choose the alternative that has a higher pay-off (i.e Harvest)

## Value of Clairvoyance
The extreme version of 'knowing more' - how much should we pay, at maximum, for 'knowing more'?

![image](https://user-images.githubusercontent.com/14092419/163652571-334fca5e-bf07-4ace-9a8e-0257a44e81d3.png)

- Make the decision based on fortune teller's prediction
- You know what the prospect will be because you purchased clairvoyance
- Certain equivalent of the Storm-No Storm uncertainty here = $1,500\*0.25 + $1000\*0.75 = $1125
- Purchasing knowledge about the future doesn't eliminate unertainty
- $1125 better than the original prospect of $1000 - pay no more than $125 for clairvoyance
- Value of Clairvoyance (VoC) = $1125 - $1000 = $125
- Do not invest more than VoC on the entire MLOps eco-system

## Detectors and Predictors
![image](https://user-images.githubusercontent.com/14092419/163653173-2b48e0e6-f675-45ed-86a1-e829443aa837.png)

Incoroprate a new uncertainty - the ML model. Collect data and train model in Assessed Form 
- Record data
- Train model from recorded data
- Evaluate Model's performance - Sensitivity and Specificity
- Calculate value provided by the model with these performance metrics

Inferential Form
- Go from assesed form to inferential form using Bayes Rule
![image](https://user-images.githubusercontent.com/14092419/163653381-4ee59518-eddf-4123-b888-3a9d87f9f241.png)
NOTE: NS/S - actual/observed; DNS/DS - predicted by detector

Decision with Detector
![image](https://user-images.githubusercontent.com/14092419/163653489-e62fa9eb-9c7d-498d-9096-1bc2b2b5f396.png)







