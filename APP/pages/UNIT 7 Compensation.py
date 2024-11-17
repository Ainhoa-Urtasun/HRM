import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT7_1():
    
    st.write(
        '''
        When an employee is compensated through pay-for-performance, her utility function is expressed as:
        '''
    )

    st.latex(
        r'''
        u_i = w e_i - C(e_i) = w e_i - g_i e_i^2
        '''
    )

    st.write(
        '''
        where:
        - $w$ is the pay rate per unit of effort
        - $e_i$ represents the effort (or work ethic) exerted by employee $i$
        - $g_i$ denotes the skill gap of employee $i$
        
        To maximize utility, the employee chooses an effort level such that the derivative of utility with respect to effort is zero:
        '''
    )

    st.latex(
        r'''
        \frac{\partial u_i}{\partial e_i} = w - \frac{\partial C(e_i)}{\partial e_i} = w - 2g_ie_i
        '''
    )

    st.write(
        '''
        Setting this derivative to zero to find the utility-maximizing effort level, we get:
        '''
    )

    st.latex(
        r'''
        w - 2 g_i e_i = 0
        '''
    )

    st.write(
        '''
        Solving for $e_i$, the employee's optimal effort is:
        '''
    )

    st.latex(
        r'''
        e_i^* = \frac{w}{2 g_i}
        '''
    )

    st.write(
        '''
        This result shows that the optimal effort level $e_i^*$ increases with the pay rate $w$ and decreases with the cost factor $g_i$. 
        In other words, a higher pay rate motivates more effort, whereas a higher cost of effort discourages it. This represents the supply of effort.
        '''
    )

    
def UNIT7_2():

    st.write(
        '''
        When an employee receives pay-for-performance with a share of the production output, their utility function includes both their base pay and a portion of the output they help produce.
        The utility function for an employee $i$ can be represented as:
        '''
    )

    st.latex(
        r'''
        u_i = w e_i + b Q - C(e_i) = w e_i + b Q - g_i e_i^2
        ''')

    st.write(
        '''
        where:
        - $w$ is the rate of pay per unit of effort
        - $e_i$ is the effort exerted by the employee
        - $b$ is the employee’s ownership share in the production output
        - $Q$ is the production function representing total output as a function of the efforts of all employees
        - $g_i$ denotes the skill gap of employee $i$

        To determine the optimal level of effort, the employee maximizes their utility by choosing $e_i$
        such that the derivative of their utility with respect to effort is zero. 
        This derivative gives us the **supply of effort** considering both the pay and ownership share.
        '''
    )

    st.write(
        '''
        Taking the derivative of the utility function with respect to effort $e_i$:
        '''
    )

    st.latex(
        r'''
        \frac{\partial u_i}{\partial e_i} = w + b \frac{\partial Q}{\partial e_i} - 2 g_i e_i
        '''
    )

    st.write(
        '''
        Substituting the expression of the output elasticity of effort:
        '''
    )

    st.latex(
        r'''
        \frac{\partial u_i}{\partial e_i} = w + b \alpha \frac{Q}{e_i} - 2 g_i e_i
        '''
    )

    st.write(
        '''
        Setting this expression to zero to maximize utility and solving for $e_i$:
        '''
    )

    st.latex(
        r'''
        e_i = \frac{w \pm \sqrt{w^2 + 8 g_i b \alpha Q}}{4 g_i}
        '''
    )

    st.write(
        '''
        This expression shows that the employee's optimal effort level $e_i^*$ depends not only on the pay rate $w$ but also on their ownership share $b$ 
        in the production function, encouraging higher effort levels as the share in output increases. 
        Conversely, a higher cost of effort $d_i$ discourages effort, balancing the incentives.
        '''
    )

st.set_page_config(page_title="UNIT 7 Compensation", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=['Pay-for-performance','Employee ownership','Practice 24'],  # required
    icons=["book", "book", "people"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Pay-for-performance":
    UNIT7_1()
elif selected == "Employee ownership":
    UNIT7_2()
elif selected == "Practice 24":
    UNIT7_3()
