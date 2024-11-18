import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT4_1():
    
    st.markdown("<h3 style='color: #4CAF50;'>🚀 Practice 12 </h3>", unsafe_allow_html=True)

st.sidebar.radio("Select a job at your firm:",("other managers", "support intellectuals and scientists, technicians and professionals", "sales representatives and similar"))
st.sidebar.write('Evaluate the job:')
    with st.sidebar.expander("Intellectual"):
        s11 = st.number_input("demonstrating willigness to learn",key='s11',min_value=0,max_value=100,step=1)
        s21 = st.number_input("collaborating in teams and networks",key='s21',min_value=0,max_value=100,step=1)
        s31 = st.number_input("working efficiently",key='s31',min_value=0,max_value=100,step=1)
        s41 = st.number_input("taking a proactive approach",key='s41',min_value=0,max_value=100,step=1)
    with st.sidebar.expander("Physical"):
        s12 = st.number_input("demonstrating willigness to learn",key='s12',min_value=0,max_value=100,step=1)
        s22 = st.number_input("collaborating in teams and networks",key='s22',min_value=0,max_value=100,step=1)
        s32 = st.number_input("working efficiently",key='s32',min_value=0,max_value=100,step=1)
        s42 = st.number_input("taking a proactive approach",key='s42',min_value=0,max_value=100,step=1)
    with st.sidebar.expander("Social"):
        s13 = st.number_input("demonstrating willigness to learn",key='s13',min_value=0,max_value=100,step=1)
        s23 = st.number_input("collaborating in teams and networks",key='s23',min_value=0,max_value=100,step=1)
        s33 = st.number_input("working efficiently",key='s33',min_value=0,max_value=100,step=1)
        s43 = st.number_input("taking a proactive approach",key='s43',min_value=0,max_value=100,step=1)
    with st.sidebar.expander("Use of methods"):
        s14 = st.number_input("demonstrating willigness to learn",key='s14',min_value=0,max_value=100,step=1)
        s24 = st.number_input("collaborating in teams and networks",key='s24',min_value=0,max_value=100,step=1)
        s34 = st.number_input("working efficiently",key='s34',min_value=0,max_value=100,step=1)
        s44 = st.number_input("Ttaking a proactive approach",key='s44',min_value=0,max_value=100,step=1)
    with st.sidebar.expander("Use of technology"):
        s15 = st.number_input("demonstrating willigness to learn",key='s15',min_value=0,max_value=100,step=1)
        s25 = st.number_input("collaborating in teams and networks",key='s25',min_value=0,max_value=100,step=1)
        s35 = st.number_input("working efficiently",key='s35',min_value=0,max_value=100,step=1)
        s45 = st.number_input("taking a proactive approach",key='s45',min_value=0,max_value=100,step=1)

    st.sidebar.write('Skill profile'):
        s1 = st.number_input("demonstrating willigness to learn",key='s1',min_value=0,max_value=100,step=1)
        s2 = st.number_input("collaborating in teams and networks",key='s2',min_value=0,max_value=100,step=1)
        s3 = st.number_input("working efficiently",key='s3',min_value=0,max_value=100,step=1)
        s4 = st.number_input("taking a proactive approach",key='s4',min_value=0,max_value=100,step=1)

    matrix = np.array([
            [s11, s12, s13, s14, s15],
            [s21, s22, s23, s24, s25],
            [s31, s32, s33, s34, s35],
            [s41, s42, s43, s44, s45]
        ])
    
    if st.button("Job evaluation"):
        st.write(matrix)

    if st.button("Job skill requirements"):
        row_norms = 0.45 * np.linalg.norm(matrix, axis=1)
        for norm in row_norms:
            st.write(norm)

    if st.button("Skill gap"):
        gap = np.sqrt(np.sum((row_norms - np.array([s1,s2,s3,s4])) ** 2))
        st.write(gap)
    
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
