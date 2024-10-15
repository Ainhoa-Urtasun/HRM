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
    st.title("Work Activities")
    st.write("""
        A **work activity** is an action performed by an employee that results in a specific output.
        Occupations are collections of work activities. O*NET identifies 41 distinct work activities,
        but for simplicity, we focus on 4: $A_1, A_2, A_3, A_4$
        """
    )

    st.components.v1.iframe("https://www.onetonline.org/find/descriptor/browse/4.A", width=800, height=1000, scrolling=True)

def UNIT2_3():
    st.title('Skills')
    st.write("""
    **Skill** is an ability or competence that an individual possesses. Employees use their skills to effectively perform work activities. 
    Skills themselves do not directly produce output; rather, they enable the completion of tasks. There are various classifications of skills. 
    Here, for simplicity, we focus on 6 skills: $S_1, S_2, S_3, S_4, S_5, S_6$
    """
    )

    st.components.v1.iframe("https://www.onetonline.org/find/descriptor/browse/2.B", width=800, height=1000, scrolling=True)

def UNIT2_4():
    st.title('Jobs and Job Evaluation')
    st.write(
    "In the context of job analysis and design, it is useful to represent a job as a matrix of work activities (rows) and basic skills (columns):"
    )

    st.latex(r"""
    J_i = 
    \begin{pmatrix}
    s_{11} & s_{12} & s_{13} & s_{14} & s_{15} & s_{16} \\
    s_{21} & s_{22} & s_{23} & s_{24} & s_{25} & s_{26} \\
    s_{31} & s_{32} & s_{33} & s_{34} & s_{35} & s_{36} \\
    s_{41} & s_{42} & s_{43} & s_{44} & s_{45} & s_{46} \\
    \end{pmatrix}
    """)

    st.write(
    "Each element $s_{ij}$ of the matrix indicates the extent to which basic skill $j$ is required for work activity $i$:"
    )

    st.latex(r"""
    0 \leq s_{ij} \leq 100
    """)

    st.write(
    "A job may not require all 10 work activities. If a job does not include a particular work activity, the corresponding row will be removed."
    )

    activities = [
    "A₁: Making decisions and solving problems",
    "A₂: Thinking creatively",
    "A₃: Controlling machines and processes",
    "A₄: Selling and Influencing Others"
    ]
    
    user_inputs = []
    for activity in activities:
        input_str = st.text_input(f"Enter (6 comma-separated) values for basic skills for {activity} (e.g., 10,20,30,40,50,60):")
        user_inputs.append(input_str)

    matrix = np.zeros((4, 6))

    if st.button("Submit"):
        try:
            matrix = [list(map(float, input_str.split(','))) for input_str in user_inputs]
            if all(len(row) == 6 for row in matrix) and len(matrix) == 4:
                matrix_np = np.array(matrix)
                st.write("Here is your 4x6 matrix:")
                st.write(matrix_np)
            else:
                st.error("Please ensure each input contains exactly 6 comma-separated numbers.")
        except ValueError:
            st.error("Invalid input. Please enter only numbers separated by commas.")

    st.write(
        "Job evaluation is a systematic process used to assess the relative worth of jobs within an organization. "
        "This assessment considers various job characteristics, such as responsibilities, required skills, and "
        "the complexity of the work activities involved. By conducting a job evaluation, organizations can "
        "establish equitable compensation structures and identify training and development needs."
    )

    st.write(
        "As an example of job evaluation, job complexity serves as a key metric in understanding the intricacies "
        "involved in different roles. Job complexity reflects the degree of difficulty associated with work "
        "activities and the range of skills necessary to perform them effectively. To quantify job complexity, "
        "we calculate the total skill requirements by summing all elements in the job matrix $J_i$:"
    )
    
    job_complexity = np.sum(matrix)
    st.write(f"Job Complexity: {job_complexity}")

def UNIT2_5():
    st.write("The cosine similarity between two work activities $A_i$ and $A_j$ is defined as follows:")

    st.latex(r'''
    \text{Cosine Similarity}(\text{A}_i, \text{A}_j) = \frac{\text{A}_i \cdot \text{A}_j}{\|\text{A}_i\| \|\text{A}_j\|}
    ''')

    st.write("Where:")
    st.write("- \( \text{WA}_i \cdot \text{WA}_j \) represents the dot product of the skill vectors for work activities \( \text{WA}_i \) and \( \text{WA}_j \), calculated as:")

    st.latex(r'''
    \text{A}_i \cdot \text{A}_j = \sum_{k=1}^{6} s_{ik} s_{jk}
    ''')

    st.write("- \( \|\text{WA}_i\| \) and \( \|\text{WA}_j\| \) denote the magnitudes of the skill vectors for work activities \( \text{WA}_i \) and \( \text{WA}_j \), calculated using:")

    st.latex(r'''
    \|\text{A}_i\| = \sqrt{\sum_{k=1}^{6} s_{ik}^2}
    ''')

   
st.set_page_config(page_title="UNIT2", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["O*NET", "Work Activities", "Basic Skills",'Jobs and Job Evaluation','Task Similarity'],  # required
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
elif selected == "Basic Skills":
    UNIT2_3()
elif selected == "Jobs and Job Evaluation":
    UNIT2_4()
elif selected == "Task Similarity":
    UNIT2_5()

