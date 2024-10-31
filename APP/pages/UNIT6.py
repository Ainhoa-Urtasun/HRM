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
        Consider the following cost of effort function:
        '''
    )

    st.latex(
            r'''
            C(e_i) = d(s_{(k)},s_i)e_i^2 \\[10pt]
            '''
        )

    st.write(
        '''
        where $e_i$ represents the effort exerted by employee $i$; $d(s_{(k)},s_i)$ is the Euclidean distance 
        between $s_{(k)}$, the vector of skill norms required by the job employee $i$ must perform, and the 
        vector of skills that employee $i$ actually possesses. The greater the distance, the higher the 
        cost of effort for the employee $i$. Remember, the vector of skill norms is derived from 
        the job evaluation process.
        
        On-the-job training aims to provide employees with the necessary 
        skills and competencies to complete tasks more efficiently, thereby reducing the cost of effort. 
        This reduction can enhance employee motivation, which in turn aligns with and positively impacts 
        the firm’s overall objectives.
        '''
    )

def UNIT6_2():

    st.write(
        """
        We use the **difference-in-differences (DiD) method** to evaluate the impact of training on the
        development of skill $s$.
        """
    )

    st.latex(
        r"""
        \text{DiD} = (S_{+1}^{\text{trained}} - S_{-1}^{\text{trained}}) - (S_{+1}^{\text{non-trained}} - S_{-1}^{\text{non-trained}})
        """
    )

    st.write(
        """
        Training occurs at time \(0\), so \(-1\) refers to the period before training, and \(+1\) refers to the period after training. 
        This technique makes two comparisons: (1) before vs. after training, and (2) trained vs. non-trained employees. 
        The combination of both comparisons offers a robust method to infer counterfactuals and determine causal effects.
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
        \text{CC} = S_{+1}^{\text{non-trained}} - S_{-1}^{\text{non-trained}}
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
        \text{CE} = S_{-1}^{\text{trained}} + (S_{+1}^{\text{non-trained}} - S_{-1}^{\text{non-trained}})
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
