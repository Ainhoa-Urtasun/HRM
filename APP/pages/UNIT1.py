import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT1_1():

    st.write(
    '''
    This course takes an analytical approach to human resource management (HRM) practices, including:

    - **Job analysis and design**
    - **Human resource (HR) planning**
    - **Recruitment**
    - **Performance evaluation**
    - **Training**
    - **Career development**
    - **Compensation**
    
    These practices are designed to maximize employee engagement, productivity, and job satisfaction.
    '''
    )

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)

    st.write(
    '''
    - [Skills intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence) from CEDEFOP (European Centre for the 
    Development of Vocational Training)
    - [SABI](https://www.unavarra.es/biblioteca?languageId=1) from the library at UPNA
    '''
    )

def UNIT1_2():

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
    st.text_input('Select a sector from NACE rev. 2 at [Skills Intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence', placeholder='Enter the name of your industry and its economic activities')
    st.text_input("Select a firm from [SABI](https://www.unavarra.es/biblioteca?languageId=1): (1) **Industry classification** Same sector above;(2) **Employees' segmentation in Spain** Senior management, Support intellectuals and scientists, technicians and professionals, and Sales representatives and similar. At least 5 women")
    st.text_input('', placeholder='Enter the name of your firm')
    st.text_input('Note: A job is not the same as an occupation. Occupations are standardized, while jobs are defined by firms', placeholder="Enter the names of the 3 jobs in your firm")
    
def UNIT1_3():
    st.write(
    ''' 
    - $Q = f(e_1, e_2,...,e_L)$ is the production function of the firm
    - $e_i$ effort employee $i$ exerts at the firm
    - $Q$ is the output the firm produces
    - $L$ number of employees at the firm
    - $J_{(1)}, J_{(2)}, J_{(3)}$ jobs within the firm
    - Tasks to be carried out by employees at the firm:
        - $t_1$: Intellectual
        - $t_2$: Physical
        - $t_3$: Social
        - $t_4$: Use of methods
        - $t_5$: Use of technology
    - Skills to be possessed by employees at the firm:
        - $s_1$: Demonstrating willigness to learn
        - $s_2$: Collaborating in teams and networks
        - $s_3$: Working efficiently
        - $s_4$: Taking a proactive approach  
    '''
    )

    st.write(
        '''
        As a measure of the contribution of each employee to the firm, we can calculate the output elasticity of employee $i$ as follows:
        '''
    )

    st.latex(r'''
    \alpha_i = \frac{\partial Q}{\partial e_i} \frac{e_i}{Q}
    ''')

    st.write(
        '''
        This output elascticity indicates the percentage change in the output
        the firm produces when employee $i$ exerts 1% more effort.
        '''
    )


def UNIT1_4():
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

# Set page configuration
st.set_page_config(page_title="UNIT1", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=['Human Resource Management (HRM)','HRM in context','Notation for the course', 'Labor productivity and unit labor cost (ULC)'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == 'Human Resource Management (HRM)':
    UNIT1_1()
elif selected == 'HRM in context':
    UNIT1_2()
elif selected == 'Notation for the course':
    UNIT1_3()
elif selected == 'Labor productivity and unit labor cost (ULC)':
    UNIT1_4()

