#Memory and Chat Bots
import os
os.environ['OPENAI_API_KEY'] = "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"

from langchain import OpenAI, ConversationChain

llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

#print(conversation.predict(input="Hi Are you there?"))
#print(conversation.predict(input="Can we talk about generative AI?"))
print("Welcome to your first AI chatbot! How can I help you today?")
for _ in range(0,3):
      human_input = input("You: ")
      ai_response = conversation.predict(input=human_input)
      print(f"AI: {ai_response}")