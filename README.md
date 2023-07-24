# EnterpriseData-with-LLM
Generative AI is creating lots of exciting use-cases across industries. To create true business value from generative AI, requires integration of Large Language Models (LLM) with enterprise knowledge base. 
LLMs are not trained on proprietary enterprise specific knowledge (but are trained on publicly available internet data), they might hallucinate and provide incorrect response to enterprise specific questions.

In this repository, I will present a way to quickly (within 1–2 hours) and securely integrate your enterprise data (Confluence pages, Salesforce Data, CRM data, Relational databases, manuals etc.) with Large Language Models (LLM). This is a full end-to-end solution - no model training, fine-tuning, or extensive deployment needed. You also do not need any specific AI/ML experience or extensive developer knowledge to deploy this solution. The answers provided will be grounded in your organisations specific knowledge, avoiding factuality issues such as hallucinations and out-of-context responses.

This solution will enable enterprises to create a lot of business use-cases like:
- Improving customer experience: intelligent chat-bots providing answers based on enterprise data- say order status, account balance etc.
- Increasing internal employee productivity: by generating enterprise specific proposals/ marketing material/manuals/job descriptions etc.
- Internal Search engine: searching code repositories, internal documents, etc.
  
![AnimatedImage](https://github.com/sachink2010/EnterpriseData-with-LLM/assets/4855287/e6e83c11-478c-404c-8a86-4cdf0d11087e)

If you want to read more about architecture choices made here, please read Medium Blog https://medium.com/@Sachin.Kulkarni.NL/generative-ai-with-enterprise-data-3c81a8bffaf2. 

Here are steps to implement this solution:

1.	Login to your AWS Account, select any region (for e.g. Ireland (eu-west-1)) as the region and navigate to Amazon SageMaker Management Console. Click on Studio link in the left and then click on the Open Studio link.
   <img width="308" alt="image" src="https://github.com/sachink2010/EnterpriseData-with-LLM/assets/4855287/77e94527-038b-4bb4-bdc0-eb769715335f">

3.	It will launch Amazon SageMaker Studio in a new browser window or tab. In the studio, click on File in the top menu. Next Open Terminal
4. 	It will open Terminal tab. You can git clone here to download repository: https://github.com/sachink2010/EnterpriseData-with-LLM
5. 	


