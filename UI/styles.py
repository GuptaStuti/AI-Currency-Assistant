import streamlit as st


def load_css():

    st.markdown(
        """

<style>

.block-container{

padding-top:2rem;

}

.stChatMessage{

border-radius:15px;

padding:15px;

margin-bottom:10px;

}

</style>

""",
        unsafe_allow_html=True,
    )
