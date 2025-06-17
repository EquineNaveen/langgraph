from typing import TypedDict
from langgraph.graph import StateGraph,START,END

class AgentState(TypedDict):
    number1: int
    number2: int            
    operation1: str
    number3: int
    operation2: str
    number4: int
    result1: str
    result2: str

def add_node(state: AgentState) -> AgentState:
    state['result1'] =state['number1'] + state['number2']
    return state
def subtract_node(state: AgentState) -> AgentState:
    state['result1'] = state['number1'] - state['number2']
    return state

def add_node2(state: AgentState) -> AgentState:
    state['result2'] =state['number3'] + state['number4']
    return state
def subtract_node2(state: AgentState) -> AgentState:
    state['result2'] = state['number3'] - state['number4']
    return state

def decide_next_node(state:AgentState) -> AgentState:
    """This node will select the next phase"""
    if state["operation1"] == "+":
        return "addition_operation"
    
    elif state["operation1"] == "-":
        return "subtraction_operation" 
    
def decide_next_node2(state:AgentState) -> AgentState:
    """This node will select the next phase"""
    if state["operation2"] == "+":
        return "addition_operation"

    elif state["operation2"] == "-":
        return "subtraction_operation"
    

graph = StateGraph(AgentState)

graph.add_node("add_node", add_node)
graph.add_node("subtract_node", subtract_node)
graph.add_node("router", lambda state:state) 

graph.add_node("add_node2", add_node2)
graph.add_node("subtract_node2", subtract_node2)
graph.add_node("router2", lambda state:state)


graph.add_edge(START, "router")

graph.add_conditional_edges(
    "router", 
    decide_next_node,
    {
        # Edge: Node format
        "addition_operation": "add_node",
        "subtraction_operation": "subtract_node"
    }
)

graph.add_edge("add_node", "router2")
graph.add_edge("subtract_node", "router2")


graph.add_conditional_edges(
    "router2", 
    decide_next_node2,
    {
        # Edge: Node format
        "addition_operation": "add_node2",
        "subtraction_operation": "subtract_node2"
    }
)


graph.add_edge("add_node2", END)
graph.add_edge("subtract_node2", END)

app = graph.compile()

with open("graph.png", "wb") as f:
    f.write(app.get_graph().draw_mermaid_png())

    
result = app.invoke({
    "number1": 10,
    "number2": 5,
    "operation1": "+",
    "number3": 20,
    "operation2": "-",
    "number4": 10
})
print(result)