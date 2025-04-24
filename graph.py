from langgraph.graph import StateGraph, END
from chain import llm
from pydantic import BaseModel

class MyState(BaseModel):
    input: str
    output: str = ""

def llm_node(state):
    if isinstance(state, dict):
        msg = state["input"]
    else:
        msg = state.input
    reply = llm.invoke(msg)
    if isinstance(state, dict):
        state["output"] = reply.content
    else:
        state.output = reply.content
    return state

def run_langgraph(message: str) -> str:
    workflow = StateGraph(state_schema=MyState)
    workflow.add_node("llm", llm_node)
    workflow.set_entry_point("llm")
    workflow.add_edge("llm", END)
    graph = workflow.compile()
    final_state = graph.invoke({"input": message})
    return final_state["output"]
