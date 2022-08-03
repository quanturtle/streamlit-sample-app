import streamlit as st
from apps.utils import get_code_snippets

def app():
    st.title('Postgres')
    st.write('A list of common PostgreSQL commands')

    get_code_snippets('postgres_data')
