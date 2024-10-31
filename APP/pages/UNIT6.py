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
        skills and competencies to complete tasks more efficiently. In other words, on-the-job training
        aims to improve the match between the employee $i$ and the job they perform. This match is measured by
        the Euclidean distance $d$, which on-the-job training seeks to reduce.
        By minimizing $d$, the cost of effort for the employee decreases, which can
        positively impact their motivation.
        '''
    )

def UNIT6_2():

    st.write(
        """
        We use the **difference-in-differences method** to evaluate the impact of training on $d$.
        """
    )

    st.latex(
        r"""
        \text{ATT} = (d_{+1}^{\text{trained}} - d_{-1}^{\text{trained}}) - (d_{+1}^{\text{non-trained}} - d_{-1}^{\text{non-trained}})
        """
    )

    st.write(
        """
        Where ATT stands for the Average Treatment Effect on the Treated. This metric represents the average effect of a treatment (or intervention) 
        on the group that actually received it, compared to a similar, untreated group. In DiD, ATT is especially valuable for assessing the impact of a policy or 
        intervention specifically on the population exposed to it, providing a clearer isolation of the effect within the treated group.

        In our case, on-the-job training serves as our treatment (or intervention). Training occurs at time 0, with −1 representing the period before training and 
        +1 the period after training. For accurate application of the DiD technique, we compare two employees with similar characteristics: 
        one who receives the training and one who does not. The Difference-in-Differences approach makes two primary comparisons: 
        (1) the periods before and after training, and (2) trained versus non-trained employees. 
        Combining these comparisons offers a robust method to infer counterfactuals and estimate causal effects accurately.
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
        \text{CC} = d_{+1}^{\text{non-trained}} - d_{-1}^{\text{non-trained}}
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
        \text{CE} = d_{-1}^{\text{trained}} + (d_{+1}^{\text{non-trained}} - d_{-1}^{\text{non-trained}})
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
