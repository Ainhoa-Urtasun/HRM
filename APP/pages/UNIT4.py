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

        A typical average performance metric is labor productivity:
        '''
    )

    st.latex(r'\text{Labor productivity} = \frac{pQ}{L}')

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.text_input("Write here the labor productivity of your firm using the latest information provided by [SABI](https://www.unavarra.es/biblioteca?languageId=1):")

def UNIT4_2():
    
    st.write(
        '''
        A more meaningful yet challenging approach to performance evaluation is assessing 
        the effort each employee exerts. Effort here is not just working hours; it reflects 
        the employee's willingness to make meaningful contributions to the firm. This includes 
        not only hours worked but also the skills and motivation required to perform tasks effectively.

        When employee effort is assessed properly, it allows the firm to understand each employee's 
        contribution to its overall value and motivates them to improve their performance.

        Next, we present several alternative metrics for evaluating employee effort.
        '''
    )

def UNIT4_3():

    st.write(
        '''
        **Output elasticity of effort** indicates the percentage change in the output the firm produces when employee
        $i$ exerts 1% more effort.
        '''
    )
    
    st.latex(
        r'''
        Q = f(e_1, e_2, \dots, e_i, \dots, e_L) \\[10pt]
        e_i \geq 0 \\[10pt]
        \alpha_i = \frac{\partial f(e_1, e_2, \dots, e_i, \dots, e_L)}{\partial e_i} 
        \cdot \frac{e_i}{f(e_1, e_2, \dots, e_i, \dots, e_L)}
        '''
    )


def UNIT4_4():

    st.write(
        '''
        Consider the following cost of effort function:
        '''
    )

    st.latex(
            r'''
            C(e_i) = (100-s_{(k)i})e_i^2 \\[10pt]
            0 \leq s_{(k)i} \leq 100
            '''
        )

    st.write(
        '''
        where $s_{(k)i}$ represents the skills employee $i$ possesses
        to perform job $J_{(k)}$. The higher the value of $s_{(k)i}$, the lower 
        cost of effort for the employee $i$.
        '''
    )

    st.write(
        '''
        We can analyze the properties of the cost of effort function
        by calculating its derivatives. Taking the first derivative with 
        respect to effort $e_i$:
        '''
    )

    st.latex(
        r'''
        C'(e_i) = \frac{d}{de_i} \left[(100 - s_{(k)i}e_i^2)\right] = 2(100 - s_{(k)i})e_i
        '''
    )

    st.write(
        '''
        This first derivative shows the marginal cost of effort. Since $(100 - s_{(k)i})$ is a positive constant, 
        the marginal cost of effort increases linearly with $e_i$.

        The second derivative with respect to $e_i$ is:
        '''
    )

    st.latex(
        r'''
        C''(e_i) = \frac{d^2}{de_i^2} \left[(100 - s_{(k)i}e_i^2)\right)] = 2(100 - s_{(k)i})
        '''
    )

    st.write(
        '''
        Since $2(100 - s_{(k)i) > 0$, the second derivative is positive, which means that the cost function
        $C(e_i)$ is convex, or "concave-up". This convexity indicates that the cost of effort 
        increases at an increasing rate as effort $e_i$ rises.
    
        **Jensen's inequality** tells us that for a convex function such as $C(e_i)$, the expected cost of 
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

def UNIT4_5():
    st.write(
        '''
        Another proxy to evaluate the effort or contribution an employee makes to the firm is by recording their
        absenteeism. In a month, we can calculate the absenteeism of a particular employee as follows:
        '''
    )

    st.latex(
        r'''
        A = \frac{\text{Days off}}{\text{Working days}}
        '''
    )

st.set_page_config(page_title="UNIT4", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Average performance evaluation",'Employee performance evaluation','Output elasticity of effort','Cost of effort','Abseteeism'],  # required
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
elif selected == "Output elasticity of effort":
    UNIT4_3()
elif selected == "Cost of effort":
    UNIT4_4()
elif selected == "Abseteeism":
    UNIT4_5()
