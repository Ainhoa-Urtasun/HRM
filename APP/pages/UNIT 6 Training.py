import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT6_1():

    st.write(
        '''
        The skill profile of a person represents their human capital, which is the result of a 
        long-term investment in skills, education, and experience. 
        Human capital refers to the knowledge, abilities, and competencies that individuals 
        bring to the workforce, contributing to productivity and economic value. There are two
        types of human capital:
        
        - **General human capital** includes skills and knowledge that are transferable 
        across different firms or industries. Examples include literacy, numeracy, problem-solving, 
        and general management skills. Because these skills are valuable to many employers, 
        individuals with high general human capital have greater mobility in the labor market.
        
        - **Specific human capital** refers to skills and knowledge that are valuable only 
        to a particular firm or job. Examples include mastery of proprietary processes, 
        familiarity with unique organizational structures,
        or job-specific technical expertise. These skills increase productivity within the specific 
        firm but are less transferable to other employers.
        
        So, the primary difference between general and specific human capital lies in transferability: 
        General human capital is portable and valued universally in the labor market. 
        Specific human capital has limited applicability outside the organization or context where it was developed.
        Employers often invest more in training related to specific human capital, while individuals bear the cost of acquiring general human capital, as it enhances their overall employability and earning potential.
        '''
    )

def UNIT6_2():
    st.write(
        '''
        As an investment, education and on-the-job training can be analyzed just like any other type of investment. Supponse
        that an individual is choosing whether to drop out or finish university this year, which we will call $t=2025$. Future
        years will be $2026, 2027,...,T$, where $T$ is the last year of her career. If the student drops out now, her salary
        in future years will be $w_{t,L}$, where the subscript $t$ refers to future periods. If she continues on in school, salary
        in future years will be $w_{t,H}$, where $w_{t,H} \geq w_{t,L}$. Given this, the increased salary from finishing school is
        $w_{t,H} - w_{t,L}$ each year.

        Education provides many benefits beyond increased salary. One is the pure joy of learnig. Education may also make you 
        more effective at home or leisure activities or increase your enjoyment of travel and literature. Here we focus on salary.

        Suppose that the interest rate is $r$ per year. This means that an investment of €1 made today would be worth $(1+r)$ next
        year, $(1+r)^2$ after two years, and so on. Similarly, €1 received next year is worth $1/(1+r)$ this year.

        With these assumptions, the present value (PV) of the return on education investment is:
        '''
    )

    st.latex(
        r'''
        PV = \sum_{t=2025}^T \frac{w_{t,H}-w_{t,L}}{(1+r)^t}
        '''
    )

    st.write(
        '''
        There are two costs of investments in education. The first is the direct cost of tuition, textbooks, a laptop,
        and other expenses. Denote this by $C_{2025}$. Direct costs are generally borne up fornt and do not need to be
        discounted. The second cost is the opportunity cost of the time spent on education. For example, typical (full-time)
        MBA students quit relatively high-paying jobs to go back to university for 21 months. When they do, they give up
        salaries that in many cases are greater than the direct cost of tuition. Denote this by $F_{2025}$

        The decision rule for any investment is that it should be made as long as the present value of the return
        on the investment exceeds the present value of the cost of the investment. This net present value equals:
        '''
    )

    st.latex(
        r'''
        NPV = \sum_{t=2025}^T \frac{w_{t,H}-w_{t,L}}{(1+r)^t} - (C_{2025}+F_{2025})
        '''
    )

    st.write(
        '''
        For a finite geometric series:
        '''
    )

    st.latex(
        r'''
        S_n = a \frac{1 - \frac{1}{(1+r)}^n}{1 - \frac{1}{(1+r)}}
        '''
    )

    st.write(
        ''' 
        - $S_n$ is the sum of the first $n$ terms
        - $a$ is the first term
        - $1/(1+r)$ is the common ratio
        - $n$ is the number of terms
        '''
     )
  
def UNIT6_3():

    st.write(
        """
        Firms aim to reduce the skill gap between the job skill requirements and an employee's skill profile. 
        They have two primary options to achieve this:

        1. **Hiring** new employees with skill profiles that closely match the job's requirements.  
        2. **On-the-job training** incumbent employees to improve their skill profiles and align them with the job requirements.
        
        We use the **Difference-in-Differences (DiD) method** to evaluate the impact of 
        on-the-job training on the **employee skill profile** $s_i = (s_{i1},s_{i2},s_{i3},s_{i4})$. To simplify the analysis,
        we focus on just one skill of the employee skill profile $s_{ij}$
        """
    )

    st.latex(
        r"""
        \text{ATT} = (s_{Tom,2026} - s_{Tom,2024}) - (s_{Noah,2026} - s_{Noah,2024})
        """
    )

    st.write(
        """
        Here, **ATT** stands for the **Average Treatment Effect on the Treated**. This metric captures 
        the effect of training on employees who received it (trained group), 
        compared to a similar group that did not receive the training (non-trained group). 

        The Difference-in-Differences (DiD) method achieves this by making two key comparisons:
        
        - **Before and after training**: Training occurs at the present year, 2025, so 2024 is before training, 
        and 2026 is after training.
        - **Training versus Non-training**: Tom receives the training whereas Noah doesn't receive any training.
        
        By combining these two comparisons, the DiD method helps estimate the causal impact of training on reducing the skill gap. 
        Note: The method is valid if the **parallel trends assumption** holds—that is, if the trained and non-trained groups 
        would have followed similar skill gap trends in the absence of training.
        """
    )

    st.write(
        """
        In DiD, we distinguish two key counterfactual outcomes:
        
        - **Counterfactual Skill Gap (CSG)**: This represents the skill gap the trained employee 
        would have experienced if he had not received the training:
        """
    )

    st.latex(
        r"""
        \text{CSG} = s_{Noah,2026} - s_{Noah,2024}
        """
    )

    st.write(
        """
        - **Counterfactual Skill Gap Change (CSGC)**: This represents how much the skill of the trained 
        employee would have changed if he hadn’t received the training:
        """
    )

    st.latex(
        r"""
        \text{CSGC} = s_{Tom,2024} + (s_{Noah,2026} - s_{Noah,2024})
        """
    )

    st.write(
        """
        The use of these counterfactuals allows us to isolate the causal impact of training by 
        estimating what would have happened in the absence of the intervention.
        """
    )

def UNIT6_4():

    st.markdown("<h3 style='color: #4CAF50;'>🚀 Practice 23 </h3>", unsafe_allow_html=True)
    with st.sidebar.expander("Tom's skill"):
        T2024 = st.number_input("2024", key="T2024", step=1)
        T2026 = st.number_input("2026", key="T2026", step=1)
    with st.sidebar.expander("Noah's skill"):
        N2024 = st.number_input("2024", key="N2024", step=1)
        N2026 = st.number_input("2026", key="N2026", step=1)
    fig = plt.figure(figsize=(5,5),dpi=100)
    plt.plot(['2024','2026'],[T2024,T2026],color='red',label='Tom')
    plt.plot(['2024','2026'],[N2024,N2026],color='blue',label='Noah')
    plt.plot(['2024','2026'],[T2024,T2024+(N2026-N2024)],color='green',ls='-.',label='Counterfactual')
    plt.title('Training evaluation')
    plt.legend()
    st.pyplot(fig)
  
st.set_page_config(page_title="UNIT 6 Training", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=['Human capital','NPV of education','Training evaluation','Practice 23'],  # required
    icons=["book", "calculator", "calculator", "person"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Human capital":
    UNIT6_1()
elif selected == "NPV of education":
    UNIT6_2()
elif selected == "Training evaluation":
    UNIT6_3()
elif selected == "Practice 23":
    UNIT6_4()
