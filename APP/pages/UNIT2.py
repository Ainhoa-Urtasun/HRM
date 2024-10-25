import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm

def UNIT2_1():
    st.write(
        '''
       [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) by CEDEFOP is a useful resource for 
       job analysis and design in Europe. Both CEDEFOP 
       (European Centre for the Development of Vocational Training) and [ESCO](https://esco.ec.europa.eu/en) 
       (European Skills, Competences, Qualifications, and Occupations) are making progress toward
       becoming the European equivalent of O*NET (Occupational Information Network), 
       the U.S. system that provides detailed information on job tasks, skills, and qualifications across various occupations.
        '''
    )
    
def UNIT2_2():
    st.write("""
        A **task** is an action performed by an employee that results in a specific output.
        [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence/tasks-within-occupations?occupation=3.32&pillar=Intellectual#3) 
        identifies 5 pillar tasks: 
        
    - $T_1$ Intellectual
    - $T_2$ Physical
    - $T_3$ Social
    - $T_4$ Use of methods
    - $T_5$ Use of technology
        """
    )

def UNIT2_3():
    st.write("""
    A **skill** is an ability or competence that an individual possesses. Employees use their skills to effectively perform 
    tasks. Skills themselves do not directly produce output; rather, they enable the completion of tasks. 
    [ESCO](https://esco.ec.europa.eu/en) has many classifications of skills. Here we consider **self-management skills and competences**:

    - $S_1$ Demonstrating willingness to learn
    - $S_2$ Maintaining a positive attitude
    - $S_3$ Taking a proactive approach
    - $S_4$ Working efficiently
    """
    )

def UNIT2_4():
    st.write(
    "In the context of job analysis and design, it is useful to represent a task as a column-vector of skills:"
    )
    
    st.latex(
        r'''
        T_j  = 
        \begin{pmatrix}
        S_{1j} \\
        S_{2j} \\ 
        S_{3j} \\ 
        S_{4j} \\
        \end{pmatrix}
        '''
    )
    
    st.write(
    "Each element $S_{ij}$ of the column vector indicates the extent to which skill $S_i$ is required for task $T_j$:"
    )    
    
    st.latex(r"""
    0 \leq S_{ij} \leq 100
    """)
             
    st.write(
        '''
        A job can be represented as a matrix of tasks where each column-vector
        corresponds to a different task:
        '''
    )
             
    st.latex(r"""
    \begin{pmatrix}
    S_{11} & S_{12} & S_{13} & S_{14} & S_{15} \\
    S_{21} & S_{22} & S_{23} & S_{24} & S_{25} \\
    S_{31} & S_{32} & S_{33} & S_{34} & S_{35} \\
    S_{41} & S_{42} & S_{43} & S_{44} & S_{45} \\
    \end{pmatrix}
    """)

    st.write(
        '''
        Jobs don't entail all tasks. If a job doesn't entail a particular task, 
        its corresponding column will be a vector of zeros.
        '''
    )

    st.write(
        '''
        Job evaluation is a systematic process used to assess the relative worth of jobs within a firm.
        By evaluating jobs, organizations can 
        establish equitable compensation structures and identify training and development needs. 
        The following formula shows
        how to measure job complexity as an example of job evaluation.
        '''
    )

    st.latex(r'\text{Job complexity = } \sum_{j=1}^{5} (S_{1j} + S_{2j} + S_{3j} + S_{4j})')

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.write('Use [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) to represent a job you wish to post as a matrix of tasks and skill requirements')
    T1, T2, T3, T4, T5 = st.columns(5)
    with T1:
        S11 = st.number_input("$S_{11}$", key="S11")
        S21 = st.number_input("$S_{21}$", key="S21")
        S31 = st.number_input("$S_{31}$", key="S31")
        S41 = st.number_input("$S_{41}$", key="S41")
    with T2:
        S12 = st.number_input("$S_{12}$", key="S12")
        S22 = st.number_input("$S_{22}$", key="S22")
        S32 = st.number_input("$S_{32}$", key="S32")
        S42 = st.number_input("$S_{42}$", key="S42")
    with T3:
        S13 = st.number_input("$S_{13}$", key="S13")
        S23 = st.number_input("$S_{23}$", key="S23")
        S33 = st.number_input("$S_{33}$", key="S33")
        S43 = st.number_input("$S_{43}$", key="S43")
    with T4:
        S14 = st.number_input("$S_{13}$", key="S14")
        S24 = st.number_input("$S_{24}$", key="S24")
        S34 = st.number_input("$S_{34}$", key="S34")
        S44 = st.number_input("$S_{44}$", key="S44")
    with T5:
        S15 = st.number_input("$S_{15}$", key="S15")
        S25 = st.number_input("$S_{25}$", key="S25")
        S35 = st.number_input("$S_{35}$", key="S35")
        S45 = st.number_input("$S_{45}$", key="S45")
    
    if st.button("Submit"):
        matrix = np.array([
            [S11, S12, S13, S14, S15],
            [S21, S22, S23, S24, S25],
            [S31, S32, S33, S34, S35],
            [S41, S42, S43, S44, S45]
        ])
    
        job_complexity = np.sum(matrix)
        st.write(f"Job Complexity: {job_complexity}")

def UNIT2_5():
    st.write("The cosine similarity between two tasls $T_i$ and $T_j$ is defined as follows:")

    st.latex(r'''
    \text{Cosine Similarity}(\text{T}_i, \text{T}_j) = \frac{\text{T}_i \cdot \text{T}_j}{\|\text{T}_i\| \|\text{T}_j\|}
    ''')

    st.write("Where the numerator contains the dot product of the skill vectors:")
   
    st.latex(r'''
    \text{T}_i \cdot \text{T}_j = S_{i1} S_{j1} + S_{i2} S_{j2} + S_{i3} S_{j3} + S_{i4} S_{j4}
    ''')

    st.write("And the denominator contains the product of the magnitudes of the skill vectors:")

    st.latex(r'''
    \|\text{T}_i\| = \sqrt{S_{i1}^2 + S_{i2}^2 + S_{i3}^2 + S_{i4}^2}
    ''')

    skills1 = st.text_input("Enter 9 numeric values for $T_i$ (comma-separated):")
    skills2 = st.text_input("Enter 9 numeric values for $T_j$ (comma-separated):")

    if st.button("Calculate Cosine Similarity"):
        try:
            # Ensure inputs are provided
            if not skills1 or not skills2:
                st.write("Please provide values for both vectors.")
            else:
                # Convert input strings into lists of floats
                vector1 = list(map(float, skills1.split(',')))
                vector2 = list(map(float, skills2.split(',')))

                # Ensure both vectors have exactly 4 values
                if len(vector1) == 4 and len(vector2) == 4:
                    # Check for zero norm to avoid division by zero
                    if norm(vector1) == 0 or norm(vector2) == 0:
                        st.write("One of the vectors is zero, cannot calculate cosine similarity.")
                    else:
                        # Calculate cosine similarity
                        cosine_similarity = np.dot(vector1, vector2) / (norm(vector1) * norm(vector2))
                        st.write(f"Cosine similarity between the two vectors is: {cosine_similarity:.4f}")
                else:
                    st.write("Please enter exactly 4 numeric values for each vector.")
        except ValueError:
            st.write("Please ensure all inputs are valid numeric values, separated by commas.")


selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Skills intelligence by CEDEFOP", "Tasks", "Skills",'Jobs and Job Evaluation','Task Similarity'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Skills intelligence by CEDEFOP":
    UNIT2_1()
elif selected == "Tasks":
    UNIT2_2()
elif selected == "Skills":
    UNIT2_3()
elif selected == "Jobs and Job Evaluation":
    UNIT2_4()
elif selected == "Task Similarity":
    UNIT2_5()

