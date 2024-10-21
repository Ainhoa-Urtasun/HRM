import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT1_1():
    st.write(
    '''
    Firms produce output (goods or services) by combining various activities.
    They are classified into industries based on their output, which determines the specific activities required for production.
    We distinguish between two types of activities:

    - $A$ activities that are performed by technology (usually routine activities)
    - $W$ **work activities** that depend exclusively on labor (usually non-routine activities)

    We represent production as a Leontieff production function:
    '''
    )

    st.latex(r"""
    Q = min (A, W)
    """)

    st.write(
        ''' 
        where:

        - $Q$ is the output
        - $A$ activities that capital performs
        - $W$ **work activities**, activities exclusively carried out by labor
        
        We assume that the activities that capital performs $A$ and the **work activities** $W$ are perfect complements,
        meaning they are both necessary for production.
        
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
        
        **Work activities** require each employee to exert effort:
        
        '''
    )

    st.latex(r"""
    W = f(e_1, e_2, \dots, e_L)
    """)

    st.write('where $e_i$ represents the effort exerted by employee $i$ and $L$ is the number of employees.')
    st.text_input("Choose an industry from [NACE](https://ec.europa.eu/eurostat/web/nace) and enter the activities that need to be completed")
    st.text_input("Use O*NET to identify **work activities** from the activities listed above")
    st.components.v1.iframe("https://www.onetonline.org/", width=800, height=600, scrolling=True)

    a = st.sidebar.text_input('Proportion of activities:',)
    a, w = st.columns(2)
    with a:
        a1 = st.number_input("activity proportion", key="a1")
    with w:
        w1 = st.number_input("work activity proportion", key="w1")
    A = np.linspace(0, 10, 100)
    W = np.linspace(0, 10, 100)
    isoquant_levels = [1, 2, 3, 4, 5]
    fig = plt.figure(figsize=(6, 6))
    for q in isoquant_levels:
        plt.plot([a*q, a*q], [b*q, b*10], color='b')  # vertical line (fixed capital)
        plt.plot([a*q, a*10], [b*q, b*q], color='b')  # horizontal line (fixed labor)

    plt.xlabel("Activities (A)")
    plt.ylabel("Work activities (W)")
    plt.title("Leontief Production Function (L-shaped Isoquants)")
    plt.grid(True)
    st.pyplot(fig)

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

def UNIT1_2():
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

