import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT3_1():
    st.write(
        '''
        HR planning involves predicting potential employee shortages or surpluses within the firm.
        In this unit, we will learn a method for making these predictions using a transition matrix. 
        The table below provides the base data we need to build the transition matrix, 
        specifically for three different jobs within a firm.
        '''
    )
             
    st.latex(r"""
    \begin{array}{|c|c|c|c|}
    \hline
    m_{11(t-1,t)} & m_{12(t-1,t)} & m_{13(t-1,t)} & s_{1(t-1,t)} \\
    \hline
    m_{21(t-1,t)} & m_{22(t-1,t)} & m_{23(t-1,t)} & s_{2(t-1,t)} \\
    \hline
    m_{31(t-1,t)} & m_{32(t-1,t)} & s_{33(t-1,t)} & s_{3(t-1,t)} \\
    \hline
    h_{1(t-1,t)} & h_{2(t-1,t)} & h_{3(t-1,t)} & \\
    \hline
    \end{array}
    """)


    st.write(
        '''
        Where $m$ represents employee mobility between jobs within the firm; $h$ represents new hires; 
        and $s$ represents separations. 
        '''
    )

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.write('Fill in data for 3 jobs at your firm (use made-up data):')
    
    L1, L2, L3, O = st.columns(4)
    with L1:
        m11 = st.number_input("$m_{11}$", key="m11", step=1)
        m21 = st.number_input("$m_{21}$", key="m21", step=1)
        m31 = st.number_input("$m_{31}$", key="m31", step=1)
        h1 = st.number_input("$h_{1}$", key="h1", step=1)
    with L2:
        m12 = st.number_input("$m_{12}$", key="m12", step=1)
        m22 = st.number_input("$m_{22}$", key="m22", step=1)
        m32 = st.number_input("$m_{32}$", key="m32", step=1)
        h2 = st.number_input("$h_{2}$", key="h2", step=1)
    with L3:
        m13 = st.number_input("$m_{13}$", key="m13", step=1)
        m23 = st.number_input("$m_{23}$", key="m23", step=1)
        m33 = st.number_input("$m_{33}$", key="m33", step=1)
        h3 = st.number_input("$h_{3}$", key="h3", step=1)
    with O:
        s1 = st.number_input("$s_{1}$", key="s1", step=1)
        s2 = st.number_input("$s_{2}$", key="s2", step=1)
        s3 = st.number_input("$s_{3}$", key="s3", step=1)

    st.write(
        '''
        By adding up the values of each of the three first rows of the table, we get the employment in a particular 
        job at $(t-1)$ at the firm:
        '''
    )

    st.latex(r'L_{i(t-1)} = m_{i1(t-1,t)} + m_{i2(t-1,t)} + m_{i3(t-1,t)} + s_{i(t-1,t)}')

    st.write(
        '''
        And by adding up the values of each of three first columns of the table, 
        we get the employment in a particular job at $t$ at the firm:
        '''
    )
    
    st.latex(r'L_{i(t)} = m_{1i(t-1,t)} + m_{2i(t-1,t)} + m_{3i(t-1,t)} + h_{i(t-1,t)}')

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.write('Employment in each job at the firm:')

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("$L_{1(t-1)}$"):
            L10 = np.array([m11, m12, m13, s1])
            L10 = np.sum(L10)
            st.write(f"Employment in job 1 at $t-1$: {L10}")
    with col2:
        if st.button("$L_{2(t-1)}$"):
            L20 = np.array([m21, m22, m23, s2])
            L20 = np.sum(L20)
            st.write(f"Employment in job 2 at $t-1$: {L20}")
    with col3:
        if st.button("$L_{3(t-1)}$"):
            L30 = np.array([m31, m32, m33, s3])
            L30 = np.sum(L30)
            st.write(f"Employment in job 3 at $t-1$: {L30}")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("$L_{1(t)}$"):
            L11 = np.array([m11, m21, m23, h1])
            L11 = np.sum(L11)
            st.write(f"Employment in job 1 at $t$: {L11}")
    with col2:
        if st.button("$L_{2(t)}$"):
            L21 = np.array([m12, m22, m32, h2])
            L21 = np.sum(L21)
            st.write(f"Employment in job 2 at $t$: {L21}")
    with col3:
        if st.button("$L_{3(t)}$"):
            L31 = np.array([m13, m23, m33, h3])
            L31 = np.sum(L31)
            st.write(f"Employment in job 3 at $t$: {L31}")

def UNIT3_2():
    st.write(
        '''
        HR planning relies on the transition matrix $T$ to make predictions of the future availability of employees at 
        $t+1$ in each different job at the firm (internal supply of labor). This is done through
        the following matrix multiplication:
        '''
    )

    st.latex(r'''
    \begin{pmatrix}
        \hat{L}_{1(t+1)} \\
        \hat{L}_{2(t+1)} \\
        \hat{L}_{3(t+1)} \\
    \end{pmatrix} = 
    \begin{pmatrix} 
        \frac{m_{11(t-1,t)}}{L_{1(t-1)}} & \frac{m_{12(t-1,t)}}{L_{1(t-1)}} & \frac{m_{13(t-1,t)}}{L_{1(t-1)}} \\ 
        \frac{m_{21(t-1,t)}}{L_{2(t-1)}} & \frac{m_{22(t-1,t)}}{L_{2(t-1)}} & \frac{m_{23(t-1,t)}}{L_{2(t-1)}} \\ 
        \frac{m_{31(t-1,t)}}{L_{3(t-1)}} & \frac{m_{32(t-1,t)}}{L_{3(t-1)}} & \frac{s_{33(t-1,t)}}{L_{3(t-1)}} \\  
    \end{pmatrix}^T
    \begin{pmatrix} 
        L_{1(t)} \\ 
        L_{2(t)} \\ 
        L_{3(t)} \\ 
    \end{pmatrix}
    '''
    )

    st.write('Complete the transition matrix $T$ of a firm')
    L1, L2, L3, O = st.columns(4)
    with L1:
        m11 = st.number_input("$m_{11}$", key="m11", step=1)
        m21 = st.number_input("$m_{21}$", key="m21", step=1)
        m31 = st.number_input("$m_{31}$", key="m31", step=1)
        h1 = st.number_input("$h_{1}$", key="h1", step=1)
    with L2:
        m12 = st.number_input("$m_{12}$", key="m12", step=1)
        m22 = st.number_input("$m_{22}$", key="m22", step=1)
        m32 = st.number_input("$m_{32}$", key="m32", step=1)
        h2 = st.number_input("$h_{2}$", key="h2", step=1)
    with L3:
        m13 = st.number_input("$m_{13}$", key="m13", step=1)
        m23 = st.number_input("$m_{23}$", key="m23", step=1)
        m33 = st.number_input("$m_{33}$", key="m33", step=1)
        h3 = st.number_input("$h_{3}$", key="h3", step=1)
    with O:
        s1 = st.number_input("$s_{1}$", key="s1", step=1)
        s2 = st.number_input("$s_{2}$", key="s2", step=1)
        s3 = st.number_input("$s_{3}$", key="s3", step=1)
        s4 = st.number_input("NaN", key="NaN", step=1)

    if st.button("Submit"):
        T = np.array([
            [m11/(m11+m12+m13+s1), m12/(m11+m12+m13+s1), m13/(m11+m12+m13+s1)],
            [m21/(m21+m22+m23+s2), m22/(m21+m22+m23+s2), m23/(m21+m22+m23+s2)],
            [m31/(m31+m32+m33+s3), m32/(m31+m32+m33+s3), m33/(m31+m32+m33+s3)],
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
    options=["Data for transition matrix construction",'Making predictions using the transition matrix'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Data for transition matrix construction":
    UNIT3_1()
elif selected == 'Making predictions using the transition matrix':
    UNIT3_2()

