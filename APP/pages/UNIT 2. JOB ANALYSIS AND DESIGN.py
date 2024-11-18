import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm

def UNIT2_1():

    st.markdown("<h3 style='color: #4CAF50;'>🚀 Practice 6 </h3>", unsafe_allow_html=True)
    st.sidebar.radio("Select a job at your firm:",("Senior management", "Support intellectuals and scientists, technicians and professionals", "Sales representatives and similar"))
    st.sidebar.write('Evaluate the job:')
    with st.sidebar.expander("Intellectual"):
        s11 = st.number_input("Demonstrating willigness to learn",key='s11',min_value=0,max_value=100,step=1)
        s21 = st.number_input("Collaborating in teams and networks",min_value=0,max_value=100,step=1)
        s31 = st.number_input("Working efficiently",key='s31',min_value=0,max_value=100,step=1)
        s41 = st.number_input("Taking a proactive approach",key='s41',min_value=0,max_value=100,step=1)
    with st.sidebar.expander("Physical"):
        s12 = st.number_input("Demonstrating willigness to learn",key='s12',min_value=0,max_value=100,step=1)
        s22 = st.number_input("Collaborating in teams and networks",key='s22',min_value=0,max_value=100,step=1)
        s32 = st.number_input("Working efficiently",key='s32',min_value=0,max_value=100,step=1)
        s42 = st.number_input("Taking a proactive approach",key='s42',min_value=0,max_value=100,step=1)
    with st.sidebar.expander("Social"):
        s13 = st.number_input("Demonstrating willigness to learn",key='s13',min_value=0,max_value=100,step=1)
        s23 = st.number_input("Collaborating in teams and networks",key='s23',min_value=0,max_value=100,step=1)
        s33 = st.number_input("Working efficiently",key='s33',min_value=0,max_value=100,step=1)
        s43 = st.number_input("Taking a proactive approach",key='s43',min_value=0,max_value=100,step=1)
    with st.sidebar.expander("Use of methods"):
        s14 = st.number_input("Demonstrating willigness to learn",key='s14',min_value=0,max_value=100,step=1)
        s24 = st.number_input("Collaborating in teams and networks",key='s24',min_value=0,max_value=100,step=1)
        s34 = st.number_input("Working efficiently",key='s34',min_value=0,max_value=100,step=1)
        s44 = st.number_input("Taking a proactive approach",key='s44',min_value=0,max_value=100,step=1)
    with st.sidebar.expander("Use of technology"):
        s15 = st.number_input("Demonstrating willigness to learn",key='s15',min_value=0,max_value=100,step=1)
        s25 = st.number_input("Collaborating in teams and networks",key='s25',min_value=0,max_value=100,step=1)
        s35 = st.number_input("Working efficiently",key='s35',min_value=0,max_value=100,step=1)
        s45 = st.number_input("Taking a proactive approach",key='s45',min_value=0,max_value=100,step=1)

    matrix = np.array([
            [s11, s12, s13, s14, s15],
            [s21, s22, s23, s24, s25],
            [s31, s32, s33, s34, s35],
            [s41, s42, s43, s44, s45]
        ])
    
    if st.button("$J_k$ Job evaluation"):
        st.write(matrix)

    if st.button("$s_k$ Job skill requirements"):
        row_norms = 0.45 * np.linalg.norm(matrix, axis=1)
        for norm in row_norms:
            st.write(norm)

# Set page configuration
st.set_page_config(page_title="UNIT 2. JOB ANALYSIS AND DESIGN", layout="wide")

selected = option_menu(
    menu_title="",  # required
    options=["UNIT 2 JOB ANALYSIS AND DESIGN"],  # required
    icons=["book", "calculator", "calculator","person"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "UNIT 2 JOB ANALYSIS AND DESIGN":
    UNIT2_1()



