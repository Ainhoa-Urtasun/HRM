import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

def UNIT3_1():
    st.write(
        '''
        HR planning involves forecasting the availability of employees across different jobs within a firm. 
        The primary goal is to anticipate potential employee shortages or surpluses. Latest available data 
        from [SABI](https://www.unavarra.es/biblioteca?languageId=1):

        - $L_{k,2022}$ The number of employees in job $J_k$ at the end of 2022
        - $L_{k,2023}$ The number of employees in job $J_k$ at the end of 2023
        '''
    )

    st.latex(
        r"""
        \begin{array}{|c|c|c|c|}
        \hline
        m_{11} & m_{12} & m_{13} & d_{1} \\
        \hline
        m_{21} & m_{22} & m_{23} & d_{3} \\
        \hline
        m_{31} & m_{32} & s_{33} & d_{3} \\
        \hline
        h_{1} & h_{2} & h_{3} & \\
        \hline
        \end{array}
        """
    )

    st.write(
        '''
        - $m_{ij}$ represents employees who moved from $J_i$ to $J_j$ during 2023
        - $h_{k}$ represents new hires or number of employees who have been recruited and started working in $J_i$ 
        during 2023
        - $d$ represents departures or number of employees who have left the firm during 2023,
        either voluntarily (quitting or retiring) or involuntarily (layoffs, dismissals). 

        The table above should meet the following restrictions:
        '''
    )

    st.latex(r'L_{k,2022} = m_{k1} + m_{k2} + m_{k3} + d_{k}')
    st.latex(r'L_{k,2023} = m_{1k} + m_{2k} + m_{3k} + h_{k}')

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.sidebar.write('Data collection:')
    with st.sidebar.expander("$J_1$ Other managers"):
        L12022 = st.number_input("$L_{1,2022}$", key='L12022', step=1, min_value=20)
        L12023 = st.number_input("$L_{1,2023}$", key='L12023', step=1, min_value=20)
    with st.sidebar.expander("$J_2$ Support intellectuals and scientists, technicians and professionals"):
        L22022 = st.number_input("$L_{2,2022}$", key='L22022', step=1, min_value=20)
        L22023 = st.number_input("$L_{2,2023}$", key='L22023', step=1, min_value=20)
    with st.sidebar.expander("$J_3$ Administrative employees"):
        L32022 = st.number_input("$L_{3,2022}$", key='L32022', step=1, min_value=20)
        L32023 = st.number_input("$L_{3,2023}$", key='L32023', step=1, min_value=20)

    m11 = L12022 - 1
    m22 = L22022 - 4
    m33 = L32022 - 3

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
        
    if st.button("Data"):
        st.write(matrix)

def UNIT3_2():
    st.write(
        '''
        HR planning makes predictions on the future availability of employees using the transition matrix $T$.
        The notation below illustrates
        the structure of the transition matrix $T$ and the calculations required to to make these predictions:
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
        \hat{L}_1 \\
        \hat{L}_2 \\
        \hat{L}_3 \\
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

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.sidebar.write('Data collection:')
    with st.sidebar.expander("$J_1$ Other managers"):
        L12022 = st.number_input("$L_{1,2022}$", key='L12022', step=1, min_value=20)
        L12023 = st.number_input("$L_{1,2023}$", key='L12023', step=1, min_value=20)
    with st.sidebar.expander("$J_2$ Support intellectuals and scientists, technicians and professionals"):
        L22022 = st.number_input("$L_{2,2022}$", key='L22022', step=1, min_value=20)
        L22023 = st.number_input("$L_{2,2023}$", key='L22023', step=1, min_value=20)
    with st.sidebar.expander("$J_3$ Administrative employees"):
        L32022 = st.number_input("$L_{3,2022}$", key='L32022', step=1, min_value=20)
        L32023 = st.number_input("$L_{3,2023}$", key='L32023', step=1, min_value=20)

    m11 = L12022 - 1
    m22 = L22022 - 4
    m33 = L32022 - 3

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
   
    if st.button("HR planning"):
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

    st.write(
    """
    ### Strategies for Predicted Skill Shortage:
    
    1. **Upskilling and Reskilling Employees**: Provide training programs to improve the skills of existing employees, focusing on critical areas needed for future roles.
    
    2. **Internal Mobility and Career Development**: Encourage internal transfers to roles that are in demand, offering clear career development paths and incentives.
    
    3. **External Recruitment**: Recruit externally to fill skill gaps, targeting skilled candidates through job fairs, headhunting, and specialized recruitment.
    
    4. **Collaboration with Educational Institutions**: Partner with universities and vocational schools to ensure a future pipeline of skilled graduates through internships and apprenticeship programs.
    
    5. **Use of Technology and Automation**: Automate tasks, especially in routine or manual work, to reduce reliance on human labor where skills are hard to find.
    
    6. **Improving Compensation and Benefits**: Offer competitive salaries and benefits to attract and retain skilled employees.
    
    ---
    
    ### Strategies for Predicted Skill Surplus:
    
    1. **Workforce Reduction Plans**: Implement downsizing strategies such as voluntary early retirement or severance packages for employees in surplus roles.
    
    2. **Redeployment**: Reassign employees to departments or roles with shortages, potentially offering additional training to align skills.
    
    3. **Flexible Work Arrangements**: Introduce part-time work, job sharing, or temporary layoffs to manage surplus labor while retaining valuable employees.
    
    4. **Cross-training Programs**: Offer cross-training to employees, enabling them to take on new tasks in other areas of the business, reducing surplus labor.
    
    5. **Strategic Use of Temporary Contracts**: Use temporary or project-based contracts for future hires to prevent long-term surplus labor.
    
    6. **Attrition Management**: Rely on natural attrition by not replacing employees who leave voluntarily, balancing the workforce over time.
    """
    )

st.set_page_config(page_title="UNIT3", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Data collection",'Transition matrix'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Data collection":
    UNIT3_1()
elif selected == 'Transition matrix':
    UNIT3_2()

