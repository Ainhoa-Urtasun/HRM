import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm

def UNIT2_1():
    st.write(
        """
        A **task** $t_j$ is an action performed by an employee that results in a specific output.
        [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) 
        identifies 5 pillar tasks: 
        
        - $t_1$: Intellectual
        - $t_2$: Physical
        - $t_3$: Social
        - $t_4$: Use of methods
        - $t_5$: Use of technology
        
        A **skill** $s_i$ is an ability or competence that an individual possesses. Employees use their skills to effectively perform 
        tasks. Skills themselves do not directly produce output; rather, they enable the completion of tasks. 
        There are many classifications of skills. 
        Here we consider the top 4 transversal skills and competences in 2023 in online job ads in the EU27 
        [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence):

        - $s_1$: Demonstrating willingness to learn
        - $s_2$: Maintaining a positive attitude
        - $s_3$: Taking a proactive approach
        - $s_4$: Working efficiently
        """
    )
    
def UNIT2_2():

    st.write(
        '''
        A job $J_{(k)}$ is a bundle of tasks. Each task requires an employee to posess
        multiple skills, so we represent each task as a column-vector of skills. Consequently, 
        a job can be represented as a matrix, where each column corresponds to a task and 
        each row represents the levels of a specific skill required to perform each 
        task within the job:
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
        Each element of the matrix $s_{ij(k)}$ represents the extent to which skill $s_i$ is required
        to perform $t_j$ in job $J_{(k)}$. We restrict $s_{ij(k)}$ to the following values:
        '''
    )

    st.latex(r'0 \leq s_{ij(k)} \leq 45')

    st.write(
        '''
        Each column of the matrix represents a task. A job doesn't necessarily entail all tasks. 
        If a job doesn't entail a particular task, 
        its corresponding column will be a vector of zeros. Each row in $J_{(k)}$ represents a
        specific skill.
        '''
    )

def UNIT2_3():

    st.write(
        '''
        Job evaluation is a systematic process used to assess the relative worth of jobs within a firm.
        By evaluating jobs, organizations can 
        establish equitable compensation structures and identify training and development needs. 
        
        Since a job is a bundle of tasks, and each task requires multiple skills, one approach to job evaluation 
        is to represent the job as a column-vector of skill norms, where each value represents
        the norm of the corresponding row in the job matrix:
        '''
    )

    st.latex(r"""
    s_{(k)} = 0.45 \begin{pmatrix} 
    \sqrt{s_{11(k)}^2 + s_{12(k)}^2 + s_{13(k)}^2 + s_{14(k)}^2 + s_{15(k)}^2} \\[10pt] 
    \sqrt{s_{21(k)}^2 + s_{22(k)}^2 + s_{23(k)}^2 + s_{24(k)}^2 + s_{25(k)}^2} \\[10pt] 
    \sqrt{s_{31(k)}^2 + s_{32(k)}^2 + s_{33(k)}^2 + s_{34(k)}^2 + s_{35(k)}^2} \\[10pt] 
    \sqrt{s_{41(k)}^2 + s_{42(k)}^2 + s_{43(k)}^2 + s_{44(k)}^2 + s_{45(k)}^2} 
    \end{pmatrix}
    """)

    st.write(
        '''
        We scale down the column-vector of skill norms by 0.45 so that:
        '''
    )

    st.latex(
        '''
        
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
    
    if st.button("Job evaluation"):
        matrix = np.array([
            [s11, s12, s13, s14, s15],
            [s21, s22, s23, s24, s25],
            [s31, s32, s33, s34, s35],
            [s41, s42, s43, s44, s45]
        ])
    
        row_norms = np.linalg.norm(matrix, axis=1)
        for norm in row_norms:
            st.write(norm)

def UNIT2_4():
    st.write(
        '''
        The difference between two tasks $t_i$ and $t_j$, can be a useful HRM metric in job design jobs, 
        helping the firm decide how to allocate tasks across jobs. This difference can be measured 
        by calculating the Euclidean distance of the skill-vectors for each task:
        '''
    )

    st.latex(r"""
    d(\mathbf{t}_i, \mathbf{t}_j) = \sqrt{(s_{1i} - s_{1j})^2 + (s_{2i} - s_{2j})^2 + (s_{3i} - s_{3j})^2 + (s_{4i} - s_{4j})^2}
    """)

    skills1 = st.text_input("Enter 4 numeric values for $t_i$ (comma-separated):")
    skills2 = st.text_input("Enter 4 numeric values for $t_j$ (comma-separated):")

    if st.button("Task difference"):
        try:
        # Check if inputs are provided
            if not skills1 or not skills2:
                st.write("Please provide values for both vectors.")
            else:
                # Convert inputs to float lists
                vector1 = np.array(list(map(float, skills1.split(','))))
                vector2 = np.array(list(map(float, skills2.split(','))))
            
                # Check if both vectors have exactly 4 values
                if len(vector1) == 4 and len(vector2) == 4:
                    # Calculate Euclidean distance
                    euclidean_distance = np.linalg.norm(vector1 - vector2)
                    st.write(euclidean_distance)
                else:
                    st.write("Please enter exactly 4 numeric values for each vector.")
        except ValueError:
            st.write("Please ensure all inputs are valid numeric values, separated by commas.")

# Set page configuration
st.set_page_config(page_title="UNIT2", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Tasks and skills",'Jobs','Job evaluation','Task difference'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Tasks and skills":
    UNIT2_1()
elif selected == "Jobs":
    UNIT2_2()
elif selected == 'Job evaluation':
    UNIT2_3()
elif selected == "Task difference":
    UNIT2_4()



