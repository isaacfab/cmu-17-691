# Class notes
Steve Choi, David Good
17-691 ML in Practice
Lecture 1
Scribe Notes

Task
* Update this file with notes for the class. Include summary of readings, in-class activities, and the lecture.
 
Lecture Notes
* Course Goals
* Course is less focused on algorithms and techniques
* More focused on product management of ML products and services
* Introducing scalability, reliability, maintainability to ML, which is hard to scale and introducing uncertainty
  * Course goal is to improve
    * Understanding about the assumptions of ML models
    * Creating value for the wider organization with ML
* Learning Objectives
  * Deploy products with ML/AI components
  * Build DE Systems and components
  * Measure value created by a ML system
  * Measure the value and quality of a production ML system
* Grading Policy
  * 60% - group project
  * 20% - class participation
  * 20% - assignments
* History of Data Science
  * DS <> ML
  * ML is one of the popular tools for analyzing data
  * Data science is a combination of CS, Math, Data
  * Lack of access to data and computing power limited development of data science
  * Breakthroughs in NN and network computers, after dot com bust, computing and data storage became drastically cheaper
  * Famous story from Aristotle about Thales of Miletus
    * From the stars, he took the data about the upcoming olive season and he took out leases on olives. Made a boat load of money by selling back the leases
    * Where to collect data? What can you do with that data to provide value? Can you capture that value?
  * Sir Francis Galton
    * Guess the weight of the ox
    * Won the ox itself for the person who guessed the correct weight
    * Avg of the guesses became better than the individual guesses
  * Experiment with pushups of the above ox experiment
    * Produce data and processed it
  * Alan Turning
     * Famous for Turning test and Turning machines
     * Google example of passing the Turing Test
  * Zillow and Opendoor
    * Zillow – real time information about housing in Pittsburgh
    * Tried to buy houses that were underpriced
 * Opendoor – we can do better. Buying houses that are underpriced and flipping them
    * Lost too much money and decompose that from a ML perspective
 * Key Class Takeaways
   * Less reliance on ML
   * Incorporate other business metrics to improve business metrics
   * Misapplication of the actual algorithm
   * Unstable/inaccurate data
   * More human expert inputs – local experts of the market, manual inspections
   * Lack of data
   * Issues with data collection processes
   * Data skew?
* Reading Notes
  * Data Scientist: The Sexiest Job of the 21st Century
    * Goldman of LinkedIn developed a key feature with the backing of then CEO, who realized the power of analytics from previous ventures, to improve LinkedIn’s click through rate by over 30%
    * In 2012, there was a severe shortage of data scientists and created bottleneck situations across industries
    * Data scientists are professionals who code and find trends in big data
    * Data scientists are going to be very well regarded in the future and will thrive in a setting where they have the freedom to explore and generate ideas for the organization
  * Companies are Failing in their Efforts to Become Data-Driven
    * Leading companies are struggling to become data driven due to organizational misalignment and cultural resistance
    * Significant investments are being made to build a data driven infrastructure and culture
    * Firms must become more serious about investing in the human side of data if they want to become more data driven
  * Zillow's home-buying debacle shows how hard it is to use AI to value real estate
    * Zillow tried to use the Zestimate to buy homes but after 8 months, shut down the home buying business
    * Challenges was to forecast home prices with a 3-6 month horizon
  * Invaluable Data Science Lessons To Learn From The Failure of Zillow’s Flipping Business
    * As the amount of Zillow's amount home data increased the quality of their models degraded
      * Data quality issues - Zillow relied on both public and user data
        * A relatively small data quality issue with accuracy problems results in a large monetary loss
        * Data Quality is hugely important - use metrics to measure data quality
      * Dependency on  algorithms
        * Where predicitons are critical use model outputs shouldn't be used to make decisions, only as supplemental information
      * Gaming the system
        * Utilize a fraud prevention team to ensure the domain isn't being manipulated fraudulently
      * Selective Focus
        * Study data science problems holistically from many perspectives before and after implementing a model
      * External Factors
        * Diversify risk and make efforts to account for external factors (e.g. labor costs rising/falling)
  * Reddit Thread
    * Mentions various issues with the underlying data that powered the algorithm
    * Mistrained the model on an bull market for housing
    * Some rumors about business decisions not being in line with model recommendations



Some ideas for the Group Product Proposal

Submit a one-page proposal for your group product (as PDF). This is the product your group will develop and demo at the end of the semester. Keep the description short and address some of the concepts presented in class 2.

Consider project ideas from these sources, while mostly focused on deep learning solutions they are a good starting point to consider;



