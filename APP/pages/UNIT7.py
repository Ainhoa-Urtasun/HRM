import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT7_1():

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
    UNIT6_1()
elif selected == "Tournament model":
    UNIT6_2()



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
    
    st.write(
        """Both labor productivity and ULC significantly impact a firm's profitability, 
        particularly in terms of Earnings Before Interest and Taxes (EBIT). 
        Firms often make decisions aimed at maximizing profits, 
        which is the focus of this section:
        """
    )
    st.latex(r'''
        EBIT = p\left(L_{1}^{e_{1}} \cdot L_{2}^{e_{2}} \cdot L_{3}^{e_{3}} \cdot K^{1-e_{1}+e_{2}-e_{3}}\right) - \left(w_{1} L_{1} + w_{2} L_{2} + w_{3} L_{3}\right) - rK
    ''')
    
    st.write("Where:")
    st.write("- $p$ is the price of the output")
    st.write("- $w_{1} L_{1} + w_{2} L_{2} + w_{3} L_{3}$ represents cost of employees")
    st.write("- $rK$ represents depreciation")

    st.write(
        "The objective is to determine the optimal values of $(L_{1}, L_{2}, L_{3})$ that maximize EBIT. "
        "We can apply gradient ascent to iteratively update the input values, moving in the direction of the gradient. "
        "The gradient indicates the direction that maximizes the objective function:"
    )
    st.latex(r'''
        (L_{1}, L_{2}, L_{3})_{\text{new}} = (L_{1}, L_{2}, L_{3})_{\text{old}} + \eta \cdot \nabla EBIT
    ''')

    st.write("Where:")
    st.write("- $\\eta$ is the learning rate (which determines the size of the steps),")
    st.write("- $\\nabla EBIT$ is the gradient of the EBIT function with respect to $(L_{1}, L_{2}, L_{3})$, defined as:")

    st.latex(r'''
    \nabla EBIT = \left( \frac{\partial EBIT}{\partial L_{1}}, \frac{\partial EBIT}{\partial L_{2}}, \frac{\partial EBIT}{\partial L_{3}} \right)
    ''')

    st.write("By calculating the gradient and updating the input values iteratively, we aim to find the optimal combination "
             "of labor and capital that maximizes EBIT, enhancing overall firm profitability.")

    L1 = st.number_input("Supply of employees in job $J_1$ at the firm", value=1, step=1)
    L2 = st.number_input("Supply of employees in job $J_2$ at the firm", value=1, step=1)
    L3 = st.number_input("Supply of employees in job $J_3$ at the firm", value=1, step=1)

    def EBIT(L1, L2, L3):
        return 120 * L1**0.2 * L2**0.5 * L3**0.1 - 5 * (L1 + L2 + L3) - 1

    def gradient_L1(L1, L2, L3):
        return 120 * 0.2 * L1**(-0.8) * L2**0.5 * L3**0.1  - 5

    def gradient_L2(L1, L2, L3):
        return 120 * 0.5 * L1**0.2 * L2**(-0.5) * L3**0.1 - 5

    def gradient_L3(L1, L2, L3):
        return 120 * 0.1 * L1**0.2 * L2**0.5 * L3**(-0.9) - 5

    initial_EBIT = EBIT(L1, L2, L3)
    st.markdown(f"<h3 style='text-align: center; color: #FF5733;'>Starting EBIT: {initial_EBIT:.2f}€</h3>", unsafe_allow_html=True)

    if st.button("First iteration"):
        L1_new = L1 + 0.02 * gradient_L1(L1, L2, L3)
        L2_new = L2 + 0.02 * gradient_L2(L1, L2, L3)
        L3_new = L3 + 0.02 * gradient_L3(L1, L2, L3)

        L1_new = round(L1_new)
        L2_new = round(L2_new)
        L3_new = round(L3_new)

        if L1_new <= 0 or L2_new <= 0 or L3_new <= 0:
            st.error("The updated values of L1, L2, and L3 must be positive. Please adjust the initial values or the learning rate.")
        else:
            new_value = EBIT(L1_new, L2_new, L3_new)
            result = pd.DataFrame({
                "Demand of employees in job $J_1$ at the firm": [L1_new],
                "Demand of employees in job $J_2$ at the firm": [L2_new],
                "Demand of employees in job $J_3$ at the firm": [L3_new],
                "EBIT": [new_value]
            })
            st.markdown(f"<h3 style='text-align: center; color: #4CAF50;'>Updated Values After First Iteration</h3>", unsafe_allow_html=True)
            st.table(result)
