import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT7_1():

    st.write(
        '''
        **Employment** refers to the number of employees, including both full-time and part-time workers. 
        **New hires** refers to the number of employees who have recently been recruited and started working at the firm.
        **Separations** refers to the number of employees who leave the firm, either voluntarily (quitting, retiring) 
        or involuntarily (layoffs, dismissals).

        We can also calculate the total employment of the firm at $(t-1)$ and at $(t)$ as well as
        its retention and turnover rates, which are critical HRM metrics.
        '''
    )

    st.latex(r'L_{(t-1)} = L_{1(t-1)}+ L_{2(t-1)} + L_{3(t-1)}')
    st.latex(r'L_{(t)} = L_{1(t)}+ L_{2(t)} + L_{3(t-1)}')
    st.latex(r'\text{Retention} = 100 \times \frac{m_{11(t-1,t)}+m_{22(t-1,t)}+m_{33(t-1,t)}}{L_{(t-1)}}')
    st.latex(r'\text{Turnover} = 100 - \text{Retention}')
    
def UNIT7_2():

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


st.set_page_config(page_title="UNIT7", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=['Turnover','Tournament model'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Turnover":
    UNIT7_1()
elif selected == "Tournament model":
    UNIT7_2()


    
   
