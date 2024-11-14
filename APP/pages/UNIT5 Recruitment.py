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

def UNIT5_3():
    
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

def UNIT5_4():
  
  st.markdown("<h3 style='color: #4CAF50;'>🚀 Practice 9 </h3>", unsafe_allow_html=True)

  st.write(
    '''
    - [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) from CEDEFOP (European Centre for the 
    Development of Vocational Training)
    - [SABI](https://www.unavarra.es/biblioteca?languageId=1) from the library at UPNA

    Choose your firm:
    1. Access the SABI database through the UPNA Library
    2. In 'Personalizar' then 'Opciones Generales', change the language to English
    3. Firm qualification based on **Employees** criteria:
      - Minimum lastest number of employees of 750
      - Employees' segmentation in Spain (last available year):
      - Other managers
      - Support intellectuals and scientists, technicians and professionals
      - Administrative employees
      - At least 10 women
    4. View list of results
    5. Select one firm from the firms that qualify
    '''
  )

  st.text_input('', placeholder='Write here the name of your firm')
  st.text_input('Select your firm and then **Overview** under **Industry & overview**',placeholder="Write here your firm's NACE Rev. 2 Primary Code and English trade description")
                                                                                                   
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
    
st.set_page_config(page_title="UNIT5 Recruitment", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Employment","Asymmetric information and adverse selection",'Skill matching','Practice 22'],  # required
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
elif selected == "Practice 22":
    UNIT5_4()

