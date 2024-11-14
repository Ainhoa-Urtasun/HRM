import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm

def UNIT2_1():
    
    st.write(
        """
        A **skill**, denoted as $s_i$, is an ability or competence that an individual possesses. Employees use their skills to effectively perform 
        tasks. Skills themselves do not directly produce output; rather, they enable the completion of tasks. 
        There are many classifications of skills. For simplicty, we focus only on the 4 
        most requested transversal skills and competences in online job ads in the EU27 in 2023
        [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence):

        - $s_1$ Demonstrating willingness to learn
        - $s_2$ Collaborating in teams and networks
        - $s_3$ Working efficiently
        - $s_4$ Taking a proactive approach
        
        A **task**, denoted as $t_j$, is an action performed by an employee that results in a specific output.
        For simplicity, we assume any economic activity can be completed by carrying out the 5 core tasks listed in
        [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence): 
        
        - $t_1$ Intellectual
        - $t_2$ Physical
        - $t_3$ Social
        - $t_4$ Use of methods
        - $t_5$ Use of technology

        A **job**, denoted as $J_k$, is a bundle of tasks ($t_1$: intellectual, $t_2$: physical,
        $t_3$: social, $t_4$: use of methods, and $t_5$: use of technology). To carry out each task,
        employees need to possess 
        multiple skills ($s_1$: demostrating willigness to learn, $s_2$: maintaining a postive attitude, 
        $s_3$: taking a proactive approach, and $s_4$: working efficiently):
        - $J_1$ Other managers
        - $J_2$ Support intellectuals and scientists, technicians and professionals
        - $J_3$ Administrative employees
        """
    )
    
def UNIT2_2():

    st.write(
        '''
        **Job evaluation** assesses the relative worth of jobs within a firm, helping in job design, 
        setting recruitment standards, establishing fair compensation, and identifying training needs. 

        The **task-skill matrix** is a tool for job evaluation, where each column corresponds 
        to one of the five core tasks, and each row represents the extent to which one the four skills is required
        to perform each task within the job:
        '''
    )
             
    st.latex(
        r"""
        J_k = \begin{pmatrix}
        s_{11k} & s_{12k} & s_{13k} & s_{14k} & s_{15k} \\
        s_{21k} & s_{22k} & s_{23k} & s_{24k} & s_{25k} \\
        s_{31k} & s_{32k} & s_{33k} & s_{34k} & s_{35k} \\
        s_{41k} & s_{42k} & s_{43k} & s_{44k} & s_{45k} \\
        \end{pmatrix} \\[10pt]
        """
    )

    st.write(
        '''
        We restrict $s_{ijk}$ to the following values:
        '''
    )

    st.latex(r'0 \leq s_{ijk} \leq 100')

    st.write(
        '''
        A job doesn't necessarily entail all tasks. 
        If a job doesn't entail a particular task, 
        its corresponding column will be a vector of zeros.

        We can further summarize the information in the matrix by calculating the norm of each
        row-vector. The result, which we refer to as **job skill requirements** provides a quantitative
        measure of the skill intensity required across the tasks a job entails, offering another tool for 
        job evaluation:
        '''
    )

    st.latex(
        r"""
        s_k = 0.45 \begin{pmatrix} 
        \|s_{1k}\| \\ 
        \|s_{2k}\| \\ 
        \|s_{3k}\| \\ 
        \|s_{4k}\| 
        \end{pmatrix} = 0.45 \begin{pmatrix} 
        \sqrt{s_{11k}^2 + s_{12k}^2 + s_{13k}^2 + s_{14k}^2 + s_{15k}^2} \\[10pt] 
        \sqrt{s_{21k}^2 + s_{22k}^2 + s_{23k}^2 + s_{24k}^2 + s_{25k}^2} \\[10pt] 
        \sqrt{s_{31k}^2 + s_{32k}^2 + s_{33k}^2 + s_{34k}^2 + s_{35k}^2} \\[10pt] 
        \sqrt{s_{41k}^2 + s_{42k}^2 + s_{43k}^2 + s_{44k}^2 + s_{45k}^2} 
        \end{pmatrix}
        """
    )

    st.write(
        '''
        We scale down the **job skill requirements** by 0.45 to keep its values within 0 and 100, making
        it easier to interpret and compare across different jobs:
        '''
    )

    st.latex(
        '''
        0 \leq  \|s_{ik}\| \leq 100
        '''
    )

def UNIT2_3():

    st.markdown("<h3 style='color: #4CAF50;'>🚀 Practice 10 </h3>", unsafe_allow_html=True)
    st.sidebar.radio("Select a job at your firm:",("Senior management", "Support intellectuals and scientists, technicians and professionals", "Sales representatives and similar"))
    st.sidebar.write('Evaluate the job:')
    with st.sidebar.expander("Intellectual"):
        s11 = st.number_input("Demonstrating willigness to learn",key='s11',step=1.0)
        s21 = st.number_input("Collaborating in teams and networks",key='s21',step=1.0)
        s31 = st.number_input("Working efficiently",key='s31',step=1.0)
        s41 = st.number_input("Taking a proactive approach",key='s41',step=1.0)
    with st.sidebar.expander("Physical"):
        s12 = st.number_input("Demonstrating willigness to learn",key='s12',step=1.0)
        s22 = st.number_input("Collaborating in teams and networks",key='s22',step=1.0)
        s32 = st.number_input("Working efficiently",key='s32',step=1.0)
        s42 = st.number_input("Taking a proactive approach",key='s42',step=1.0)
    with st.sidebar.expander("Social"):
        s13 = st.number_input("Demonstrating willigness to learn",key='s13',step=1.0)
        s23 = st.number_input("Collaborating in teams and networks",key='s23',step=1.0)
        s33 = st.number_input("Working efficiently",key='s33',step=1.0)
        s43 = st.number_input("Taking a proactive approach",key='s43',step=1.0)
    with st.sidebar.expander("Use of methods"):
        s14 = st.number_input("Demonstrating willigness to learn",key='s14',step=1.0)
        s24 = st.number_input("Collaborating in teams and networks",key='s24',step=1.0)
        s34 = st.number_input("Working efficiently",key='s34',step=1.0)
        s44 = st.number_input("Taking a proactive approach",key='s44',step=1.0)
    with st.sidebar.expander("Use of technology"):
        s15 = st.number_input("Demonstrating willigness to learn",key='s15',step=1.0)
        s25 = st.number_input("Collaborating in teams and networks",key='s25',step=1.0)
        s35 = st.number_input("Working efficiently",key='s35',step=1.0)
        s45 = st.number_input("Taking a proactive approach",key='s45',step=1.0)

    matrix = np.array([
            [s11, s12, s13, s14, s15],
            [s21, s22, s23, s24, s25],
            [s31, s32, s33, s34, s35],
            [s41, s42, s43, s44, s45]
        ])
    
    if st.button("$J_k$ Job evaluation"):
        st.write(matrix)

    if st.button("$s_k$ Job skill requirements"):
        row_norms = 0.45 * np.linalg.norm(matrix, axis=1)
        for norm in row_norms:
            st.write(norm)

# Set page configuration
st.set_page_config(page_title="UNIT 2 Job Analysis and Design", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Tasks, skills, and jobs",'Job evaluation and job skill requirements','Practice 10% (accumulated)'],  # required
    icons=["book", "calculator", "person"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Tasks, skills, and jobs":
    UNIT2_1()
elif selected == "Job evaluation and job skill requirements":
    UNIT2_2()
elif selected == "Practice 10% (accumulated)":
    UNIT2_3()



