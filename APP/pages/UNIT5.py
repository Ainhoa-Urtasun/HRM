import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT5_1():

    st.write(
    '''
    Any firm, regardless of its size, structure, or legal form of ownership, 
    produces an output (good or service) and performs **economic activities** 
    to achieve this. Firms are classified into sectors (industries) based on the output 
    they produce and the economic activities they perform. 

    To perform these economic activities, firms decide which technologies to adopt
    and which jobs to post in the labor market.
    
    A job consists of a bundle of tasks, and just as firms are classified into sectors (industries), 
    jobs are classified into occupations based on the tasks they entail. 

    There are standard classifications for firms into sectors, 
    such as NACE rev. 2, the European Classification of Economic Activities.
    There are also standard classificationf for jobs into occupations, 
    such as ISCO that stands for International Standard Classification 
    of Occupations.
    '''
    )

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics</h3>", unsafe_allow_html=True)
    st.markdown(
        '''
        Select the sector of your firm from NACE rev. 2 at [Skills Intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence)
        '''
    )
    st.text_input('', placeholder='Enter the name of your industry and its economic activities')
    st.markdown(
        """
        Select a firm from [SABI](https://www.unavarra.es/biblioteca?languageId=1):
        (1) Industry classification: The firm must be classified in the sector selected above;
        (2) Employees' segmentation in Spain: Senior manager, Support intellectuals and scientists, technicians 
        and professionals, and Sales representatives and similar; and at least 5 women
        """
     )
    st.text_input('', placeholder='Enter the name of your firm')
    st.markdown(
        '''
        Match the names of your 3 jobs above with ISCO at [Skills Intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence).
        Note: A job is not the same as an occupation. Occupations are standardized, while jobs are defined by firms
        '''
    )
    st.text_input('', placeholder="Enter the names of the 3 jobs in your firm")

def UNIT5_2():

    st.write(
        '''
        Employment refers to the number of employees, including both full-time and part-time workers. 
        If we have information of employment in a firm at the job level, 
        we can calculate the total employment of the firm at -1 and at 0 as follows:
        '''
    )

    st.latex(r'L_{-1} = L_{(1,-1)} + L_{(2,-1)} + L_{(3,-1)}')
    st.latex(r'L_0 = L_{(1,0)} + L_{(2,0)} + L_{(3,0)}')

    st.write(
        '''
        $L_{(-1)}$ and $L_{0}$ refers to employment in the firm at two consecutive points in time (e.g., years).
        If we know employment at several points in time (for multiple years, for instance), we can calculate the compound annual growth rate (CAGR) 
        of employment over $t$ years as follows:
        '''
    )

    st.latex(
        r'''
        \text{CAGR} = \left( \frac{L_t}{L_0} \right)^{\frac{1}{t}} - 1
        '''
    )


    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.write('Fill in data for the 3 jobs at your firm (use made-up data):')
    
    L1, L2, L3, D = st.columns(4)
    with L1:
        m11 = st.number_input("$m_{(1)(1)}$", key="m11", step=1)
        m21 = st.number_input("$m_{(2)(1)}$", key="m21", step=1)
        m31 = st.number_input("$m_{(3)(1)}$", key="m31", step=1)
        h1 = st.number_input("$h_{(1)}$", key="h1", step=1)
    with L2:
        m12 = st.number_input("$m_{(1)(2)}$", key="m12", step=1)
        m22 = st.number_input("$m_{(2)(2)}$", key="m22", step=1)
        m32 = st.number_input("$m_{(3)(2)}$", key="m32", step=1)
        h2 = st.number_input("$h_{(2)}$", key="h2", step=1)
    with L3:
        m13 = st.number_input("$m_{(1)(3)}$", key="m13", step=1)
        m23 = st.number_input("$m_{(2)(3)}$", key="m23", step=1)
        m33 = st.number_input("$m_{(3)(3)}$", key="m33", step=1)
        h3 = st.number_input("$h_{(3)}$", key="h3", step=1)
    with D:
        d1 = st.number_input("$d_{(1)}$", key="d1", step=1)
        d2 = st.number_input("$d_{(2)}$", key="d2", step=1)
        d3 = st.number_input("$d_{(3)}$", key="d3", step=1)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("$L_{(1,-1)}$"):
            L1past = np.array([m11, m12, m13, d1])
            L1past = np.sum(L1past)
            st.write(f"Employment in job 1 at -1: {L1past}")
    with col2:
        if st.button("$L_{(2,-1)}$"):
            L2past = np.array([m21, m22, m23, d2])
            L2past = np.sum(L2past)
            st.write(f"Employment in job 2 at -1: {L2past}")
    with col3:
        if st.button("$L_{(3,-1)}$"):
            L3past = np.array([m31, m32, m33, d3])
            L3past = np.sum(L3past)
            st.write(f"Employment in job 3 at -1: {L3past}")
    with col4:
        if st.button("$L_{(-1)}$"):
            Lpast = np.array([L1past, L2past, L3past])
            Lpast = np.sum(Lpast)
            st.write(f"Employment at your firm at -1: {Lpast}")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("$L_{(1,0)}$"):
            L1present = np.array([m11, m21, m23, h1])
            L1present = np.sum(L1present)
            st.write(f"Employment in job 1 at 0: {L1present}")
    with col2:
        if st.button("$L_{(2,0)}$"):
            L2present = np.array([m12, m22, m32, h2])
            L2present = np.sum(L2present)
            st.write(f"Employment in job 2 at 0: {L2present}")
    with col3:
        if st.button("$L_{(3,0)}$"):
            L3present = np.array([m13, m23, m33, h3])
            L3present = np.sum(L3present)
            st.write(f"Employment in job 3 at 0: {L3present}")
    with col4:
        if st.button("$L_{(0)}$"):
            Lpresent = np.array([L1present, L2present, L3present])
            Lpresent = np.sum(Lpresent)
            st.write(f"Employment at your firm at 0: {Lpresent}")

    with st.sidebar.expander("Number of employees at your firm from [SABI](https://www.unavarra.es/biblioteca?languageId=1)"):
        L2020 = st.number_input("2020", step=1)
        L2021 = st.number_input("2021", step=1)
        L2022 = st.number_input("2022", step=1)

    fig = plt.figure(figsize=(5,5),dpi=100)
    plt.plot(['2020','2021','2022'],[L2020,L2021,L2022],color='red')
    plt.title('Employment over time')
    st.pyplot(fig)

def UNIT5_3():
    
    st.write(
        '''
        In recruiting, **asymmetric information** arises because job candidates 
        know more about their skills than the firm does. This can lead to **adverse selection**, 
        where the firm may end up hiring less qualified candidates due to this information gap. 
        Here’s how adverse selection occurs: to attract a pool of candidates, 
        the firm posts a job ad specifying the tasks, required skills, credentials, 
        and salary for the role. Due to limited information about each candidate’s true abilities, 
        the employer offers an average salary for the position. 
        This attracts candidates who meet the listed credentials, but these credentials, 
        while signaling a certain level of qualification, do not fully reveal each candidate's suitability.
    
        However, this average salary might be too low for the 'good' candidates 
        while still appealing to 'wrong' ones, 
        resulting in adverse selection where primarily 'wrong' candidates apply.

        '''
    )

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.text_input('From [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) choose one occupation for which you wish to post a job:')
    st.text_input('For that job posting, set the salary to match the median monthly gross income (in EUR) for the occupation, as reported in [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence):')
    st.text_input('Explain why you might unintentionally attract and hire the wrong candidates for the job:')

def UNIT5_4():
    
    st.write(
        '''
        Consider the following **cost of effort** for the job candidate:
        '''
    )

    st.latex(
            r'''
            C(e_i) = g_i e_i^2 \\[10pt]
            '''
        )

    st.write(
        '''
        where $e_i$ represents the effort job candidate $i$ would exert if hired; 
        $g_i$ is the **skill gap** of job candidate $i$ calculated as the Euclidean distance 
        between $s_{(k)}$, the **skill requirements** for the job, and $s_i$, the 
        **skill profile** of job candidate $i$. Well-matched job candidates will show 
        a low skill gap $g_i$ whereas poorly-matched job candidates will show a high skill gap $g_i$. 
        The greater the distance, the higher the 
        cost of effort for the job candidate $i$. Remember, $s_{(k)}$ is derived from 
        the job evaluation process.

        To attract well-matched job candidates, the firm can specify in the job posting both the required 
        level of effort and the corresponding salary, which compensates well-matched candidates 
        but not poorly-matched ones. This approach will deter poorly-matched candidates, 
        as their high cost of effort would require a significantly higher salary to make the job worthwhile. 
        By setting these conditions—a high level of required effort at a relatively low salary—during a probation period, 
        the company can assess the candidate’s fit for the role and decide whether to offer a long-term job contract.
        '''
    )
    
st.set_page_config(page_title="UNIT5", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=['HRM in context',"Employment","Asymmetric information and adverse selection",'Skill matching'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "HRM in context":
    UNIT5_1()
elif selected == "Employment":
    UNIT5_2()
elif selected == "Asymmetric information and adverse selection":
    UNIT5_3()
elif selected == "Skill matching":
    UNIT5_4()

