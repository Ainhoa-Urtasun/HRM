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
    st.text_input('From [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) choose one occupation for which you wish to post a job:')
    st.text_input('For that job posting, offer a salary equal to the median monthly gross income in EUR for that occupation as reported in [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence):')
    st.text_input('Explain why you might end up recruiting the wrong job candidates:')

def UNIT4_3():
    st.write(r"The cost of effort for each employee or job candidate is defined as:")
    st.write(r"$$C(e) = (100 - S)e^2$$")
    st.write(r"where:")
    st.write(r" - \( C(e) \) is the total cost of effort,")
    st.write(r" - \( e \) represents the level of effort exerted,")
    st.write(r" - \( S \) denotes the skill or credential level required to apply for the job.")

    st.write(r"Assuming \( S = 99 \), indicating a high-skill candidate, then their cost of effort becomes:")
    st.write(r"$$C(e) = e^2$$")
    st.write(r"This lower cost reflects that the high-skill candidate possesses the necessary skill abundantly, making effort less costly for them.")

    st.write(r"For a low-skill candidate, assuming \( S = 0 \), the cost of effort is:")
    st.write(r"$$C(e) = 100 e^2$$")
    st.write(r"This higher cost implies that it would be more expensive for the low-skill candidate to exert the same level of effort as the high-skill candidate.")

    st.write(r"The company offers a salary of 4,000, expecting a target effort level of \( e = 200 \).")
    st.write(r"Under this salary and effort expectation, a high-skill candidate (\( S = 99 \)) is willing to exert the required effort, as their cost of effort \( C(e) = e^2 = 200^2 = 40,000 \) is feasible.")
    st.write(r"In contrast, a low-skill candidate (\( S = 0 \)) would face a prohibitive cost of \( C(e) = 100 \times 200^2 = 4,000,000 \) and thus would not apply.")
    st.write(r"The challenge remains: how to measure and control for the actual effort exerted by candidates to ensure that the required skill level aligns with job expectations.")

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
    options=["Employment","Asymmetric information and adverse selection",'Ways to mitigate adverse selection','Signaling'],  # required
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
elif selected == "Ways to mitigate adverse selection":
    UNIT4_3()
elif selected == "Signaling":
    UNIT4_4()

