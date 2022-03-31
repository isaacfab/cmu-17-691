# Class notes

Update this file with notes for the class. Include summay of readings, in-class activities, and the lecture.

## Reading Summary

### Ariticle 3: **[Intro Docs for Evidently.ai tool](https://docs.evidentlyai.com/)**

Evidently is an open-source Python library for data scientists and ML engineers. It helps evaluate, test and monitor the performance of ML models from validation to production.

Evidently has a modular approach with 3 interfaces on top of the shared `Analyzer` functionality.

1. Interactive visual reports: Evidently generates interactive HTML reports from `pandas.DataFrame` or `csv` files. like Data Drift and Quality, Categorical and Numerical Target Drift, Classification Performance and Regression Performance.

2. Data and model profiling: Evidently also generates JSON `Profiles`, which can be used to integrate the data or model evaluation step into the ML pipeline.

3. Real-time ML monitoring: Evidently also has `Monitors` that collect data and model metrics from a deployed ML service, which can be used to build live monitoring dashboards.