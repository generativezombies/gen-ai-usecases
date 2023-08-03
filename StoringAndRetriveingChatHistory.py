# Storing and retrieving chat history
import os
os.environ['OPENAI_API_KEY'] = "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"
 
from langchain import OpenAI, ConversationChain
from langchain.memory import ChatMessageHistory, ConversationBufferMemory
from langchain.schema import messages_from_dict, messages_to_dict

history = ChatMessageHistory()
history.add_user_message("Hello ! lets talk about generative ai")
history.add_ai_message("I'm ready to talk about generative ai")
dicts = messages_to_dict(history.messages)
#print(dicts)
new_messages = messages_from_dict(dicts)

llm = OpenAI(temperature=0)
history = ChatMessageHistory(messages=new_messages)
buffer = ConversationBufferMemory(chat_memory=history)
conversation = ConversationChain(llm=llm, memory=buffer, verbose=True)

print(conversation.predict(input="What are they?"))
print(conversation.memory)