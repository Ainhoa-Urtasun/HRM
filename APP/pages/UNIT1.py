import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT1_1():
    st.write(
    '''
    Firms produce output (goods or service)s by combining various tasks. 
    They are classified into industries based on their output, which determines the specific tasks required for production.
    We distinguish between two types of tasks:

    - Tasks that are performed by capital (usually routine tasks)
    - Tasks that depend exclusively on labor (usually non-routine tasks)

    We represent the production function of a firm as a Constant Elasticity of Substitution (CES) production function as in Cnossen (2024):
    '''
    )

    st.latex(r"""
    q = A \left[ \alpha a^\rho + (1 - \alpha) w a^\rho \right]^{\frac{1}{\rho}}
    """)

    st.write(
        ''' 
        where:

        - $q$ is the output
        - $A$ is the total factor productivity (a scaling parameter)
        - $a$ and $wa$ are the inputs, with $a$ activities that capital performs and $wa$ **work activities**, activities exclusively carried out by labor.
        - $\alpha$ is the distribution parameter
        - $\rho$ determines the degree of substitution between the inputs
        
        The firm-specific elasticity of substitution is:
        '''
    )

    st.latex(r"""
    \sigma = \frac{1}{1 - \rho}
    """)

    st.write(
        '''
        Human resource management (HRM) takes on the **organization** and **motivation** of employees in performing **work activities**
        by implementing HRM practices
        such as: 
        - **Job analysis and design**
        - **HR planning**
        - **Recruiting**
        - **Performance evaluation**
        - **Training**
        - **Career development**
        - **Compensation**
        '''
    )

    st.write(
        '''
        **Work activities** require each employee to exert effort, where $e_i$ represents the effort exerted for employee $i$:
        '''
    )

    st.latex(r"""
    wa = f(e_1, e_2, \dots, e_L)
    """)

    st.text_input("Choose an industry from [NACE](https://ec.europa.eu/eurostat/web/nace) and enter the activities that need to be completed")
    st.text_input("Use O*NET to identify **work activities** from the activities listed above")
    st.components.v1.iframe("https://www.onetonline.org/", width=800, height=600, scrolling=True)

def UNIT1_2():
    st.write(
        '''
        Employees significantly influence the firm's performance and profitability. 
        '''
    )
    st.latex(r'EBIT = pq - wL -rK')
    st.write(
        '''where $p$ is the price of the output the firm produces, $w$ is the average salary paid by the firm to its employees, 
        and $r$ is the cost of technology. This values can be derived from the Income Statement. Let's see how we can use them 
        to use them to calculate **labor productivity** and **ULC**.
        '''
    )
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
    options=["HRM in context", "Labor productivity and unit labor cost (ULC)"],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "HRM in context":
    UNIT1_1()
elif selected == "Labor productivity and unit labor cost (ULC)":
    UNIT1_2()

