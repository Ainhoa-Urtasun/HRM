import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm

def UNIT2_1():
    st.write(
        """
        A **task** is an action performed by an employee that results in a specific output.
        [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence/tasks-within-occupations?occupation=3.32&pillar=Intellectual#3) 
        identifies 5 pillar tasks: 
        
        - $t_1$ Intellectual
        - $t_2$ Physical
        - $t_3$ Social
        - $t_4$ Use of methods
        - $t_5$ Use of technology
        
        A **skill** is an ability or competence that an individual possesses. Employees use their skills to effectively perform 
        tasks. Skills themselves do not directly produce output; rather, they enable the completion of tasks. 
        There are many classifications of skills. 
        Here we consider **self-management skills and competences**:

        - $s_1$ Demonstrating willingness to learn
        - $s_2$ Maintaining a positive attitude
        - $s_3$ Taking a proactive approach
        - $s_4$ Working efficiently

        In the context of job analysis and design, it is useful to represent a task $t_j$ as a column-vector of skills:
        """
    )
    
    st.latex(
        r'''
        t_j  = 
        \begin{pmatrix}
        s_{1j} \\
        s_{2j} \\ 
        s_{3j} \\ 
        s_{4j} \\
        \end{pmatrix}
        '''
    )
    
    st.write(
        '''
        Each element $s_{ij}$ of the column vector indicates the extent 
        to which skill $s_i$ is required for task $t_j$:
        '''
    )    
    
def UNIT2_2():
    st.write(
        '''
        As a bundle of tasks, any job $J_k$ can be represented as a matrix of tasks where each column-vector
        corresponds to a different task:
        '''
    )
             
    st.latex(
        r"""
        J_k = \begin{pmatrix}
        s_{11(k)} & s_{12(k)} & s_{13(k)} & s_{14(k)} & s_{15(k)} \\
        s_{21(k)} & s_{22(k)} & s_{23(k)} & s_{24(k)} & s_{25(k)} \\
        s_{31(k)} & s_{32(k)} & s_{33(k)} & s_{34(k)} & s_{35(k)} \\
        s_{41(k)} & s_{42(k)} & s_{43(k)} & s_{44(k)} & s_{45(k)} \\
        \end{pmatrix} \\[10pt]
        """
    )

    st.write(
        '''
        Jobs don't entail all tasks. If a job doesn't entail a particular task, 
        its corresponding column will be a vector of zeros. Each row in $J_k$ correspond to 
        a particular skill so if we add up the values of a particular row, we get how much of
        a particular skill is required to successfully perform $J_k$, that we restrict to:
        '''
    )

    st.latex(
        '''
        0 \leq s_{i(k)} = \sum_j^5 s_{ij(k)} \leq 100 
        '''
    )

def UNIT2_3():

    st.write(
        '''
        Job evaluation is a systematic process used to assess the relative worth of jobs within a firm.
        By evaluating jobs, organizations can 
        establish equitable compensation structures and identify training and development needs. 
        The following formula shows
        how to evaluate job $J_k$:
        '''
    )

    st.latex(r'\text{s(k) = } \sum_{i=1}^{4} s_i(k)')

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.write('Use [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) to represent a job you wish to post as a matrix of tasks and skill requirements')
    
    t1, t2, t3, t4, t5 = st.columns(5)
    with t1:
        s11 = st.number_input("$s_{11}$", key="s11")
        s21 = st.number_input("$s_{21}$", key="s21")
        s31 = st.number_input("$s_{31}$", key="s31")
        s41 = st.number_input("$s_{41}$", key="s41")
    with t2:
        s12 = st.number_input("$s_{12}$", key="s12")
        s22 = st.number_input("$s_{22}$", key="s22")
        s32 = st.number_input("$s_{32}$", key="s32")
        s42 = st.number_input("$s_{42}$", key="s42")
    with t3:
        s13 = st.number_input("$s_{13}$", key="s13")
        s23 = st.number_input("$s_{23}$", key="s23")
        s33 = st.number_input("$s_{33}$", key="s33")
        s43 = st.number_input("$s_{43}$", key="s43")
    with t4:
        s14 = st.number_input("$s_{14}$", key="s14")
        s24 = st.number_input("$s_{24}$", key="s24")
        s34 = st.number_input("$s_{34}$", key="s34")
        s44 = st.number_input("$s_{44}$", key="s44")
    with t5:
        s15 = st.number_input("$s_{15}$", key="s15")
        s25 = st.number_input("$s_{25}$", key="s25")
        s35 = st.number_input("$s_{35}$", key="s35")
        s45 = st.number_input("$s_{45}$", key="s45")
    
    if st.button("Submit"):
        matrix = np.array([
            [s11, s12, s13, s14, s15],
            [s21, s22, s23, s24, s25],
            [s31, s32, s33, s34, s35],
            [s41, s42, s43, s44, s45]
        ])
    
        job_complexity = np.sum(matrix)
        st.write(f"Job Complexity: {job_complexity}")

def UNIT2_3():
    st.write("The cosine similarity between two tasks $t_i$ and $t_j$ is defined as follows:")

    st.latex(r'''
    \text{Cosine Similarity}(\text{t}_i, \text{t}_j) = \frac{\text{t}_i \cdot \text{t}_j}{\|\text{t}_i\| \|\text{t}_j\|}
    ''')

    st.write("Where the numerator contains the dot product of the skill vectors:")
   
    st.latex(r'''
    \text{t}_i \cdot \text{t}_j = s_{i1} s_{j1} + s_{i2} s_{j2} + s_{i3} s_{j3} + s_{i4} s_{j4}
    ''')

    st.write("And the denominator contains the product of the magnitudes of the skill vectors:")

    st.latex(r'''
    \|\text{t}_i\| = \sqrt{s_{i1}^2 + s_{i2}^2 + s_{i3}^2 + s_{i4}^2}
    ''')

    skills1 = st.text_input("Enter 4 numeric values for $t_i$ (comma-separated):")
    skills2 = st.text_input("Enter 4 numeric values for $t_j$ (comma-separated):")

    if st.button("Calculate Cosine Similarity"):
        try:
            if not skills1 or not skills2:
                st.write("Please provide values for both vectors.")
            else:
                vector1 = list(map(float, skills1.split(',')))
                vector2 = list(map(float, skills2.split(',')))

                if len(vector1) == 4 and len(vector2) == 4:
                    if norm(vector1) == 0 or norm(vector2) == 0:
                        st.write("One of the vectors is zero, cannot calculate cosine similarity.")
                    else:
                        cosine_similarity = np.dot(vector1, vector2) / (norm(vector1) * norm(vector2))
                        st.write(f"Cosine similarity between the two vectors is: {cosine_similarity:.4f}")
                else:
                    st.write("Please enter exactly 4 numeric values for each vector.")
        except ValueError:
            st.write("Please ensure all inputs are valid numeric values, separated by commas.")

# Set page configuration
st.set_page_config(page_title="UNIT2", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Tasks and skills",'Jobs and Job Evaluation','Task Similarity'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Tasks and skills":
    UNIT2_1()
elif selected == "Jobs and Job Evaluation":
    UNIT2_2()
elif selected == "Task Similarity":
    UNIT2_3()



