import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def UNIT1_1():
    st.write(
        '''Firms produce goods or services by combining various tasks. 
        They are classified into industries based on their output, which determines the specific tasks required for production.
        We distinguish between two types of tasks:
        
        - Tasks that are performed by capital (typically routine tasks)
        - Tasks that depend exclusively on labor (typically non-routine tasks). 
        
        The production function, based on a CES (Constant Elasticity of Substitution) structure, is expressed as (Cnossen, 2024):
        '''
    )

    st.latex(r"""
    q = \left[ a^\rho + wa^\rho \right]^{\frac{1}{\rho}}
    """)

    st.write(
        ''' 
        where $a$ represents activities that capital performs and $wa$ represents **work activities**, activities exclusively carried out by labor.
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

    st.text_input("Choose an industry from [NACE](https://ec.europa.eu/eurostat/web/nace) and enter the activities that need to be completed")
    st.text_input("Use O*NET to decide which of activities above are **work activities**")
    st.components.v1.iframe("https://www.onetonline.org/", width=800, height=600, scrolling=True)

    with st.expander("Show the notation for the **Human Resource Management (HRM)** course"):
        st.write("- $L$ number of employees at the firm")
        st.write("- $e_1, e_2, e_3,...,e_L$ effort exerted by each employee at the firm")
        st.write("- $Q(e_1, e_2, e_3,...,e_L)$ production function of the firm")
        st.write("- $W_1, W_2, W_3, W_4, W_5, W_6$ work activities performed by employees")
        st.write("- $S_1, S_2, S_3, S_4$ skills possessed by employees")

    st.write("Use the section above to view the notation for the **Human Resource Management (HRM)** course.")

def UNIT1_2():
    st.write(
        '''
        Employees significantly influence the firm's performance and profitability. 
        '''
    )
    st.latex(r'EBIT = pQ(e_1,e_2,...,e_L) - wL -rK')
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

