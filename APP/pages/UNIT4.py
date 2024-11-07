import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT4_1():

    st.write(
        '''
        Performance evaluation assesses how well employees perform within the firm. 
        This can be done in two ways:
        - **On average**
        - **Individually**, which is challenging but also more meaningful. 
        
        Performance evaluation also distinguishes between:
        - **The extensive margin** addresses employee participation in tasks. Examples of extensive margin
        performance evaluation measures include attendance and absenteeism
        - **The intensive margin** focuses on the level of effort and productivity during tasks, examining
        how employees perform while working

        A common average performance metric for the intensive margin is **labor productivity**:
        '''
    )

    st.latex(r'\text{Labor productivity} = \frac{pQ}{L}')

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.text_input("Write here the labor productivity of your firm using the latest information provided by [SABI](https://www.unavarra.es/biblioteca?languageId=1):")
    
def UNIT4_2():

    st.write(
        '''
        **Output elasticity of effort** measures the performance of an employee on the 
        intensive margin, indicating the percentage change in the output the firm produces when employee
        $i$ exerts 1% more effort.
        '''
    )
    
    st.latex(
        r'''
        Q = f(e_1, e_2, \dots, e_i, \dots, e_L) \\[10pt]
        e_i \geq 0 \\[10pt]
        \alpha_i = \frac{Q}{\partial e_i} \frac{e_i}{Q}
        '''
    )

def UNIT4_3():
    

def UNIT4_4():

    st.write(
        '''
        Consider the following **cost of effort** function:
        '''
    )

    st.latex(
            r'''
            C(e_i) = g_i e_i^2 \\[10pt]
            '''
        )

    st.write(
        '''
        where:
        - $e_i$ represents the effort exerted by employee $i$
        - $g_i$ is the **skill gap** of employee $i$ calculated as the Euclidean distance 
        between $s_{(k)}$, the **skill requirements** for the job employee $i$ performs, and $s_i$, the 
        **skill profile** of employee $i$. The greater the skill gap, the higher the 
        cost of effort for employee $i$.
        '''
    )

    st.latex(
        r"""
        g_i = \sqrt{(s_{1i} - s_{1j})^2 + (s_{2i} - s_{2j})^2 + (s_{3i} - s_{3j})^2 + (s_{4i} - s_{4j})^2}
        """
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
        C'(e_i) = 2 g_i e_i
        '''
    )

    st.write(
        '''
        This first derivative shows the marginal cost of effort. Since $g_i>0$, 
        the marginal cost of effort increases linearly with $e_i$.

        The second derivative with respect to $e_i$ is:
        '''
    )

    st.latex(
        r'''
        C''(e_i) = 2 g_i
        '''
    )

    st.write(
        '''
        Since $g_i>0$, the second derivative is positive, which means that the cost function
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
    options=['Classification','Output elasticity of effort','Skill gap','Cost of effort','Abseteeism'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Classification":
    UNIT4_1()
elif selected == "Output elasticity of effort":
    UNIT4_2()
elif selected == "Skill gap":
    UNIT4_3()
elif selected == "Cost of effort":
    UNIT4_4()
elif selected == "Abseteeism":
    UNIT4_5()
