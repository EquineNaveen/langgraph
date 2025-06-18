from typing import TypedDict, List, Annotated,Sequence
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage,SystemMessage,BaseMessage
from langchain_core.tools import tool
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.graph.message import add_messages

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  # Changed to another chat-compatible model
    task="text-generation",         
    )


class AgentState(TypedDict):
     messages: Annotated[Sequence[BaseMessage], add_messages]

@tool
def add(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b

@tool
def subtract(a: int, b: int):
    """Subtraction function"""
    return a - b

@tool
def multiply(a: int, b: int):
    """Multiplication function"""
    return a * b

tools = [add, subtract, multiply]

model = ChatHuggingFace(llm=llm).bind_tools(tools)

def model_call(state:AgentState) -> AgentState:
    system_prompt = SystemMessage(content=
        "You are my AI assistant, please answer my query to the best of your ability."
    )
    response = model.invoke([system_prompt] + state["messages"])
    return {"messages": [response]}

def should_continue(state: AgentState): 
    messages = state["messages"]
    last_message = messages[-1]
    print(f"Last message: {last_message}")
    if not last_message.tool_calls:
        print(last_message.tool_calls) 
        return "end"
    else:
        print(last_message.tool_calls)
        return "continue"
    
graph = StateGraph(AgentState)
graph.add_node("our_agent", model_call)


tool_node = ToolNode(tools=tools)
graph.add_node("tools", tool_node)

graph.set_entry_point("our_agent")

graph.add_conditional_edges(
    "our_agent",
    should_continue,
    {
        "continue": "tools",
        "end": END,
    },
)

graph.add_edge("tools", "our_agent")

app = graph.compile()

with open("graph.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())

def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

inputs = {"messages": [("user", "add 3 and 4 and subtract the result with 1, Also tell me a joke please.")]}
print_stream(app.stream(inputs, stream_mode="values"))