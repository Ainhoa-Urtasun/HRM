import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT1_1():
                                                                                                    
    st.write(
        '''
        Human Resource Management (HRM) consists of HRM practices designed to maximize employee engagement, productivity, and job satisfaction. HRM practices include:
        - **Job Analysis and Design** (UNIT 2): Covers tasks, skills, jobs, job evaluation, and skill requirements for each job.
        - **HR Planning** (UNIT 3): Starts with data collection to show how to forecast employee availability using the transition matrix.
        - **Employee Performance Evaluation** (UNIT 4): Addresses the intensive margin.
        - **Recruitment** (UNIT 5): Discusses employment, asymmetric information, adverse selection, and how to mitage it.
        - **On-the-Job Training** (UNIT 6): Presents training as a way to reduce the skill gap of incumbent workers and uses the difference-in-differences method to measure training impacts.
        - **Compensation** (UNIT 7): Explores pay-for-performance models and employee-ownership options.
        - **Career Development** (UNIT 8): Introduces the tournament model as a framework for employee growth and progression.
        '''
    )

def UNIT1_2():
  
  st.write(
    '''
    Any firm, regardless of its size, structure, or legal form of ownership, 
    produces **output** (a good or a service) and performs **economic activities** 
    necessary for that production. Firms are classified into sectors (industries) based on the output 
    they produce and the economic activities they perform. There are standard classifications for 
    economic activities, such as **NACE Rev. 2, the European Classification of Economic Activities**.

    These economic activities are carried out by both employees and technology.
    Consequently, a firm's decisions on which technologies to adopt and which jobs to post
    in the labor market will depend on the specific economic activities required.
        
    Just as firms are classified into industries based on the output
    they produce and associated economic activities, jobs are classified into
    occupations depending on the tasks they entail. Same as for economic activities, 
    there are standard classifications for occupations, 
    such as **ISCO (International Standard Classification 
    of Occupations)**. 
        
    It is important to note that a job is not the same as an occupation. 
    Occupations are standardized, while jobs are more
    flexible as they are designed by firms. 
    '''
  )

def UNIT1_2():
  st.write(
    ''' 
    - $Q = f(e_1, e_2,...,e_L)$ is the production function of the firm
    - $e_i$ effort employee $i$ exerts at the firm, $e_i > 0$
    - $Q$ is the output the firm produces
    - $L$ number of employees at the firm
    - Skills, denoted as $s_i$, to be possessed by employees at the firm:
      - $s_1$ Demonstrating willigness to learn
      - $s_2$ Collaborating in teams and networks
      - $s_3$ Working efficiently
      - $s_4$ Taking a proactive approach  
    - Tasks, denoted as $t_j$, to be carried out by employees at the firm:
      - $t_1$ Intellectual
      - $t_2$ Physical
      - $t_3$ Social
      - $t_4$ Use of methods
      - $t_5$ Use of technology
    - Jobs, denoted as $J_k$, within the firm:
      - $J_1$ Other managers
      - $J_2$ Support intellectuals and scientists, technicians and professionals
      - $J_3$ Administrative employees
    
    In this course, we assume a **joint production function**, 
    where the firm's output results from the **collective contribution of each employee's effort**.
    The **output elasticity of effort** measures the impact of each employee's individual
    effort on the firm's output:
    '''
  )

  st.latex(
    r'''
    \alpha_i = \frac{\partial Q}{\partial e_i} \frac{e_i}{Q}
    '''
  )

  st.write(
    '''
    This output elasticity indicates the percentage change in the output
    the firm produces when employee $i$ exerts 1% more effort.
    '''
  )

def UNIT1_3():
  
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

def UNIT1_5():
  
  st.markdown("<h3 style='color: #4CAF50;'>🚀 Practice 9% (accumulated) </h3>", unsafe_allow_html=True)

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

# Set page configuration
st.set_page_config(page_title="UNIT 1 Human Resource Management (HRM)", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=['HRM practices','HRM in context','Notation for the course','Labor productivity and ULC','Practice 9% (accumulated)'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == 'HRM practices':
    UNIT1_1()
elif selected == 'HRM in context':
    UNIT1_2()
elif selected == 'Notation for the course':
    UNIT1_3()
elif selected == 'Labor productivity and ULC':
    UNIT1_4()
elif selected == 'Practice 9% (accumulated)':
    UNIT1_5()

