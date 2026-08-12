import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.header("💱 Currency Assistant")

        st.divider()

        st.subheader("Features")

        st.write("✅ Currency Conversion")

        st.write("✅ Live Exchange Rates")

        st.write("✅ Currency Information")

        st.divider()

        clear = st.button("🗑 Clear Chat")

        return clear
