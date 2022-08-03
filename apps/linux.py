import streamlit as st
from apps.utils import get_code_snippets

def app():
    st.title('Linux')
    st.write('A list of common linux commands')

    get_code_snippets('linux_data')