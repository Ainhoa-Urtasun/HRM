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
        '''
        Consider two employees, employee 1 and employee 2, competing for a prize $w$. The winner receives $w$, and the loser receives $-w$. 
        The probability of winning for Employee 1 is given by:
        '''
    )
    
    st.latex(
        r'''
        p_1 = \frac{e_1}{e_1 + e_2}
        '''
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


    
   
