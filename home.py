import streamlit as st
from streamlit_extras.great_tables import great_tables

st.html("<style>[data-testid='stHeaderActionElements'] {display: none;}</style>")

st.markdown("""
<style>
div.stButton > button[kind="secondary"] {
    border: none !important;
    border-radius: 0 !important;
    justify-content: flex-start !important;
    margin-top: 0 !important;
    margin-bottom: 0 !important;
    padding-top: 0 !important;
    padding-bottom: 0 !important;
}

[data-testid="stExpander"] details summary {
    background-color: #accff2!important;
}
            
[data-testid="stExpander"] details summary p {
    font-size: 1.75rem !important;
    font-weight: bold !important;
}
</style>
""", unsafe_allow_html=True)




with st.expander(label="Unit 1 - Intro to Python", expanded=True):
    with st.container(border=True):
        # st.subheader("Intro to Python")
        st.write("abstract")
    
    u1l1 = st.button("Lesson 1: Variables and Data Types", width="stretch")
    u1l2 = st.button("Lesson 2: Operations and Conditionals", width="stretch")
    u1l3 = st.button("Lesson 3: Collections", width="stretch")
    u1l4 = st.button("Lesson 4: Loops", width="stretch")
    u1l5 = st.button("Lesson 5: Functions", width="stretch")
    p1 = st.button("Project: Storefront", width="stretch")

button_pages = {
    u1l1: "u1l1",
    u1l2: "u1l2", 
    u1l3: "u1l3",
    u1l4: "u1l4",
    u1l5: "u1l5",
    p1: "p1"
}

for button, page_key in button_pages.items():
    if button:
        st.switch_page("u1l1.py")
        break

with st.expander(label="Unit 2 - Object-Oriented Programming", expanded=True):
    with st.container(border=True):
        st.subheader("Object-Oriented Programming")
        st.write("abstract")

with st.expander(label="Unit 3 - Intro to Machine Learning", expanded=True):
    with st.container(border=True):
        st.subheader("Intro to Machine Learning")
        st.write("abstract")

with st.expander(label="Unit 4 - Linear Regression", expanded=True):
    with st.container(border=True):
        st.subheader("Linear Regression")
        st.write("abstract")

with st.expander(label="Unit 5 - Convolutional Neural Networks", expanded=True):
    with st.container(border=True):
        st.subheader("OConvolutional Neural Networks")
        st.write("abstract")

with st.expander(label="Unit 6 - Reinforcement Learning", expanded=True):
    with st.container(border=True):
        st.subheader("Reinforcement Learning")
        st.write("abstract")