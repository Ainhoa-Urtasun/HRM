import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT4_1():

    st.write(
        '''
        Performance evaluation refers to assessing how well employees perform within the firm. 
        Performance can be evaluated on average or for each specific employee, with the latter being more challenging 
        but also more meaningful.

        A typical average performance metric is labor productivity.
        '''
    )

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.text_input("Write here the labor productivity of your firm using the latest information provided by [SABI](https://www.unavarra.es/biblioteca?languageId=1):")

def UNIT4_2():
    
    st.write(
        '''
        A more meaningful but also more challenging way to evaluate performance is to assess 
        how well each employee performs within the firm. If done properly, 
        this allows the firm to understand each employee's contribution to its value 
        and to motivate them to improve their performance.

        Nex, we present several alternative metrics for evaluating employee performance. 

        '''
    )

def UNIT4_3():

    st.write(
        '''
        **Output elasticity of effort** indicates the percentage change in the output the firm produces when employee
        $i$ exerts 1% more effort.
    
    st.latex(
         r'''
        Q = f(e_1, e_2, \dots, e_i, \dots, e_L)
        e_i \geq 0
        \alpha_i = \frac{\partial f(e_1, e_2, \dots, e_i, \dots, e_L)}{\partial e_i} \cdot \frac{e_i}{f(e_1, e_2, \dots, e_i, \dots, e_L)}
        '''
    )

    st.write(
        '''
        In any case, employee's effort is challenging to assess. To explain why, we first need to clarify 
        what it means. By effort, we refer to an employee's willingness to make meaningful 
        contributions to the firm. While it could include the number of working hours, it also encompasses 
        possessing the necessary skills and motivation to perform tasks effectively. 
        One proxy for employee effort could be absenteeism. For each employee, we can calculate 
        absenteeism as the ratio of the number of days absent from work to the total number of workdays.
        '''
    )

    st.write(
        '''
        Another proxy for evaluating employee's effort is the employee cost of effort function. We consider the following
        cost of effort function:
        '''
    )

    st.latex(
            r'''
            C(e_i) = (100-S_i)e_i^2
            '''
        )

    st.write(
        '''
        where $S_i$ represents the most requested transversal skill in online job ads within the EU27: 
        'Demonstrating willingness to learn.'
        '''
    )

    st.latex(
        r"""
        0 \leq S_{i} \leq 100
        """
    )

    st.write(
        '''
        Thus, the lower the willingness to learn, the higher the employee's cost of effort.
        '''
    )

    st.write(
        '''
        We can analyze its properties by calculating its derivatives. Taking the first derivative with 
        respect to effort $e_i$:
        '''
    )

    st.latex(
        r'''
        C'(e_i) = \frac{d}{de_i} \left[(100 - S_i)e_i^2\right] = 2(100 - S_i)e_i
        '''
    )

    st.write(
        '''
        This first derivative shows the marginal cost of effort. Since $(100 - S_i)$ is a positive constant, 
        the marginal cost of effort increases linearly with $e_i$.

        The second derivative with respect to $e_i$ is:
        '''
    )

    st.latex(
        r'''
        C''(e_i) = \frac{d^2}{de_i^2} \left[(100 - S_i)e_i^2\right] = 2(100 - S_i)
        '''
    )

    st.write(
        '''
        Since $2(100 - S_i) > 0$, the second derivative is positive, which means that the cost function
        $C(e_i)$ is convex, or "concave-up". This convexity indicates that the cost of effort 
        increases at an increasing rate as effort $e_i$ rises.
    
        Jensen's inequality tells us that for a convex function such as $C(e_i)$, the expected cost of 
        effort is at least the cost of the expected effort. Mathematically:
        '''
    )

    st.latex(
        r'''
        E[C(e_i)] \geq C(E[e_i])
        '''
    )

    st.write(
        '''
        This inequality implies that, due to the convex nature of $C(e_i)$, 
        any variability in effort will lead to a higher average cost compared to a 
        scenario where effort is consistent. Thus, encouraging consistent effort across employees 
        minimizes the cost impact due to the convexity of the function.
        '''
    )

st.set_page_config(page_title="UNIT4", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Average performance evaluation",'Employee performance evaluation'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Average performance evaluation":
    UNIT4_1()
elif selected == "Employee performance evaluation":
    UNIT4_2()
