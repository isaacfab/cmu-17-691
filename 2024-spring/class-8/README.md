# Class Notes

## Lecture Insights

### MLOps Stack
- Data sourcing is a key part of ML engineering. Once you start collecting your own data, how you collect it can have long term consequences.
- Ethical considerations show up in integration testing and deployment to production, a stage which in turn feeds the ML engineering lifecycle.
- Most subcomponents associated with ethics and governance correspond to Data Versioning, Data Labeling, Model Versioning, MVP Demos, CI/CD, testing and Model Monitoring:
<img width="967" alt="image" src="https://github.com/isaacfab/cmu-17-691/assets/149334866/96718887-92d7-49ad-a171-260419054fba">

### Ethics
- AI/ML ethics matter because it can help identify biases in AI tooling.
- Thinking about how to hedge against issues of bias in your team's project plans.
- Four primary categories for ethics considerations:
<img width="337" alt="image" src="https://github.com/isaacfab/cmu-17-691/assets/149334866/83b6d2fd-621d-4d41-b704-1283d8ffc7ed">

- Data Security and Privacy Risk: Amazon fined $877M over 2019-2022
- Adversarial/Counter AI: be cautious about abuse cases, such as celebrity deep fakes
- Unpredictable Behavior: Microsoft's Tay was turned into a racist chatbot
- Harmful/Biased Autonomy: facial recognition software with bias towards certain ethnicities


### Governance
- In the right setting, governance can encourage best practices in engineering
- It's not just for fun, in some places it's required by law (such as GDPR)
- Governance can vary significantly by industry, such as government applications
- Data flywheel model lifecycle requires governance
<img width="335" alt="image" src="https://github.com/isaacfab/cmu-17-691/assets/149334866/b697a9d5-0f56-41d7-8131-f9f0f42a06f5">

- Governance starts with a strategy which outlines specific values
- DVC is an example of a model governance tool 
- DataHub is an example of a data governance tool 

### Wrap Up
- Consider ethical implcations of your product at all stages of development
- Governance is critical to both ethcial and provenance concerns for prouct improvement

## Reading Summary

### Ethics and AI: 3 Conversations Companies Need to Be Having by Ried Blackman et a.
- The article discusses the necessity for companies to have actionable conversations about AI ethics, emphasizing the importance of assembling a senior-level working group comprising technologists, legal experts, ethicists, and business leaders to address ethical risks effectively. It outlines three crucial conversations that companies need to have: defining ethical standards for AI, identifying gaps between current practices and desired standards, and understanding the complex sources of ethical problems to operationalize solutions.

### A Practical Guide to Building Ethical AI by Reid Blackman
- Companies are increasingly aware of the perils of overlooking ethical concerns in AI development, as illustrated by legal and reputational challenges encountered by industry giants like IBM and Goldman Sachs. To combat these risks, a practical seven-step approach is proposed, emphasizing the utilization of existing infrastructure, customization of frameworks, and cultivation of organizational awareness.

### What is AI Model Governance? by Harrish Doddi
- Financial institutions utilize data scientists to develop models for functions like fraud prevention, but lack visibility into their deployment and decision-making post-lab. AI model governance aims to bring accountability by tracking model versions, variables, access, behavior metrics, and security, overcoming challenges posed by siloed development and ensuring consistency across organizational environments.

## References and Sources
(to-do)
