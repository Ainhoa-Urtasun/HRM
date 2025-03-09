import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

def HR_planning():

    st.sidebar.write('Number of workers at end of 2022 and the end of 2023 (just numbers, no commas or dots):')
    with st.sidebar.expander("Other managers"):
        L12022 = st.number_input("$L_{1,2022}$", key='L12022', step=1, min_value=0)
        L12023 = st.number_input("$L_{1,2023}$", key='L12023', step=1, min_value=0)
    with st.sidebar.expander("Support intellectuals and scientists, technicians and professionals"):
        L22022 = st.number_input("$L_{2,2022}$", key='L22022', step=1, min_value=0)
        L22023 = st.number_input("$L_{2,2023}$", key='L22023', step=1, min_value=0)
    with st.sidebar.expander("Administrative employees"):
        L32022 = st.number_input("$L_{3,2022}$", key='L32022', step=1, min_value=0)
        L32023 = st.number_input("$L_{3,2023}$", key='L32023', step=1, min_value=0)

    m12 = m13 = m31 = m32 = 0
    m21 = 1
    m23 = 2    
    m11 = np.min([L12022,L12023]) - 1
    m22 = np.min([L22022,L22023]) - 6  
    m33 = np.min([L32022,L32023]) - 2
    if L12022 < L12023: 
        t1 = 1
        h1 = L12023 - m11 - 1
    else:
        h1 = 0
        t1 = L12022 - m11
    if L22022 < L22023: 
        t2 = 3
        h2 = L22023 - m22
    else:
        h2 = 0
        t2 = L22022 - m22
    if L32022 < L32023: 
        t3 = 2
        h3 = L32023 - m33 - 2
    else:
        h3 = 0
        t3 = L32022 - m33
        
    matrix = np.array([
        [m11, m12, m13, t1],
        [m21, m22, m23, t2],
        [m31, m32, m33, t3],
        [h1,  h2,  h3,  np.nan]  # np.nan for the bottom-right cell
        ])
        
    if st.button("HR planning table"):
        st.write(matrix)
   
    if st.button("Predictions for May 2025"):
        T = np.array([
            [m11/(m11+m12+m13+t1), m12/(m11+m12+m13+t1), m13/(m11+m12+m13+t1)],
            [m21/(m21+m22+m23+t2), m22/(m21+m22+m23+t2), m23/(m21+m22+m23+t2)],
            [m31/(m31+m32+m33+t3), m32/(m31+m32+m33+t3), m33/(m31+m32+m33+t3)],
        ])

        L = np.array([
            [m11+m21+m31+h1],
            [m12+m22+m32+h2],
            [m13+m23+m33+h3],
        ])
    
        predictions = T.T @ L
        for prediction in predictions:
            st.write(prediction[0])

    st.write("""
    **Consider that your firm**:
    1. Produces according to $Q=L_1^{0.1}L_2^{0.72}L_3^{0.05}K^{0.11}$
    2. Sold 1,000 units of its product in 2023 
    2. Pays Administrative employees the yearly gross income for Professionals in the EU in 2023 from Skills Intelligence
    3. Uses 1 unit of capital
    """)
    st.text_area("", placeholder="Estimate the precise shortage or surplus of Support intellectuals and scientists, technicians and professionals for May 2025")
    st.text_area("", placeholder="Recommend the strategy the firm should follow to prevent labor mismatch. In the case of a shortage, provide an estimate of the vacancy yield")

st.set_page_config(page_title="HR planning", layout="wide")

selected = option_menu(
    menu_title="",  # required
    options=['HR planning'],  # required
    icons=["calculator", "calculator", "person"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "HR planning":
    HR_planning()

