import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT4_1():
    
    st.markdown("<h3 style='color: #4CAF50;'>🚀 Practice 12 </h3>", unsafe_allow_html=True)
    st.sidebar.multiselect("Select two tasks of the job at your firm:",("Intellectual","Physical","Social","Use of methods","Use of technology"))
    st.sidebar.write('Evaluate the job:')
    with st.sidebar.expander("$t_i$"):
        s1i = st.number_input("$s_{1i(k)}$ Demonstrating willigness to learn",key='s1i',step=1.0)
        s2i = st.number_input("$s_{2i(k)}$ Collaborating in teams and networks",key='s2i',step=1.0)
        s3i = st.number_input("$s_{3i(k)}$ Working efficiently",key='s3i',step=1.0)
        s4i = st.number_input("$s_{4i(k)}$ Taking a proactive approach",key='s4i',step=1.0)
    with st.sidebar.expander("$t_j$"):
        s1j = st.number_input("$s_{1j(k)}$ Demonstrating willigness to learn",key='s1j',step=1.0)
        s2j = st.number_input("$s_{2j(k)}$ Collaborating in teams and networks",key='s2j',step=1.0)
        s3j = st.number_input("$s_{3j(k)}$ Working efficiently",key='s3j',step=1.0)
        s4j = st.number_input("$s_{4j(k)}$ Taking a proactive approach",key='s4j',step=1.0)

    if st.button("Skill gap"):
        ti = np.array([
            [s1i],
            [s2i],
            [s3i],
            [s4i]
        ])
        tj = np.array([
            [s1j],
            [s2j],
            [s3j],
            [s4j]
        ])
        euclidean_distance = 0.45 * np.linalg.norm(ti - tj)
        st.write(euclidean_distance)


st.set_page_config(page_title="UNIT 4. Employee Performance Evaluation", layout="wide")

selected = option_menu(
    menu_title="",  # required
    options=['UNIT 4. EMPLOYEE PERFORMANCE EVALUATION'],  # required
    icons=["house", "calculator", "calculator", "book", "calculator",'people'],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "UNIT 4. EMPLOYEE PERFORMANCE EVALUATION":
    UNIT4_1()
