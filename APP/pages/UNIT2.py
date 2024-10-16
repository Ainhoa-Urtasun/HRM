import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT2_1():
    st.components.v1.iframe("https://www.onetonline.org/", width=800, height=1000, scrolling=True)
    
    st.write(
        "O\\*NET Online is a comprehensive tool for career exploration and job analysis. "
        "It offers detailed descriptions of the tasks, skills, and other attributes required for more than 1,000 jobs, "
        "making it an invaluable resource for job seekers, workforce development professionals, and HR specialists. "
        "By providing standardized information on various job roles, O\\*NET Online facilitates job analysis and design, "
        "helping users understand the specific demands and characteristics of different occupations."
    )

def UNIT2_2():
    st.write("""
        A **work activity** is an action performed by an employee that results in a specific output.
        O*NET identifies 41 distinct work activities. We consider, for simplicity, that the firm requires 
        its employees to perform 4 work activities: $A_1, A_2, A_3, A_4$. 
        In reality, of course, the number of work activities is much larger.
        """
    )

    st.write("Enter 4 work activities ($A_i$) from O*NET:")
    st.text_input("$A_1$")
    st.text_input("$A_2$")
    st.text_input("$A_3$")
    st.text_input("$A_4$")
    st.components.v1.iframe("https://www.onetonline.org/find/descriptor/browse/4.A", width=800, height=1000, scrolling=True)

def UNIT2_3():
    st.write("""
    **Skill** is an ability or competence that an individual possesses. Employees use their skills to effectively perform work activities. 
    Skills themselves do not directly produce output; rather, they enable the completion of tasks. There are various classifications of skills. 
    Here, for simplicity, we focus on 6 skills: $S_1, S_2, S_3, S_4, S_5, S_6$
    """
    )

    st.write("Enter 6 skills ($S_i$) from O*NET:")
    st.text_input("$S_1$")
    st.text_input("$S_2$")
    st.text_input("$S_3$")
    st.text_input("$S_4$")
    st.text_input("$S_5$")
    st.text_input("$S_6$")
    st.components.v1.iframe("https://www.onetonline.org/find/descriptor/browse/2.B", width=800, height=1000, scrolling=True)

def UNIT2_4():
    st.write(
    "In the context of job analysis and design, it is useful to represent a work activity as a vector of skills:"
    )
    
    st.latex(r'A_i = (s_{i1}, s_{i2}, s_{i3}, s_{i4}, s_{i5}, s_{i6})')

    st.write(
    "Each element $s_{ij}$ of the vector indicates the extent to which skill $j$ is required for work activity $i$:"
    )    
    
    st.latex(r"""
    0 \leq s_{ij} \leq 100
    """)
             
    st.write(
        '''
        Since a job is a bundle of work activities, 
        we can represent it as a matrix where each row corresponds to the skill vector required for a particular work activity.
        '''
    )
             
    st.latex(r"""
    \begin{pmatrix}
    s_{11} & s_{12} & s_{13} & s_{14} & s_{15} & s_{16} \\
    s_{21} & s_{22} & s_{23} & s_{24} & s_{25} & s_{26} \\
    s_{31} & s_{32} & s_{33} & s_{34} & s_{35} & s_{36} \\
    s_{41} & s_{42} & s_{43} & s_{44} & s_{45} & s_{46} \\
    \end{pmatrix}
    """)

    st.write(
        '''
        A job may not require all 4 work activities. If a job does not include a particular work activity, 
        the corresponding row will be a vector of zeros.
        '''
    )

    st.write(
        '''
        Job evaluation is a systematic process used to assess the relative worth of jobs within an organization.
        This assessment considers various job characteristics, such as responsibilities, required skills, and 
        the complexity of the work activities involved. By conducting a job evaluation, organizations can 
        establish equitable compensation structures and identify training and development needs. The following formula shows
        how to measure job complexity as an example of job evaluation.
        '''
    )

    st.latex(r'\text{Job complexity: }\sum_{i=1}^{4} \sum_{j=1}^{6} s_{ij}')

    st.write("Enter 4 work activities ($A_i$) and 6 skills ($S_i$) from O*NET:")
    activity1 = st.text_input("$A_1$")
    skills1 = st.text_input(f"Enter the importance (0-100) of the 6 skills for $A_1$ (e.g., 10,20,30,40,50,60):")
    activity2 = st.text_input("$A_2$")
    skills2 = st.text_input(f"Enter the importance (0-100) of the 6 skills for $A_2$ (e.g., 10,20,30,40,50,60):")
    activity3 = st.text_input("$A_3$")
    skills3 = st.text_input(f"Enter the importance (0-100) of the 6 skills for $A_3$ (e.g., 10,20,30,40,50,60):")
    activity4 = st.text_input("$A_4$")
    skills4 = st.text_input(f"Enter the importance (0-100) of the 6 skills for $A_4$ (e.g., 10,20,30,40,50,60):")

    matrix = np.zeros((4, 6))

    if st.button("Submit"):
        try:
            user_inputs = [skills1, skills2, skills3, skills4]
            matrix = [list(map(float, input_str.split(','))) for input_str in user_inputs]
            if all(len(row) == 6 for row in matrix) and len(matrix) == 4:
                matrix_np = np.array(matrix)
                st.write("Here is your 4x6 matrix:")
                st.write(matrix_np)
            else:
                st.write("Please enter exactly 6 values for each activity.")
        except ValueError:
            st.write("Please enter valid numeric values for the skills.")
    
    job_complexity = np.sum(matrix)
    st.write(f"Job Complexity: {job_complexity}")

def UNIT2_5():
    st.write("The cosine similarity between two work activities $A_i$ and $A_j$ is defined as follows:")

    st.latex(r'''
    \text{Cosine Similarity}(\text{A}_i, \text{A}_j) = \frac{\text{A}_i \cdot \text{A}_j}{\|\text{A}_i\| \|\text{A}_j\|}
    ''')

    st.write("Where the numerator represents the dot product of the skill vectors for work activities $A_i$ and $A_j$, calculated as:")
   
    st.latex(r'''
    \text{A}_i \cdot \text{A}_j = \sum_{k=1}^{6} s_{ik} s_{jk}
    ''')

    st.write("And the denominator contains the product of the magnitudes of the skill vectors for work activities $A_i$ and $A_j$, calculated as:")

    st.latex(r'''
    \|\text{A}_i\| = \sqrt{\sum_{k=1}^{6} s_{ik}^2}
    ''')

   
st.set_page_config(page_title="UNIT2", layout="wide")

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

