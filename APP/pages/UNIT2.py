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
       job analysis and design in Europe. CEDEFOP 
       (European Centre for the Development of Vocational Training) and ESCO 
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
    **Skill** is an ability or competence that an individual possesses. Employees use their skills to effectively perform 
    tasks. Skills themselves do not directly produce output; rather, they enable the completion of tasks. 
    [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence/trend-focus/skills-online-job-advertisements?year=2023&country=EU27_2020#3)
    identifies 9 transversal skills and competences as the most requested skills in online job ads in EU27:

    - $S_1$ Demonstrating willigness to learn
    - $S_2$ Collaborating in teams and networks
    - $S_3$ Working efficiently
    - $S_4$ Taking a proactive approach
    - $S_5$ Supporting others
    - $S_6$ Thinking creatively and innovatively
    - $S_7$ Leading others
    - $S_8$ Maintaining a positive attitude
    - $S_9$ Processing information, ideas and concepts
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
        S_{5j} \\
        S_{6j} \\
        S_{7j} \\
        S_{8j} \\
        S_{9j} \\
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
    S_{51} & S_{52} & S_{53} & S_{54} & S_{55} \\
    S_{61} & S_{62} & S_{63} & S_{64} & S_{65} \\
    S_{71} & S_{72} & S_{73} & S_{74} & S_{75} \\
    S_{81} & S_{82} & S_{83} & S_{84} & S_{85} \\
    S_{91} & S_{92} & S_{93} & S_{94} & S_{95} \\
    \end{pmatrix}
    """)

    st.write(
        '''
        If a job doesn't entail a particular work activity, 
        the corresponding row will be a vector of zeros.
        '''
    )

    st.write(
        '''
        Job evaluation is a systematic process used to assess the relative worth of jobs within a firm.
        This assessment considers various job characteristics, such as responsibilities, required skills, and 
        the complexity of the work activities involved. By conducting a job evaluation, organizations can 
        establish equitable compensation structures and identify training and development needs. The following formula shows
        how to measure job complexity as an example of job evaluation.
        '''
    )

    st.latex(r'\text{Job complexity = } \sum_{j=1}^{5} (S_{1j} + S_{2j} + S_{3j} + S_{4j} + S_{5j} + S_{6j} + S_{7j} + S_{8j} + S_{9j})')
    
    st.write('Use [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) to represent a job as a matrix of tasks and skill requirements')
    T1, T2, T3, T4, T5 = st.columns(5)
    with T1:
        S11 = st.number_input("$S_{11}$", key="S11")
        S21 = st.number_input("$S_{21}$", key="S21")
        S31 = st.number_input("$S_{31}$", key="S31")
        S41 = st.number_input("$S_{41}$", key="S41")
        S51 = st.number_input("$S_{51}$", key="S51")
        S61 = st.number_input("$S_{61}$", key="S61")
        S71 = st.number_input("$S_{71}$", key="S71")
        S81 = st.number_input("$S_{81}$", key="S81")
        S91 = st.number_input("$S_{91}$", key="S91")
    with T2:
        S12 = st.number_input("$S_{12}$", key="S12")
        S22 = st.number_input("$S_{22}$", key="S22")
        S32 = st.number_input("$S_{32}$", key="S32")
        S42 = st.number_input("$S_{42}$", key="S42")
        S52 = st.number_input("$S_{52}$", key="S52")
        S62 = st.number_input("$S_{62}$", key="S62")
        S72 = st.number_input("$S_{72}$", key="S72")
        S82 = st.number_input("$S_{82}$", key="S82")
        S92 = st.number_input("$S_{92}$", key="S92")
    with T3:
        S13 = st.number_input("$S_{13}$", key="S13")
        S23 = st.number_input("$S_{23}$", key="S23")
        S33 = st.number_input("$S_{33}$", key="S33")
        S43 = st.number_input("$S_{43}$", key="S43")
        S53 = st.number_input("$S_{53}$", key="S53")
        S63 = st.number_input("$S_{63}$", key="S63")
        S73 = st.number_input("$S_{73}$", key="S73")
        S83 = st.number_input("$S_{83}$", key="S83")
        S93 = st.number_input("$S_{93}$", key="S93")
    with t4:
        S14 = st.number_input("$S_{13}$", key="S14")
        S24 = st.number_input("$S_{24}$", key="S24")
        S34 = st.number_input("$S_{34}$", key="S34")
        S44 = st.number_input("$S_{44}$", key="S44")
        S54 = st.number_input("$S_{54}$", key="S54")
        S64 = st.number_input("$S_{64}$", key="S64")
        S74 = st.number_input("$S_{74}$", key="S74")
        S84 = st.number_input("$S_{84}$", key="S84")
        S94 = st.number_input("$S_{94}$", key="S94")
    with T5:
        S15 = st.number_input("$S_{15}$", key="S15")
        S25 = st.number_input("$S_{25}$", key="S25")
        S35 = st.number_input("$S_{35}$", key="S35")
        S45 = st.number_input("$S_{45}$", key="S45")
        S55 = st.number_input("$S_{55}$", key="S55")
        S65 = st.number_input("$S_{65}$", key="S65")
        S75 = st.number_input("$S_{75}$", key="S75")
        S85 = st.number_input("$S_{85}$", key="S85")
        S95 = st.number_input("$S_{95}$", key="S95")
    
    if st.button("Submit"):
        matrix = np.array([
            [S11, S12, S13, S14, S15],
            [S21, S22, S23, S24, S25],
            [S31, S32, S33, S34, S35],
            [S41, S42, S43, S44, S45],
            [S51, S52, S53, S54, S55],
            [S61, S62, S63, S64, S65],
            [S71, S72, S73, S74, S75],
            [S81, S82, S83, S84, S85],
            [S91, S92, S93, S94, S95]
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
    \text{T}_i \cdot \text{T}_j = S_{i1} S_{j1} + S_{i2} S_{j2} + S_{i3} S_{j3} + S_{i4} S_{j4} + S_{i5} S_{j5} +S_{i6} S_{j6}
    + S_{i7} S_{j7} + S_{i8} S_{j8} + S_{i9} S_{j9}
    ''')

    st.write("And the denominator contains the product of the magnitudes of the skill vectors:")

    st.latex(r'''
    \|\text{T}_i\| = \sqrt{S_{i1}^2 + S_{i2}^2 + S_{i3}^2 + S_{i4}^2 + S_{i5}^2 + S_{i6}^2 + S_{i7}^2 + S_{i8}^2 + S_{i9}^2 +}
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

