# ML Tools and Infrastructure
## Lessons Covered So Far
- Data can be leveraged to provide value.
- Value is best delivered via a software product which has many more considerations than just modeling. The ecosystem of
  how to collect, curate, aggregate, and use the data is also important.
- Data products are a broad category and ML products are specific to using data for creating value via prediction that is
  always undergoing improvement.
- Product quality is only measured by how much value it generates so understanding the user is critical. Emphasize user
  adoption and create value to users.
- Start building an ML product as simple as possible
    - Heuristic model
    - AutoML
    - Open Source

## MLOps Overview
### Definitions
-	MLOps: DevOps x ML; Extension of DevOps methodology to include ML and data science assets as first-class citizens within the DevOps ecology
-	DevOps: a set of practices that combines software development (Dev) and IT operations (Ops); aims to shorten the systems development life cycle and provide continuous delivery with high software quality; many features no automated/triggered
### Basic Components of an ML Product

Data flywheel: Ops integrates data flywheel principle, where additional data improves model
## Workforce Roles
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>Workforce Roles</title>
   </head>
   <body>
      <hr>
      <table>
         <tr>
            <td style=min-width:50px>Type</td>
            <td style=min-width:50px>Role</td>
            <td style=min-width:50px>Description</td>
            <td style=min-width:50px>Responsibilities</td>
            <td style=min-width:50px>Tools</td>
         </tr>
         <tr>
            <td style=min-width:50px rowspan="4">Data owners</td>
            <td style=min-width:50px>Chief information officer</td>
            <td style=min-width:50px>
               Oversees the people, processes and technologies within a company's IT
               organization to ensure they deliver outcomes
               that support the goals of the business.
            </td>
            <td style=min-width:50px>
               • Information systems strategy<br/>
               • Access control policies<br/>
               • Approves and manages data ecosystem relationships with other system owners<br/>
               • Ensures compliance with legal and ethical standards
            </td>
            <td style=min-width:50px></td>
         </tr>
         <tr>
            <td style=min-width:50px>Chief data officer</td>
            <td style=min-width:50px>Senior exec responsible for the utilization and governance of data across the org</td>
            <td style=min-width:50px>
               • Organization data strategy<br/>
               • Implements and approves much of the data ecosystem<br/>
               • Compliance and governance<br/>
               • Ensures compliance with legal and ethical standards
            </td>
            <td style=min-width:50px></td>
         </tr>
         <tr>
            <td style=min-width:50px>IT system owner</td>
            <td style=min-width:50px>Owns' a particular data generating system</td>
            <td style=min-width:50px>
               • Deploy and maintain a system of value for an organization<br/>
               • Responsible for the security of the systems information
            </td>
            <td style=min-width:50px></td>
         </tr>
         <tr>
            <td style=min-width:50px>Product manager</td>
            <td style=min-width:50px>Identifies customer need and the larger business objectives that a product or feature will fulfill, articulates what success looks like for a product, and rallies a team to turn that vision into a reality</td>
            <td style=min-width:50px>
               • Customer discovery<br/>
               • Product design and development<br/>
               • Ensures compliance with legal and ethical standards<br/>
               • Build and motivate a team to turn a product into reality<br/>
               • Coordinates with other data owners
            </td>
            <td style=min-width:50px></td>
         </tr>
         <tr>
            <td style=min-width:50px rowspan="2">Data steward / custodian</td>
            <td style=min-width:50px>Data engineer</td>
            <td style=min-width:50px>Builds and maintains data management systems</td>
            <td style=min-width:50px>
               • Architecting data management systems<br/>
               • Conversant in RDBMS and big data<br/>
               • Build data pipelines to move data from sensors to the data lake
            </td>
            <td style=min-width:50px>
               • SQL<br/>
               • Python/Java<br/>
               • Orchestration (Airflow, Snowplow)
            </td>
         </tr>
         <tr>
            <td style=min-width:50px>Database administrator (old school data engineer)</td>
            <td style=min-width:50px>Maintains a data management systems</td>
            <td style=min-width:50px>
               Maintaining an organizations
               authoritative database (typically a
               large-scale RDBMS – Oracle, MS
               SQL, Salesforce, etc.)
            </td>
            <td style=min-width:50px>
               • SQL<br/>
               • Vendor specific training
            </td>
         </tr>
         <tr>
            <td style=min-width:50px rowspan="6">Data Users</td>
            <td style=min-width:50px>Data analyst</td>
            <td style=min-width:50px>Gets data and data focused products into the hands of organizational decision makers; 'gate-keeper' of the data</td>
            <td style=min-width:50px>
               • Data Analysis (summary statistics and visualizations)<br/>
               • Custom Data Retrieval<br/>
               • Building and Maintaining Dashboards
            </td>
            <td style=min-width:50px>
               • PowerBI<br/>
               • Tableau<br/>
               • Excel<br/>
               • Database
            </td>
         </tr>
         <tr>
            <td style=min-width:50px>Self serve data analyst</td>
            <td style=min-width:50px>Uses 'self serve' tool to answer ad hoc questions</td>
            <td style=min-width:50px>
               • Answer questions with requests for support
            </td>
            <td style=min-width:50px>
               • Spreadsheets<br/>
               • Business Intelligence
            </td>
         </tr>
         <tr>
            <td style=min-width:50px>Data scientist</td>
            <td style=min-width:50px>Uses data and algorithms to uncover useful insights</td>
            <td style=min-width:50px>
               • Exploratory Data Analysis<br/>
               • Statistical Modeling (Inference and Hypothesis Testing)<br/>
               • Decision Analysis/Support<br/>
               • Part of a small team
            </td>
            <td style=min-width:50px>
               • Python<br/>
               • Jupyter<br/>
               • Git<br/>
               • sklearn, tf, pytorch, etc
            </td>
         </tr>
         <tr>
            <td style=min-width:50px>Citizen data scientist</td>
            <td style=min-width:50px>Lay user who uses low/no code environments that automate advanced analysis</td>
            <td style=min-width:50px>• Create ad hoc analysis</td>
            <td style=min-width:50px>• Low/No code tools such as Data Robot</td>
         </tr>
         <tr>
            <td style=min-width:50px>ML Engineer</td>
            <td style=min-width:50px>Designs, builds, and productionizes ML models to solve business challenges</td>
            <td style=min-width:50px>
               • Architects and Trains ML Models<br/>
               • Deploys trained models into ‘production’ software<br/>
               • Part of a small team with other developers<br/>
            </td>
            <td style=min-width:50px>
               • Python<br/>
               • Jupyter<br/>
               • Git<br/>
               • sklearn, tf, pytorch, etc
            </td>
         </tr>
         <tr>
            <td style=min-width:50px>Software developer</td>
            <td style=min-width:50px>Builds applications that integrate data insights (graphs to ML models)</td>
            <td style=min-width:50px>
               • Architects and builds various application types (web, mobile, IoT, etc.)<br/>
               • Deploys trained models into ‘production’ software<br/>
               • Part of a small team with other developers
            </td>
            <td style=min-width:50px>
               • IDEs<br/>
               • VCS<br/>
               • Debugging and profiling tools
            </td>
         </tr>
      </table>
      <hr>
   </body>
</html>

### Collaborative roles
-	Most technical collaboration tools are specific to DevOps; not suitable for ML
-	Most data scientists prefer jupyter notebooks (JSON)
-	Declarative approaches are young, not industry standard
    -	Nbdev (notebook dev)
    -	DVC (data version control)
    -	DagsHub <used in class>

## Infrastructure Stack
- There is an ML System Problem
    - ML Systems are hard to design well
    - It is easy to incur technical debt
    - Models are often bespoke and not declarative

## Example Sub-Components of an ML Product
A reference to choose components for your own product!


## In Class Discussion
Based on your readings, what are some considerations when deciding on cloud infrastructure for an ML Product?
-	Cost: cost of ETL, training, deployment, run time
-	Minimize with infrastructure optimization
-	Mixed approach: cloud now, repatriate later
-	Consider immediate and life-time cost
-	Collaborative challenges / friction mitigation
-	Scaling implications
-	Security

Comment on one item from the ‘Changelog’ in the article Emerging Architecture for Modern Data Infrastructure
- No change
    -	Stability of cloud warehouses, relational DBS
    -	Dashboards are the most common application in output layer
- Change
    -	Interest in metrics layer
    -	Growth of reverse ETL vendors
    -	Profits for data discovery and observability companies
    -	Data-centric approach to ML vs modelling improvements; previously thought model was most important aspect of MLOps; Interesting to see that nothing has changed much
    -	Pre-trained models can save significant time and resources

What are some challenges your group will face when designing an ML product based on the State of MLOps article?
-	Model dev & performance goals
-	MLOps change quickly, should do self-improvement
-	SME
-	Team members with different expertise might make cooperation difficult
-	CD immature process
