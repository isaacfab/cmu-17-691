# Class 10 17691
## Class Notes
### Classical Decision $ vs. Analysis Effect
- CDT based on the principles of expected utility theory, which involves weighing the probabilities of different outcomes against their respective utilities (values or benefits)
- Involves determining the optimal decision by selecting the option with the highest expected utility
- Analysis Paralysis can be overcome by setting clear goals and priorities, limiting the amount of information considered, and establishing a timeline for making a decision.
- Classical Decision Theory assumes rational decision-making and uses expected utility theory to determine the optimal decision, while Analysis Paralysis refers to the phenomenon of becoming overwhelmed by information and options, leading to difficulty in making a decision.
![image](https://user-images.githubusercontent.com/59854195/233800821-af93cae7-f693-4883-8d7c-2e65762588e1.png)

### Decision making characteristics
- Choice between 2 or more decisions called alternatives
- Uncertainty associated with an alternative
- Options that are likely to happen after uncertainty called prospects
- Values associated with each prospect/alternative
- Expectation calculation can be made to calculate the value of each of prospect/alternative 

![image](https://user-images.githubusercontent.com/59854195/233800564-121105e0-b526-419f-9c21-4386633a2cdb.png)

- Expectation value calculation (e-value)
![image](https://user-images.githubusercontent.com/59854195/233800571-ca62850e-4080-4177-9e3b-59ae9677ec58.png)
### Value of Clairvoyance

(https://ieeexplore.ieee.org/abstract/document/4082150)
- Clairvoyance is a hypothetical state in which a decision maker has perfect information and knows the outcome of all possible actions before making a decision.
- A decision maker is able to accurately predict the consequences of every possible choice and select the option that leads to the best possible outcome.
- The concept of clairvoyance serves as a benchmark or ideal for evaluating the quality of decisions made under uncertainty.
![image](https://user-images.githubusercontent.com/59854195/233800622-d2affce0-98e8-4df6-8fa7-d5cb6177d6b3.png)
Value of clairvoyance= 1125-1000= $125

### Detector and Predictor (Assessed Form)
- Don’t have the perfect knowledge, instead have a predictor that is able to predict the outcome with some specificity/sensitivity.
- Value of sensitivity
![image](https://user-images.githubusercontent.com/59854195/233800692-1624d40d-37e0-4e38-b78c-a6de2a6d48e3.png)

### Inferential Form (Bayes Theorem)
- Make a decision based on detector outcome
- Predict probability of actual outcome given the detection
![image](https://user-images.githubusercontent.com/59854195/233800710-2a7ea692-1d34-4b9c-99d4-89755078f576.png)

### Decision with Detector (Using Inferred Form)
![image](https://user-images.githubusercontent.com/59854195/233800724-9fc84574-67cf-4ae2-aab5-6083cd2267f2.png)

## In - Class Exercise
Using your function, assuming model sensitivity and specificity are the same, find the point of model quality (sensitivity and specificity) we are indifferent to having the sensor/model.
Plot the value of data (difference between not buying the sensor and buying the sensor) against various sensitivity/specificity (range 0-1 by .01 increments). Paste this plot and your answer to the previous task on your team slide.

```python
def predidct_value(p_storm, sensitivity, specificity, payout_of_harvest, payout_of_no_harvest_storm, payout_of_no_harvest_and_no_storm):
    p_dns = (specificity * (1 - p_storm) + p_storm * (1 - specificity))
    p_ns_dns = specificity * (1 - p_storm) / p_dns
    p_ds = (sensitivity * p_storm) + ( 1 - p_storm) * (1 - sensitivity)
    p_s_ds = (sensitivity * p_storm) / p_ds
    value_no_storm = max(payout_of_harvest, p_ns_dns * payout_of_no_harvest_and_no_storm + (1 - p_ns_dns) * payout_of_no_harvest_storm)
    value_storm = max(payout_of_harvest, p_s_ds * payout_of_no_harvest_storm + payout_of_no_harvest_and_no_storm * (1 - p_s_ds))
    value_no_harvest = p_dns * value_no_storm + p_ds* value_storm
    return abs(value_no_harvest - payout_of_harvest)
```
The predict_value function takes in various parameters related to weather patterns and payouts for harvest and no harvest scenarios. It then calculates the probabilities of different events occurring and uses them to calculate the expected value of harvest and no harvest scenarios under different weather conditions. The function returns the absolute difference between the expected value of a no harvest scenario and the payout of a harvest scenario. This method can be used to assess the risk and potential benefits of different decision choices related to agriculture and weather.
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

x = [x/100 for x in range(1, 101)]
y = [predidct_value(0.75, x/100, x/100, 1000, 500, 1500) for x in range(1,101)]
ax.plot(x, y)


ax.grid(True)
plt.show()
```
![image](https://user-images.githubusercontent.com/59854195/233801801-d8263ec7-7ad6-4221-98fe-c105ed80aba1.png)


Answer: We can see from 0.25-0.75 model quality (sensitivity and specificity) we are indifferent to having the sensor/model.
