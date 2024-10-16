import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT1_1():
    st.write(
        '''
        Human resource management (HRM) takes on the organization and motivation of employees by implementing HRM practices
        such as job analysis and design, recruitment, HR planning, performance evaluation, training, compensation, 
        and career development. HRM is implemented at the firm level.
        '''
    )

    st.text_input("Enter the name of the firm from SABI")
    st.text_input("Enter the 2-digit NAICS code and title of the firm from SABI")
    st.components.v1.iframe("https://www.unavarra.es/biblioteca?languageId=1", width=800, height=600, scrolling=True)
    st.text_input("Enter the activities this firm needs to perform")

    st.write(
        '''
        The output the firm produces determines the set of activities it needs to perform. Firms are classified 
        into industries depending on the output they produce. The North American Industry Classification System (NAICS) provides
        a standard classification of firms into industries.
        '''
    )

    st.write(
        '''
        The firm allocates (organizes) these activities across labor and technology. The activities that labor needs to
        carry out are called **work activities** and HRM is responsible for organizing and motivating employees to carry out
        these **work activities** efficiently and effectively.
        '''
    )

def UNIT1_2():
    with st.expander("Show the notation for the **Human Resource Management (HRM)** course"):
        st.latex(r'Q = A(e_1,e_2,...,e_L) \cdot (L_H)^\alpha \cdot (L_L)^\beta \cdot K^\gamma')
        st.write("- $Q$ total output produced by the firm modeled as a Cobb-Douglas production function")
        st.write("- $A$ total factor productivity (TFP), which depends on the effort exerted by each employee at the firm")
        st.write("- $L_H$ high-skill labor")
        st.write("- $L_L$ low-skill labor")
        st.write("- $L = L_H + L_L$ total number of employees at the firm")
        st.write("- $K$ technology")
        st.write("- $W_1, W_2, W_3, W_4$ work activities performed by employees")
        st.write("- $S_1, S_2, S_3, S_4, S_5, S_6$ skills possessed by employees")

    st.write("Use the section above to view the notation for the **Human Resource Management (HRM)** course.")

def UNIT1_3():
    st.latex(r'Q = A(e_1,e_2,...e_L) \cdot (L_H)^\alpha \cdot (L_L)^\beta \cdot K^\gamma')
    st.latex(r"\text{Output elasticity of high-skill labor } \frac{\partial Q}{\partial L_H} \cdot \frac{L_H}{Q} = \alpha")
    st.latex(r"\text{Output elasticity of low-skill labor } \frac{\partial Q}{\partial L_L} \cdot \frac{L_L}{Q} = \beta")
    st.write(
        '''
        The output elasticity of high-skill labor shows the percentage change in output associated with a 1% change in high-skill labor, holding
        other factors constant. In the same way,
        the output elasticity of low-skill labor shows the percentage change in output associated with a 1% change in low-skill labor, holding other 
        factors consta. Therefore, 
        these elasticities capture how important each type of labor is to the production process.
        '''
    )

def UNIT1_4():
    st.latex(r'EBIT = pQ - w(L_H+L_L) -rK')
    st.write(
        '''where $p$ is the price of the output the firm produces, $w$ is the average salary paid by the firm to its employees, 
        and $$ is the cost of technology. EBIT is therefore obtained by substracting the cost of employees and depreciation from operating revenue.
        Next, we practice calculating labor productivity and ULC using these items from the Income Statement
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
    options=["HRM", "Notation for the Course", "Output Elasticities of Labor", "Labor Productivity and Unit Labor Cost (ULC)"],  # required
    icons=["house", "book", "calculator", "person", "globe"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="vertical",
)

# Call the selected section
if selected == "HRM":
    UNIT1_1()
elif selected == "Notation for the Course":
    UNIT1_2()
elif selected == "Output Elasticities of Labor":
    UNIT1_3()
elif selected == "Labor Productivity and Unit Labor Cost (ULC)":
    UNIT1_4()

