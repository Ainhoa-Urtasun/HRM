import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT4_1():

    st.write(
        '''
        Employment refers to the number of employees, including both full-time and part-time workers. 
        If we have information of employment in a firm at the job level, 
        we can calculate the total employment of the firm at $(t-1)$ and at $(t)$ as follows,
        assuming $N$ jobs both at $t-1$ and $t$:
        '''
    )

    st.latex(r'L_{(t-1)} = L_{1(t-1)}+ L_{2(t-1)} + ... + L_{N(t-1)}')
    st.latex(r'L_{(t)} = L_{1(t)}+ L_{2(t)} + ...+ L_{N(t-1)}')

    st.write(
        '''
        Then if we have information of yearly employment in a firm we can calculate the 
        compound annual growth rate of employment as follows:
        '''
    )

    st.latex(r'''
    \text{CAGR} = \left( \frac{L_{t+k}}{L_{t}} \right)^{\frac{1}{k}} - 1
    ''')

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.write('From [SABI](https://www.unavarra.es/biblioteca?languageId=1) and for your firm, visualize employment:')
    
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

def UNIT4_2():
    
    st.write(
        '''
        In recruiting, **asymmetric information** arises when candidates know more about their abilities than the firm. 
        This can lead to **adverse selection**, where the firm might hire less qualified candidates because it lacks full information. 
        To mitigate this, candidates use **signaling** (e.g., qualifications, experience) to indicate their abilities, while firms engage 
        in **screening** (e.g., interviews, tests) to gather more information. Additionally, firms often use **probation periods** to assess 
        an employee’s true performance before making long-term commitments, reducing the risks of hiring based on incomplete information.
        '''
    )

def UNIT4_3():

    st.write(
        '''
        Suppose $Q = e_1^\alpha$ When a company posts a job online, two types of candidates apply: 
        right (high-effort) candidates and wrong (low-effort) candidates. 
        Let's denote the effort levels of these candidates as $e_R$ (right candidates) and $e_W$ (wrong candidates), 
        with:
        '''
    )
    st.latex(r'e_R > e_W')
    
    st.write(
        '''
        However, due to **asymmetric information**, the employer 
        cannot distinguish between these two types of candidates initially.
        The employer knows that there is a probability $p$ that the candidate is the right one, 
        and a probability $1-p$ that the candidate is wrong. Due to uncertainty, the employer has to offer
        a unique salary based on the **average effort** of both types of candidates:
        '''
    )

    st.latex(r'\bar w = p \times e_R + (1-p) \times e_L')
        
    st.write(
        '''
        As a result, only the wrong candidates accept the offer, creating a **pooling equilibrium** 
        where low-effort workers dominate.
        '''
    )

def UNIT4_4():
    
    st.write(
        '''
        To reach a **separating equilibrium**, where the employer can differentiate between 
        the two types of candidates, they may rely on **signaling**. 
        In this context, candidates can signal their ability through obtaining **ECTS credits** aligned with the job. 
        Although both right and wrong candidates can obtain ECTS, it is more costly for the wrong candidates.
        
        This leads to the following conditions:
        1. For the wrong candidate, the salary they earn without ECTS must be greater 
        than the salary they would earn with ECTS, minus the cost of obtaining ECTS.
        2. For the right candidate, the salary with ECTS, minus the cost of obtaining ECTS, 
        must be greater than the salary without ECTS.

        This signaling helps the employer distinguish between the two types of candidates, 
        leading to a more efficient recruitment process.

        These conditions ensure that wrong candidates do not find it worthwhile to obtain ECTS, while right candidates do. 
        Therefore, signaling through ECTS helps employers differentiate candidates based on their effort levels.
        '''
    )

st.set_page_config(page_title="UNIT4", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Employment","Asymmetric information",'Adverse selection','Signaling'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Employment":
    UNIT4_1()
elif selected == "Asymmetric information":
    UNIT4_2()
elif selected == "Adverse selection":
    UNIT4_3()
elif selected == "Signaling":
    UNIT4_4()

