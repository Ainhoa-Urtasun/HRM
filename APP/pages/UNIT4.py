import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT4_1():

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

    st.write(
        """
        When a company posts a job online, two types of candidates apply: 
        'right' (high-effort) candidates and 'wrong' (low-effort) candidates. 
        Let's denote the effort levels of these candidates as eR (right candidates) and eW (wrong candidates), 
        with eR > eW. However, due to **asymmetric information**, the employer 
        cannot distinguish between these two types of candidates initially.
        The employer knows that there is a probability **p** that the candidate is the 'right' one, 
        and a probability **1-p** that the candidate is 'wrong'. To deal with this uncertainty, 
        the employer may offer a salary based on the **average effort** of both types of candidates. 
        As a result, only the 'wrong' candidates accept the offer, creating a **pooling equilibrium** 
        where low-effort workers dominate.


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
        """
    )

st.write("""
#### Formulation

Let:
- **S_0** be the salary offered without ECTS
- **S_1** be the salary offered with ECTS
- **C_w** be the cost of obtaining ECTS for a wrong candidate
- **C_r** be the cost of obtaining ECTS for a right candidate

The two conditions are:
1. Wrong candidate:  
   \[
   S_0 > S_1 - C_w
   \]
2. Right candidate:  
   \[
   S_1 - C_r > S_0
   \]

These conditions ensure that wrong candidates do not find it worthwhile to obtain ECTS, while right candidates do. Therefore, signaling through ECTS helps employers differentiate candidates based on their effort levels.
""")



st.set_page_config(page_title="UNIT4", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Employment","Asymmetric Information"],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Employment":
    UNIT4_1()
if selected == "Asymmetric Information":
    UNIT4_2()

