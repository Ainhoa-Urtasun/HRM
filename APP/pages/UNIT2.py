import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT2_1():
    st.title("O*NET")
    st.markdown(
        "[O*NET Online](https://www.onetonline.org/) is a comprehensive tool for career exploration and job analysis. "
        "It offers detailed descriptions of the tasks, skills, and other attributes required for more than 1,000 jobs, "
        "making it an invaluable resource for job seekers, workforce development professionals, and HR specialists. "
        "By providing standardized information on various job roles, O*NET Online facilitates job analysis and design, "
        "helping users understand the specific demands and characteristics of different occupations."
    )

def UNIT2_2():
    st.title("Work Activities")
    st.write(
        "A **work activity** is an action performed by an individual that results in a specific output. "
        "Jobs are collections of work activities. Every firm transforms inputs into outputs (goods and services). "
        "The nature of these outputs determines both the industry classification of the firm and the work activities its employees must perform. "
        "This highlights the importance of understanding industry classifications. O*NET identifies 41 distinct work activities, "
        "but for simplicity, we focus on 4 working activities:"
    )

    activities = {
    "A1": "A₁: Making decisions and solving problems",
    "A2": "A₂: Thinking creatively",
    "A3": "A₃: Controlling machines and processes",
    "A4": "A₄: Selling and Influencing Others"
    }

    selected_activity = st.selectbox("Select a Work Activity:", list(activities.values()))

def UNIT2_3():
    st.title('Basic Skills')
    st.write("""
    **Skill** is an ability or competence that an individual possesses. Employees use their skills to effectively perform work activities. 
    Skills themselves do not directly produce output; rather, they enable the completion of tasks. There are various classifications of skills. 
    Here, we focus on basic skills as defined by O*NET. Basic skills are developed capacities that facilitate learning and the rapid acquisition of knowledge.
    """)

    skills = {
    "S1": "S₁: Active listening",
    "S2": "S₂: Mathematics",
    "S3": "S₃: Reading comprehension",
    "S4": "S₄: Science",
    "S5": "S₅: Speaking",
    "S6": "S₆: Writing",
    }

    selected_skill = st.selectbox("Select a Basic Skill:", list(skills.values()))

def UNIT2_4():
    st.title('Jobs')
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


st.set_page_config(page_title="UNIT2", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["O*NET", "Work Activities", "Basic Skills",'Jobs'],  # required
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
elif selected == "Jobs":
    UNIT2_4()

