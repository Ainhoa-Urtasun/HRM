import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT5_1():
    st.latex(
        r"""
        \begin{array}{|c|c|c|c|}
        \hline
        m_{11} & m_{12} & m_{13} & d_{1} \\
        \hline
        m_{21} & m_{22} & m_{23} & d_{3} \\
        \hline
        m_{31} & m_{32} & s_{33} & d_{3} \\
        \hline
        h_{1} & h_{2} & h_{3} & \\
        \hline
        \end{array}
        """
    )

    st.write(
        '''
        Employment refers to the number of employees, including both full-time and part-time workers. 
        From the above table, we can calculate the total employment of the firm at the end of 2022 and
        at the end of 2023 as follows:
        '''
    )

    st.latex(r'L_{2022} = L_{(1,2022)} + L_{(2,2022)} + L_{(3,2022)}')
    st.latex(r'L_0 = L_{(1,2023)} + L_{(2,2023)} + L_{(3,2023)}')

    st.write(
        '''
        The compound annual growth rate (CAGR) of employment over $t$ years is calculated as follows:
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
        the employer may set a moderate salary for the position. 
        This job posting will attract candidates who meet the listed credentials and are satisfied with the
        offered salary. The credentials, while signaling a certain level of qualification, 
        do not fully reveal each candidate's suitability.
    
        If the salary offered in the job ad is too low for the 'good' candidates but sufficient for 'less qualified'
        candidates, this will resulting in adverse selection, where primarily less suitable candidates apply.
        '''
    )

def UNIT5_3():
    
    st.write(
        '''
        Same as for incumbent employees, we consider the following **cost of effort** for the job candidate:
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
        - $e_i$ represents the effort exerted by employee $i$, with $e_i \geq 0$
        - $g_i$ is the **skill gap** of employee $i$, with $g_i \geq 0$. The greater their skill gap, the higher the 
        cost of effort for employee $i$. Well-matched job candidates will show 
        a low skill gap $g_i$ whereas poorly-matched job candidates will show a high skill gap $g_i$. 
        The greater the distance, the higher the 
        cost of effort for the job candidate $i$. Remember, $s_{(k)}$ is derived from 
        the job evaluation process.
        
        To mitigate adverse selection when recruiting and attract 
        well-matched job candidates, the firm can specify in the job posting not only the credentials        
        but also the required skills, tasks, level of effort, and a salary that compensates 
        well-matched candidates but not poorly-matched ones. This approach will deter poorly-matched candidates, 
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

