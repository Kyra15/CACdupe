import streamlit as st

def wide_space_default():
    st.set_page_config(layout="wide")  

wide_space_default()

pg = st.navigation([st.Page("home.py", title="Home"), st.Page("lesson.py", title="Unit 1"), st.Page("editor.py", title="Free Code")])
pg.run()
