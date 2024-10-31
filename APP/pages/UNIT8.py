import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT8_1():

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
        - $w$ represents the rate of pay per unit of effort,
        - $e_i$ is the effort exerted by the employee,
        - $C(e_i)$ is the cost of effort, typically represented by $C(e_i) = d_i e_i^2$, where $d_i$ is a factor that increases with the difficulty of effort for the employee.

        To determine the optimal level of effort, the employee maximizes their utility by choosing $e_i$ such that the derivative of their utility with respect to effort is zero. 
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
        Substituting \( C(e_i) = d_i e_i^2 \):
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

    
def UNIT8_2():

    st.write(
        '''
        Consider two employees, employee 1 and employee 2, competing for a prize $w$. The winner receives $w$, and the loser receives $-w$. 
        The probability of winning for employee 1 and for employee 2 is given by, respectively:
        '''
    )
    
    st.latex(
        r'''
        p_1 = \frac{e_1}{e_1 + e_2}
        '''
    )

    st.latex(
        r'''
        p_2 = \frac{e_2}{e_1 + e_2}
        '''
    )

    st.write(
        '''
        The expected utility for each employee depends on their probability of winning, the prize, and the cost of effort. 
        Let \( C(e_i) = d_i e_i^2 \) represent the cost of effort for each employee.

        '''
    )


    st.latex(
        r'''
        U_1 = \frac{e_1}{e_1 + e_2} w - \frac{e_2}{e_1 + e_2} w - d_1 e_1^2 \\[10pt]
        U_2 = \frac{e_2}{e_1 + e_2} w - \frac{e_1}{e_1 + e_2} w - d_2 e_2^2
        '''
    )

    st.write(
        '''
        Each employee chooses their effort level to maximize their expected utility. We find the optimal effort levels by 
        taking the first-order conditions of their expected utility functions with respect to their efforts.
        '''
    )

    st.latex(
        r'''
        \frac{\partial U_1}{\partial e_1} = \frac{\partial}{\partial e_1} \left( \frac{e_1}{e_1 + e_2} w - \frac{e_2}{e_1 + e_2} w - d_1 e_1^2 \right) = 0 \\[10pt]
        \frac{\partial U_1}{\partial e_1} = \frac{w}{(e_1 + e_2)^2} e_2 - d_1 e_1 = 0 \\[10pt]
        \frac{\partial U_2}{\partial e_2} = \frac{\partial}{\partial e_2} \left( \frac{e_2}{e_1 + e_2} w - \frac{e_1}{e_1 + e_2} w - d_2 e_2^2 \right) = 0 \\[10pt]
        \frac{\partial U_2}{\partial e_2} = \frac{w}{(e_1 + e_2)^2} e_1 - d_2 e_2 = 0 \\[10pt]
        e_1^* = \frac{w}{d_1} \cdot \frac{e_2}{(e_1 + e_2)^2} \\[10pt]
        e_2^* = \frac{w}{d_2} \cdot \frac{e_1}{(e_1 + e_2)^2}
        '''
    )

st.set_page_config(page_title="UNIT8", layout="wide")

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
    UNIT8_1()
elif selected == "Employee ownership":
    UNIT8_2()
