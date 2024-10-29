import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT4_1():

    st.write(
        '''
        Performance evaluation refers to assessing how well employees perform within the firm. 
        Performance can be evaluated on average or for each specific employee, with the latter being more challenging 
        but also more meaningful.

        A typical average performance evaluation metric is labor productivity.
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

def UNIT5_3():
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

st.set_page_config(page_title="UNIT4", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Average performance evaluation",'Employee performance evaluation'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Average performance evaluation":
    UNIT4_1()
elif selected == "Employee performance evaluation":
    UNIT4_2()
