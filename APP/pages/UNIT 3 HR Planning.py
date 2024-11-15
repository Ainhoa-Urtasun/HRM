import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

def UNIT3_1():

    st.latex(
        r"""
        \begin{array}{|c|c|c|c|}
        \hline
        m_{11} & m_{12} & m_{13} & d_{1} \\
        \hline
        m_{21} & m_{22} & m_{23} & d_{3} \\
        \hline
        m_{31} & m_{32} & m_{33} & d_{3} \\
        \hline
        h_{1} & h_{2} & h_{3} & \\
        \hline
        \end{array}
        """
    )

    st.write(
        '''
        - $m_{ij}$ represents employees who moved from job $J_i$ to job $J_j$ during 2022
        - $d_k$ represents the departures or separations of employees who were in job $J_k$ at the end of 2022 and 
        left the firm during 2023, either voluntarily (e.g., quitting or retiring) or involuntarily (e.g., layoffs or dismissals)
        - $h_{k}$ represents new hires or number of employees who have been recruited and started working in job $J_k$ 
        during 2023
  

        The table above should meet the following:
        - $L_{k,2022} = m_{k1} + m_{k2} + m_{k3} + d_{k}$ where row-summation gives the number of employees in job $J_k$ at the end of 2022
        - $L_{k,2023} = m_{1k} + m_{2k} + m_{3k} + h_{k}$ where column-summation gives the number of employees in job $J_k$ at the end of 2023
        
        Jobs, denoted as $J_k$, within the firm:
        - $J_1$ Other managers
        - $J_2$ Support intellectuals and scientists, technicians and professionals
        - $J_3$ Administrative employees

        Using this data, retention in and turnover in job $J_k$, respectively:
        '''
    )

    st.latex(
        r'''
        R_k = 100 \times \frac{m_{k,k}}{L_{k,2022}} \\[10pt]
        T_k = 100 - R_k
        '''
    )

def UNIT3_2():
    st.write(
        '''
        HR planning makes predictions on the future availability of employees using the transition matrix $T$.
        The notation below illustrates
        the structure of the transition matrix $T$ and the calculations required to use historical data from 2022 and 
        2023 to predict the future (end of 2024) availability of employees in each job at the firm. To be able to use available data
        from SABI, this analysis should be conducted before the end of 2024:
        '''
    )

    st.latex(
        r'''
        T =
        \begin{pmatrix}
        \frac{m_{11}}{L_{1,2022}} & \frac{m_{12}}{L_{1,2022}} & \frac{m_{13}}{L_{1,2022}} \\ 
        \frac{m_{21}}{L_{2,2022}} & \frac{m_{22}}{L_{2,2022}} & \frac{m_{23}}{L_{2,2022}} \\ 
        \frac{m_{31}}{L_{(3,2022)}} & \frac{m_{32}}{L_{3,2022}} & \frac{m_{33}}{L_{3,2022}} \\  
        \end{pmatrix} \\[10pt]
        
        \begin{pmatrix}
        \hat{L}_{2024} \\
        \hat{L}_{2024} \\
        \hat{L}_{2024} \\
        \end{pmatrix} = 
        \begin{pmatrix}
        \frac{m_{11}}{L_{1,2022}} & \frac{m_{12}}{L_{1,2022}} & \frac{m_{13}}{L_{1,2022}} \\ 
        \frac{m_{21}}{L_{(2,2022)}} & \frac{m_{22}}{L_{2,2022}} & \frac{m_{23}}{L_{2,2022}} \\ 
        \frac{m_{31}}{L_{(3,2022)}} & \frac{m_{32}}{L_{3,2022}} & \frac{m_{33}}{L_{3,2022}} \\  
        \end{pmatrix}^T
        \begin{pmatrix} 
        L_{1,2023} \\ 
        L_{2,2023} \\ 
        L_{3,2023} \\ 
        \end{pmatrix}
        '''
    )

def UNIT3_3():

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

st.set_page_config(page_title="UNIT 3 HR Planning", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["HR planning table",'Forecasting the availability of employees using the transition matrix','Practice 12'],  # required
    icons=["calculator", "calculator", "person"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "HR planning table":
    UNIT3_1()
elif selected == 'Forecasting the availability of employees using the transition matrix':
    UNIT3_2()
elif selected == 'Practice 12':
    UNIT3_3()

