import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def UNIT5_1():

    st.write(
        '''
        Employment refers to the number of employees, including both full-time and part-time workers.
        It is an extensive margin metric as it doesn't inform about employee performance, that is
        how effectively employees are performing their jobs.
        '''
    )
    st.latex(
        r"""
        \begin{array}{|c|c|c|c|}
        \hline
        m_{11} & m_{12} & m_{13} & d_{1} \\
        \hline
        m_{21} & m_{22} & m_{23} & d_{3} \\
        \hline
        m_{31} & m_{32} & m_{33} & d_{3} \\
        \hline
        h_{1} & h_{2} & h_{3} & \\
        \hline
        \end{array}
        """
    )

    st.write(
        '''
        From the HR planning table, employment at the end of 2022
        and at the end of 2023 at the firm can be calculated as follows:
        '''
    )

    st.latex(r'L_{2022} = L_{1,2022} + L_{2,2022} + L_{3,2022}')
    st.latex(r'L_{2023} = L_{1,2023} + L_{2,2023} + L_{3,2023}')

    st.write(
        '''
        Labor turnover and retention at the firm level during 2022,
        denoted as $T$ and $R$, respectively, are calculated as follows, where $d_k$ represents the departures or separations of employees who
        were in job $J_k$ at the end of 2022 and left the firm during 2023, either voluntarily (e.g., quitting or retiring) or involuntarily (e.g., layoffs or dismissals):
        '''
    )

    st.latex(
        r'''
        T = 100 \times \frac{(d_1+d_2+d_3)}{L_{2022}} \\[10pt]
        R = 100 - T
        '''
    )

    st.write(
        '''
        The compound annual growth rate (CAGR) of employment over $t$ years is calculated as follows:
        '''
    )

    st.latex(
        r'''
        CAGR = frac{L_t}{L_0}^{\frac{1}{t}} - 1
        '''
    )

def UNIT5_2():

    st.write(
        '''
        In the HR planning table, $h_k$ represents new hires or number of employees who have been recruited and started working in job $J_k$ during 2023.
        Adding them up, we get total hires in 2023 by the firm:
        '''
    )

    st.latex(r'h = h_1 + h_2 + h_3')

    st.write(
        '''
        Hiring $h$ employees is not an immediate process, but it results from several steps: 
        1. The firm has a number of job vacancies (same as job openings), representing jobs that need to be filled: $v$
        2. To attract and recruit a pool of job candidates, the firm post the job vacancies. Today, online job postings are very common. 
        The number of job postings (same as job advertisements)
        may differ from the number of job vacancies, but for simplicity, we assume they are the same
        3. Finally, the firm selects or hires a number of job candidates: $h$

        A firm's hiring rate results from two factors, the firm's vacancy yield and the firm's vacancy rate:
        '''
    )

    st.latex(
        r'''
        \frac{h}{L} = \frac{h}{v} \times \frac{v}{L}
        '''
    )

    st.write(
        '''
        A firm's **vacancy yield** measures the efficiency of converting job vacancies into hires. It is the ratio of hires $h$ 
        to job vacancies $v$. It indicates how many times hires are made per job vacancy. A higher vacancy yield suggests the firm
        is more effective in filling open positions, while a lower yield might indicate challenges in attracting or selecting 
        suitable candidates.

        Occupational vacancy rates in the labor market indicate a higher demand for workers in that occupation, suggesting better job opportunities
        and potential for growth.
        '''
    )
        

def UNIT5_3():
    st.write(
        '''
        **Asymmetric Information:** Job candidates have more information about their skills, abilities, and work ethic than the hiring firm.
        
        **Adverse Selection:** Due to this information asymmetry, the firm may unintentionally attract and hire less qualified candidates.
        
        **The Mechanism:**
        1. **Average salary offer:** The firm, unsure of the true quality of candidates, offers a moderate salary.
        2. **Attracting less qualified candidates:** Less qualified candidates, satisfied with the offered salary, are more likely to apply.
        3. **Deterring highly qualified candidates:** Highly qualified candidates, seeking higher compensation for their skills, may be deterred.
        4. **Skewed applicant pool:** As a result, the pool of applicants becomes skewed towards less qualified individuals.
       
        This leads to a situation where the firm ends up with a less desirable workforce than it intended.

        **Screening** and **signaling** are concepts in economics that help to address information asymmetry, 
        where one party in a transaction has more information than the other.

        - **Screening**: This is a strategy used by the less informed party to gather information and distinguish 
        between different types of individuals or products. For instance, a company might use a rigorous application process, 
        including tests and interviews, to screen job candidates and identify the most qualified ones.
        - **Signaling**: This is a strategy used by the more informed party to convey credible 
        information to the less informed party. 
        For example, a highly skilled worker might earn a prestigious degree to signal their abilities to potential employers.
        '''
    )

def UNIT5_4():
    
    st.write(
        '''
        Matching a job candidate's skills with the job requirements involves both both screening and signaling. 
        This helps to minimize the risk of hiring less qualified candidtes (adverse selection).
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
        
        To reduce the risk of hiring unqualified candidates (adverse selection) 
        and attract the right people, firms should clearly outline the required 
        qualifications, skills, and responsibilities in job postings. 
        The offered salary should be competitive for well-matched candidates but not overly attractive 
        to those who are less qualified.

        By setting challenging expectations during a probationary period, 
        companies can assess a candidate's true abilities and commitment. 
        This approach deters unqualified individuals who would struggle to meet the demands of the role.
        '''
    )

def UNIT5_5():
  
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
                                                                                                   
  with st.sidebar.expander("Number of employees at your firm from [SABI](https://www.unavarra.es/biblioteca?languageId=1)"):
    L2020 = st.number_input("2020",key='L2020',value=1.0,step=1.0)
    L2021 = st.number_input("2021",key='L2021',value=1.0,step=1.0)
    L2022 = st.number_input("2022",key='L2022',value=1.0,step=1.0)

  L = [L2020,L2021,L2022]

  fig = plt.figure(figsize=(5,5),dpi=100)
  plt.plot(['2020','2021','2022'],L,color='red',label='Employment')
  plt.title('Employment over time')
  plt.legend()
  st.pyplot(fig)
    
st.set_page_config(page_title="UNIT5 Hiring", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Employment","Vacancy yield","Asymmetric information and adverse selection",'Skill matching','Practice 22'],  # required
    icons=["calculator", "calculator", "book", "book","person"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "Employment":
    UNIT5_1()
elif selected == "Vacancy yield":
    UNIT5_2()
elif selected == "Asymmetric information and adverse selection":
    UNIT5_3()
elif selected == "Skill matching":
    UNIT5_4()
elif selected == "Practice 22":
    UNIT5_5()

