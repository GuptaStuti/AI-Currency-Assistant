import streamlit as st


def render_header():

    st.title("💱 AI Currency Assistant")

    st.caption("Powered by LangChain • LangGraph • HuggingFace")

    st.info("""
        ### Try asking:

        • Convert 5000 USD to INR

        • Convert 1000 EUR to AED

        • What is today's AED to INR rate?

        • What is AED?
        """)
