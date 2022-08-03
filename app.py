import streamlit as st
from multiapp import MultiApp
from apps import home, linux, git, postgres, nginx # import your app modules here
import os

app = MultiApp()

st.title('Personal website & Cheatsheet')

# Apps
app.add_app("Home", home.app)
app.add_app("Linux", linux.app)
app.add_app("Git", git.app)
app.add_app("Postgres", postgres.app)
app.add_app("Nginx", nginx.app)

# Run main app
app.run()
