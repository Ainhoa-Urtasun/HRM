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
        Given the cost of effort for each employee:
        '''
    )

    st.latex(
        '''
        C(e_i) = (100-S_i)e_i^2
        '''
    )

    st.write(
        '''
        Where $e_i$ is the effort exerted by employee $i$ and $S_i$ represents a skill 
        or a combination of skills employee needs to possess. Training will target the 
        development of $S_i$.

        Employee $i$ exerts effort $e_i$ to successfuly carry out tasks. Effort includes factors such as time, 
        willingness, involvement, and character. 
        Effort is costly, but on-the-job training aims to provide employees with the necessary 
        skills and competencies to complete tasks more efficiently, thereby reducing the cost of effort. 
        This reduction can enhance employee motivation, which in turn aligns with and positively impacts 
        the firm’s overall objectives.
        '''
    )

def UNIT6_2():

    st.write(
        """
        We use the **difference-in-differences (DiD) method** to evaluate the impact of training on the
        development of skill $S$.
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
