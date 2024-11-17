import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

def UNIT3_1():

    st.markdown("<h3 style='color: #4CAF50;'>🚀 Practice 12 </h3>", unsafe_allow_html=True)
    st.sidebar.write('Input historical data from the end of 2022 and the end of 2023:')
    with st.sidebar.expander("$J_1$ Other managers"):
        L12022 = st.number_input("$L_{1,2022}$", key='L12022', step=1, min_value=0)
        L12023 = st.number_input("$L_{1,2023}$", key='L12023', step=1, min_value=0)
    with st.sidebar.expander("$J_2$ Support intellectuals and scientists, technicians and professionals"):
        L22022 = st.number_input("$L_{2,2022}$", key='L22022', step=1, min_value=0)
        L22023 = st.number_input("$L_{2,2023}$", key='L22023', step=1, min_value=0)
    with st.sidebar.expander("$J_3$ Administrative employees"):
        L32022 = st.number_input("$L_{3,2022}$", key='L32022', step=1, min_value=0)
        L32023 = st.number_input("$L_{3,2023}$", key='L32023', step=1, min_value=0)

    m11 = np.minimum(L12022,L12023) - 1
    m22 = np.minimum(L22022,L22023) - 4
    m33 = np.minimum(L32022,L32023) - 3

    h1 = L12023 - m11
    m21 = m31 = 0
    m23 = 1
    d2 = L22022 - m21 - m22 - m23
    m32 = 2
    d3 = 1
    d1 = m13 = 0
    m12 = L12022 - m11
    h2 = L22023 - m12 - m22 - m32
    h3 = L32023 - m13 - m23 - m33

    matrix = np.array([
        [m11, m12, m13, d1],
        [m21, m22, m23, d2],
        [m31, m32, m33, d3],
        [h1,  h2,  h3,  np.nan]  # np.nan for the bottom-right cell
        ])
        
    if st.button("HR planning table"):
        st.write(matrix)
   
    if st.button("HR planning for the end of 2024"):
        T = np.array([
            [m11/(m11+m12+m13+d1), m12/(m11+m12+m13+d1), m13/(m11+m12+m13+d1)],
            [m21/(m21+m22+m23+d2), m22/(m21+m22+m23+d2), m23/(m21+m22+m23+d2)],
            [m31/(m31+m32+m33+d3), m32/(m31+m32+m33+d3), m33/(m31+m32+m33+d3)],
        ])

        L = np.array([
            [m11+m21+m31+h1],
            [m12+m22+m32+h2],
            [m13+m23+m33+h3],
        ])
    
        predictions = T.T @ L
        for prediction in predictions:
            st.write(prediction[0])

st.set_page_config(page_title="UNIT 3 HR PLANNING", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["HR planning table",'Forecasting the availability of employees using the transition matrix','HR PLANNING'],  # required
    icons=["calculator", "calculator", "person"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "HR PLANNING":
    UNIT3_1()

