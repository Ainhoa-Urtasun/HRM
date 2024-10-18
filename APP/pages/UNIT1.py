import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT1_1():
    st.write(
        '''
        Human resource management (HRM) takes on the **organization** and **motivation** of employees by implementing HRM practices
        such as 
        - **Job analysis and design**
        - **HR planning**
        - **Recruiting**
        - **Performance evaluation**
        - **Training**
        - **Career development**
        - **Compensation**
        '''
    )

def UNIT1_2():
    st.write(
        '''
        Firms make two important decisions:

        1. **What to produce:** This decision determines the output (product or service) and, in turn, the tasks that need to be
        completed. Firms are classified into industries depending on this decision. See [NACE](https://ec.europa.eu/eurostat/web/nace)

        2. **How to produce it:** This involves deciding which technology to use and how to allocate tasks between labor and technology
            
        '''
    )

    st.write(
        '''
        The activities that labor needs to
        carry out are called **work activities** and HRM is responsible for organizing and motivating employees to carry out
        these **work activities** efficiently and effectively.
        '''
    )
    
    st.text_input("Enter the name of the firm from SABI")
    st.text_input("Enter the 2-digit NAICS code and title of the firm from SABI")
    st.components.v1.iframe("https://www.unavarra.es/biblioteca?languageId=1", width=800, height=600, scrolling=True)
    st.text_input("Enter the activities this firm needs to perform")




def UNIT1_3():
    with st.expander("Show the notation for the **Human Resource Management (HRM)** course"):
        st.write("- $Q = L_1^{e_1}L_2^{e_2}L_3^{e_3}K^a$ represents the output produced by the firm (Cobb-Douglas production function)")
        st.write("- $L_1$ number of workers in job 1 at the firm")
        st.write("- $L_2$ number of workers in job 2 at the firm")
        st.write("- $L_3$ number of workers in job 3 at the firm")
        st.write("- $L = L_1 + L_2 + L_3$ total number of employees at the firm")
        st.write("- $K$ technology")
        st.write("- $A_1, A_2, A_3, A_4$ work activities performed by employees")
        st.write("- $S_1, S_2, S_3, S_4, S_5, S_6$ skills possessed by employees")

    st.write("Use the section above to view the notation for the **Human Resource Management (HRM)** course.")

def UNIT1_5():
    st.write('''
    The production function includes three different types of labor, each performing a different job. The output elasticity for each type of labor indicates the 
    percentage change in output resulting from a 1% change in that type of labor, holding other inputs constant. These elasticities reflect the contribution of each 
    labor type to the firm's overall production process.
    ''')

    st.write('The output elasticity of labor in job 1 at the firm:')
    st.latex(r" \frac{\partial Q}{\partial L_1} \cdot \frac{L_1}{Q} = e_1")
    st.write('The output elasticity of labor in job 2 at the firm:')
    st.latex(r" \frac{\partial Q}{\partial L_2} \cdot \frac{L_2}{Q} = e_2")
    st.write('The output elasticity of labor in job 3 at the firm:')
    st.latex(r" \frac{\partial Q}{\partial L_3} \cdot \frac{L_3}{Q} = e_3")

def UNIT1_4():
    st.latex(r'EBIT = pQ - w(L_H+L_L) -rK')
    st.write(
        '''where $p$ is the price of the output the firm produces, $w$ is the average salary paid by the firm to its employees, 
        and $r$ is the cost of technology. This values can be derived from the Income Statement. Next, we practice how to use them
        to calculate labor productivity and ULC.
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
    options=["HRM", "HRM in context", "Notation for the course", "Labor productivity and unit labor cost (ULC)"],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "HRM":
    UNIT1_1()
elif selected == "HRM in context":
    UNIT1_2()
elif selected == "Notation for the course":
    UNIT1_3()
elif selected == "Labor productivity and unit labor cost (ULC)":
    UNIT1_4()

