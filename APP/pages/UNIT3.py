import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT3_1():
    st.write(
        '''
        The transition matrix of a firm, $M$, represents employee mobility both wihin the firm, between different jobs, and from the
        firm to the external market.
        '''
    )
             
    st.latex(r"""M = 
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
        In recruiting, **asymmetric information** arises when candidates know more about their abilities than the firm. 
    This can lead to **adverse selection**, where the firm might hire less qualified candidates because it lacks full information. 
    To mitigate this, candidates use **signaling** (e.g., qualifications, experience) to indicate their abilities, while firms engage 
    in **screening** (e.g., interviews, tests) to gather more information. Additionally, firms often use **probation periods** to assess 
    an employee’s true performance before making long-term commitments, reducing the risks of hiring based on incomplete information.
        '''
    )

def UNIT3_2():

    st.latex(r'''
    \text{CAGR} = \left( \frac{E_{n}}{E_{0}} \right)^{\frac{1}{n}} - 1
    ''')


    st.components.v1.iframe("https://www.unavarra.es/biblioteca?languageId=1", width=800, height=600, scrolling=True)
    
    employees_input = st.sidebar.text_input("Number of Employees (comma-separated for 2019, 2020, 2021):", "1,1,1")
    employees = np.fromstring(employees_input, sep=',')
        
    df = pd.DataFrame({
        "Year": ["2019", "2020", "2021"],
        "Employment": employees,
    })

    fig, ax = plt.subplots()
    ax.plot(["2019", "2020", "2021"], employees, marker='x', label='Employment')    
    ax.set_xlabel('Year')
    ax.set_ylabel('Metrics')
    ax.set_title("Employment Over Time")
    ax.legend()
    st.pyplot(fig)

def UNIT3_3():
    st.latex(r'L_{(t)} = L_{(t-1)} + h_{(t-1,t)} - s_{(t-1,t)}')
    st.latex(r'L_{i(t)} = L_{i(t-1)} + h_{i(t-1,t)} - s_{i(t-1,t)}')


st.set_page_config(page_title="UNIT3", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Transition Matrix","Employment","Employment Across Jobs"],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Transition Matrix":
    UNIT3_1()
if selected == "Employment":
    UNIT3_2()
if selected == "Employment Across Jobs":
    UNIT3_3()

