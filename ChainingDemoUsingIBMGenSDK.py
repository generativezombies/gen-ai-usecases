#Chaining using IBM Generative AI SDK

import os
#import genai.extensions.langchain
from dotenv import load_dotenv
from genai.credentials import Credentials
from genai import PromptPattern
from genai.schemas import GenerateParams
from genai.extensions.langchain import LangChainInterface
from langchain.chains import SimpleSequentialChain
from langchain import LLMChain

# make sure you have a .env file under ibm-generative-ai root with
# GENAI_KEY=<your-genai-key>
# GENAI_API=<genai-api-endpoint>
load_dotenv()
api_key = os.getenv("GENAI_KEY", None)
api_url = os.getenv("GENAI_API", None)
creds = Credentials(api_key, api_endpoint=api_url) # credentials object to access the LLM service
params = GenerateParams(decoding_method="greedy", max_new_tokens=1000)

#Simple chaining: Prompt + LLM 
# First Chain
langchain_model = LangChainInterface(model="google/flan-ul2", params=params, credentials=creds)
template = PromptPattern.from_str("What is the good name of a IT software company that provides: {{services}}")
#template = PromptPattern.from_file("C://Users//00028Z744//Desktop//desktop-bkp//Generative-AI-watsonX//prompt-templates//template1.yaml")
first_prompt = template.langchain.as_template()
first_chain = LLMChain(llm=langchain_model, prompt=first_prompt) #model + prompt template

#print(langchain_model(template.format(question="What are the services provided by IBM?")))
#Second Chain
second_template = PromptPattern.from_str("Who is the founder of the company: {{company_name}}")
second_prompt = second_template.langchain.as_template()
second_chain = LLMChain(llm=langchain_model, prompt=second_prompt)

#Third Chain
third_template = PromptPattern.from_str("More detail about : {{founder_name}}")
third_prompt = third_template.langchain.as_template()
third_chain = LLMChain(llm=langchain_model, prompt=third_prompt) 

overall_chain = SimpleSequentialChain(chains=[first_chain,second_chain,third_chain], verbose=True)

#companydetail = overall_chain.run("cloud services")
companydetail = overall_chain.run("blockchain")
print(companydetail)

