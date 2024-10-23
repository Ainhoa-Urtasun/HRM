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
        3 jobs has 4 rows and 4 columns:
        '''
    )
             
    st.latex(r"""T (4 \times 4) = 
    \begin{pmatrix}
    m_{11(t-1,t)} & m_{12(t-1,t)} & m_{13(t-1,t)} & s_{1(t-1,t)} \\
    m_{21(t-1,t)} & m_{22(t-1,t)} & m_{23(t-1,t)} & s_{2(t-1,t)} \\
    m_{31(t-1,t)} & m_{32(t-1,t)} & s_{33(t-1,t)} & s_{3(t-1,t)} \\
    h_{1(t-1,t)} & h_{2(t-1,t)} & h_{3(t-1,t)} & - \\
    \end{pmatrix}
    """)

    st.write(
        '''
        Where $m$ represents employee mobility between jobs within the firm; $h$ represents new hires; and $s$ represents separations. 
        From row-wise summations of $M$, we get the employment in a particular job at $(t-1)$ at the firm.
        And from column-wise summations of $M$, we get the employment in a particular job at $t$ at the firm:
        '''
    )

    st.write('Complete the transition matrix $T$ of a firm')
    L1, L2, L3, L4 = st.columns(4)
    with L1:
        S11 = st.number_input("$S_{11}$", key="S11")
        S21 = st.number_input("$S_{21}$", key="S21")
        S31 = st.number_input("$S_{31}$", key="S31")
        S41 = st.number_input("$S_{41}$", key="S41")
        S51 = st.number_input("$S_{51}$", key="S51")
        S61 = st.number_input("$S_{61}$", key="S61")
        S71 = st.number_input("$S_{71}$", key="S71")
        S81 = st.number_input("$S_{81}$", key="S81")
        S91 = st.number_input("$S_{91}$", key="S91")
    with W2:
        S12 = st.number_input("$S_{12}$", key="S12")
        S22 = st.number_input("$S_{22}$", key="S22")
        S32 = st.number_input("$S_{32}$", key="S32")
        S42 = st.number_input("$S_{42}$", key="S42")
        S52 = st.number_input("$S_{52}$", key="S52")
        S62 = st.number_input("$S_{62}$", key="S62")
        S72 = st.number_input("$S_{72}$", key="S72")
        S82 = st.number_input("$S_{82}$", key="S82")
        S92 = st.number_input("$S_{92}$", key="S92")
    with W3:
        S13 = st.number_input("$S_{13}$", key="S13")
        S23 = st.number_input("$S_{23}$", key="S23")
        S33 = st.number_input("$S_{33}$", key="S33")
        S43 = st.number_input("$S_{43}$", key="S43")
        S53 = st.number_input("$S_{53}$", key="S53")
        S63 = st.number_input("$S_{63}$", key="S63")
        S73 = st.number_input("$S_{73}$", key="S73")
        S83 = st.number_input("$S_{83}$", key="S83")
        S93 = st.number_input("$S_{93}$", key="S93")
    with W4:
        S14 = st.number_input("$S_{13}$", key="S14")
        S24 = st.number_input("$S_{24}$", key="S24")
        S34 = st.number_input("$S_{34}$", key="S34")
        S44 = st.number_input("$S_{44}$", key="S44")
        S54 = st.number_input("$S_{54}$", key="S54")
        S64 = st.number_input("$S_{64}$", key="S64")
        S74 = st.number_input("$S_{74}$", key="S74")
        S84 = st.number_input("$S_{84}$", key="S84")
        S94 = st.number_input("$S_{94}$", key="S94")
    with W5:
        S15 = st.number_input("$S_{15}$", key="S15")
        S25 = st.number_input("$S_{25}$", key="S25")
        S35 = st.number_input("$S_{35}$", key="S35")
        S45 = st.number_input("$S_{45}$", key="S45")
        S55 = st.number_input("$S_{55}$", key="S55")
        S65 = st.number_input("$S_{65}$", key="S65")
        S75 = st.number_input("$S_{75}$", key="S75")
        S85 = st.number_input("$S_{85}$", key="S85")
        S95 = st.number_input("$S_{95}$", key="S95")
    
    if st.button("Submit"):
        matrix = np.array([
            [S11, S12, S13, S14, S15],
            [S21, S22, S23, S24, S25],
            [S31, S32, S33, S34, S35],
            [S41, S42, S43, S44, S45],
            [S51, S52, S53, S54, S55],
            [S61, S62, S63, S64, S65],
            [S71, S72, S73, S74, S75],
            [S81, S82, S83, S84, S85],
            [S91, S92, S93, S94, S95]
        ])
    
        job_complexity = np.sum(matrix)
        st.write(f"Job Complexity: {job_complexity}")

    st.latex(r'L_{i(t-1)} = m_{i1(t-1,t)} + m_{i2(t-1,t)} + m_{i3(t-1,t)} + s_{i(t-1,t)}')
    st.latex(r'L_{i(t)} = m_{1i(t-1,t)} + m_{2i(t-1,t)} + m_{3i(t-1,t)} + h_{i(t-1,t)}')
    
    st.write(
        '''
        **Employment** refers to the number of employees, including both full-time and part-time workers. 
        **New hires** refers to the number of employees who have recently been recruited and started working at the firm.
        **Separations** refers to the number of employees who leave the firm, either voluntarily (quitting, retiring) 
        or involuntarily (layoffs, dismissals). In addition to **employment**, **new hires**, and **separations**, 
        there are other critical aspects that affect recruitment in a firm: job vacancies (or job openings) and job postings (or job advertisements, or job ads). 
        **Job vacancies (job openings)** represent the number of available positions at the firm for which the firm is actively seeking candidates. 
        **Job postings (job advertisements, job ads)** are advertisements made by the firm to fill open positions, specifying required qualifications and job responsibilities.
        '''
    )

    st.write(
        '''
        From the transition matrix $T$ we can calculate the total employment of the firm at $(t-1)$ and at $(t)$ as well as
        its retention and turnover rates, which are critical HRM metrics.
        '''
    )

    st.latex(r'L_{(t-1)} = L_{1(t-1)}+ L_{2(t-1)} + L_{3(t-1)}')
    st.latex(r'L_{(t)} = L_{1(t)}+ L_{2(t)} + L_{3(t-1)}')
    st.latex(r'\text{Retention} = 100 \times \frac{m_{11(t-1,t)}+m_{22(t-1,t)}+m_{33(t-1,t)}}{L_{(t-1)}}')
    st.latex(r'\text{Turnover} = 100 - \text{Retention}')

st.set_page_config(page_title="UNIT3", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Transition Matrix"],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Transition Matrix":
    UNIT3_1()

