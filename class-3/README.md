# Class notes
Update this file with notes for the class. Include summay of readings, in-class activities, and the lecture.
### Artical Summaries: 
#### Article 1: https://ml-ops.org/content/end-to-end-ml-workflow

3 main artifacts: Data, ML Model, Code
3 main phases: data engineering (data acquisition and preparation), ML model engineering (training and serving), code engineering (integration of model into the product)
Phase 1: Data engineering 
Data ingestion: collect Spark, HDFS, CSV, synthetic data generation
Exploratory data analysis & visualization: meta data, structure of data, detection of major issues
Data cleaning and wrangling: initial step of re-formatting data, including data imputation
Data labeling: prepare the data label, collective information so the model can learn from raw data
Data splitting: splits data into train, test, validation etc. 
Phase 2: Model engineering
Model training: apply algorithm to train, feature engineering, hyperparameter tuning
Model evaluation: clear objective with stakeholders, determine a success metric
Model testing: run the model using the test data
Model packaging: exporting ML into format (PMML, PFA, ONNX etc.), ready for business sector to consume
Phase 3: Model deployment phase
Model serving: addressing ML model artifact in production environment
Model performance monitoring: develop metrics to measure ML model performances, watch for signals for re-training. Signs might include prediction deviation. Monitor model drift
Model performance logging: mark inference request on log-record, including environment variables, feature values, hyperparameters, code for the running model etc.

#### Article 2: https://www.fast.ai/2020/01/07/data-questionnaire/

Areas to consider before deployment an data project: organizational, data, analytics, implementation, maintenance, constraints
Ultimate question: what is the business objective, and how can the model help?
Organizational
Career path for DS, current recruitment process, consider work allocation, software and hardware involved, consider when would the work be outsourced
Current data driven approach, and profit drivers (actions and decisions to influence the driver)
Estimated ROI, consider time constraints and deadline
Data
Current data platforms (Hadoop, OLAP, OLTP, spreadsheets)
Data accessibility, constraints in incorporating data
Analytics
Current analytics tools, investigate cloud processing, measure of “good model”
Situation of visualization (predictive), tabular reporting, and predictive modeling
Implementation
Review past data-driven projects, validity of analytical models
IT integration challenge, staff  level training, monitor and support
Maintenance & constraints
Determine model rebuild frequency, logged maintenance, support requirements
Any culture, skills, structure that will place limitation on data project?

#### Article 3: https://hbr.org/2018/10/how-to-decide-which-data-science-projects-to-pursue
Main Point: What is a good data strategy?
It needs a well-coordinated organizational core. It’s built on a centralized technology investment and well-selected and coordinated defaults for the architecture of data applications. 
It should be specific in the short term and flexible in the long term. Make a five-year plan for the strategy. 
It considers one key insight: data science projects are not independent from one another. 
How to select a good data project? 
Here’s what project selection looks like in a firm with an excellent data strategy: First, the company collects ideas. This effort should be spread as broadly as possible across the organization, at all levels. If you only see good and obvious ideas on your list, worry — that’s a sign that you are missing out on creative thinking. Once you have a large list, filter by the technical plausibility of an idea. Then, create the scatterplot described above, which evaluates each project on its relative cost/complexity and value to the business.


#### Article 4: https://www.fast.ai/2021/11/04/data-disasters/
Main Point: Towards Greater Data Resilience. 
Data work always get undervalued and this will cause data disasters. 
To improve the data resilience, we can: 
Valuing data work 
From the example of covid data collection, we should understand how much data we really do need, and how tough it is when it’s missing. Rather than try to automate everything, the developer should focus on how humans and machines can best work together to take advantage of their different strengths. 
Documenting context of data 
Numbers cannot stand alone, we need to understand how they were measured, who was included and excluded, relevant design decisions, under what situations a dataset is appropriate to use vs. not. 
Close contact with the data 
Meaningful, ongoing, and compensated involvement of the people impacted
The developer should understand how “bad data” will impact the people involved. 

#### Article 5: https://media.defense.gov/2020/Oct/08/2002514180/-1/-1/0/DOD-DATA-STRATEGY.PDF 

Main point: The DoD Data Strategy. 
DoD is a data-centric organization and supports National Defense Strategy and Digital Modernization to make data driven decisions. 
The DoD reports claims 8 guiding principles that are foundational to all data efforts in the DoD. All these principles are focused on the value of the data and how the data can impact the real word settings. The DoD then brings out the 4 Essential Capabilities necessary to enable all 7 goals the organization wants to achieve. 
In general, DoD want to become a data-centric organization, and make the data visible, accessible, understandable, linked, trustworth, interpretable, and secure. 

#### Article 6: https://towardsdatascience.com/dont-make-data-scientists-do-scrum-de87bc921a6b
Main Point: Don’t make data scientist do scrum. 
“Scrum is a lightweight framework that helps people, teams and organizations generate value through adaptive solutions for complex problems.” 
However, in this article, the author stated that the Scrum is process-heavy and its not ideal for data scientists. 
Firstly, she mentioned scrum is immutable. Which means the scrum framework is very inflexible. The author complains that this immutability makes the Agile framework not Agile at all. 
Secondly, she mentioned data scientists usually work on several “products” and oftentimes their work is not an increment. Which is unnecessary to us the Sprint and Scrum at all. 
Thirdly, the author mentions that Data scientists do not always need a product owner. And take ownership away. The author believes that even if two data scientists are working on the same project, in my opinion, each one should still own different parts of the project. 
Finally, the author mentioned the Scrum is and Sprint functions are not user-friendly for data scientists. 
Alternatively, the author believes that for most data science works. The best way to maintain the data science project is to create documentations with transparency. 

### Lecture Notes: 
#### Data Focused Projects: 
Data projects have a broad range of complexity and purposes. 

#### Data Project Types: 
AI, Prescriptive, 

#### Organizational Data Strategy:
Companies and organizations have a document data strategy, providing visions and goals, criterias of selecting data projects. 

#### AI Index Report:
Summary of trendy topics in AI. Some examples include private investment in AI, cross-border collaboration, and AI ethics . Data is often the focus when improving model performance

#### Hugging Face: 
AI products community 

#### CRISP-DM:
Cross industry standard process for data mining. Workflow starts from understanding problems, preparing problems, and deploying models.

#### Data Science Process Workflow:
Problem, acquire, parse, filter, mine, represent, refine, interact, solution
Simplified version becomes: business question, munge, model, visualize (outcome), solution

#### Problem Definition - Fog of War:
There are decisions that need to be made under the fog (unknown), which determine the outcome of war (project). The goal is to reduce the uncertainty of decision (fog), and understand the value provided by reduced uncertainty.

#### Problem Definition - User Discovery:
The user discovery process usually happens before development of the project. Four types of user discovery processes: interviews, focus groups, surveys, MVP user testing and feedback. 

### In Class activities summaries: 
#### Data Project Checklist Important Questions: 
1. Exec experience? 
2. What the most import strategics
3. How are Data Scientists recruited?
4. How actions connected to result?
5. What data is available?
6. What systems are available, is there any major shift/change within the organization?
7. When is refactoring performed on code? How is correctness and performance of models maintained and validated during refactoring?
8. Reconsider why the model is successful, why did it work or why it didn’t work?
9. How to track the effectiveness of a model? Perhaps market has changed and the model is no longer valid, determine frequency need to calibrate and test the existing model
10. Determine ROI of the project, what is the business value the models ill bring to the organization?

#### Jeremy Howard: 
Fast.ai is a good resource to read on to pick up. His work mostly focus on high-end products.

#### Basic ML Project Workflow:
Problem Definition, data curation and labeling, data modeling, model deployment & monitoring.

#### Data Flywheel - Data Network effects:
More users lead to more data, smarter algorithms, better products, eventually lead to more users. 

#### Challenges with ML Projects:
There might be poor problem scoping, lack of access to reliable data and data labeling, lack of architecture design to support scale, and unaligned value proposition.


