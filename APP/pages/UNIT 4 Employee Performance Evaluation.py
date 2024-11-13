import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT4_1():

    st.write(
        '''
        Employee performance evaluation assesses how well employees perform within the firm. 
        This can be done in two ways:
        - **On average**
        - **Individually**, which is challenging but also more meaningful 
        
        Employee performance evaluation also distinguishes between:
        - **The extensive margin** evaluates employee participation in tasks. Examples of extensive margin
        evaluation include attendance and absenteeism
        - **The intensive margin** evaluates the level of effort and productivity during tasks, examining
        how employees perform while working. Examples of intensive margin evaluation include labor productivity,
        ULC, output elasticity of labor, and the skill gap.
        '''
    )

def UNIT4_2():
    st.write(
        '''
        From the Income Statement of a firm: 
        '''
    )
    st.latex(r'EBIT = pQ - wL - M - K')
    st.write(
        '''
        - $p$ is the price of the output the firm produces
        - $pQ$ represents operating revenue
        - $w$ is the average salary paid by the firm to its employees
        - $wL$ is cost of employees
        - $M$ are material costs
        - $K$ is depreciation

        From the Income Statement of a firm, we can obtain two critical indicators of employee performance 
        at the intensive margin:
        '''
    )

    st.latex(r'\text{Labor productivity} = \frac{pQ}{L}')
    st.latex(r'\text{ULC} = \frac{wL}{pQ}')

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    with st.sidebar.expander("Cost of employees at your firm from [SABI](https://www.unavarra.es/biblioteca?languageId=1)"):
        C2020 = st.number_input("2020",key='C2020',step=1.0)
        C2021 = st.number_input("2021",key='C2021',step=1.0)
        C2022 = st.number_input("2022",key='C2022',step=1.0)
    with st.sidebar.expander("Operating revenue of your firm from [SABI](https://www.unavarra.es/biblioteca?languageId=1)"):
        OR2020 = st.number_input("2020",key='OR2020',value=1.0,step=1.0)
        OR2021 = st.number_input("2021",key='OR2021',value=1.0,step=1.0)
        OR2022 = st.number_input("2022",key='OR2022',value=1.0,step=1.0)
    with st.sidebar.expander("Number of employees at your firm from [SABI](https://www.unavarra.es/biblioteca?languageId=1)"):
        L2020 = st.number_input("2020",key='L2020',value=1.0,step=1.0)
        L2021 = st.number_input("2021",key='L2021',value=1.0,step=1.0)
        L2022 = st.number_input("2022",key='L2022',value=1.0,step=1.0)

    LP = [OR2020/L2020,OR2021/L2021,OR2022/L2022]
    ULC = [C2020/OR2020,C2021/OR2021,C2022/OR2022]

    fig = plt.figure(figsize=(5,5),dpi=100)
    plt.plot(['2020','2021','2022'],LP,color='red',label='Labor productivity')
    plt.plot(['2020','2021','2022'],ULC,color='blue',label='ULC')
    plt.title('HRM metrics over time')
    plt.legend()
    st.pyplot(fig)
    
def UNIT4_3():

    st.write(
        '''
        In this course, we assume a **joint production function**, 
        where the firm's output results from the **collective contribution of each employee's effort**.
        '''
    )

    st.latex(
        r'''
        Q = f(e_1, e_2, \dots, e_i, \dots, e_L) \\[10pt]
        e_i \geq 0 \\[10pt]
        '''
    )

    st.write(
        '''
        The **output elasticity of effort** measures the impact of each employee's individual
        effort on the firm's output:
        '''
    )

    st.latex(
        r'''
        \alpha_i = \frac{Q}{\partial e_i} \frac{e_i}{Q}
        '''
    )

    st.write(
        '''
        This output elasticity indicates the percentage change in the output
        the firm produces when employee $i$ exerts 1% more effort.
        '''
    )
def UNIT4_4():
    
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

def UNIT4_5():

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

st.set_page_config(page_title="UNIT 4 Employee Performance Evaluation", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=['Classification','Labor productivity and ULC','Output elasticity of effort','Skill gap','Cost of effort'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Classification":
    UNIT4_1()
elif selected == "Labor productivity and ULC":
    UNIT4_2()
elif selected == "Output elasticity of effort":
    UNIT4_3()
elif selected == "Skill gap":
    UNIT4_4()
elif selected == "Cost of effort":
    UNIT4_5()