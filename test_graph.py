from langchain_core.messages import HumanMessage
from agent import graph

response = graph.invoke({"messages": [HumanMessage("Convert 1000 AED to INR")]})

print(response["messages"][-1].content)
