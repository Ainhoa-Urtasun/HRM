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
        The primary goal is to anticipate potential employee shortages or surpluses. Effective HR planning requires the
        following data:

        - $L_{(k,-1)}$ The number of employees in job $J_{(k)}$ at time point -1 (representing the past)
        - $L_{(k,0)}$ The number of employees in job $J_{(k)}$ at time point 0 (representing the present moment)
        '''
    )

    st.latex(
        r"""
        \begin{array}{|c|c|c|c|}
        \hline
        m_{(1)(1)} & m_{(1)(2)} & m_{(1)(3)} & d_{(1)} \\
        \hline
        m_{(2)(1)} & m_{(2)(2)} & m_{(2)(3)} & d_{(2)} \\
        \hline
        m_{(3)(1)} & m_{(3)(2)} & s_{(3)(3)} & d_{(3)} \\
        \hline
        h_{(1)} & h_{(2)} & h_{(3)} & \\
        \hline
        \end{array}
        """
    )

    st.write(
        '''
        - $m_{(i)(j)}$ represents employees who moved from $J_{(i)}$ to $J_{(j)}$ during the period $(-1,0)$
        - $h_{(k)}$ represents new hires or number of employees who have been recruited and started working in $J_{(i)}$ 
        during the period $(-1,0)$
        - $d$ represents departures or number of employees who have left the firm during the period $(-1,0)$,
        either voluntarily (quitting or retiring) or involuntarily (layoffs, dismissals). 

        The table above should meet the following restrictions:
        '''
    )

    st.latex(r'L_{(k,-1)} = m_{(k)(1)} + m_{(k)(2)} + m_{(k)(3)} + d_{(k)}')
    st.latex(r'L_{(k,0)} = m_{(1)(k)} + m_{(2)(k)} + m_{(3)(k)} + h_{(k)}')

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.sidebar.write('Data collection:')
    with st.sidebar.expander("$J_{(1)}$ Senior management"):
        L1past = st.number_input("$L_{(1,-1)}$",key='L1past',step=1,min_value=3)
        L1present = st.number_input("$L_{(1,0)}$",key='L1present',step=1,min_value=3)
    with st.sidebar.expander("$J_{(2)}$ Support intellectuals and scientists, technicians and professionals"):
        L2past = st.number_input("$L_{(2,-1)}$",key='L2past',step=1,min_value=3)
        L2present = st.number_input("$L_{(2,0)}$",key='L2present',step=1,min_value=3)
    with st.sidebar.expander("$J_{(3)}$ Sales representatives and similar"):
        L3past = st.number_input("$L_{(3,-1)}$",key='L3past',step=1,min_value=3)
        L3present = st.number_input("$L_{(3,0)}$",key='L3present',step=1,min_value=3)

    random.seed(42)
    m11 = random.randint(0, L1past - 1)
    m12 = random.randint(0, L1past - m11 - 1)
    m13 = random.randint(0, L1past - m11 - m12 - 1)
    d1 = L1past - m11 - m12 - m13
    m21 = random.randint(0, L2past - 1)
    m22 = random.randint(0, L2past - m21 - 1)
    m23 = random.randint(0, L2past - m21 - m22 - 1)
    d2 = L2past - m21 - m22 - m23
    m31 = random.randint(0, L3past - 1)
    m32 = random.randint(0, L3past - m31 - 1)
    m33 = random.randint(0, L3past - m31 - m32 - 1)
    d3 = L3past - m31 - m32 - m33
    h1 = L1present - m11 - m21 - m31
    h2 = L2present - m12 - m22 - m32
    h3 = L3present - m13 - m23 - m33
    
    matrix = np.array([
            [m11, m12, m13, d1],
            [m21, m22, m23, d2],
            [m31, m32, m33, d3],
            [h1, h2, h3, np.nan]
    ])
    
    if st.button("Data"):
        st.write(matrix)

def UNIT3_2():
    st.write(
        '''
        HR planning relies on the transition matrix $T$ to make predictions of the future availability of employees at 
        $t+1$ in each different job at the firm (internal supply of labor). The notation below illustrates
        the structure of the transition matrix $T$ and the calculations required to to make these predictions:
        '''
    )

    st.latex(
        r'''
        T =
        \begin{pmatrix}
        \frac{m_{(1)(1)}}{L_{(1,-1)}} & \frac{m_{(1)(2)}}{L_{1,-1}} & \frac{m_{(1)(3)}}{L_{1,-1}} \\ 
        \frac{m_{(2)(1)}}{L_{(2,-1)}} & \frac{m_{(2)(2)}}{L_{2,-1}} & \frac{m_{(2)(3)}}{L_{2,-1}} \\ 
        \frac{m_{(3)(1)}}{L_{(3,-1)}} & \frac{m_{(3)(2)}}{L_{3,-1}} & \frac{m_{(3)(3)}}{L_{3,-1}} \\  
        \end{pmatrix} \\[10pt]
        
        \begin{pmatrix}
        \hat{L}_{(1)} \\
        \hat{L}_{(2)} \\
        \hat{L}_{(3)} \\
        \end{pmatrix} = 
        \begin{pmatrix}
        \frac{m_{(1)(1)}}{L_{(1,-1)}} & \frac{m_{(1)(2)}}{L_{1,-1}} & \frac{m_{(1)(3)}}{L_{1,-1}} \\ 
        \frac{m_{(2)(1)}}{L_{(2,-1)}} & \frac{m_{(2)(2)}}{L_{2,-1}} & \frac{m_{(2)(3)}}{L_{2,-1}} \\ 
        \frac{m_{(3)(1)}}{L_{(3,-1)}} & \frac{m_{(3)(2)}}{L_{3,-1}} & \frac{m_{(3)(3)}}{L_{3,-1}} \\  
        \end{pmatrix}^T
        \begin{pmatrix} 
        L_{(1,0)} \\ 
        L_{(2,0)} \\ 
        L_{(3,0)} \\ 
        \end{pmatrix}
        '''
    )

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.write('Fill in data for the 3 jobs at your firm (use made-up data):')
    
    L1, L2, L3, D = st.columns(4)
    with L1:
        m11 = st.number_input("$m_{(1)(1)}$", key="m11", step=1)
        m21 = st.number_input("$m_{(2)(1)}$", key="m21", step=1)
        m31 = st.number_input("$m_{(3)(1)}$", key="m31", step=1)
        h1 = st.number_input("$h_{(1)}$", key="h1", step=1)
    with L2:
        m12 = st.number_input("$m_{(1)(2)}$", key="m12", step=1)
        m22 = st.number_input("$m_{(2)(2)}$", key="m22", step=1)
        m32 = st.number_input("$m_{(3)(2)}$", key="m32", step=1)
        h2 = st.number_input("$h_{(2)}$", key="h2", step=1)
    with L3:
        m13 = st.number_input("$m_{(1)(3)}$", key="m13", step=1)
        m23 = st.number_input("$m_{(2)(3)}$", key="m23", step=1)
        m33 = st.number_input("$m_{(3)(3)}$", key="m33", step=1)
        h3 = st.number_input("$h_{(3)}$", key="h3", step=1)
    with D:
        d1 = st.number_input("$d_{(1)}$", key="d1", step=1)
        d2 = st.number_input("$d_{(2)}$", key="d2", step=1)
        d3 = st.number_input("$d_{(3)}$", key="d3", step=1)

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
        st.write(f"Predictions: {predictions}")

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

