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
        We use the **Difference-in-Differences (DiD) method** to evaluate the impact of 
        on-the-job training on the **average skill gap** $g$.
        """
    )

    st.latex(
        r"""
        \text{ATT} = (g_{+1}^{\text{trained}} - g_{-1}^{\text{trained}}) - (g_{+1}^{\text{non-trained}} - g_{-1}^{\text{non-trained}})
        """
    )

    st.write(
        """
        Here, **ATT** stands for the **Average Treatment Effect on the Treated**. This metric captures 
        the effect of training on employees who received it (trained group), 
        compared to a similar group that did not receive the training (non-trained group). 

        The Difference-in-Differences (DiD) method achieves this by making two key comparisons:
        
        - **Before and after training**: Training occurs at time 0, so −1 represents the period before training, and +1 represents the period after training.
        - **Trained versus non-trained employees**: $g^{trained}$ denotes the average skill gap of employees who received training,
        while $g^{non-trained}$ denotes the average skill gap of employees who did not.

        By combining these two comparisons, the DiD method helps estimate the causal impact of training on reducing the skill gap. 
        Note: The method is valid if the **parallel trends assumption** holds—that is, if the trained and non-trained groups 
        would have followed similar skill gap trends in the absence of training.
        """
    )

    st.write(
        """
        In DiD, we distinguish two key counterfactual outcomes:
        
        - **Counterfactual Skill Gap (CSG)**: This represents the skill gap the trained group 
        of employees would have experienced if they had not received the training.
        """
    )

    st.latex(
        r"""
        \text{CSG} = g_{+1}^{\text{non-trained}} - g_{-1}^{\text{non-trained}}
        """
    )

    st.write(
        """
        - **Counterfactual Skill Gap Change (CSGC)**: This represents how much the skill gap of the trained 
        group of employees would have changed if they hadn’t received training.
        """
    )

    st.latex(
        r"""
        \text{CSGC} = g_{-1}^{\text{trained}} + (g_{+1}^{\text{non-trained}} - g_{-1}^{\text{non-trained}})
        """
    )

    st.write(
        """
        The use of these counterfactuals allows us to isolate the causal impact of training by 
        estimating what would have happened in the absence of the intervention.
        """
    )

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.write('Training assessment:')
    with st.sidebar.expander("Trained Inputs"):
        gtbefore = st.text_input("$g_{-1}^{trained}$", key="gt0", step=1)
        gtafter = st.text_input("$g_{+1}^{trained}$", key="gt1", step=1)
    with st.sidebar.expander("Non-trained Inputs"):
        gnbefore = st.text_input("$g_{-1}^{non-trained}$", key="gn0", step=1)
        gnafter = st.text_input("$g_{+1}^{non-trained}$", key="gn1", step=1)
    fig = plt.figure(figsize=(5,5),dpi=100)
    plt.plot(['Before','After'],[gtbefore,gtafter],color='red',label='Trained')
    plt.plot(['Before','After'],[gnbefore,gnafter],color='blue',label='Non-trained')
    plt.plot(['Before','After'],[gtbefore,gtbefore+(gnafter-gnbefore)],color='blue',ls='-.',label='Counterfactual')
    plt.title('Skill gap')
    plt.legend()
    st.pyplot(fig)
  
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
