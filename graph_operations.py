from typing import TypedDict,List
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    """
    Represents the state of the agent.
    """
    name: str
    values:List[int]
    operation: str
    result: str

def graph_operations(state:AgentState) -> AgentState:
    """ Performs operations on the agent's values based on the specified operation."""
    if state['operation'] == '+':
        state['result'] = f"hi {state['name']}, your answer is {sum(state['values'])}"
    elif state['operation'] == '*':
        product = 1
        for value in state['values']:
            product *= value
        state['result'] = f"Hi {state['name']}, your answer is {product}"
    return state

graph=StateGraph(AgentState)
graph.add_node("graph_operations", graph_operations)
graph.set_entry_point("graph_operations")
graph.set_finish_point("graph_operations")
app = graph.compile()

result = app.invoke({"operation":"+", "name": "Alice", "values": [1, 2, 3, 4]})
print(result["result"])
