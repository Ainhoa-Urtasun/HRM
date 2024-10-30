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
    produces an output (good or service) and engages in **economic activities** 
    to achieve this. Firms are classified into sectors (industries) based on the output 
    they produce and the associated economic activities. 

    To execute these economic activities, firms decide which technologies to adopt
    and which jobs to post in the labor market.
    
    A job consists of a bundle of tasks, and just as firms are classified into sectors (industries), 
    jobs are classified into occupations based on the tasks they entail. 

    There are standard classifications for firms into sectors, 
    such as NACE which is the European Classification of Economic Activities
    and for jobs into occupations, 
    such as ISCO that stands for International Standard Classification 
    of Occupations.
    '''
    )

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics</h3>", unsafe_allow_html=True)
    st.text_input(
        '''
        Select the sector into which you want your firm to be classified using NACE at 
        [Skills Intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence).
        Write here the industry name and economic activities:
        '''
    )
    st.markdown(
    '''
    Select 3 jobs for your firm using ISCO occupations at 
    [Skills Intelligence](https://www.cedefop.europa.eu/en/tools/skills-intelligence).
    '''
    )
    st.text_input(
    "Titles of the 3 jobs:",
    placeholder="A job is not the same as an occupation. Occupations are standardized, while jobs are defined by firms."
    )
    st.markdown(
    '''
    Select a firm using [SABI](https://www.unavarra.es/biblioteca?languageId=1). Qualification criteria:
    
    1. The firm must be classified in the sector selected above.
    2. The firm must have fewer than 25 employees.
    '''
    )
    st.text_input("Firm name:")

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
        - $s_2$: Maintaining a positive attitude
        - $s_3$: Taking a proactive approach
        - $s_4$: Working efficiently  
    '''
    )

    st.write(
        '''
        As a measure of the contribution of each employee to the firm, we can calculate the output elasticity of employee $i$ as follows:
        '''
    )

    st.latex(r'''
    \alpha_i = \frac{\partial f(e_1, e_2, \dots, e_i, \dots, e_L)}{\partial e_i} \cdot \frac{e_i}{f(e_1, e_2, \dots, e_i, \dots, e_L)}
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
    st.latex(r'EBIT = pQ - wL - dM - rK')
    st.write(
        '''
        - $p$ is the price of the output the firm produces
        - $pQ$ represents operating revenue
        - $w$ is the average salary paid by the firm to its employees
        - $wL$ is cost of employees
        - $d$ is the unit cost of materials
        - $dM$ are material costs
        - $r$ is the cost of technology
        - $rK$ is depreciation
        '''
    )

    st.latex(r'Labor \ productivity = \frac{pQ}{L}')
    st.latex(r'ULC = \frac{wL}{pQ}')

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics </h3>", unsafe_allow_html=True)
    st.write(
        '''
        From [SABI](https://www.unavarra.es/biblioteca?languageId=1) 
        and for your firm, visualize labor productivity and ULC:
        '''
    )
  
    cost_input = st.sidebar.text_input("Cost of employees (comma-separated for 2019, 2020, 2021):", "0,0,0")
    revenue_input = st.sidebar.text_input("Operating revenue (comma-separated for 2019, 2020, 2021):", "1,1,1")
    employees_input = st.sidebar.text_input("Number of employees (comma-separated for 2019, 2020, 2021):", "1,1,1")

    costs = np.fromstring(cost_input, sep=',')
    revenues = np.fromstring(revenue_input, sep=',')
    employees = np.fromstring(employees_input, sep=',')

    labor_productivity = revenues / employees / 1000  # Convert to thousands
    unit_labor_cost = costs / revenues
        
    df = pd.DataFrame({
        "Year": ["2019", "2020", "2021"],
        "Labor productivity (in thousands)": labor_productivity,
        "ULC": unit_labor_cost
    })

    fig, ax = plt.subplots()
    ax.plot(["2019", "2020", "2021"], labor_productivity, marker='x', label='Labor productivity')
    ax.plot(["2019", "2020", "2021"], unit_labor_cost, marker='o', label='ULC')        
    ax.set_xlabel('Year')
    ax.legend()
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

