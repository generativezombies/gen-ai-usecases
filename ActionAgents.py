# Action Agents 

import pprint
import os
os.environ['OPENAI_API_KEY'] = "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"
#from langchain.agents import get_all_tool_names
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent
prompt = "When was the first indian prime minister born?"

#pp=pprint.PrettyPrinter(indent=4)
#pp.pprint(get_all_tool_names())
llm = OpenAI(temperature=0)
tools = load_tools(['wikipedia'], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
agent.run(prompt)