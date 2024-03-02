import streamlit as st

from components.tabs.local_files import local_files
from components.tabs.github_repo import github_repo
from components.tabs.website import website


def file_upload():
    st.title("Import your documents.")
    st.caption("Upload your documents to intelligently talk to them.")
    st.write("")

    with st.expander("💻 &nbsp; **Local Files**", expanded=False):
        local_files()

  #  with st.expander("🗂️ &nbsp;**GitHub Repo**", expanded=False):
  #      github_repo()

  #  with st.expander("🌐 &nbsp; **Website**", expanded=False):
  #      website()
