import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT6_1():

    st.write(
        '''
        Firms have two options for skill development (or upskilling): 
        
        1. Hiring new employees
        2. Training incumbent employees
        
        Upskilling may be necesary to adopt new technologies, such as 
        robots and artificial intelligence (AI).

        Here we focus on on-the-job training.
        '''
    )

    st.write(
        '''
        Consider the following **cost of effort** for the job candidate:
        '''
    )

    st.latex(
            r'''
            C(e_i) = g_i e_i^2 \\[10pt]
            '''
        )

    st.write(
        '''
        where $e_i$ represents the effort employee $i$ exerts; 
        $g_i$ is the **skill gap** of employee $i$ calculated as the Euclidean distance 
        between $s_{(k)}$, the **skill requirements** for the job, and $s_i$, the 
        **skill profile** of employee $i$. Remember, $s_{(k)}$ is derived from 
        the job evaluation process.
        
        On-the-job training aims to provide employees with the 
        skills and competencies needed to complete tasks more efficiently. In other words,     
        on-the-job training aims to reduce the skill gap $g_i$.
        By minimizing $g_i$, the cost of effort for the employee decreases, which can
        positively impact their motivation.
        '''
    )

def UNIT6_2():

    st.write(
        """
        We use the **difference-in-differences method** to evaluate the impact of training on $g_i$:
        """
    )

    st.latex(
        r"""
        \text{ATT} = (g_{+1}^{\text{trained}} - g_{-1}^{\text{trained}}) - (g_{+1}^{\text{non-trained}} - g_{-1}^{\text{non-trained}})
        """
    )

    st.write(
        """
        Where ATT stands for Average Treatment Effect on the Treated. This metric represents the average effect of a treatment (or intervention) 
        on the group that actually received it, compared to a similar, untreated group. ATT is especially valuable for assessing the impact of a policy or 
        intervention. We use ATT for assessing the impact of on-the-job training on employees. 

        The difference-in-differences method makes two comparisons: 
        (1) Before and after training: Training occurs at time 0, −1 refers to the before the training and 
        +1 after the training;
        (2) Trained versus non-trained employees: $g^{trained}$ refers to the average skill gap of a group of employees who received the training; and 
        $g^{non-trained}$ refers to the average skill gap of a group of employees who didn't receive any training.
        
        The combination of the two comparisons offers a robust method to infer counterfactuals and estimate 
        causal effects accurately. 
        """
    )

    st.write("#### Counterfactual Outcomes")

    st.write(
        """
        We distinguish two counterfactual outcomes:
        - **Counterfactual change (CC)**: What the trained employee's effort would have been if they hadn't received training:
        """
    )

    st.latex(
        r"""
        \text{CC} = g_{+1}^{\text{non-trained}} - g_{-1}^{\text{non-trained}}
        """
    )

    st.write(
        """
        - **Counterfactual effort (CE)**: How much the trained employee's effort would have 
        changed if they hadn't received training:
        """
    )

    st.latex(
        r"""
        \text{CE} = g_{-1}^{\text{trained}} + (g_{+1}^{\text{non-trained}} - g_{-1}^{\text{non-trained}})
        """
    )


st.set_page_config(page_title="UNIT6", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=['Skill development','Training evaluation'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Skill development":
    UNIT6_1()
elif selected == "Training evaluation":
    UNIT6_2()
