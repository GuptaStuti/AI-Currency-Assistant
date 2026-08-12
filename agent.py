from tools.currency_converter import currency_converter
from tools.currency_info import currency_information
from tools.exchange_rate import get_exchange_rate

from langchain_core.messages import SystemMessage

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

from typing_extensions import TypedDict
from typing import Annotated

from prompts import SYSTEM_PROMPT

from llm import chat_model

# ----------------------------------------------
# tool binding
# ----------------------------------------------

model = chat_model.bind_tools(
    [currency_converter, currency_information, get_exchange_rate]
)

# ----------------------------------------------
# The Graph State
# ----------------------------------------------


class CurrencyState(TypedDict):

    messages: Annotated[list, add_messages]


# ---------------------------------------------
# Assistant Node
# ---------------------------------------------


def assistant(state: CurrencyState):

    messages = [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"]

    response = model.invoke(messages)

    return {"messages": [response]}


# ----------------------------------------------
# Create the tool node
# ----------------------------------------------

tool_node = ToolNode([currency_converter, currency_information, get_exchange_rate])

# -------------------------
# Build Graph
# -------------------------

builder = StateGraph(CurrencyState)

builder.add_node("assistant", assistant)

builder.add_node("tools", tool_node)

builder.add_edge(START, "assistant")

builder.add_conditional_edges("assistant", tools_condition)

builder.add_edge("tools", "assistant")

memory = MemorySaver()

graph = builder.compile(checkpointer=memory)
