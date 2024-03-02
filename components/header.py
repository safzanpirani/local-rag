import streamlit as st


def set_page_header():
    st.header("Intelligent Conversations with Documents", anchor=False)
    st.caption(
        "Upload files for retrieval augmented generation (RAG) with open-source Large Language Models (LLMs)."
    )
