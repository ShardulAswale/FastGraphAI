from langgraph.graph import StateGraph, END
from typing import TypedDict, Literal

# State type
class State(TypedDict):
    input: str
    output: str
    type: Literal["weather", "time", "unknown"]

# Node 1: Classifier
def classify_node(state: State) -> State:
    input_text = state["input"].lower()
    if "weather" in input_text:
        state["type"] = "weather"
    elif "time" in input_text:
        state["type"] = "time"
    else:
        state["type"] = "unknown"
    return state

# Node 2: Weather
def weather_node(state: State) -> State:
    state["output"] = "It's 24°C and sunny ☀️"
    return state

# Node 3: Time
def time_node(state: State) -> State:
    state["output"] = "It's 2:00 PM 🕑"
    return state

# Fallback Node
def fallback_node(state: State) -> State:
    state["output"] = f"You said: {state['input']}"
    return state

# Define graph
builder = StateGraph(State)
builder.add_node("classify", classify_node)
builder.add_node("weather", weather_node)
builder.add_node("time", time_node)
builder.add_node("fallback", fallback_node)

# Routes
builder.set_entry_point("classify")
builder.add_conditional_edges(
    "classify",
    lambda state: state["type"],
    {
        "weather": "weather",
        "time": "time",
        "unknown": "fallback"
    }
)

builder.add_edge("weather", END)
builder.add_edge("time", END)
builder.add_edge("fallback", END)

graph = builder.compile()

# Run the graph
def run_graph(user_input: str) -> str:
    result = graph.invoke({"input": user_input})
    return result["output"]
