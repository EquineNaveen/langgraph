from typing import Dict,TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    """
    Represents the state of the agent.
    """
    name: str
    description: str
    result: str
    
def compliment_agent(state: AgentState) -> AgentState:
    """ Generates a personalized compliment for the agent based on its state."""
    state['result'] = state['name']+" "+state['description']
    return state

graph=StateGraph(AgentState)    
graph.add_node("compliment", compliment_agent)
graph.set_entry_point("compliment")
graph.set_finish_point("compliment")

app = graph.compile()

result = app.invoke({"name": "Bob", "description": "a great job!"})
print(result["result"])