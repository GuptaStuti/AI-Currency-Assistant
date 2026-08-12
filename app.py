import streamlit as st
from langchain_core.messages import HumanMessage
from agent import graph
from UI.header import render_header
from UI.sidebar import render_sidebar
from UI.chat import display_chat
from UI.footer import render_footer
from UI.styles import load_css
import uuid

st.set_page_config(page_title="AI Currency Assistant", page_icon="💱", layout="wide")

load_css()

render_header()

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

if "messages" not in st.session_state:

    st.session_state.messages = []

clear_chat = render_sidebar()

if clear_chat:

    st.session_state.messages = []
    st.session_state.thread_id = str(uuid.uuid4())
    st.rerun()

display_chat(st.session_state.messages)

prompt = st.chat_input("Ask me anything about currencies...")

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = graph.invoke(
                {"messages": [HumanMessage(content=prompt)]},
                config={"configurable": {"thread_id": st.session_state.thread_id}},
            )

            answer = response["messages"][-1].content

            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

render_footer()
