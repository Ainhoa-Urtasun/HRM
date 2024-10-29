import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT6_1():

    st.write(
        '''
        When a firm needs new skills, it has two primary options: 
        it can acquire them from the labor market by hiring new workers, 
        or it can provide on-the-job training to its existing employees.

        Hiring brings in fresh expertise and potentially diverse perspectives, 
        while training incumbents can enhance skills without disrupting established 
        organizational knowledge and culture. Both approaches have trade-offs in cost, 
        time, and impact on the current workforce.
        '''
    )

def UNIT6_2():

    st.write(
        """
        Employees receive on-the-job training to improve their performance. 
        Training programs are designed to enhance employees' skills. By focusing on skill development, 
        HR managers ensure that employees acquire the necessary competencies to perform their tasks more efficiently 
        and contribute to the overall success of the organization.
        
        Employee $i$ exerts effort $e_i$ to successfuly carry out tasks. Effort includes factors such as time, 
        willingness, involvement, and character. 
        Effort is costly, but on-the-job training aims to provide employees with the necessary 
        skills and competencies to complete tasks more efficiently, thereby reducing the cost of effort. 
        This reduction can enhance employee motivation, which in turn aligns with and positively impacts 
        the firm’s overall objectives.
    
        We use the **difference-in-differences (DiD) method** to evaluate the impact of training:
        """
    )

    st.latex(r"""
    \text{DiD} = (e_{+1}^{\text{trained}} - e_{-1}^{\text{trained}}) - (e_{+1}^{\text{non-trained}} - e_{-1}^{\text{non-trained}})
    """)

st.write(
    r"""
    where \(e\) represents employee effort. Although we typically refer to effort at the employee-task level, \(e_{ij}\), we omit the subscript here for simplicity. Training occurs at time \(0\), so \(-1\) refers to the period before training, and \(+1\) refers to the period after training. This technique makes two comparisons: (1) before vs. after training, and (2) trained vs. non-trained employees. The combination of both comparisons offers a robust method to infer counterfactuals and determine causal effects.
    """
)

st.write("#### Counterfactual Outcomes")

st.write(
    """
    We distinguish two counterfactual outcomes:
    - **Counterfactual change (CC)**: What the trained employee's effort would have been if they hadn't received training:
    """
)

st.latex(r"""
\text{CC} = e_{+1}^{\text{non-trained}} - e_{-1}^{\text{non-trained}}
""")

st.write(
    """
    - **Counterfactual effort (CE)**: How much the trained employee's effort would have changed if they hadn't received training:
    """
)

st.latex(r"""
\text{CE} = e_{-1}^{\text{trained}} + (e_{+1}^{\text{non-trained}} - e_{-1}^{\text{non-trained}})
""")


st.set_page_config(page_title="UNIT6", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=['Skill improvement','Training evaluation'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Skill improvement":
    UNIT6_1()
elif selected == "Training evaluation":
    UNIT6_2()
