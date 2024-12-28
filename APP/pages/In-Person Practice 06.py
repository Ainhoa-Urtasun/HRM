import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm

def practice_06():

    st.sidebar.radio("Select a job at your firm:",("other managers", "support intellectuals and scientists, technicians and professionals", "sales representatives and similar"))
    st.sidebar.write('Evaluate the job:')
    with st.sidebar.expander("intellectual"):
        s11 = st.number_input("demonstrating willigness to learn",key='s11',min_value=0,max_value=100,step=1)
        s12 = st.number_input("collaborating in teams and networks",min_value=0,max_value=100,step=1)
        s13 = st.number_input("working efficiently",key='s31',min_value=0,max_value=100,step=1)
        s14 = st.number_input("taking a proactive approach",key='s41',min_value=0,max_value=100,step=1)
    with st.sidebar.expander("physical"):
        s21 = st.number_input("demonstrating willigness to learn",key='s12',min_value=0,max_value=100,step=1)
        s22 = st.number_input("collaborating in teams and networks",key='s22',min_value=0,max_value=100,step=1)
        s23 = st.number_input("working efficiently",key='s32',min_value=0,max_value=100,step=1)
        s24 = st.number_input("taking a proactive approach",key='s42',min_value=0,max_value=100,step=1)
    with st.sidebar.expander("social"):
        s31 = st.number_input("demonstrating willigness to learn",key='s13',min_value=0,max_value=100,step=1)
        s32 = st.number_input("collaborating in teams and networks",key='s23',min_value=0,max_value=100,step=1)
        s33 = st.number_input("working efficiently",key='s33',min_value=0,max_value=100,step=1)
        s34 = st.number_input("taking a proactive approach",key='s43',min_value=0,max_value=100,step=1)
    with st.sidebar.expander("use of methods"):
        s41 = st.number_input("demonstrating willigness to learn",key='s14',min_value=0,max_value=100,step=1)
        s42 = st.number_input("collaborating in teams and networks",key='s24',min_value=0,max_value=100,step=1)
        s43 = st.number_input("working efficiently",key='s34',min_value=0,max_value=100,step=1)
        s44 = st.number_input("Ttaking a proactive approach",key='s44',min_value=0,max_value=100,step=1)
    with st.sidebar.expander("use of technology"):
        s51 = st.number_input("demonstrating willigness to learn",key='s15',min_value=0,max_value=100,step=1)
        s52 = st.number_input("collaborating in teams and networks",key='s25',min_value=0,max_value=100,step=1)
        s53 = st.number_input("working efficiently",key='s35',min_value=0,max_value=100,step=1)
        s54 = st.number_input("taking a proactive approach",key='s45',min_value=0,max_value=100,step=1)

    matrix = np.array([
            [s11, s12, s13, s14],
            [s21, s22, s23, s24],
            [s31, s32, s33, s34],
            [s41, s42, s43, s44],
            [s51, s52, s53, s54],
        ])
    
    if st.button("Matrix of tasks and skills of the job"):
        st.write(matrix)

    if st.button("Euclidean norms of the column vectors scaled down so each skill ranges from 0 to 100"):
        norms = (5**(-0.5)) * np.linalg.norm(matrix, axis=0)
        st.write(norms)


# Set page configuration
st.set_page_config(page_title="In-Person Practice 6", layout="wide")

selected = option_menu(
    menu_title="",  # required
    options=["In-Person Practice 06"],  # required
    icons=["book", "calculator", "calculator","person"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "In-Person Practice 06":
    practice_06()



