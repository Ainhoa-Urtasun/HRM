import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm

def UNIT2_1():
    st.write(
        '''
        O\\*NET Online is a comprehensive tool for career exploration and job analysis.
        It offers detailed descriptions of the tasks, skills, and other attributes required for more than 1,000 jobs,
        making it an invaluable resource for job seekers, workforce development professionals, and HR specialists.
        By providing standardized information on various job roles, O\\*NET Online facilitates job analysis and design,
        helping users understand the specific demands and characteristics of different occupations.
        '''
    )
    st.components.v1.iframe("https://www.onetonline.org/", width=800, height=1000, scrolling=True)
    
def UNIT2_2():
    st.write("""
        A **work activity** is an action performed by an employee that results in a specific output.
        O*NET identifies 41 distinct work activities. We consider, for simplicity, that the firm requires 
        its employees to perform 6 work activities: $W_1, W_2, W_3, W_4, W_5, W_6$. 
        In reality, of course, the number of work activities is much larger.
        """
    )

    st.write("Enter 6 work activities ($W_i$) from O*NET:")
    st.text_input("$W_1$")
    st.text_input("$W_2$")
    st.text_input("$W_3$")
    st.text_input("$W_4$")
    st.text_input("$W_5$")
    st.text_input("$W_6$")
    st.components.v1.iframe("https://www.onetonline.org/find/descriptor/browse/4.A", width=800, height=1000, scrolling=True)

def UNIT2_3():
    st.write("""
    **Skill** is an ability or competence that an individual possesses. Employees use their skills to effectively perform work activities. 
    Skills themselves do not directly produce output; rather, they enable the completion of tasks. There are various classifications of skills. 
    Here, for simplicity, we focus on 4 skills: $S_1, S_2, S_3, S_4$
    """
    )

    st.write("Enter 4 skills ($S_i$) from O*NET:")
    st.text_input("$S_1$")
    st.text_input("$S_2$")
    st.text_input("$S_3$")
    st.text_input("$S_4$")
    st.components.v1.iframe("https://www.onetonline.org/find/descriptor/browse/2.B", width=800, height=1000, scrolling=True)

def UNIT2_4():
    st.write(
    "In the context of job analysis and design, it is useful to represent a work activity as a vector of skills:"
    )
    
    st.latex(r'W_i = (s_{i1}, s_{i2}, s_{i3}, s_{i4})')

    st.write(
    "Each element $s_{ij}$ of the vector indicates the extent to which skill $j$ is required for work activity $i$:"
    )    
    
    st.latex(r"""
    0 \leq s_{ij} \leq 100
    """)
             
    st.write(
        '''
        A job is a matrix of work activities where each row corresponds to the skill vector of a particular work activity.
        '''
    )
             
    st.latex(r"""
    \begin{pmatrix}
    s_{11} & s_{12} & s_{13} & s_{14} \\
    s_{21} & s_{22} & s_{23} & s_{24} \\
    s_{31} & s_{32} & s_{33} & s_{34} \\
    s_{41} & s_{42} & s_{43} & s_{44} \\
    s_{51} & s_{52} & s_{53} & s_{54} \\
    s_{61} & s_{62} & s_{63} & s_{64} \\
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

    st.latex(r'\text{Job complexity: }\sum_{i=1}^{6} \sum_{j=1}^{4} s_{ij}')

    st.components.v1.iframe("https://www.onetonline.org/", width=800, height=1000, scrolling=True)

    st.write("From O\\*NET, type 6 different work activities and its corresponding sill vector:")
    activity1 = st.text_input("$W_1$")
    skills1 = st.text_input(f"Enter the 4-skill vector of $A_1$ (e.g., 10,20,30,40):")
    activity2 = st.text_input("$W_2$")
    skills2 = st.text_input(f"Enter the 4-skill vector of $A_2$ (e.g., 10,20,30,40):")
    activity3 = st.text_input("$W_3$")
    skills3 = st.text_input(f"Enter the 4-skill vector of $A_3$ (e.g., 10,20,30,40):")
    activity4 = st.text_input("$W_4$")
    skills4 = st.text_input(f"Enter the 4-skill vector of $A_4$ (e.g., 10,20,30,40):")
    activity5 = st.text_input("$W_5$")
    skills5 = st.text_input(f"Enter the 4-skill vector of $A_5$ (e.g., 10,20,30,40):")
    activity6 = st.text_input("$W_6$")
    skills6 = st.text_input(f"Enter the 4-skill vector of $A_6$ (e.g., 10,20,30,40):")

    matrix = np.zeros((6, 4))

    if st.button("Submit"):
        try:
            user_inputs = [skills1, skills2, skills3, skills4, skills5, skills6]
            matrix = [list(map(float, input_str.split(','))) for input_str in user_inputs]

            # Check if all rows have exactly 4 values and there are 6 rows
            if all(len(row) == 4 for row in matrix) and len(matrix) == 6:
                matrix_np = np.array(matrix)
                st.write("Here is your 6X4 matrix:")
                st.write(matrix_np)
            else:
                st.write("Please enter exactly 4 numeric values for each skill input.")
        except ValueError:
            st.write("Please enter valid numeric values for the skills.")
            
    job_complexity = np.sum(matrix)
    st.write(f"Job Complexity: {job_complexity}")

def UNIT2_5():
    st.write("The cosine similarity between two work activities $W_i$ and $W_j$ is defined as follows:")

    st.latex(r'''
    \text{Cosine Similarity}(\text{W}_i, \text{W}_j) = \frac{\text{W}_i \cdot \text{W}_j}{\|\text{W}_i\| \|\text{W}_j\|}
    ''')

    st.write("Where the numerator contains the dot product of the skill vectors:")
   
    st.latex(r'''
    \text{W}_i \cdot \text{W}_j = s_{i1} s_{j1} + s_{i2} s_{j2} + s_{i3} s_{j3} + s_{i4} s_{j4}
    ''')

    st.write("And the denominator contains the product of the magnitudes of the skill vectors:")

    st.latex(r'''
    \|\text{W}_i\| = \sqrt{s_{i1}^2 + s_{i2}^2 + s_{i3}^2 + s_{i4}^2}
    ''')

    skills1 = st.text_input("Enter 4 numeric values for Skill Vector 1 (comma-separated):")
    skills2 = st.text_input("Enter 4 numeric values for Skill Vector 2 (comma-separated):")

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
    options=["O*NET", "Work Activities", "Skills",'Jobs and Job Evaluation','Task Similarity'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "O*NET":
    UNIT2_1()
elif selected == "Work Activities":
    UNIT2_2()
elif selected == "Skills":
    UNIT2_3()
elif selected == "Jobs and Job Evaluation":
    UNIT2_4()
elif selected == "Task Similarity":
    UNIT2_5()

