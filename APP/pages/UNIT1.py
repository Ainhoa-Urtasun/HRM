import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT1_1():

    st.write(
    '''
    Firms make two key decisions:

    - **What output (good or service) to produce**: This decision determines the set of tasks the firm needs to complete 
    using both technology and employees, as well as the industry in which the firm is classified.
    - **How to produce it**:
        1. Which technology to use
        2. Which tasks to automate (**Automated-Tasks**) and which tasks employees will carry out (**Job-Tasks**)
        3. Which HRM strategy to implement. There are two main HRM strategies:
            - **High-road HRM strategy**: Focuses on investing in employees through higher wages, 
            skills development, and fostering innovation, aiming for long-term productivity, employee engagement, and sustainable growth.
            - **Low-road HRM strategy**: Prioritizes cost-cutting by minimizing wages, reducing training, 
            and relying on low-skilled labor, often at the expense of long-term growth and employee well-being.

    This course teaches how to implement HRM practices—such as job analysis and design, HR planning, recruitment, performance 
    evaluation, training, career development, and compensation—to **Job-Tasks**, assuming the firm has already decided what output to produce, 
    which technology to use, and which tasks to automate, while following a high-road HRM strategy.
    '''
    )

    st.text_input("Choose an industry from [NACE](https://ec.europa.eu/eurostat/web/nace) and list the tasks a firm in that industry needs to complete using both technology and employees.")
    st.text_input("Select 6 **Job-Tasks** for employees at a firm in that industry from [O*NET](https://www.onetcenter.org/database.html#act).")
 
def UNIT1_2():

    st.write(
    '''
    Firms produce output (goods or services) by combining various tasks.
    Firms are classified into industries based on their output, which determines the specific tasks required for production.
    We distinguish between two types of tasks:

    - **Automated-Tasks** (carried out by technology)
    - **Job-Tasks** (carried out by employees)

    We represent production as a Leontieff production function:
    '''
    )

    st.latex(r"""
    Q = min [x(\text{Automated-Tasks}), y(\text{Job-Tasks})]
    """)

    st.write(
        ''' 
        where:

        - $Q$ is the output
        - $x$ proportion of Automated-Tasks
        - $y$ proportion of Job-Tasks
        
        We assume that Automated-Tasks and Job-Tasks are perfect complements,
        meaning they are both necessary for production.
        

        Job-Tasks require each employee to exert effort:
        
        '''
    )

    st.latex(r"""
    \text{Job-Tasks} = f(e_1, e_2, \dots, e_L)
    """)

    st.write('where $e_i$ represents the effort exerted by employee $i$ and $L$ is the number of employees.')
   
    a = st.sidebar.number_input('Proportion of Automated-Tasks (x):', min_value=0.01, max_value=10.0, value=1.0, step=0.01)
    b = st.sidebar.number_input('Proportion of Job-Tasks (y):', min_value=0.01, max_value=10.0, value=1.0, step=0.01)
    isoquant_levels = [1, 2, 3, 4, 5]
    fig = plt.figure(figsize=(6, 6))
    for q in isoquant_levels:
        plt.plot([a * q, a * q], [b * q, b * 10], color='b')  # vertical line
        plt.plot([a * q, a * 10], [b * q, b * q], color='b')  # horizontal line
        plt.xlabel("Automated-tasks (A)")
    plt.ylabel("Job-tasks (B)")
    plt.title("Leontief Production Function (L-shaped Isoquants)")
    plt.grid(True)
    st.pyplot(fig)
    
def UNIT1_3():
    st.write(
        '''
        Employees significantly influence the firm's performance and profitability. 
        '''
    )
    st.latex(r'EBIT = pQ - wL -rK')
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

