import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT5_1():

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
        We can calculate the compound annual growth rate (CAGR) of employment during $t$ years as follows:
        '''
    )

    st.latex(r'''
    \text{CAGR} = \left( \frac{L_t}{L_0} \right)^{\frac{1}{t}} - 1
    ''')

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.write('From [SABI](https://www.unavarra.es/biblioteca?languageId=1) and for your firm, visualize employment:')
    
    employees_input = st.sidebar.text_input("Number of Employees (comma-separated for 2019, 2020, 2021):", "1,1,1")
    employees = np.fromstring(employees_input, sep=',')
        
    df = pd.DataFrame({
        "Year": ["2019", "2020", "2021"],
        "Employment": employees,
    })

    fig, ax = plt.subplots()
    ax.plot(["2019", "2020", "2021"], employees, marker='x', label='Employment')    
    ax.set_xlabel('Year')
    ax.set_ylabel('Metrics')
    ax.set_title("Employment Over Time")
    ax.legend()
    st.pyplot(fig)

def UNIT5_2():
    
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
    st.text_input('For that job posting, offer a salary equal to the median monthly gross income in EUR for that occupation as reported in [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence):')
    st.text_input('Explain why you might end up recruiting the wrong job candidates:')

def UNIT5_3():
    st.write(
        '''
        Consider the following cost of effort for each job candidate:
        '''
    )

    st.latex(
            r'''
            C(e_i) = d(s_{(k)},s_i)e_i^2 \\[10pt]
            '''
        )

    st.write(
        '''
        where $e_i$ represents the effort job candidate $i$ would exert if hired; $d(s_{(k)},s_i)$ is the Euclidean distance 
        between $s_{(k)}$, the vector of skill norms required by the job job candidate $i$ would have to perform if hired, and the 
        vector of skills that job candidate $i$ actually possesses. The value of $d$ measures the matching between 
        the job candidate and the job they are supposed to perform if hired.
        Well-matched job candidates will show a low $d$ whereas poorly-matched job candidates will show a high $d$.The greater the distance, the higher the 
        cost of effort for the job candidate $i$. Remember, the vector of skill norms is derived from 
        the job evaluation process.

        To attract well-matched job candidates, the firm can specify in the job posting both the effort required and the 
        corresponding salary that compensates well-matched job candidates. This approach will deter poorly-matched job candidates, as
        their high cost of effort would require a significantly higher salary to make the job worthwhile.        
        '''
    )
    
st.set_page_config(page_title="UNIT5", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Employment","Asymmetric information and adverse selection",'Skill matching'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Employment":
    UNIT5_1()
elif selected == "Asymmetric information and adverse selection":
    UNIT5_2()
elif selected == "Skill matching":
    UNIT5_3()

