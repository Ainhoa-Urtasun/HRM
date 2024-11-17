import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT8_1():

    st.write(
        '''
        Career development is an HRM practice that supports employees in achieving their career goals and advancing within
        the organization. It typically includes training, mentoring, succession planning, and providing growth opportunities
        such as promotions.

        Next we consider the tournament model to view career progression as a series of competitions
        where employees compete for limited promotions or rewards at higher levels.

        Rewards (e.g., salary increases, status, or power) increase with each level, incentivizing employees to
        compete for advacement.

        Employees at lower levels exert effort not only for their current compensation but also for the potential of winning the 
        'tournament' and attaining a promotion.
        
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

st.set_page_config(page_title="UNIT 8 Career Development", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=['Promotions','Tournament model'],  # required
    icons=["book","person"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Turnover":
    UNIT7_1()
elif selected == "Tournament model":
    UNIT7_2()


    
   
