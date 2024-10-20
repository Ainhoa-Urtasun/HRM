import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT3_1():
    st.write(
        '''
        HR planning involves forecasting potential skill shortages or surpluses within the firm. 
        A useful tool for HR planning is the firm's transition matrix, $M$,
        which represents employee mobility both within the firm (between different jobs) 
        and from the firm to the external labor market. The transition matrix of a firm with
        3 jobs has 4 rows and 4 columns:
        '''
    )
             
    st.latex(r"""M (4 \times 4) = 
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
        From the transition matrix $M$ we can calculate the total employment of the firm at $(t-1)$ and at $(t)$ as well as
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

