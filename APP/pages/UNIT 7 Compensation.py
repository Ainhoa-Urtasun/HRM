import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT7_1():

    st.write(
        '''
        When an employee receives pay-for-performance, their utility looks as follows:
        '''
    )

    st.latex(r'''
        u_i = w \times e_i - C(e_i)
        ''')

    st.write(
        '''
        where:
        - $w$ represents the rate of pay per unit of effort
        - $e_i$ is the effort exerted by the employee
        - $C(e_i)$ is the cost of effort, represented by $C(e_i) = g_i e_i^2$, where $g_i$ is the skill gap of employee
        $i$ calculated as the Euclidean distance between $s_k$, the skill requirements for the job employee $i$ performs,
        and $s_i$, the skill profile of employee $i$
        
        To determine the optimal level of effort, the employee maximizes their utility by choosing $e_i$ 
        such that the derivative of their utility with respect to effort is zero. 
        This derivative gives us the employee's **supply of effort**.

        Taking the derivative of the utility function with respect to effort $e_i$:
        '''
    )

    st.latex(
        r'''
        \frac{\partial u_i}{\partial e_i} = w - \frac{\partial C(e_i)}{\partial e_i}
        '''
    )

    st.write(
        '''
        Substituting $C(e_i) = d_i e_i^2$:
        '''
    )

    st.latex(
        r'''
        \frac{\partial u_i}{\partial e_i} = w - 2 d_i e_i
        ''')

    st.write(
        '''
        Setting this derivative equal to zero to maximize utility, we get:
        '''
    )

    st.latex(r'''
        w - 2 d_i e_i = 0
        ''')

    st.write(
        '''
        Solving for $e_i$, the optimal supply of effort by the employee is:
        '''
    )

    st.latex(
        r'''
        e_i^* = \frac{w}{2 d_i}
        '''
    )

    st.write(
        '''
        This shows that the employee's optimal effort level $e_i^*$ increases with the rate of pay $w$ and decreases with the cost factor $d_i$. 
        In other words, a higher pay rate incentivizes more effort, while a higher cost of effort discourages it.
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
        u_i = w \times e_i + b \times f(e_1, e_2, \dots) - C(e_i)
        ''')

    st.write(
        '''
        where:
        - $w$ is the rate of pay per unit of effort,
        - $e_i$ is the effort exerted by the employee,
        - $b$ is the employee’s ownership share in the production output,
        - $f(e_1, e_2, \dots)$ is the production function representing total output as a function of the efforts of all employees,
        - $C(e_i)$ is the cost of effort, typically $C(e_i) = d_i e_i^2$, where $d_i$ reflects the costliness of exerting effort for the employee.

        To determine the optimal level of effort, the employee maximizes their utility by choosing \( e_i \) such that the derivative of their utility with respect to effort is zero. This derivative gives us the **supply of effort** considering both the pay and ownership share.
        '''
    )

    st.write(
        '''
        Taking the derivative of the utility function with respect to effort $e_i$:
        '''
    )

    st.latex(
        r'''
        \frac{\partial u_i}{\partial e_i} = w + b \times \frac{\partial f(e_1, e_2, \dots)}{\partial e_i} - \frac{\partial C(e_i)}{\partial e_i}
        ''')

    st.write(
        '''
        Substituting $C(e_i) = d_i e_i^2$:
        '''
    )

    st.latex(
        r'''
        \frac{\partial u_i}{\partial e_i} = w + b \times \frac{\partial f(e_1, e_2, \dots)}{\partial e_i} - 2 d_i e_i
        '''
    )

    st.write(
        '''
        Setting this derivative equal to zero to maximize utility, we get:
        '''
    )

    st.latex(
        r'''
        w + \alpha \frac{\partial f(e_1, e_2, \dots)}{\partial e_i} - 2 d_i e_i = 0
        '''
    )

    st.write(
        '''
        Solving for $e_i$, the optimal supply of effort by the employee is:
        '''
    )

    st.latex(
        r'''
        e_i^* = \frac{w + b \times \frac{\partial f(e_1, e_2, \dots)}{\partial e_i}}{2 d_i}
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
    options=['Pay-for-performance','Employee ownership'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Pay-for-performance":
    UNIT7_1()
elif selected == "Employee ownership":
    UNIT7_2()
