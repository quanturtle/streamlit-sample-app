import streamlit as st
from apps.utils import get_code_snippets

def app():
    st.title('Nginx')
    st.write('A list of common nginx commands')

    get_code_snippets('nginx_data')
