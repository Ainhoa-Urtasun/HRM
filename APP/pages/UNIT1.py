import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT1_1():

    st.write(
    '''
    Firms are grouped into sectors based on their economic activities. To perform these economic activities, 
    firms decide which technology to adopt and which occupations to employ. 
    An occupation refers to a group of jobs that involve similar tasks and duties, as well as the 
    same qualifications and skills requirements. Economic activities and occupations are classified using standard systems, 
    such as NACE (Nomenclature of Economic Activities) for industries and 
    ISCO (International Standard Classification of Occupations) for occupations.

    This course takes an analytical approach to human resource management (HRM) practices
    such as job analysis and design, human resource (HR) planning, recruitment, performance evaluation, training, career development,
    and compensation designed to maximize employee engagement, productivity, and satisfaction.

    '''
    )

    st.text_input("Select an industry from [NACE](https://www.cedefop.europa.eu/en/tools/skills-intelligence/sectors?sector=05) and list the economic activities a firm in that industry would carry out")
    st.text_input("Select which occupations you will hire from [ISCO](https://www.cedefop.europa.eu/en/tools/skills-intelligence/occupations?occupation=4.41)")
 
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

    st.latex(r'Labor \ Productivity = \frac{pQ}{L}')
    st.latex(r'ULC = \frac{wL}{pQ}')
    st.components.v1.iframe("https://www.unavarra.es/biblioteca?languageId=1", width=800, height=600, scrolling=True)
  
    cost_input = st.sidebar.text_input("Cost of Employees (comma-separated for 2019, 2020, 2021):", "0,0,0")
    revenue_input = st.sidebar.text_input("Operating Revenue (comma-separated for 2019, 2020, 2021):", "1,1,1")
    employees_input = st.sidebar.text_input("Number of Employees (comma-separated for 2019, 2020, 2021):", "1,1,1")

    costs = np.fromstring(cost_input, sep=',')
    revenues = np.fromstring(revenue_input, sep=',')
    employees = np.fromstring(employees_input, sep=',')

    labor_productivity = revenues / employees / 1000  # Convert to thousands
    unit_labor_cost = costs / revenues
        
    df = pd.DataFrame({
        "Year": ["2019", "2020", "2021"],
        "Labor Productivity (in thousands)": labor_productivity,
        "Unit Labor Cost": unit_labor_cost
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

