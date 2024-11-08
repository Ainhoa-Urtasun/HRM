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
        - **Individually**, which is challenging but also more meaningful 
        
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
    
    st.write(
        '''
        The **skill gap** between an employee and the job they are performing can be 
        measured by he Euclidean distance between the **job skill requirements** $s_k$ 
        and the **employee skill profile** $s_i = (s_{i1}, s_{i2}, s_{i3}, s_{i4})$:
        '''
    )

    st.latex(
        r"""
        g_i = \sqrt{(\|s_{1k}\| - s_{1i})^2 + (\|s_{2k}\| - s_{2i})^2 + (\|s_{3k}\| - s_{3i})^2 + (\|s_{4k}\| - s_{4i})^2}
        """
    )

    st.write(
        '''
        As a performance evaluation metric, the **skill gap** is useful for decisions on
        recruitment, training, and compensation.
        '''
    )

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.sidebar.multiselect("Select two tasks of the job at your firm:",("Intellectual","Physical","Social","Use of methods","Use of technology"))
    st.sidebar.write('Evaluate the job:')
    with st.sidebar.expander("$t_i$"):
        s1i = st.number_input("$s_{1i(k)}$ Demonstrating willigness to learn",key='s1i',step=1.0)
        s2i = st.number_input("$s_{2i(k)}$ Collaborating in teams and networks",key='s2i',step=1.0)
        s3i = st.number_input("$s_{3i(k)}$ Working efficiently",key='s3i',step=1.0)
        s4i = st.number_input("$s_{4i(k)}$ Taking a proactive approach",key='s4i',step=1.0)
    with st.sidebar.expander("$t_j$"):
        s1j = st.number_input("$s_{1j(k)}$ Demonstrating willigness to learn",key='s1j',step=1.0)
        s2j = st.number_input("$s_{2j(k)}$ Collaborating in teams and networks",key='s2j',step=1.0)
        s3j = st.number_input("$s_{3j(k)}$ Working efficiently",key='s3j',step=1.0)
        s4j = st.number_input("$s_{4j(k)}$ Taking a proactive approach",key='s4j',step=1.0)

    if st.button("Skill gap"):
        ti = np.array([
            [s1i],
            [s2i],
            [s3i],
            [s4i]
        ])
        tj = np.array([
            [s1j],
            [s2j],
            [s3j],
            [s4j]
        ])
        euclidean_distance = 0.45 * np.linalg.norm(ti - tj)
        st.write(euclidean_distance)

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

st.set_page_config(page_title="UNIT4", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=['Classification','Output elasticity of effort','Skill gap','Cost of effort'],  # required
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
