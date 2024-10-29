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
        In recruiting, **asymmetric information** arises because job candidates 
        know more about their skills than the firm does. This can lead to **adverse selection**, 
        where the firm may end up hiring less qualified candidates due to this information gap. 
        Here’s how adverse selection occurs: to attract a pool of candidates, 
        the firm posts a job ad specifying the tasks, required skills, credentials, 
        and salary for the role. Due to limited information about each candidate’s true abilities, 
        the employer offers an average salary for the position. 
        This attracts candidates who meet the listed credentials, but these credentials, 
        while signaling a certain level of qualification, do not fully reveal each candidate's suitability.
    
        However, this average salary might be too low for the 'good' candidates 
        while still appealing to 'wrong' ones, 
        resulting in adverse selection where primarily 'wrong' candidates apply.

        '''
    )

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.write('Use [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) and chose one occupation for which you wish to post a job and offer the average salary:')

def UNIT4_3():
    st.write('Suppose $L$ employees at a firm contribute to output as follows:')
    st.latex(r'Q = e_1^{\alpha_1} \times e_2^{\alpha_2} \times \cdots \times e_L^{\alpha_L}')
    st.write('The output elasticity of each employee follows this order:')
    st.latex(r'\alpha_1 > \alpha_2 > \cdots > \alpha_L')
    st.write(
        '''
        The firm is about to hire a new employee from the labor market. Suppose the firm wishes to hire 
        an employee who contributes the maximum possible, that is, one whose output elasticity is the highest. 
        However, due to **asymmetric information**, the employer doesn't know the exact contribution of each candidate 
        to the firm’s value. To attract candidates, the employer needs to offer a salary. 
    
        The employer could offer a high salary to attract good candidates who are expected to contribute significantly. 
        However, if the employer offers a salary equal to the highest contribution, anyone might apply, pretending 
        to be the best candidate. Given this asymmetric information, the firm decides to offer a salary that is equal 
        to the expected contribution of the candidate pool:
        '''
    )
    
    st.latex(r'w = \mathbb{E}(\alpha) = \sum_{i=1}^{L} p_i \alpha_i')
    st.write(
        '''
        As a result, only candidates with lower contributions (the "wrong" candidates) accept the offer, 
        creating a **pooling equilibrium** where lower-contribution candidates dominate.
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
    options=["Employment","Asymmetric information and adverse selection",'Adverse selection','Signaling'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Employment":
    UNIT4_1()
elif selected == "Asymmetric information and adverse selection":
    UNIT4_2()
elif selected == "Adverse selection":
    UNIT4_3()
elif selected == "Signaling":
    UNIT4_4()

