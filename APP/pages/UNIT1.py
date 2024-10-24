import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT1_1():

    st.write(
    '''
    Any firm, regardless of its size, structure, or legal form of ownership, 
    produces an output (good or service) and engages in **economic activities** 
    to achieve this. Firms are classified into sectors (industries) based on the output 
    they produce and the associated economic activities. 

    To execute these economic activities, firms decide which technologies to adopt
    and which jobs to post in the labor market.
    
    A job consists of a bundle of tasks and just as firms are classified into sectors (industries), 
    jobs are classified into occupations based on the tasks they entail. 
    
    There are standard classifications for firms into sectors, 
    such as NACE (Nomenclature of Economic Activities), and for jobs into occupations, 
    such as ISCO (International Standard Classification of Occupations).

    '''
    )

    st.markdown("<h3 style='color: #4CAF50;'>🚀 HRM Analytics: Applying Concepts to a Real Firm </h3>", unsafe_allow_html=True)
    st.text_input("Select a sector for your firm from [NACE](https://www.cedefop.europa.eu/en/tools/skills-intelligence/sectors?sector=05) and describe the key economic activities it engages in")
    st.text_input("Select the occupations for which you will post jobs from [ISCO](https://www.cedefop.europa.eu/en/tools/skills-intelligence/occupations?occupation=4.41)")

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
    
def UNIT1_2():
    st.write(
        ''' 
        - $Q = f(e_1, e_2,...,e_L)$ is the production function of the firm
        - $e_i$ effort employee $i$ exerts at the firm
        - $L$ number of employees at the firm
        - $EBIT = pQ - wL - rK$ Earnings Before Interest and Taxes (EBIT) of the firm
        - $T_1, T_2, T_3, T_4, T_5$ tasks employees carry out
        - $S_1, S_2, S_3, S_4, S_5, S_6, S_7, S_8, S_9$ skills employees have      
        '''
    )

    st.write(
        '''
        As a measure of the contribution of each employee to the firm, we can calculate the output elasticity of the effort
        exerted by each employee as follows:
        '''
    )

    st.latex(r'''
    \varepsilon_{e_i} = \frac{\partial f(e_1, e_2, \dots, e_i, \dots, e_L)}{\partial e_i} \cdot \frac{e_i}{f(e_1, e_2, \dots, e_i, \dots, e_L)}
    ''')


def UNIT1_3():
    st.write(
        '''
        Employees significantly influence the firm's performance and profitability. 
        '''
    )
    st.latex(r'EBIT = pQ - wL - dM - rK')
    st.write(
        '''where $p$ is the price of the output the firm produces; $pQ$ represents operating revenue; $w$ is the average salary 
        paid by the firm to its employees; $wL$ is cost of employees; $d$ is the unit cost of materials; $dM$ are material costs;
        $r$ is the cost of technology; $rK$ is depreciation. These values are recorded in the Income Statement. 
        '''
    )

    st.latex(r'Labor \ productivity = \frac{pQ}{L}')
    st.latex(r'ULC = \frac{wL}{pQ}')
    st.components.v1.iframe("https://www.unavarra.es/biblioteca?languageId=1", width=800, height=600, scrolling=True)
  
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
    ax.plot(["2019", "2020", "2021"], labor_productivity, marker='x', label='Labor Productivity')
    ax.plot(["2019", "2020", "2021"], unit_labor_cost, marker='o', label='Unit Labor Cost')        
    ax.set_xlabel('Year')
    ax.set_ylabel('Metrics')
    ax.set_title("Trends in HRM metrics")
    ax.legend()
    st.pyplot(fig)

# Set page configuration
st.set_page_config(page_title="UNIT1", layout="wide")

selected = option_menu(
    menu_title="Main Menu",  # required
    options=['Human Resource Management (HRM)','Notation for the course', 'Labor productivity and unit labor cost (ULC)'],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == 'Human Resource Management (HRM)':
    UNIT1_1()
elif selected == 'Notation for the course':
    UNIT1_2()
elif selected == 'Labor productivity and unit labor cost (ULC)':
    UNIT1_3()

