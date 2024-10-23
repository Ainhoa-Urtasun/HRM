import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT3_1():
    st.write(
        '''
        HR planning involves forecasting potential skill shortages or surpluses within the firm. 
        A useful tool for HR planning is the firm's transition matrix, $T$,
        which represents employee mobility both within the firm (between different jobs) 
        and from the firm to the external labor market. The transition matrix of a firm with
        3 jobs looks as follows:
        '''
    )
             
    st.latex(r"""T (4 \times 4) = 
    \begin{pmatrix}
    m_{11(t-1,t)} & m_{12(t-1,t)} & m_{13(t-1,t)} & s_{1(t-1,t)} \\
    m_{21(t-1,t)} & m_{22(t-1,t)} & m_{23(t-1,t)} & s_{2(t-1,t)} \\
    m_{31(t-1,t)} & m_{32(t-1,t)} & s_{33(t-1,t)} & s_{3(t-1,t)} \\
    h_{1(t-1,t)} & h_{2(t-1,t)} & h_{3(t-1,t)} & NaN \\
    \end{pmatrix}
    """)

    st.write(
        '''
        Where $m$ represents employee mobility between jobs within the firm; $h$ represents new hires; 
        and $s$ represents separations. 

        '''
    )

    st.write('Complete the transition matrix $T$ of a firm')
    L1, L2, L3, O = st.columns(4)
    with L1:
        m11 = st.number_input("$m_{11}$", key="m11")
        m21 = st.number_input("$m_{21}$", key="m21")
        m31 = st.number_input("$m_{31}$", key="m31")
        h1 = st.number_input("$h_{1}$", key="h1")
    with L2:
        m12 = st.number_input("$m_{12}$", key="m12")
        m22 = st.number_input("$m_{22}$", key="m22")
        m32 = st.number_input("$m_{32}$", key="m32")
        h2 = st.number_input("$h_{2}$", key="h2")
    with L3:
        m13 = st.number_input("$m_{13}$", key="m13")
        m23 = st.number_input("$m_{23}$", key="m23")
        m33 = st.number_input("$m_{33}$", key="m33")
        h3 = st.number_input("$h_{3}$", key="h3")
    with O:
        s1 = st.number_input("$s_{1}$", key="s1")
        s2 = st.number_input("$s_{2}$", key="s2")
        s3 = st.number_input("$s_{3}$", key="s3")
        NaN = st.number_input("$NaN$", key="NaN")

    st.write(
        '''
        From row-wise summation of each of the three first rows of $T$, we get the employment in a particular 
        job at $(t-1)$ at the firm.
        And from column-wise summation of each of three first columns of $T$, 
        we get the employment in a particular job at $t$ at the firm:
        '''
    )

    st.latex(r'L_{i(t-1)} = m_{i1(t-1,t)} + m_{i2(t-1,t)} + m_{i3(t-1,t)} + s_{i(t-1,t)}')
    st.latex(r'L_{i(t)} = m_{1i(t-1,t)} + m_{2i(t-1,t)} + m_{3i(t-1,t)} + h_{i(t-1,t)}')

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("$L_{1(t-1)}$"):
            L10 = np.array([m11, m12, m13, s1])
            L10 = np.sum(L10)
            st.write(f"Employment in job 1 at $t-1$: {L10}")
    with col2:
        if st.button("$L_{2(t-1)}$"):
            L20 = np.array([m21, m22, m23, s2])
            L20 = np.sum(L20)
            st.write(f"Employment in job 2 at $t-1$: {L20}")
    with col3:
        if st.button("$L_{3(t-1)}$"):
            L30 = np.array([m31, m32, m33, s3])
            L30 = np.sum(L30)
            st.write(f"Employment in job 3 at $t-1$: {L30}")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("$L_{1(t)}$"):
            L11 = np.array([m11, m21, m23, h1])
            L11 = np.sum(L10)
            st.write(f"Employment in job 1 at $t$: {L1}")
    with col2:
        if st.button("$L_{2(t)}$"):
            L21 = np.array([m12, m22, m32, h2])
            L21 = np.sum(L21)
            st.write(f"Employment in job 2 at $t$: {L21}")
    with col3:
        if st.button("$L_{3(t)}$"):
            L31 = np.array([m13, m23, m33, h3])
            L31 = np.sum(L31)
            st.write(f"Employment in job 3 at $t$: {L3}")

    
    st.write(
        '''
        **Employment** refers to the number of employees, including both full-time and part-time workers. 
        **New hires** refers to the number of employees who have recently been recruited and started working at the firm.
        **Separations** refers to the number of employees who leave the firm, either voluntarily (quitting, retiring) 
        or involuntarily (layoffs, dismissals).
        '''
    )

    st.write(
        '''
        From the transition matrix $T$, we can calculate the total employment of the firm at $(t-1)$ and at $(t)$ as well as
        its retention and turnover rates, which are critical HRM metrics.
        '''
    )

    st.latex(r'L_{(t-1)} = L_{1(t-1)}+ L_{2(t-1)} + L_{3(t-1)}')
    st.latex(r'L_{(t)} = L_{1(t)}+ L_{2(t)} + L_{3(t-1)}')
    st.latex(r'\text{Retention} = 100 \times \frac{m_{11(t-1,t)}+m_{22(t-1,t)}+m_{33(t-1,t)}}{L_{(t-1)}}')
    st.latex(r'\text{Turnover} = 100 - \text{Retention}')

def UNIT3_2():
    st.write(
        '''
        HR planning relies on the transition matrix $T$ to make predictions of the future availability of employees at 
        $t+1$ in each different job at the firm (internal supply of labor). This is done through
        the following matrix multiplication:
        '''
    )

    st.latex(r'''\hat{L}_{t+1} = 
        \begin{pmatrix}
        m_{11(t-1,t)} & m_{12(t-1,t)} & m_{13(t-1,t)} & s_{1(t-1,t)} \\
        m_{21(t-1,t)} & m_{22(t-1,t)} & m_{23(t-1,t)} & s_{2(t-1,t)} \\
        m_{31(t-1,t)} & m_{32(t-1,t)} & s_{33(t-1,t)} & s_{3(t-1,t)} \\
        h_{1(t-1,t)} & h_{2(t-1,t)} & h_{3(t-1,t)} & - \\
        \end{pmatrix}
        '''
    )
    

st.set_page_config(page_title="UNIT3", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Transition matrix",'Making predictions'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Transition matrix":
    UNIT3_1()
elif selected == 'Making predictions':
    UNIT3_2()

