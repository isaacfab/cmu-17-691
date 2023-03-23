# Class Notes
#### Previous Class Review: 
- Data Projects ~ primary focus is data 
- ML Products vs. Research 
    - 3/4 focus on data in ML Products to 1/4 models/algorithms 
    - Research heavily focused on models/algorithms

### Data Strategy
- guiding document drafted by leaders
- outlines vision and goal
- selection of data projects should be inline with the overarching data strrategy  

>collect data a priori -> unique and relevent data will make products more beneficial

### Data Project Workflow - CRISP-DM 
![image](https://user-images.githubusercontent.com/93678940/227079781-45f95df4-3338-457d-afc6-66b1f8eea565.png)  
[picture reference](https://www.datascience-pm.com/crisp-dm-2/)

### Problem Definition (Business Question, Business Understanding, etc.)
- goal of data project is to reduce the uncertainty of decisions
- important to understand the value provided by reduced uncertainty

#### User Discovery:
*primary goal should be to find out if people will actually use the product*   
methods:  
- interviews, focus groups, surveys, MVP with feedback, etc.  
>Note: gold standard is MVP with feedback  

### Machine Learning Projects  
Basic Components: Data Engineering, Data Science, Software Engineering   
Workflow:  
![image](https://user-images.githubusercontent.com/93678940/227079686-27ba23fc-7b19-4c9d-a038-400f74f94f9b.png)  
[picture reference](https://ml-ops.org/content/end-to-end-ml-workflow)  
> Does the project address a real user problem?

#### Data Flywheel - Data Network Effects  
![image](https://user-images.githubusercontent.com/93678940/227079494-0b192775-00ae-4993-9fc2-25f63fb4793a.png)  
[picture reference](https://dataloop.ai/book/the-data-flywheel-effect/)  
> Build in the capability to trigger the data flywheel upfront  

#### The AI Canvas  
![image](https://user-images.githubusercontent.com/93678940/227079155-cda95c4f-4822-473f-a7f6-4fcdd3b24471.png)   
[picture reference](https://medium.com/the-business-of-ai/the-ai-canvas-7a8717cddbe9)  
Helps organize thoughts and ensure the project makes sense 

### Challenges with ML Projects  
<table>
    <tr>
        <td> - Poor Problem scoping </td>
        <td> - Access to reliable data and data labeling </td>
    </tr>
    <tr>
        <td> - Lack of architecture design to support scale </td>
        <td> - Unaligned value proposition </td>
    <tr>
</table>

## In Class Exercise  

#### In Jeremy Howards article: Data Project Checklist pick two questions (from two different sections) that your team believes are important and explain why.   
- Historical Info  
- ROI of Project  
- Model En 
- Retraining frequency *  
- Focus on Data Collection **  
- Strategic Priority *  
- Valid Analytical Models  
- Anayltical Tools  
- Metrics  
- Data Availablility  

## Reading Notes:   

## 
[End-to-End machine Learning Workflow](https://ml-ops.org/content/end-to-end-ml-workflow)  
#### Notes:  
Outlines the workflow for Machine Learning projects to include the individual aspects of each major step (Data Engineering, Model Engineering, Model Deployment).  
##### Data Engineering  
1. Data Ingestion  
2. Exploration and Validation  
3. Data Wrangling (Cleaning)  
4. Data Labeling  
5. Data Splitting  
##### Model Engineering  
1. Model Training  
2. Model Evaluation  
3. Model Testing  
4. Model Packaging   
##### Model Deployment  
1. Model Serving  
2. Model Performance Monitoring  
3. Model Performance Logging  

## 
[Data Project Checklist](https://www.fast.ai/posts/2020-01-07-data-questionnaire.html)  
#### Notes:  
Outlines various questions that should be asked prior to starting a data project. These questions cover various aspects of data, metrics, capabilities, etc. that will be vital it clearing up any questions/doubts on what needs to be done, what can be done, and how it can be done. The questions are broken into into different sections that focus on different key aspects of the problem formulation. The breakdown can be seen below:  
![image](https://user-images.githubusercontent.com/93678940/227247466-e498eebc-95b8-4061-8607-f73894127d50.png)  

## 
[How to Decide Which Data Science Projects to Pursue](https://hbr.org/2018/10/how-to-decide-which-data-science-projects-to-pursue)  
#### Notes:  
Discusses how to identify what data science projects should be taken on. Key takeaways are that data projects need to fall inline with an 'excellent data strategy.' Additionally, the author contests the common practice of just going for whichever projects should produce the most results compared to input effort. Instead she suggests using a similar schema as a first step, but then draw parallels between projects that may build on each other or be related. Seeing these dependencies could make some of the more complicated projects less daunting or possibly show reasons some of the other tasks may not be possible.  

## 
[Avoiding Data Disasters](https://www.fast.ai/posts/2021-11-04-data-disasters.html)  
#### Notes:  
Uses a case study of a UK covid tracking app that was implemented to try and answer a question that it was not initially designed for. The app was meant to track the average covid case but was eventually used to try and answer questions about Long Covid. The fact that the data collected did not include a lot of the things necessary to answer questions about long covid became a major issue and eventually spread disinformation instead of answering questions. The author continues to discuss how import data is and how data always has a context that needs to be taken into account and NOT used out of context. The author also focuses on looking at who will be most impacted and ensuring that data is being used in a fair and ethical manner. 

## 
[DoD Data Strategy](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://media.defense.gov/2020/Oct/08/2002514180/-1/-1/0/DOD-DATA-STRATEGY.PDF)  
#### Notes:  
Outlines the Department of Defenses Data Strategy moving forward. Specifies areas it wants to improve and outlines what 'success' looks like for each area. Provides the vision, focus areas, guiding principles, essential capabilites and goals for the DOD moving towards accordance with this Data Strategy. The document further discusses the 8 guiding principles that the DOD will use as a foundation of all data efforts, the 4 essential capabilities they see as essential to enable their goals, their 7 goals and then their path moving forward.  
##### 8 Guiding Principles  
1. Data is a Strategic Asset  
2. Collective Data Stewardship  
3. Data Ethics  
4. Data Collection  
5. Enterprise-Wide Data Access and Availability  
6. Data for Artificial Intelligence Training  
7. Data Fit for Purpose  
8. Design for Compliance  
##### 4 Essential Capabilities  
1. Architecture  
2. Standards  
3. Governance  
4. Talent and Culture  
##### 7 Goals (VAULTIS)  
1. Make Data <strong>V</strong>isible  
2. Make Data <strong>A</strong>ccessible  
3. Make Data <strong>U</strong>nderstandable  
4. Make Data <strong>L</strong>inked  
5. Make Data <strong>T</strong>rustworthy  
6. Make Data <strong>I</strong>nteroperable  
7. Make Data <strong>S</strong>ecure  

## 
[Don't Make Data Scientists Do Scrum](https://towardsdatascience.com/dont-make-data-scientists-do-scrum-de87bc921a6b)  
#### Notes:  
Discusses several aspects of Scrum and then why/how they are not applicable to Data Science Projects. The author then goes on to discuss what may be a useful framework (which does incorporate some ascpects of Scrum) for Data Science projects vs. the Scrum framework that seems primarily geared towards software development. Key takewayas from the argument is that Scrum is geared towards a development practice that often builds on one project and has a clear definition of done whereas Data Science projects are often far more vague and a Data Scientist could have several projects. Since the Data Science projects have more of a research aspect, some of the core elements of Scrum do not make sense to impose on a data science project, it needs to be a more flexible model that keeps the pillars of transparency, inspection and adaption but without the rigid outline.  
