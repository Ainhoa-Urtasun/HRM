import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm

def UNIT2_1():
    
    st.write(
        """
        A **task**, denoted as $t_j$, is an action performed by an employee that results in a specific output.
        For simplicity, we assume any economic activity can be completed by carrying out the 5 core tasks listed in
        [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence): 
        
        - $t_1$: Intellectual
        - $t_2$: Physical
        - $t_3$: Social
        - $t_4$: Use of methods
        - $t_5$: Use of technology
        
        A **skill**, denoted as $s_i$, is an ability or competence that an individual possesses. Employees use their skills to effectively perform 
        tasks. Skills themselves do not directly produce output; rather, they enable the completion of tasks. 
        There are many classifications of skills. For simplicty, we focus only on the 4 
        most requested transversal skills and competences in online job ads in the EU27 in 2023
        [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence):

        - $s_1$: Demonstrating willingness to learn
        - $s_2$: Collaborating in teams and networks
        - $s_3$: Working efficiently
        - $s_4$: Taking a proactive approach

        A **job**, denoted as $J_{(k)}$, is a bundle of tasks ($t_1$: intellectual, $t_2$: physical,
        $t_3$: social, $t_4$: use of methods, and $t_5$: use of technology). To carry out each task,
        employees need to possess 
        multiple skills ($s_1$: demostrating willigness to learn, $s_2$: maintaining a postive attitude, 
        $s_3$: taking a proactive approach, and $s_4$: working efficiently). 
        
        """
    )
    
def UNIT2_2():

    st.write(
        '''
        **Job evaluation** is the process of assessing the relative worth of jobs within a firm.
        By evaluating jobs, firms can establish equitable compensation structures and identify training 
        and development needs. 

        To evaluate a job, we represent it as a **task-skill matrix**, where each column corresponds 
        to one of the five core tasks, and each row represents the extent to which one the four skills is required
        to perform each task within the job:
        '''
    )
             
    st.latex(
        r"""
        J_{(k)} = \begin{pmatrix}
        s_{11(k)} & s_{12(k)} & s_{13(k)} & s_{14(k)} & s_{15(k)} \\
        s_{21(k)} & s_{22(k)} & s_{23(k)} & s_{24(k)} & s_{25(k)} \\
        s_{31(k)} & s_{32(k)} & s_{33(k)} & s_{34(k)} & s_{35(k)} \\
        s_{41(k)} & s_{42(k)} & s_{43(k)} & s_{44(k)} & s_{45(k)} \\
        \end{pmatrix} \\[10pt]
        """
    )

    st.write(
        '''
        We restrict $s_{ij(k)}$ to the following values:
        '''
    )

    st.latex(r'0 \leq s_{ij(k)} \leq 100')

    st.write(
        '''
        A job doesn't necessarily entail all tasks. 
        If a job doesn't entail a particular task, 
        its corresponding column will be a vector of zeros.

        We can further summarize the information in the matrix by calculating the norm of each
        row-vector. The result, which we refer to as **skill-set of a job** provides a quantitative
        measure of the skill intensity required across tasks, offering another dimension for 
        job evaluation:
        '''
    )

    st.latex(r"""
    s_{(k)} = 0.45 \begin{pmatrix} 
    \|s_{1(k)}\| \\ 
    \|s_{2(k)}\| \\ 
    \|s_{3(k)}\| \\ 
    \|s_{4(k)}\| 
    \end{pmatrix} = 0.45 \begin{pmatrix} 
    \sqrt{s_{11(k)}^2 + s_{12(k)}^2 + s_{13(k)}^2 + s_{14(k)}^2 + s_{15(k)}^2} \\[10pt] 
    \sqrt{s_{21(k)}^2 + s_{22(k)}^2 + s_{23(k)}^2 + s_{24(k)}^2 + s_{25(k)}^2} \\[10pt] 
    \sqrt{s_{31(k)}^2 + s_{32(k)}^2 + s_{33(k)}^2 + s_{34(k)}^2 + s_{35(k)}^2} \\[10pt] 
    \sqrt{s_{41(k)}^2 + s_{42(k)}^2 + s_{43(k)}^2 + s_{44(k)}^2 + s_{45(k)}^2} 
    \end{pmatrix}
    """)

    st.write(
        '''
        We scale down the **skill-set of a job** by 0.45 to keep its values within 0 and 100, making
        it easier to interpret and compare across different jobs:
        '''
    )

    st.latex(
        '''
        0 \leq  \|s_{i(k)}\| \leq 100
        '''
    )

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.write(
        '''
        Use [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) to 
        represent one of the 3 jobs in your firm as matrix of tasks and skill requirements:
        '''
    )
    
    t1, t2, t3, t4, t5 = st.columns(5)
    with t1:
        s11 = st.number_input("$s_{11}$", key="s11",step=1)
        s21 = st.number_input("$s_{21}$", key="s21",step=1)
        s31 = st.number_input("$s_{31}$", key="s31",step=1)
        s41 = st.number_input("$s_{41}$", key="s41",step=1)
    with t2:
        s12 = st.number_input("$s_{12}$", key="s12",step=1)
        s22 = st.number_input("$s_{22}$", key="s22",step=1)
        s32 = st.number_input("$s_{32}$", key="s32",step=1)
        s42 = st.number_input("$s_{42}$", key="s42",step=1)
    with t3:
        s13 = st.number_input("$s_{13}$", key="s13",step=1)
        s23 = st.number_input("$s_{23}$", key="s23",step=1)
        s33 = st.number_input("$s_{33}$", key="s33",step=1)
        s43 = st.number_input("$s_{43}$", key="s43",step=1)
    with t4:
        s14 = st.number_input("$s_{14}$", key="s14",step=1)
        s24 = st.number_input("$s_{24}$", key="s24",step=1)
        s34 = st.number_input("$s_{34}$", key="s34",step=1)
        s44 = st.number_input("$s_{44}$", key="s44",step=1)
    with t5:
        s15 = st.number_input("$s_{15}$", key="s15",step=1)
        s25 = st.number_input("$s_{25}$", key="s25",step=1)
        s35 = st.number_input("$s_{35}$", key="s35",step=1)
        s45 = st.number_input("$s_{45}$", key="s45",step=1)
    
    if st.button("Skill-set of the job"):
        matrix = np.array([
            [s11, s12, s13, s14, s15],
            [s21, s22, s23, s24, s25],
            [s31, s32, s33, s34, s35],
            [s41, s42, s43, s44, s45]
        ])
    
        row_norms = 0.45 * np.linalg.norm(matrix, axis=1)
        for norm in row_norms:
            st.write(norm)

def UNIT2_3():
    st.write(
        '''
        The difference between two tasks $t_i$ and $t_j$, can be a useful HRM metric in job design, 
        helping the firm decide how to allocate tasks across jobs. This difference can be measured 
        by calculating the Euclidean distance of the skill-vectors for each task:
        '''
    )

    st.latex(r"""
    d(\mathbf{t}_i, \mathbf{t}_j) = \sqrt{(s_{1i} - s_{1j})^2 + (s_{2i} - s_{2j})^2 + (s_{3i} - s_{3j})^2 + (s_{4i} - s_{4j})^2}
    """)

    ti, tj = st.columns(2)
    with ti:
        s1i = st.number_input("$s_{1i}$", key="s1i",step=1)
        s2i = st.number_input("$s_{2i}$", key="s2i",step=1)
        s3i = st.number_input("$s_{3i}$", key="s3i",step=1)
        s4i = st.number_input("$s_{4i}$", key="s4i",step=1)
    with tj:
        s1j = st.number_input("$s_{1j}$", key="s1j",step=1)
        s2j = st.number_input("$s_{2j}$", key="s2j",step=1)
        s3j = st.number_input("$s_{3j}$", key="s3j",step=1)
        s4j = st.number_input("$s_{4j}$", key="s4j",step=1)
    
    if st.button("Task difference"):
        ti = np.array([
            [s1i],
            [s2i],
            [s3i],
            [s4i]
        ])
        tj = np.array([
            [s1j],
            [s2j],
            [s3j],
            [s4j]
        ])
        euclidean_distance = 0.45 * np.linalg.norm(ti - tj)
        st.write(euclidean_distance)

# Set page configuration
st.set_page_config(page_title="UNIT2", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Tasks, skills, and jobs",'Job evaluation','Task difference'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Tasks, skills, and jobs":
    UNIT2_1()
elif selected == "Job evaluation":
    UNIT2_2()
elif selected == "Task difference":
    UNIT2_3()



