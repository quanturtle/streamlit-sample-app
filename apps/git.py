import streamlit as st
from apps.utils import get_code_snippets

def app():
    st.title('Git')
    st.write('A list of common git commands')

    get_code_snippets('git_data')