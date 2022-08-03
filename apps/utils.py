import os
import streamlit as st

def get_code_snippets(dir_to_search):
    base_path = os.path.dirname(os.path.realpath(__file__))
    code_snippets_path = os.path.join(base_path, dir_to_search)

    for folder in os.listdir(code_snippets_path):
        st.subheader(folder)
        file_path = os.path.join(code_snippets_path, folder)
        
        for file_name in os.listdir(file_path):
            snippet_title = ' '.join(file_name.replace('.md','').split('_'))

            file_to_open = os.path.join(file_path, file_name)
            
            with open(file_to_open, 'r') as file:
                file_contents = file.read()
            
            st.expander(snippet_title).markdown(file_contents)