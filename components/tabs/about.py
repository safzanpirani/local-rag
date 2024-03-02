import streamlit as st

from datetime import datetime


def about():
    st.title("Local RAG Implementation")
    st.caption(f"Developed as a Major Project at St. Peter's Engineering College &copy; {datetime.now().year}")
    st.write("")

    links_html = """
    <ul style="list-style-type:none; padding-left:0;">
        <li>
            <a href="https://github.com/safzanpirani/local-rag" style="color: grey;">GitHub</a>
        </li>
    </ul>
    """

    resources_html = """
    <ul style="list-style-type:none; padding-left:0;">
        <li>
            <a href="https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/" style="color: grey;">
                What is RAG?
            </a>
        </li>
        <li>
            <a href="https://aws.amazon.com/what-is/embeddings-in-machine-learning/" style="color: grey;">
                What are embeddings?
            </a>
        </li>
    </ul>
    """

    st.subheader("Links")
    st.markdown(links_html, unsafe_allow_html=True)

    st.subheader("Resources")
    st.markdown(resources_html, unsafe_allow_html=True)
