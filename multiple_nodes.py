from typing import TypedDict,List
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name: str
    age: int
    skills: List[str]
    result:str

def first_node(state: AgentState) -> AgentState:
    state['result'] =f"{state['name']} ,welcome to the system"
    return state

def second_node(state: AgentState) -> AgentState:
    state['result'] = f"{state['result']}, you are {state['age']} years old!"
    return state

def third_node(state:AgentState) -> AgentState:
    """This node will list the user's skills in a formatted string"""
    state["result"] = state["result"] + f" You have skills in: {', '.join(state['skills'])}"

    return state

graph=StateGraph(AgentState)
graph.add_node("first_node", first_node)
graph.add_node("second_node", second_node)
graph.add_node("third_node", third_node)

graph.set_entry_point("first_node")
graph.add_edge("first_node", "second_node")
graph.add_edge("second_node", "third_node") 
graph.set_finish_point("third_node")

app=graph.compile()

result = app.invoke({"name": "Linda", "age": 31, "skills":["Python", "Machine Learning", "LangGraph"]})

print(result['result']) 


# Export the graph as a PNG image
with open("graph.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())