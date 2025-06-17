from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage
from typing import TypedDict, List
import os

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  # Changed to another chat-compatible model
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)


class AgentState(TypedDict):
    messages: HumanMessage

def model_response(state: AgentState) -> AgentState:
    """Generate a response from the model based on the current state"""
    response = model.invoke([state["messages"]])  # Wrap in a list
    print(f"Model response: {response.content}")
    return state
graph=StateGraph(AgentState) 
graph.add_node("model_response", model_response)
graph.add_edge(START, "model_response")
graph.add_edge("model_response", END)
app=graph.compile()

with open("graph.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())


user_input = input("Enter your message: ")
while user_input.lower() != "exit":
    app.invoke({"messages": HumanMessage(content=user_input)})
    user_input = input("Enter your message: ")

